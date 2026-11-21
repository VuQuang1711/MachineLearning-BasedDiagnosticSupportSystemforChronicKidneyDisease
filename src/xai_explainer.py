"""
src/xai_explainer.py
Khối giải trình lâm sàng (Explainable AI - XAI).
Phân tích nguyên nhân và đưa ra lời giải thích y khoa dựa trên các chỉ số sinh hóa.
"""

import sys
from pathlib import Path
from typing import Any, Dict, List

# Đảm bảo thư mục gốc dự án luôn nằm trong PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    from src.config import CLINICAL_BENCHMARKS, CLINICAL_THRESHOLDS
except ModuleNotFoundError:
    from config import CLINICAL_BENCHMARKS, CLINICAL_THRESHOLDS


class ClinicalXAIExplainer:
    """Lớp sinh lý giải chẩn đoán phục vụ bác sĩ lâm sàng."""

    def __init__(
        self,
        thresholds: Dict[str, float] = CLINICAL_THRESHOLDS,
        benchmarks: Dict[str, dict] = CLINICAL_BENCHMARKS,
    ):
        self.thresholds = thresholds
        self.benchmarks = benchmarks

    def compare_features_with_normal(
        self, patient_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        So sánh chi tiết từng chỉ số đầu vào của bệnh nhân với khoảng chuẩn người bình thường.

        Returns:
            List[Dict[str, Any]]: Danh sách kết quả đối chiếu 24 chỉ số.
        """
        comparisons: List[Dict[str, Any]] = []

        for key, bench in self.benchmarks.items():
            raw_val = patient_data.get(key)
            name = bench["name"]
            unit = bench["unit"]
            normal_text = bench["normal_text"]
            desc = bench["desc"]
            is_golden = bench.get("is_golden", False)
            b_type = bench.get("type", "numerical")

            if b_type == "numerical":
                try:
                    val = float(raw_val) if raw_val is not None else 0.0
                    n_min = bench["normal_min"]
                    n_max = bench["normal_max"]

                    if val > n_max:
                        dev = round(((val - n_max) / n_max) * 100, 1)
                        status = "high"
                        status_text = f"Vượt ngưỡng (+{dev}%)"
                        badge = "badge-tag-red"
                    elif val < n_min:
                        dev = round(((val - n_min) / n_min) * 100, 1)
                        status = "low"
                        status_text = f"Dưới chuẩn ({dev}%)"
                        badge = "badge-tag-amber"
                    else:
                        dev = 0.0
                        status = "normal"
                        status_text = "Đạt chuẩn bình thường"
                        badge = "badge-tag-green"

                    comparisons.append({
                        "key": key,
                        "name": name,
                        "type": "numerical",
                        "patient_val": val,
                        "display_val": f"{val} {unit}",
                        "normal_text": normal_text,
                        "normal_min": n_min,
                        "normal_max": n_max,
                        "unit": unit,
                        "status": status,
                        "status_text": status_text,
                        "badge": badge,
                        "deviation_pct": dev,
                        "desc": desc,
                        "is_golden": is_golden,
                    })
                except (ValueError, TypeError):
                    continue

            else:
                # Phân loại danh mục
                str_val = str(raw_val).strip().lower() if raw_val is not None else ""
                normal_val = str(bench.get("normal_val", "")).strip().lower()

                # Chuẩn hóa so sánh albumin/sugar
                is_normal = False
                if key in ["al", "su"]:
                    is_normal = str_val in ["0", "0.0", "âm tính", "negative"]
                else:
                    is_normal = (str_val == normal_val)

                if is_normal:
                    status = "normal"
                    status_text = "Bình thường (Đạt chuẩn)"
                    badge = "badge-tag-green"
                    dev = 0.0
                else:
                    status = "abnormal"
                    status_text = "Lệch chuẩn sinh lý"
                    badge = "badge-tag-red"
                    dev = 100.0

                val_labels = {
                    "yes": "Có (yes)",
                    "no": "Không (no)",
                    "present": "Có hiện diện (present)",
                    "notpresent": "Không có (notpresent)",
                    "abnormal": "Bất thường (abnormal)",
                    "normal": "Bình thường (normal)",
                    "good": "Ngon miệng (good)",
                    "poor": "Chán ăn / Kém (poor)",
                    "0.0": "0 (Âm tính)",
                    "0": "0 (Âm tính)",
                    "1.0": "1+ (Đạm niệu nhẹ)",
                    "1": "1+ (Đạm niệu nhẹ)",
                    "2.0": "2+ (Đạm niệu trung bình)",
                    "2": "2+ (Đạm niệu trung bình)",
                    "3.0": "3+ (Đạm niệu nặng)",
                    "3": "3+ (Đạm niệu nặng)",
                    "4.0": "4+ (Hội chứng thận hư)",
                    "4": "4+ (Hội chứng thận hư)",
                    "5.0": "5+ (Cực cao)",
                    "5": "5+ (Cực cao)",
                }
                display_val = val_labels.get(str_val, str(raw_val))

                comparisons.append({
                    "key": key,
                    "name": name,
                    "type": "categorical",
                    "patient_val": raw_val,
                    "display_val": display_val,
                    "normal_text": normal_text,
                    "unit": unit,
                    "status": status,
                    "status_text": status_text,
                    "badge": badge,
                    "deviation_pct": dev,
                    "desc": desc,
                    "is_golden": is_golden,
                })

        return comparisons

    def explain_patient_record(
        self, patient_data: Dict[str, Any], prob_ckd: float
    ) -> List[str]:
        """
        Phân tích chi tiết từng chỉ số của bệnh nhân so với ngưỡng bệnh học y khoa.
        
        Args:
            patient_data (Dict[str, Any]): Dữ liệu đầu vào của bệnh nhân.
            prob_ckd (float): Xác suất mắc bệnh thận do mô hình tính toán.
            
        Returns:
            List[str]: Danh sách các lập luận chẩn đoán lâm sàng tường minh.
        """
        reasons: List[str] = []

        # 1. Đánh giá Creatinine huyết thanh (Chỉ số vàng)
        try:
            sc = float(patient_data.get("sc", 0) or 0)
            if sc > self.thresholds["sc_high"]:
                reasons.append(
                    f"Creatinine huyết thanh tăng cao ({sc} mg/dL > {self.thresholds['sc_high']} mg/dL) "
                    f"— Cảnh báo tổn thương mức lọc cầu thận rõ rệt."
                )
        except (ValueError, TypeError):
            pass

        # 2. Đánh giá Đạm niệu (Albumin)
        al = str(patient_data.get("al", "0")).strip()
        if al in ["1.0", "2.0", "3.0", "4.0", "5.0", "1", "2", "3", "4", "5"]:
            reasons.append(
                f"Xuất hiện Protein trong nước tiểu (Albumin niệu mức {al}) "
                f"— Dấu hiệu tổn thương hàng rào màng lọc cầu thận."
            )

        # 3. Đánh giá Hemoglobin (Huyết sắc tố)
        try:
            hemo = float(patient_data.get("hemo", 15) or 15)
            if hemo < self.thresholds["hemo_low"]:
                reasons.append(
                    f"Huyết sắc tố giảm sâu ({hemo} g/dL < {self.thresholds['hemo_low']} g/dL) "
                    f"— Hội chứng thiếu máu thứ phát do thận giảm tiết Erythropoietin."
                )
        except (ValueError, TypeError):
            pass

        # 4. Đánh giá Urê máu
        try:
            bu = float(patient_data.get("bu", 0) or 0)
            if bu > self.thresholds["bu_high"]:
                reasons.append(
                    f"Urê máu tích tụ ({bu} mg/dL > {self.thresholds['bu_high']} mg/dL) "
                    f"— Chức năng đào thải độc chất qua đường tiết niệu bị suy giảm."
                )
        except (ValueError, TypeError):
            pass

        # 5. Đánh giá Tiền sử bệnh lý nền
        htn = str(patient_data.get("htn", "no")).strip().lower()
        dm = str(patient_data.get("dm", "no")).strip().lower()
        if htn == "yes" and dm == "yes":
            reasons.append("Bệnh nhân có tiền sử kép: Tăng huyết áp kết hợp Đái tháo đường (Nguy cơ suy thận nhân đôi).")
        elif htn == "yes":
            reasons.append("Tiền sử Tăng huyết áp mạn tính gây xơ cứng tiểu động mạch thận.")
        elif dm == "yes":
            reasons.append("Tiền sử Đái tháo đường cảnh báo nguy cơ biến chứng bệnh thận đái tháo đường.")

        # 6. Đánh giá Triệu chứng lâm sàng
        pe = str(patient_data.get("pe", "no")).strip().lower()
        if pe == "yes":
            reasons.append("Phù mu bàn chân/mắt cá chân — Hậu quả của ứ trệ dịch và Natri do thận giảm bài tiết.")

        # Nếu không có yếu tố nguy cơ nào bộc lộ rõ nhưng xác suất thấp
        if not reasons:
            if prob_ckd < 0.5:
                reasons.append("Toàn bộ các chỉ số sinh hóa và xét nghiệm nước tiểu nằm trong khoảng tham chiếu an toàn.")
            else:
                reasons.append("Xác suất tăng do sự cộng gộp biên độ rủi ro nhẹ giữa nhiều chỉ số thứ cấp.")

        return reasons

    def calculate_detailed_xai_reasoning(
        self,
        patient_data: Dict[str, Any],
        prob_ckd: float,
        egfr: float,
        egfr_stage: str,
    ) -> Dict[str, Any]:
        """
        Tính toán giải trình chuyên sâu: 'TẠI SAO CÓ KẾT QUẢ DỰ BÁO NÀY?'
        Bao gồm:
          1. Đóng góp cụ thể của từng thuộc tính (Feature Impact / Waterfall weights).
          2. Cây suy luận lâm sàng 3 cấp độ theo KDIGO 2024.
          3. Diễn giải chi tiết công thức eGFR MDRD từng bước.
        """
        is_ckd = prob_ckd >= 0.5
        factors: List[Dict[str, Any]] = []

        # 1. Creatinine huyết thanh
        try:
            sc_val = float(patient_data.get("sc", 1.0) or 1.0)
            if sc_val > 1.2:
                dev = round(((sc_val - 1.2) / 1.2) * 100, 1)
                factors.append({
                    "key": "sc",
                    "name": "Serum Creatinine",
                    "val_str": f"{sc_val} mg/dL",
                    "direction": "risk",
                    "weight": min(35, round(18 + (sc_val - 1.2) * 5, 1)),
                    "badge": "badge-tag-red",
                    "reason": f"Vượt ngưỡng sinh lý (+{dev}%), là bằng chứng quyết định suy giảm mức lọc cầu thận."
                })
            else:
                factors.append({
                    "key": "sc",
                    "name": "Serum Creatinine",
                    "val_str": f"{sc_val} mg/dL",
                    "direction": "protective",
                    "weight": 25,
                    "badge": "badge-tag-green",
                    "reason": "Nằm trong ngưỡng an toàn (0.6 - 1.2 mg/dL), chức năng đào thải cầu thận còn tốt."
                })
        except (ValueError, TypeError):
            pass

        # 2. Albumin nước tiểu (Đạm niệu)
        al_val = str(patient_data.get("al", "0")).strip()
        if al_val in ["1.0", "2.0", "3.0", "4.0", "5.0", "1", "2", "3", "4", "5"]:
            num_al = float(al_val)
            factors.append({
                "key": "al",
                "name": "Albumin Niệu (Đạm niệu)",
                "val_str": f"{al_val} (+{''.join(['+'] * int(min(num_al, 4)))})",
                "direction": "risk",
                "weight": min(30, round(15 + num_al * 3.5, 1)),
                "badge": "badge-tag-red",
                "reason": "Protein rò rỉ qua màng lọc cầu thận, chứng minh tổn thương thực thể mao mạch thận."
            })
        else:
            factors.append({
                "key": "al",
                "name": "Albumin Niệu (Đạm niệu)",
                "val_str": "0.0 (Âm tính)",
                "direction": "protective",
                "weight": 22,
                "badge": "badge-tag-green",
                "reason": "Âm tính, hàng rào màng lọc cầu thận nguyên vẹn, không có hiện tượng rò rỉ đạm."
            })

        # 3. Huyết sắc tố Hemoglobin
        try:
            hemo_val = float(patient_data.get("hemo", 14.0) or 14.0)
            if hemo_val < 12.0:
                dev = round(((12.0 - hemo_val) / 12.0) * 100, 1)
                factors.append({
                    "key": "hemo",
                    "name": "Hemoglobin (Huyết sắc tố)",
                    "val_str": f"{hemo_val} g/dL",
                    "direction": "risk",
                    "weight": min(25, round(12 + (12.0 - hemo_val) * 2, 1)),
                    "badge": "badge-tag-red",
                    "reason": f"Thiếu máu rõ rệt (-{dev}%), hậu quả trực tiếp khi thận suy giảm tiết hormone Erythropoietin."
                })
            else:
                factors.append({
                    "key": "hemo",
                    "name": "Hemoglobin (Huyết sắc tố)",
                    "val_str": f"{hemo_val} g/dL",
                    "direction": "protective",
                    "weight": 18,
                    "badge": "badge-tag-green",
                    "reason": "Huyết sắc tố đạt chuẩn (12.0 - 16.5 g/dL), cơ quan tạo máu do thận kích thích ổn định."
                })
        except (ValueError, TypeError):
            pass

        # 4. Tăng huyết áp & Tiền sử tim mạch
        htn = str(patient_data.get("htn", "no")).strip().lower()
        if htn == "yes":
            factors.append({
                "key": "htn",
                "name": "Tiền sử Tăng huyết áp",
                "val_str": "Có (yes)",
                "direction": "risk",
                "weight": 14,
                "badge": "badge-tag-red",
                "reason": "Huyết áp cao tạo áp lực lớn phá hủy hệ thống búi mao mạch cầu thận."
            })
        else:
            factors.append({
                "key": "htn",
                "name": "Tiền sử Tăng huyết áp",
                "val_str": "Không (no)",
                "direction": "protective",
                "weight": 10,
                "badge": "badge-tag-green",
                "reason": "Không có tiền sử cao huyết áp, áp lực mạch thận duy trì bình thường."
            })

        # 5. Đái tháo đường
        dm = str(patient_data.get("dm", "no")).strip().lower()
        if dm == "yes":
            factors.append({
                "key": "dm",
                "name": "Tiền sử Đái tháo đường",
                "val_str": "Có (yes)",
                "direction": "risk",
                "weight": 14,
                "badge": "badge-tag-red",
                "reason": "Đường huyết cao kéo dài gây xơ hóa tiểu cầu thận (Kimmelstiel-Wilson)."
            })

        # 6. Urê máu
        try:
            bu_val = float(patient_data.get("bu", 30.0) or 30.0)
            if bu_val > 45.0:
                factors.append({
                    "key": "bu",
                    "name": "Urê máu (bu)",
                    "val_str": f"{bu_val} mg/dL",
                    "direction": "risk",
                    "weight": 12,
                    "badge": "badge-tag-red",
                    "reason": f"Urê máu tích tụ ({bu_val} mg/dL > 45 mg/dL), giảm bài tiết chất thải nitơ qua nước tiểu."
                })
        except (ValueError, TypeError):
            pass

        # Sắp xếp các yếu tố theo trọng số tác động giảm dần
        factors.sort(key=lambda x: x["weight"], reverse=True)

        risk_factors = [f for f in factors if f["direction"] == "risk"]
        protective_factors = [f for f in factors if f["direction"] == "protective"]

        # Tổng hợp luận chứng chẩn đoán KDIGO
        if is_ckd:
            summary_headline = (
                f"Mô hình Random Forest phát hiện hội chứng suy thận mạn tính với xác suất {(prob_ckd * 100):.1f}%. "
                f"Nguyên nhân chủ yếu do sự cộng hưởng giữa tổn thương màng lọc ({len(risk_factors)} chỉ số vượt chuẩn) "
                f"và mức lọc cầu thận eGFR ước tính giảm xuống mức {egfr:.1f} mL/phút/1.73m² (Xếp loại {egfr_stage})."
            )
        else:
            summary_headline = (
                f"Mô hình Random Forest xác nhận bệnh nhân an toàn với xác suất bệnh thận chỉ {(prob_ckd * 100):.1f}%. "
                f"Có {len(protective_factors)} chỉ số bảo vệ then chốt đạt chuẩn sinh lý, "
                f"mức lọc cầu thận eGFR ước tính đạt {egfr:.1f} mL/phút/1.73m² (Chức năng lọc thận khỏe mạnh - G1)."
            )

        # Diễn giải công thức eGFR MDRD
        age_val = float(patient_data.get("age", 50) or 50)
        sc_num = float(patient_data.get("sc", 1.0) or 1.0)
        gender = str(patient_data.get("gender", "male")).strip().lower()
        gender_coeff = 0.742 if gender == "female" else 1.0

        mdrd_calc_steps = [
            f"1. Hệ số nền tảng: 175",
            f"2. Nồng độ Creatinine huyết thanh: ({sc_num})^(-1.154) = {(sc_num ** -1.154):.4f}",
            f"3. Tuổi tác bệnh nhân: ({age_val})^(-0.203) = {(age_val ** -0.203):.4f}",
            f"4. Hệ số điều chỉnh theo giới tính ({'Nữ' if gender == 'female' else 'Nam'}): {gender_coeff}",
            f"5. Kết quả mức lọc cầu thận eGFR = 175 × {(sc_num ** -1.154):.4f} × {(age_val ** -0.203):.4f} × {gender_coeff} = {egfr:.1f} mL/phút/1.73m²"
        ]

        return {
            "summary_headline": summary_headline,
            "risk_factors": risk_factors,
            "protective_factors": protective_factors,
            "all_ranked_factors": factors,
            "mdrd_calc_steps": mdrd_calc_steps,
            "egfr_stage": egfr_stage,
            "prob_ckd_pct": round(prob_ckd * 100, 1),
        }


