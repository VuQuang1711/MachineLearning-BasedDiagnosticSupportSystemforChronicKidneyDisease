"""
test/MainTest_1_ModelMetrics.py
Kiểm thử ngưỡng hiệu năng mô hình y tế (Recall >= 96%, F1 >= 95%, ROC-AUC >= 0.98).
"""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.data_loader import CKDDataLoader
from src.model_logic import CKDPredictor


class TestModelMetrics(unittest.TestCase):
    """Bộ kiểm thử các thước đo chất lượng chẩn đoán y khoa."""

    @classmethod
    def setUpClass(cls):
        cls.loader = CKDDataLoader()
        cls.df = cls.loader.load_and_clean_raw_data()
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = cls.loader.split_data(cls.df)
        cls.predictor = CKDPredictor()
        cls.predictor.train_and_save(cls.X_train, cls.y_train)

    def test_medical_recall_threshold(self):
        """Tiêu chí y tế số 1: Tỷ lệ phát hiện bệnh nhân CKD (Recall) phải >= 96%."""
        metrics = self.predictor.evaluate(self.X_test, self.y_test)
        print("\n[KIỂM THỬ HIỆU NĂNG MÔ HÌNH THỰC TẾ]:")
        for k, v in metrics.items():
            print(f"  - {k}: {v * 100:.2f}%" if k != "ROC-AUC" else f"  - {k}: {v:.4f}")

        self.assertGreaterEqual(
            metrics["Recall"],
            0.96,
            "Chỉ số Recall phải đạt >= 96.0% để triệt tiêu lỗi bỏ sót bệnh nhân suy thận (False Negative)!",
        )
        self.assertGreaterEqual(
            metrics["F1-Score"],
            0.95,
            "Chỉ số F1-Score điều hòa phải đạt >= 95.0%.",
        )
        self.assertGreaterEqual(
            metrics["ROC-AUC"],
            0.98,
            "Diện tích dưới đường cong ROC-AUC phải đạt >= 0.98.",
        )


if __name__ == "__main__":
    unittest.main()

