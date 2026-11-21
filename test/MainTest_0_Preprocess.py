"""
test/MainTest_0_Preprocess.py
Kiểm thử quy trình làm sạch dữ liệu và tính độc lập chống rò rỉ dữ liệu (Data Leakage).
"""

import sys
from pathlib import Path
import unittest

# Đưa thư mục gốc dự án vào PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.data_loader import CKDDataLoader


class TestPreprocessing(unittest.TestCase):
    """Bộ kiểm thử khâu tiền xử lý dữ liệu lâm sàng."""

    def setUp(self):
        self.loader = CKDDataLoader()
        self.df = self.loader.load_and_clean_raw_data()

    def test_clean_data_shape_and_target(self):
        """Kiểm tra tổng số mẫu và cấu trúc cột nhãn."""
        self.assertEqual(len(self.df), 400, "Tổng số quan sát phải đạt đúng 400 mẫu.")
        self.assertIn("target", self.df.columns, "Cột nhãn 'target' phải được tạo thành công.")
        self.assertEqual(set(self.df["target"].unique()), {0, 1}, "Nhãn phải là nhị phân {0, 1}.")

    def test_stratified_split_independence(self):
        """Kiểm tra tỷ lệ phân tách Train/Test (80/20) và tính phân tầng nhãn."""
        X_train, X_test, y_train, y_test = self.loader.split_data(self.df)
        self.assertEqual(len(X_train), 320, "Tập Train phải chứa đúng 320 mẫu (80%).")
        self.assertEqual(len(X_test), 80, "Tập Test phải chứa đúng 80 mẫu (20%).")

        ratio_train = y_train.mean()
        ratio_test = y_test.mean()
        self.assertAlmostEqual(
            ratio_train,
            ratio_test,
            delta=0.05,
            msg="Tỷ lệ phân tầng nhãn bệnh nhân CKD giữa Train và Test phải tương đồng.",
        )

    def test_pipeline_transformation_shape(self):
        """Kiểm tra kích thước ma trận đặc trưng sau khi qua ColumnTransformer."""
        X_train, X_test, _, _ = self.loader.split_data(self.df)
        preprocessor = self.loader.get_preprocessing_pipeline()

        X_train_proc = preprocessor.fit_transform(X_train)
        X_test_proc = preprocessor.transform(X_test)

        self.assertEqual(
            X_train_proc.shape[1],
            35,
            f"Số chiều ma trận sau One-Hot phải đạt đúng 35 chiều (nhận được {X_train_proc.shape[1]}).",
        )
        self.assertEqual(
            X_test_proc.shape[1],
            35,
            "Số chiều ma trận tập Test phải khớp tuyệt đối 35 chiều.",
        )

    def test_data_audit_no_duplicates_and_no_constants(self):
        """Kiểm toán dữ liệu thô & sạch: không dòng trùng lặp, không cột hằng số, nhận diện cột id."""
        import pandas as pd

        df_raw = pd.read_csv(self.loader.data_path)
        audit = self.loader.audit_raw_data(df_raw)

        self.assertEqual(audit["duplicated_rows"], 0, "Dữ liệu thô không được có dòng trùng lặp.")
        self.assertEqual(audit["constant_cols"], [], "Dữ liệu thô không được chứa cột hằng số (nunique <= 1).")
        self.assertIn("id", audit["id_like_cols"], "Phải phát hiện cột định danh 'id' có nunique == len(df_raw).")

        self.assertNotIn("id", self.df.columns, "Cột 'id' phải bị loại bỏ sau khi làm sạch.")
        self.assertEqual(int(self.df.duplicated().sum()), 0, "Dữ liệu sạch không có dòng trùng lặp.")
        self.assertEqual(
            int((self.df.drop(columns=["target"]).nunique(dropna=True) <= 1).sum()),
            0,
            "Dữ liệu sạch không có cột hằng số.",
        )

    def test_eda_summary_and_preprocessing_breakdown(self):
        """Kiểm tra bảng eda_summary và đối chiếu số cột Trước (24) -> Sau Tiền xử lý (35)."""
        import numpy as np

        eda_summary = self.loader.build_eda_summary(self.df)
        self.assertEqual(len(eda_summary), 7, "Bảng eda_summary phải đầy đủ 7 chỉ tiêu kiểm toán.")

        X_train, X_test, _, _ = self.loader.split_data(self.df)
        preprocessor = self.loader.get_preprocessing_pipeline()
        X_train_proc = preprocessor.fit_transform(X_train)
        X_test_proc = preprocessor.transform(X_test)

        summary = self.loader.get_preprocessing_summary(preprocessor)
        self.assertEqual(summary["before_num"], 11)
        self.assertEqual(summary["before_cat"], 13)
        self.assertEqual(summary["before_total"], 24)
        self.assertEqual(summary["after_num"], 11)
        self.assertEqual(summary["after_cat"], 24)
        self.assertEqual(summary["after_total"], 35)
        self.assertEqual(len(summary["all_feature_names"]), 35)
        self.assertEqual(int(np.isnan(X_train_proc).sum()), 0, "Train sau tiền xử lý phải có 0 ô NaN.")
        self.assertEqual(int(np.isnan(X_test_proc).sum()), 0, "Test sau tiền xử lý phải có 0 ô NaN.")


if __name__ == "__main__":
    unittest.main()

