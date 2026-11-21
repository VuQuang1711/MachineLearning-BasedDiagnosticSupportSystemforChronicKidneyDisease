"""
src/data_loader.py
Chịu trách nhiệm nạp dữ liệu, làm sạch ký tự rác, chia tách tập Train/Test 
và khởi tạo ColumnTransformer Pipeline chống rò rỉ dữ liệu (Data Leakage).
"""

import sys
from pathlib import Path
from typing import Tuple
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Đảm bảo thư mục gốc dự án luôn nằm trong PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    from src.config import (
        CATEGORICAL_FEATURES,
        NUMERICAL_FEATURES,
        RANDOM_STATE,
        RAW_DATA_PATH,
        TARGET_COLUMN,
        TEST_SIZE,
    )
except ModuleNotFoundError:
    from config import (
        CATEGORICAL_FEATURES,
        NUMERICAL_FEATURES,
        RANDOM_STATE,
        RAW_DATA_PATH,
        TARGET_COLUMN,
        TEST_SIZE,
    )


class CKDDataLoader:
    """Lớp xử lý và tải dữ liệu Bệnh Thận Mãn Tính chuẩn mực."""

    def __init__(self, data_path: str = None):
        if data_path:
            self.data_path = str(data_path)
        else:
            # Ưu tiên kiểm tra DatasetForProject/MLDataset, sau đó đến data/
            from src.config import DATASET_FOR_PROJECT_PATH, RAW_DATA_PATH
            if DATASET_FOR_PROJECT_PATH.exists():
                self.data_path = str(DATASET_FOR_PROJECT_PATH)
            else:
                self.data_path = str(RAW_DATA_PATH)

    def load_and_clean_raw_data(self) -> pd.DataFrame:
        """
        Nạp file CSV thô, loại bỏ ký tự trắng thừa ('\t'), chuẩn hóa nhãn và ép kiểu.
        Tự động kiểm tra Google Drive, DatasetForProject hoặc tự động tải từ KaggleHub.
        
        Returns:
            pd.DataFrame: Dữ liệu sạch đã chuẩn hóa kiểu dữ liệu.
        """
        path_obj = Path(self.data_path)
        if not path_obj.exists():
            # Kiểm tra thêm đường dẫn DatasetForProject nếu path_obj chưa tồn tại
            from src.config import DATASET_FOR_PROJECT_PATH
            if DATASET_FOR_PROJECT_PATH.exists():
                self.data_path = str(DATASET_FOR_PROJECT_PATH)
                path_obj = DATASET_FOR_PROJECT_PATH

        if not path_obj.exists():
            try:
                import kagglehub
                from kagglehub import KaggleDatasetAdapter
                print(f"[INFO] '{self.data_path}' không tồn tại, tự động tải qua KaggleHub...")
                df = kagglehub.load_dataset(
                    KaggleDatasetAdapter.PANDAS,
                    "akshayksingh/kidney-disease-dataset",
                    "kidney_disease.csv",
                )
                path_obj.parent.mkdir(parents=True, exist_ok=True)
                df.to_csv(self.data_path, index=False)
                print(f"[SUCCESS] Đã lưu bản sao dữ liệu về: {self.data_path}")
            except Exception as err:
                print(f"[WARN] Lỗi tải qua KaggleHub: {err}")
                df = pd.read_csv(self.data_path)
        else:
            df = pd.read_csv(self.data_path)
        
        # 1. Loại bỏ cột id nếu tồn tại
        if "id" in df.columns:
            df = df.drop(columns=["id"])

        # 2. Làm sạch cột nhãn mục tiêu
        df[TARGET_COLUMN] = (
            df[TARGET_COLUMN]
            .astype(str)
            .str.strip()
            .str.replace("\t", "")
        )
        # Giữ lại các nhãn hợp lệ
        df = df[df[TARGET_COLUMN].isin(["ckd", "notckd"])].copy()
        df["target"] = df[TARGET_COLUMN].map({"ckd": 1, "notckd": 0}).astype(int)
        df = df.drop(columns=[TARGET_COLUMN])

        # 3. Làm sạch ký tự rác trong các cột định lượng bị đọc nhầm kiểu chuỗi
        for col in ["pcv", "wc", "rc"]:
            if col in df.columns:
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.strip()
                    .str.replace("\t", "")
                    .str.replace("?", "")
                )
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # 4. Làm sạch khoảng trắng rác trong các cột định tính
        for col in CATEGORICAL_FEATURES:
            if col in df.columns:
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.strip()
                    .str.replace("\t", "")
                    .replace({"nan": np.nan, "?": np.nan})
                )

        # 5. Ép kiểu số cho toàn bộ cột định lượng
        for col in NUMERICAL_FEATURES:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        return df

    @staticmethod
    def audit_raw_data(df_raw: pd.DataFrame) -> dict:
        """
        Kiểm toán dữ liệu thô tường minh: dòng trùng lặp, số giá trị duy nhất (nunique),
        cột hằng số (nunique <= 1) và cột định danh (nunique == len(df_raw)).

        Args:
            df_raw (pd.DataFrame): DataFrame gốc đọc trực tiếp từ CSV.

        Returns:
            dict: Báo cáo kiểm toán dữ liệu đầu vào.
        """
        n_rows, n_cols = df_raw.shape
        duplicated_rows = int(df_raw.duplicated().sum())
        nunique_series = df_raw.nunique(dropna=True).sort_values()
        constant_cols = [col for col, cnt in nunique_series.items() if cnt <= 1]
        id_like_cols = [col for col, cnt in nunique_series.items() if cnt == n_rows]

        return {
            "n_rows": int(n_rows),
            "n_cols": int(n_cols),
            "duplicated_rows": duplicated_rows,
            "constant_cols": constant_cols,
            "id_like_cols": id_like_cols,
            "nunique_sorted": nunique_series,
        }

    @staticmethod
    def build_eda_summary(df: pd.DataFrame) -> pd.DataFrame:
        """
        Tạo bảng tổng hợp eda_summary cô đọng cuối phần EDA.

        Args:
            df (pd.DataFrame): DataFrame sau khi làm sạch có cột 'target'.

        Returns:
            pd.DataFrame: Bảng tổng hợp các chỉ tiêu chất lượng dữ liệu.
        """
        feature_df = df.drop(columns=["target"]) if "target" in df.columns else df
        n_rows = len(df)
        n_features = feature_df.shape[1]
        total_cells = n_rows * n_features
        total_missing = int(feature_df.isnull().sum().sum())
        missing_pct = round((total_missing / total_cells) * 100, 2) if total_cells else 0.0
        duplicated_rows = int(df.duplicated().sum())
        constant_cols = int((feature_df.nunique(dropna=True) <= 1).sum())
        ckd_count = int((df["target"] == 1).sum()) if "target" in df.columns else 0
        notckd_count = int((df["target"] == 0).sum()) if "target" in df.columns else 0

        rows = [
            ("Tổng số mẫu (bệnh nhân)", f"{n_rows}"),
            ("Tổng số đặc trưng đầu vào", f"{n_features} ({len(NUMERICAL_FEATURES)} số + {len(CATEGORICAL_FEATURES)} phân loại)"),
            ("Tổng số ô khuyết thiếu (NaN)", f"{total_missing:,} / {total_cells:,} ({missing_pct}%)"),
            ("Số dòng trùng lặp (Duplicated)", f"{duplicated_rows}"),
            ("Số cột hằng số (nunique <= 1)", f"{constant_cols}"),
            ("Nhãn CKD (target = 1)", f"{ckd_count} ({ckd_count / n_rows * 100:.2f}%)" if n_rows else "0"),
            ("Nhãn Not-CKD (target = 0)", f"{notckd_count} ({notckd_count / n_rows * 100:.2f}%)" if n_rows else "0"),
        ]
        return pd.DataFrame(rows, columns=["Chỉ tiêu kiểm toán (EDA Summary)", "Giá trị"])

    @staticmethod
    def get_preprocessing_summary(preprocessor: ColumnTransformer) -> dict:
        """
        Thống kê chi tiết số lượng và danh sách tên cột Trước vs Sau Tiền xử lý.

        Args:
            preprocessor (ColumnTransformer): ColumnTransformer đã được .fit().

        Returns:
            dict: Thống kê số lượng và danh sách tên cột từ get_feature_names_out().
        """
        all_names = list(preprocessor.get_feature_names_out())
        num_out = [name for name in all_names if name.startswith("num__")]
        cat_out = [name for name in all_names if name.startswith("cat__")]

        return {
            "before_num": len(NUMERICAL_FEATURES),
            "before_cat": len(CATEGORICAL_FEATURES),
            "before_total": len(NUMERICAL_FEATURES) + len(CATEGORICAL_FEATURES),
            "after_num": len(num_out),
            "after_cat": len(cat_out),
            "after_total": len(all_names),
            "num_feature_names": num_out,
            "cat_feature_names": cat_out,
            "all_feature_names": all_names,
        }

    @staticmethod
    def get_preprocessing_pipeline() -> ColumnTransformer:
        """
        Tạo ColumnTransformer xử lý biến liên tục và biến danh mục độc lập.
        Đảm bảo không vi phạm Data Leakage khi kết hợp vào Pipeline tổng thể.
        
        Returns:
            ColumnTransformer: Khối biến đổi sẵn sàng fit trên tập Train.
        """
        # Pipeline cho 11 biến định lượng liên tục
        num_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ])

        # Pipeline cho 13 biến định tính danh mục
        cat_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(drop="first", handle_unknown="ignore", sparse_output=False)),
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", num_pipeline, NUMERICAL_FEATURES),
                ("cat", cat_pipeline, CATEGORICAL_FEATURES),
            ],
            remainder="drop",
        )
        return preprocessor

    def split_data(
        self, df: pd.DataFrame
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Phân tách dữ liệu thành tập Huấn luyện (80%) và Kiểm thử (20%) phân tầng.
        
        Args:
            df (pd.DataFrame): Dữ liệu sạch đã gán nhãn 'target'.
            
        Returns:
            Tuple: X_train, X_test, y_train, y_test.
        """
        X = df.drop(columns=["target"])
        y = df["target"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            stratify=y,
        )
        return X_train, X_test, y_train, y_test

    def get_raw_dataset_for_table(self) -> dict:
        """
        Nạp toàn bộ 400 mẫu bệnh án gốc phục vụ bảng dữ liệu tương tác (Dataset Explorer).
        
        Returns:
            dict: Thông tin thống kê và toàn bộ danh sách 400 bản ghi bệnh án.
        """
        df_raw = pd.read_csv(self.data_path)
        
        # Làm sạch cột classification
        df_raw["classification"] = (
            df_raw["classification"]
            .astype(str)
            .str.strip()
            .str.replace("\t", "")
        )
        
        # Đảm bảo có cột id
        if "id" not in df_raw.columns:
            df_raw["id"] = range(len(df_raw))
        else:
            df_raw["id"] = df_raw["id"].fillna(0).astype(int)

        # Chuẩn hóa khoảng trắng các cột chuỗi
        for col in df_raw.columns:
            if df_raw[col].dtype == object:
                df_raw[col] = (
                    df_raw[col]
                    .astype(str)
                    .str.strip()
                    .str.replace("\t", "")
                    .replace({"nan": None, "?": None, "": None})
                )

        records = []
        for _, row in df_raw.iterrows():
            rec = {}
            for col in df_raw.columns:
                val = row[col]
                if pd.isna(val) or val is None or val == "None":
                    rec[col] = None
                else:
                    rec[col] = val
            records.append(rec)

        ckd_cnt = sum(1 for r in records if r.get("classification") == "ckd")
        notckd_cnt = sum(1 for r in records if r.get("classification") == "notckd")
        total_cnt = len(records)

        return {
            "total_count": total_cnt,
            "ckd_count": ckd_cnt,
            "notckd_count": notckd_cnt,
            "ckd_pct": round((ckd_cnt / total_cnt) * 100, 1) if total_cnt else 0,
            "notckd_pct": round((notckd_cnt / total_cnt) * 100, 1) if total_cnt else 0,
            "records": records,
        }


