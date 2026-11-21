"""
src/model_logic.py
Lớp CKDPredictor: Đóng gói huấn luyện, đánh giá, tuần tự hóa bằng joblib
và cung cấp phương thức suy luận dự báo an toàn cho 1 bệnh nhân.
"""

import sys
from pathlib import Path
from typing import Any, Dict
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.pipeline import Pipeline

# Đảm bảo thư mục gốc dự án luôn nằm trong PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    from src.config import (
        ALL_FEATURES,
        CATEGORICAL_FEATURES,
        DECISION_THRESHOLD,
        MODEL_PIPELINE_PATH,
        NUMERICAL_FEATURES,
        RANDOM_STATE,
    )
    from src.data_loader import CKDDataLoader
    from src.xai_explainer import ClinicalXAIExplainer
except ModuleNotFoundError:
    from config import (
        ALL_FEATURES,
        CATEGORICAL_FEATURES,
        DECISION_THRESHOLD,
        MODEL_PIPELINE_PATH,
        NUMERICAL_FEATURES,
        RANDOM_STATE,
    )
    from data_loader import CKDDataLoader
    from xai_explainer import ClinicalXAIExplainer


class CKDPredictor:
    """Lớp điều khiển huấn luyện và suy luận mô hình chẩn đoán CKD."""

    def __init__(self, model_path: Path = MODEL_PIPELINE_PATH):
        self.model_path = model_path
        self.pipeline: Pipeline = None
        self.xai = ClinicalXAIExplainer()

    def train_and_save(
        self, X_train: pd.DataFrame, y_train: pd.Series
    ) -> Pipeline:
        """
        Khởi tạo Pipeline scikit-learn nguyên khối, huấn luyện và lưu ra đĩa cứng.
        """
        preprocessor = CKDDataLoader.get_preprocessing_pipeline()

        # Khởi tạo mô hình Random Forest tối ưu (đồng bộ 100% với GridSearchCV chống Overfitting)
        classifier = RandomForestClassifier(
            criterion="entropy",
            n_estimators=100,
            max_depth=5,
            min_samples_split=6,
            min_samples_leaf=3,
            random_state=RANDOM_STATE,
        )

        # Đóng gói nguyên khối End-to-End
        self.pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", classifier),
        ])

        self.pipeline.fit(X_train, y_train)

        # Tạo thư mục cha nếu chưa tồn tại
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.pipeline, str(self.model_path))
        print(f"[INFO] Huấn luyện và lưu Pipeline thành công tại: {self.model_path}")
        return self.pipeline

    def load_model(self) -> None:
        """Nạp Pipeline từ tệp nhị phân joblib."""
        if not self.model_path.exists():
            raise FileNotFoundError(f"Không tìm thấy mô hình tại: {self.model_path}. Vui lòng huấn luyện trước!")
        self.pipeline = joblib.load(str(self.model_path))

    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> Dict[str, float]:
        """Đánh giá toàn diện các chỉ số y tế trên tập Test độc lập."""
        if self.pipeline is None:
            self.load_model()

        y_pred = self.pipeline.predict(X_test)
        y_proba = self.pipeline.predict_proba(X_test)[:, 1]

        metrics = {
            "Accuracy": float(accuracy_score(y_test, y_pred)),
            "Precision": float(precision_score(y_test, y_pred, zero_division=0)),
            "Recall": float(recall_score(y_test, y_pred, zero_division=0)),
            "F1-Score": float(f1_score(y_test, y_pred, zero_division=0)),
            "ROC-AUC": float(roc_auc_score(y_test, y_proba)),
        }
        return metrics

    @staticmethod
    def _normalize_patient_dataframe(patient_dict: Dict[str, Any]) -> pd.DataFrame:
        """
        Chuẩn hóa dữ liệu đầu vào 1 bệnh nhân khớp 100% định dạng lúc huấn luyện:
        - Chuyển None/chuỗi rỗng sang np.nan để SimpleImputer xử lý chuẩn xác.
        - Chuẩn hóa chuỗi số cho các cột phân loại ('sg', 'al', 'su') như '1.020' -> '1.02', '0' -> '0.0'.
        - Ép kiểu số thực cho 11 biến định lượng.
        """
        row: Dict[str, Any] = {}
        for col in ALL_FEATURES:
            val = patient_dict.get(col, np.nan)
            if val is None or (isinstance(val, str) and val.strip() in ("", "?", "nan", "None")):
                row[col] = np.nan
            elif col in NUMERICAL_FEATURES:
                try:
                    row[col] = float(str(val).strip())
                except (ValueError, TypeError):
                    row[col] = np.nan
            elif col in ("sg", "al", "su"):
                try:
                    row[col] = str(float(str(val).strip()))
                except (ValueError, TypeError):
                    row[col] = str(val).strip()
            else:
                row[col] = str(val).strip().lower()
        df_row = pd.DataFrame([row], columns=ALL_FEATURES)
        for col in CATEGORICAL_FEATURES:
            df_row[col] = df_row[col].astype(object)
        return df_row

    def predict_single_patient(self, patient_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Dự đoán cho 1 bệnh nhân từ dữ liệu JSON của Web và sinh báo cáo XAI.
        """
        if self.pipeline is None:
            self.load_model()

        # Tạo DataFrame chuẩn hóa đúng 24 cột
        df_input = self._normalize_patient_dataframe(patient_dict)

        # Suy luận xác suất
        prob_ckd = float(self.pipeline.predict_proba(df_input)[0][1])
        prediction = int(prob_ckd >= DECISION_THRESHOLD)

        # Xác định cấp độ rủi ro y khoa
        if prob_ckd >= 0.80:
            risk_level = "Nguy cơ Rất Cao (Critical Risk)"
            recommendation = "Cần chuyển tuyến bác sĩ chuyên khoa thận - tiết niệu ngay lập tức để làm xét nghiệm sinh thiết/chức năng thận."
        elif prob_ckd >= 0.50:
            risk_level = "Nguy cơ Trung Bình (Moderate Risk)"
            recommendation = "Nghi ngờ có tổn thương chức năng lọc thận. Khuyến nghị làm lại xét nghiệm nước tiểu và theo dõi huyết áp."
        else:
            risk_level = "Nguy cơ Thấp (Low Risk / Healthy)"
            recommendation = "Các chỉ số hiện tại ở ngưỡng an toàn. Duy trì lối sống lành mạnh và khám sức khỏe định kỳ hàng năm."

        label = "BỆNH THẬN MÃN TÍNH (CKD)" if prediction == 1 else "BÌNH THƯỜNG (NOT CKD)"

        # Tính toán mức lọc cầu thận ước tính (eGFR) theo phương trình chuẩn MDRD y khoa
        try:
            sc_val = float(patient_dict.get("sc", 1.0) or 1.0)
            age_val = float(patient_dict.get("age", 50.0) or 50.0)
            gender = str(patient_dict.get("gender", "male")).strip().lower()
            gender_coeff = 0.742 if gender == "female" else 1.0
            if sc_val > 0 and age_val > 0:
                egfr_val = round(175.0 * (sc_val ** -1.154) * (age_val ** -0.203) * gender_coeff, 1)
            else:
                egfr_val = 90.0
        except Exception:
            egfr_val = 90.0

        if egfr_val >= 90:
            egfr_stage = "G1 (Bình thường / Nguy cơ thấp)"
        elif egfr_val >= 60:
            egfr_stage = "G2 (Tổn thương mức độ nhẹ)"
        elif egfr_val >= 45:
            egfr_stage = "G3a (Suy giảm mức lọc nhẹ - vừa)"
        elif egfr_val >= 30:
            egfr_stage = "G3b (Suy giảm mức lọc vừa - nặng)"
        elif egfr_val >= 15:
            egfr_stage = "G4 (Suy giảm mức lọc rất nặng)"
        else:
            egfr_stage = "G5 (Suy thận giai đoạn cuối - ESRD)"

        # Sinh lời giải trình từ khối XAI
        xai_rationale = self.xai.explain_patient_record(patient_dict, prob_ckd)

        # So sánh chi tiết từng chỉ số đầu vào với khoảng chuẩn người bình thường
        feature_comparisons = self.xai.compare_features_with_normal(patient_dict)

        # Giải trình chuyên sâu: Tại sao mô hình đưa ra kết quả như vậy?
        detailed_xai = self.xai.calculate_detailed_xai_reasoning(
            patient_dict, prob_ckd, egfr_val, egfr_stage
        )

        return {
            "prediction": prediction,
            "label": label,
            "probability_ckd": round(prob_ckd, 4),
            "confidence_percentage": round(prob_ckd * 100, 2) if prediction == 1 else round((1 - prob_ckd) * 100, 2),
            "risk_level": risk_level,
            "egfr": egfr_val,
            "egfr_stage": egfr_stage,
            "recommendation": recommendation,
            "xai_rationale": xai_rationale,
            "feature_comparisons": feature_comparisons,
            "detailed_xai": detailed_xai,
        }

