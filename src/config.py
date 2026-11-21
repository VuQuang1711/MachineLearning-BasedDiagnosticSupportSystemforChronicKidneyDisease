"""
src/config.py
Cấu hình tập trung toàn bộ tham số, siêu tham số, đường dẫn và ngưỡng y tế.
"""

from pathlib import Path
from typing import Dict, List

# 1. Đường dẫn thư mục dự án
BASE_DIR: Path = Path(__file__).resolve().parent.parent
DATA_DIR: Path = BASE_DIR / "data"
MODELS_DIR: Path = BASE_DIR / "models"
OUTPUT_DIR: Path = BASE_DIR / "OutputForProject" / "MLOutput"

# Đường dẫn bộ dữ liệu ưu tiên (DatasetForProject) và mặc định (data/)
DATASET_FOR_PROJECT_PATH: Path = BASE_DIR / "DatasetForProject" / "MLDataset" / "kidney_disease.csv"
RAW_DATA_PATH: Path = DATA_DIR / "kidney_disease.csv"
CLEANED_DATA_PATH: Path = DATA_DIR / "kidney_disease_cleaned.csv"
MODEL_PIPELINE_PATH: Path = MODELS_DIR / "kidney_disease_pipeline.joblib"
METADATA_PATH: Path = MODELS_DIR / "model_metadata.json"

# 2. Định nghĩa danh sách 24 đặc trưng lâm sàng
NUMERICAL_FEATURES: List[str] = [
    "age",   # Tuổi (năm)
    "bp",    # Huyết áp (mmHg)
    "bgr",   # Đường huyết ngẫu nhiên (mg/dL)
    "bu",    # Urê máu (mg/dL)
    "sc",    # Creatinine huyết thanh (mg/dL)
    "sod",   # Natri (mEq/L)
    "pot",   # Kali (mEq/L)
    "hemo",  # Huyết sắc tố Hemoglobin (g/dL)
    "pcv",   # Thể tích khối hồng cầu (%)
    "wc",    # Số lượng bạch cầu (cells/cumm)
    "rc"     # Số lượng hồng cầu (millions/cmm)
]

CATEGORICAL_FEATURES: List[str] = [
    "sg",    # Tỷ trọng nước tiểu
    "al",    # Đạm Albumin nước tiểu
    "su",    # Đường trong nước tiểu
    "rbc",   # Tế bào hồng cầu nước tiểu
    "pc",    # Tế bào mủ
    "pcc",   # Đám tế bào mủ
    "ba",    # Vi khuẩn nước tiểu
    "htn",   # Tiền sử tăng huyết áp
    "dm",    # Tiền sử đái tháo đường
    "cad",   # Bệnh động mạch vành
    "appet", # Cảm giác thèm ăn
    "pe",    # Phù mắt cá chân
    "ane"    # Hội chứng thiếu máu
]

ALL_FEATURES: List[str] = NUMERICAL_FEATURES + CATEGORICAL_FEATURES
TARGET_COLUMN: str = "classification"

# 3. Ngưỡng cảnh báo sinh hóa lâm sàng phục vụ giải trình XAI
CLINICAL_THRESHOLDS: Dict[str, float] = {
    "sc_high": 1.4,      # Creatinine > 1.4 mg/dL là dấu hiệu suy giảm mức lọc cầu thận
    "bu_high": 50.0,     # Urê máu > 50 mg/dL là hội chứng ure huyết
    "hemo_low": 12.0,    # Hemoglobin < 12 g/dL là thiếu máu lâm sàng
    "bp_high": 130.0,    # Huyết áp tâm thu >= 130 mmHg là tăng huyết áp
    "bgr_high": 140.0    # Đường huyết ngẫu nhiên >= 140 mg/dL cảnh báo tiểu đường
}

