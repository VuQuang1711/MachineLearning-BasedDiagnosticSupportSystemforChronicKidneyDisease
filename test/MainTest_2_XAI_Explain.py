"""
test/MainTest_2_XAI_Explain.py
Kiểm thử tính chính xác của khối giải trình lâm sàng XAI (Explainable AI).
"""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.xai_explainer import ClinicalXAIExplainer


class TestXAIExplainer(unittest.TestCase):
    """Bộ kiểm thử khả năng diễn giải lý do y khoa."""

    def setUp(self):
        self.explainer = ClinicalXAIExplainer()

    def test_high_creatinine_explanation(self):
        """Kiểm tra phản hồi khi bệnh nhân có Creatinine cao (> 1.4 mg/dL)."""
        patient = {
            "sc": 2.8,
            "al": "0.0",
            "hemo": 14.5,
            "htn": "no",
            "dm": "no",
        }
        reasons = self.explainer.explain_patient_record(patient, prob_ckd=0.85)
        has_creatinine_warning = any("Creatinine" in r for r in reasons)
        self.assertTrue(
            has_creatinine_warning,
            "Khối XAI bắt buộc phải cảnh báo khi Creatinine vượt ngưỡng 1.4 mg/dL.",
        )

    def test_proteinuria_explanation(self):
        """Kiểm tra phản hồi khi bệnh nhân có Albumin niệu (al >= 1)."""
        patient = {
            "sc": 1.0,
            "al": "3.0",
            "hemo": 13.0,
            "htn": "no",
            "dm": "no",
        }
        reasons = self.explainer.explain_patient_record(patient, prob_ckd=0.75)
        has_albumin_warning = any("Albumin" in r or "Protein" in r for r in reasons)
        self.assertTrue(
            has_albumin_warning,
            "Khối XAI bắt buộc phải giải trình dấu hiệu đạm niệu khi al >= 1.",
        )


if __name__ == "__main__":
    unittest.main()

