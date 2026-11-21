"""
test/MainTest_4_ClinicalBenchmarks.py
Kiểm thử chuẩn hóa khoảng tham chiếu sinh lý người bình thường và đối chiếu độ lệch lâm sàng.
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config import ALL_FEATURES, CLINICAL_BENCHMARKS
from src.xai_explainer import ClinicalXAIExplainer
from src.app import app


class TestClinicalBenchmarks(unittest.TestCase):
    """Kiểm thử bộ dữ liệu chuẩn hóa người bình thường & cơ chế đối chiếu."""

    def setUp(self):
        self.explainer = ClinicalXAIExplainer()
        self.client = app.test_client()

    def test_01_benchmarks_cover_all_24_features(self):
        """Đảm bảo tất cả 24 đặc trưng lâm sàng đều được định nghĩa chuẩn sinh lý."""
        self.assertEqual(len(CLINICAL_BENCHMARKS), 24)
        for feat in ALL_FEATURES:
            self.assertIn(feat, CLINICAL_BENCHMARKS, f"Thiếu chỉ số {feat} trong CLINICAL_BENCHMARKS")
            b = CLINICAL_BENCHMARKS[feat]
            self.assertIn("name", b)
            self.assertIn("type", b)
            self.assertIn("unit", b)
            self.assertIn("normal_text", b)
            self.assertIn("desc", b)

    def test_02_compare_severe_patient_deviations(self):
        """Kiểm thử tính toán độ lệch cho bệnh nhân suy thận nặng."""
        sample_ckd = {
            "age": 62, "bp": 85, "sc": 3.2, "bu": 58.0, "bgr": 155.0,
            "hemo": 9.5, "pcv": 30, "sod": 135.0, "pot": 4.8, "wc": 9200, "rc": 3.4,
            "sg": "1.010", "al": "3.0", "su": "1.0", "rbc": "abnormal", "pc": "abnormal",
            "pcc": "notpresent", "ba": "notpresent", "htn": "yes", "dm": "yes",
            "cad": "no", "appet": "poor", "pe": "yes", "ane": "yes"
        }

        comps = self.explainer.compare_features_with_normal(sample_ckd)
        self.assertEqual(len(comps), 24)

        comp_dict = {c["key"]: c for c in comps}

        # Creatinine 3.2 mg/dL vượt ngưỡng 1.2 mg/dL (+166.7%)
        sc = comp_dict["sc"]
        self.assertEqual(sc["status"], "high")
        self.assertGreater(sc["deviation_pct"], 100.0)
        self.assertEqual(sc["badge"], "badge-tag-red")

        # Hemoglobin 9.5 g/dL dưới chuẩn 12.0 g/dL (-20.8%)
        hemo = comp_dict["hemo"]
        self.assertEqual(hemo["status"], "low")
        self.assertLess(hemo["deviation_pct"], 0.0)
        self.assertEqual(hemo["badge"], "badge-tag-amber")

        # Tăng huyết áp (htn = yes)
        htn = comp_dict["htn"]
        self.assertEqual(htn["status"], "abnormal")
        self.assertEqual(htn["badge"], "badge-tag-red")

    def test_03_compare_healthy_person(self):
        """Kiểm thử tính toán độ lệch cho người bình thường (khỏe mạnh)."""
        sample_healthy = {
            "age": 34, "bp": 70, "sc": 0.9, "bu": 24.0, "bgr": 95.0,
            "hemo": 15.2, "pcv": 46, "sod": 142.0, "pot": 4.1, "wc": 6500, "rc": 5.1,
            "sg": "1.020", "al": "0.0", "su": "0.0", "rbc": "normal", "pc": "normal",
            "pcc": "notpresent", "ba": "notpresent", "htn": "no", "dm": "no",
            "cad": "no", "appet": "good", "pe": "no", "ane": "no"
        }

        comps = self.explainer.compare_features_with_normal(sample_healthy)
        comp_dict = {c["key"]: c for c in comps}

        # sc = 0.9 (nằm trong 0.6 - 1.2) -> normal
        sc = comp_dict["sc"]
        self.assertEqual(sc["status"], "normal")
        self.assertEqual(sc["deviation_pct"], 0.0)

        # hemo = 15.2 -> normal
        hemo = comp_dict["hemo"]
        self.assertEqual(hemo["status"], "normal")

        # htn = no -> normal
        htn = comp_dict["htn"]
        self.assertEqual(htn["status"], "normal")

    def test_04_api_benchmarks_endpoint(self):
        """Kiểm thử API GET /api/benchmarks."""
        response = self.client.get("/api/benchmarks")
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data["status"], "success")
        self.assertIn("data", json_data)
        self.assertEqual(len(json_data["data"]), 24)

    def test_05_api_predict_includes_feature_comparisons(self):
        """Kiểm thử API POST /api/predict trả về feature_comparisons đầy đủ 24 chỉ số."""
        payload = {
            "age": 55, "bp": 80, "sg": "1.020", "al": "0.0", "su": "0.0",
            "rbc": "normal", "pc": "normal", "pcc": "notpresent", "ba": "notpresent",
            "bgr": 100, "bu": 30, "sc": 1.0, "sod": 140, "pot": 4.5, "hemo": 15.0,
            "pcv": 45, "wc": 7000, "rc": 5.0, "htn": "no", "dm": "no", "cad": "no",
            "appet": "good", "pe": "no", "ane": "no"
        }
        response = self.client.post("/api/predict", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()["data"]
        self.assertIn("feature_comparisons", data)
        self.assertEqual(len(data["feature_comparisons"]), 24)

    def test_06_api_dataset_endpoint(self):
        """Kiểm thử API GET /api/dataset nạp toàn bộ 400 ca bệnh án và phân trang."""
        response = self.client.get("/api/dataset?page=1&page_size=15&classification=all")
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data["status"], "success")
        self.assertEqual(json_data["summary"]["total_count"], 400)
        self.assertEqual(json_data["summary"]["ckd_count"], 250)
        self.assertEqual(json_data["summary"]["notckd_count"], 150)
        self.assertEqual(len(json_data["records"]), 15)

        # Lọc chỉ lấy ca CKD
        res_ckd = self.client.get("/api/dataset?classification=ckd&page_size=all")
        self.assertEqual(len(res_ckd.get_json()["records"]), 250)

    def test_07_api_predict_includes_detailed_xai(self):
        """Kiểm thử giải trình chuyên sâu 'Tại sao có kết quả này?' (detailed_xai)."""
        payload = {
            "age": 62, "bp": 85, "sc": 3.2, "bu": 58.0, "bgr": 155.0,
            "hemo": 9.5, "pcv": 30, "sod": 135.0, "pot": 4.8, "wc": 9200, "rc": 3.4,
            "sg": "1.010", "al": "3.0", "su": "1.0", "rbc": "abnormal", "pc": "abnormal",
            "pcc": "notpresent", "ba": "notpresent", "htn": "yes", "dm": "yes",
            "cad": "no", "appet": "poor", "pe": "yes", "ane": "yes"
        }
        response = self.client.post("/api/predict", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()["data"]
        self.assertIn("detailed_xai", data)
        xai = data["detailed_xai"]
        self.assertIn("summary_headline", xai)
        self.assertIn("risk_factors", xai)
        self.assertIn("all_ranked_factors", xai)
        self.assertIn("mdrd_calc_steps", xai)
        self.assertGreater(len(xai["risk_factors"]), 0)


if __name__ == "__main__":
    unittest.main()

