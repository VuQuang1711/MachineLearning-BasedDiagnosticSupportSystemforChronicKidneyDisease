"""
test/MainTest_3_StressTest.py
Kiểm thử lập trình phòng thủ (Defensive Robustness) với dữ liệu khuyết thiếu hoặc ngoại lai.
"""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.model_logic import CKDPredictor


class TestDefensiveStress(unittest.TestCase):
    """Kiểm tra khả năng chịu lỗi và tự phục hồi của mô hình."""

    @classmethod
    def setUpClass(cls):
        cls.predictor = CKDPredictor()
        try:
            cls.predictor.load_model()
        except Exception:
            from src.data_loader import CKDDataLoader
            loader = CKDDataLoader()
            df = loader.load_and_clean_raw_data()
            X_tr, _, y_tr, _ = loader.split_data(df)
            cls.predictor.train_and_save(X_tr, y_tr)

    def test_missing_features_graceful_handling(self):
        """Người dùng chỉ điền 3 trường, để trống toàn bộ 21 trường còn lại."""
        partial_patient = {
            "age": 60,
            "sc": 4.5,
            "al": "2.0",
        }
        # Hệ thống không được crash, SimpleImputer phải tự động điền các trường thiếu
        result = self.predictor.predict_single_patient(partial_patient)
        self.assertIn("prediction", result)
        self.assertIn("probability_ckd", result)
        self.assertEqual(result["prediction"], 1, "Bệnh nhân có sc=4.5 và al=2.0 phải được nhận diện nguy cơ cao.")

    def test_empty_record_fallback(self):
        """Trường hợp cực đoan: Gửi một dict hoàn toàn rỗng."""
        empty_patient = {}
        result = self.predictor.predict_single_patient(empty_patient)
        self.assertIn("prediction", result)
        self.assertTrue(0.0 <= result["probability_ckd"] <= 1.0)


if __name__ == "__main__":
    unittest.main()