# 4. KHOẢNG THAM CHIẾU SINH LÝ CHUẨN CỦA NGƯỜI BÌNH THƯỜNG (HEALTHY BENCHMARKS)
# Theo tiêu chuẩn Bộ Y Tế Việt Nam & Hướng dẫn Quốc tế KDIGO 2024 / WHO
CLINICAL_BENCHMARKS: Dict[str, dict] = {
    # --- 11 CHỈ SỐ SINH HÓA MÁU ---
    "age": {
        "name": "Tuổi",
        "type": "numerical",
        "unit": "năm",
        "normal_min": 18.0,
        "normal_max": 60.0,
        "normal_text": "18 - 60 tuổi",
        "desc": "Độ tuổi sinh lý trưởng thành khỏe mạnh (sau 60 tuổi eGFR giảm sinh lý ~1 mL/phút/năm)",
        "is_golden": False
    },
    "bp": {
        "name": "Huyết áp tĩnh (bp)",
        "type": "numerical",
        "unit": "mmHg",
        "normal_min": 60.0,
        "normal_max": 80.0,
        "normal_text": "60 - 80 mmHg",
        "desc": "Huyết áp tối ưu bảo vệ thận < 120/80 mmHg; >= 90 mmHg gây tổn thương vi mạch cầu thận",
        "is_golden": False
    },
    "sc": {
        "name": "Serum Creatinine (sc)",
        "type": "numerical",
        "unit": "mg/dL",
        "normal_min": 0.6,
        "normal_max": 1.2,
        "normal_text": "0.6 - 1.2 mg/dL",
        "desc": "Chỉ số vàng đánh giá chức năng lọc cầu thận. > 1.2 mg/dL cảnh báo suy thận tiến triển",
        "is_golden": True
    },
    "bu": {
        "name": "Urê máu (bu)",
        "type": "numerical",
        "unit": "mg/dL",
        "normal_min": 10.0,
        "normal_max": 45.0,
        "normal_text": "10.0 - 45.0 mg/dL",
        "desc": "Sản phẩm thoái hóa protein; > 50 mg/dL phản ánh hội chứng urê máu cao và ứ trệ chất độc",
        "is_golden": False
    },
    "bgr": {
        "name": "Đường huyết đói (bgr)",
        "type": "numerical",
        "unit": "mg/dL",
        "normal_min": 70.0,
        "normal_max": 110.0,
        "normal_text": "70.0 - 110.0 mg/dL",
        "desc": "Đường huyết ổn định; > 126 mg/dL cảnh báo đái tháo đường - nguyên nhân hàng đầu gây CKD",
        "is_golden": False
    },
    "hemo": {
        "name": "Huyết sắc tố (hemo)",
        "type": "numerical",
        "unit": "g/dL",
        "normal_min": 12.0,
        "normal_max": 16.5,
        "normal_text": "12.0 - 16.5 g/dL",
        "desc": "Chỉ số vàng huyết học. < 12 g/dL là thiếu máu mạn do thận giảm tiết hormon Erythropoietin",
        "is_golden": True
    },
    "pcv": {
        "name": "Dung tích hồng cầu (pcv)",
        "type": "numerical",
        "unit": "%",
        "normal_min": 36.0,
        "normal_max": 48.0,
        "normal_text": "36.0 - 48.0 %",
        "desc": "Tỷ lệ thể tích khối hồng cầu; < 36% phản ánh tình trạng thiếu máu hoặc ứ dịch tuần hoàn",
        "is_golden": False
    },
    "sod": {
        "name": "Natri máu (sod)",
        "type": "numerical",
        "unit": "mEq/L",
        "normal_min": 135.0,
        "normal_max": 145.0,
        "normal_text": "135.0 - 145.0 mEq/L",
        "desc": "Điện giải chính dịch ngoại bào; duy trì cân bằng thẩm thấu và huyết áp cơ thể",
        "is_golden": False
    },
    "pot": {
        "name": "Kali máu (pot)",
        "type": "numerical",
        "unit": "mEq/L",
        "normal_min": 3.5,
        "normal_max": 5.0,
        "normal_text": "3.5 - 5.0 mEq/L",
        "desc": "Điện giải nội bào tối quan trọng; > 5.0 mEq/L là tăng kali máu đe dọa ngừng tim trong suy thận",
        "is_golden": False
    },
    "wc": {
        "name": "Số lượng bạch cầu (wc)",
        "type": "numerical",
        "unit": "cells/μL",
        "normal_min": 4000.0,
        "normal_max": 10000.0,
        "normal_text": "4,000 - 10,000 cells/μL",
        "desc": "Chỉ số tế bào miễn dịch; > 10,000 cells/μL cảnh báo nhiễm trùng hoặc viêm cầu thận cấp",
        "is_golden": False
    },
    "rc": {
        "name": "Số lượng hồng cầu (rc)",
        "type": "numerical",
        "unit": "triệu/μL",
        "normal_min": 4.2,
        "normal_max": 5.8,
        "normal_text": "4.2 - 5.8 triệu/μL",
        "desc": "Mật độ hồng cầu vận chuyển oxy; suy giảm khi chức năng nội tiết của thận bị tổn thương",
        "is_golden": False
    },

    # --- 7 CHỈ SỐ PHÂN TÍCH NƯỚC TIỂU ---
    "sg": {
        "name": "Tỷ trọng nước tiểu (sg)",
        "type": "numerical",
        "unit": "tỷ trọng",
        "normal_min": 1.015,
        "normal_max": 1.025,
        "normal_text": "1.015 - 1.025",
        "desc": "Khả năng cô đặc nước tiểu của ống thận; <= 1.010 phản ánh mất chức năng cô đặc (nước tiểu đẳng trương)",
        "is_golden": False
    },
    "al": {
        "name": "Albumin niệu (al)",
        "type": "categorical",
        "unit": "mức độ",
        "normal_val": "0.0",
        "normal_text": "0.0 (Âm tính / Bình thường)",
        "desc": "Chỉ số vàng màng lọc cầu thận. >= 1+ (Đạm niệu) là bằng chứng tổn thương hàng rào mao mạch thận",
        "is_golden": True
    },
    "su": {
        "name": "Đường niệu (su)",
        "type": "categorical",
        "unit": "mức độ",
        "normal_val": "0.0",
        "normal_text": "0.0 (Âm tính)",
        "desc": "Bình thường không có đường trong nước tiểu; dương tính khi đường huyết vượt ngưỡng tái hấp thu ống thận",
        "is_golden": False
    },
    "rbc": {
        "name": "Hồng cầu niệu (rbc)",
        "type": "categorical",
        "unit": "kết quả",
        "normal_val": "normal",
        "normal_text": "normal (Bình thường / Âm tính)",
        "desc": "Xuất hiện hồng cầu trong nước tiểu (tiểu máu) gợi ý viêm cầu thận, sỏi hoặc u thận",
        "is_golden": False
    },
    "pc": {
        "name": "Tế bào mủ (pc)",
        "type": "categorical",
        "unit": "kết quả",
        "normal_val": "normal",
        "normal_text": "normal (Bình thường)",
        "desc": "Bạch cầu thoái hóa trong nước tiểu; bất thường khi có nhiễm trùng đường tiết niệu",
        "is_golden": False
    },
    "pcc": {
        "name": "Đám tế bào mủ (pcc)",
        "type": "categorical",
        "unit": "hiện diện",
        "normal_val": "notpresent",
        "normal_text": "notpresent (Không có)",
        "desc": "Các cụm tế bào mủ kết tụ; phản ánh đợt nhiễm trùng tiết niệu cấp tính",
        "is_golden": False
    },
    "ba": {
        "name": "Vi khuẩn niệu (ba)",
        "type": "categorical",
        "unit": "hiện diện",
        "normal_val": "notpresent",
        "normal_text": "notpresent (Không có vi khuẩn)",
        "desc": "Nước tiểu bình thường vô khuẩn; có vi khuẩn là bằng chứng nhiễm khuẩn tiết niệu",
        "is_golden": False
    },

    # --- 6 TIỀN SỬ BỆNH & TRIỆU CHỨNG THỰC THỂ ---
    "htn": {
        "name": "Tăng huyết áp (htn)",
        "type": "categorical",
        "unit": "tiền sử",
        "normal_val": "no",
        "normal_text": "no (Không có tiền sử)",
        "desc": "Huyết áp cao lâu năm phá hủy các tiểu cầu thận dẫn đến xơ hóa cầu thận tiến triển",
        "is_golden": False
    },
    "dm": {
        "name": "Đái tháo đường (dm)",
        "type": "categorical",
        "unit": "tiền sử",
        "normal_val": "no",
        "normal_text": "no (Không mắc)",
        "desc": "Nguyên nhân số 1 gây bệnh thận giai đoạn cuối trên toàn cầu (Bệnh thận đái tháo đường)",
        "is_golden": False
    },
    "cad": {
        "name": "Bệnh mạch vành tim (cad)",
        "type": "categorical",
        "unit": "tiền sử",
        "normal_val": "no",
        "normal_text": "no (Không có)",
        "desc": "Tổn thương mạch máu nuôi cơ tim, thường kết hợp trong hội chứng tim - thận (Cardiorenal Syndrome)",
        "is_golden": False
    },
    "appet": {
        "name": "Cảm giác thèm ăn (appet)",
        "type": "categorical",
        "unit": "triệu chứng",
        "normal_val": "good",
        "normal_text": "good (Ăn ngon miệng)",
        "desc": "Chán ăn, ăn không ngon là biểu hiện sớm của tình trạng tích tụ độc tố ure trong máu",
        "is_golden": False
    },
    "pe": {
        "name": "Phù mu bàn chân (pe)",
        "type": "categorical",
        "unit": "triệu chứng",
        "normal_val": "no",
        "normal_text": "no (Không phù nề)",
        "desc": "Dấu hiệu ứ trệ muối và nước do thận giảm bài tiết dịch, thường phù mắt cá và cẳng chân",
        "is_golden": False
    },
    "ane": {
        "name": "Hội chứng thiếu máu (ane)",
        "type": "categorical",
        "unit": "triệu chứng",
        "normal_val": "no",
        "normal_text": "no (Không thiếu máu)",
        "desc": "Da xanh, niêm mạc nhợt, mệt mỏi do thận suy giảm sản xuất Erythropoietin kích thích tủy xương",
        "is_golden": False
    }
}

# 5. Tham số tối ưu mô hình
DECISION_THRESHOLD: float = 0.50
RANDOM_STATE: int = 42
TEST_SIZE: float = 0.20

