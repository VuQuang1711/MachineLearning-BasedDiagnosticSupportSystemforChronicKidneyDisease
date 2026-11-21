# BỘ HỒ SƠ BÁO CÁO KỸ THUẬT & HỌC THUẬT ĐỒ ÁN HỌC MÁY (MACHINE LEARNING)

## ĐỀ TÀI: BT04 — CHẨN ĐOÁN BỆNH THẬN MÃN TÍNH (CHRONIC KIDNEY DISEASE - CKD)

- **Học phần:** Học Máy (Machine Learning) — Năm học: 2026–2027
- **Lớp học phần:** 15DHKHDL04
- **Giảng viên hướng dẫn (GVHD):** ThS. Nguyễn Thị Huyền Trang
- **Bộ môn:** Khoa học Dữ liệu (KHDL) — Khoa Công Nghệ Thông Tin — Trường Đại học Công Thương TP.HCM (HUIT)

---

### DANH SÁCH THÀNH VIÊN NHÓM & BẢNG PHÂN CÔNG NHIỆM VỤ CHI TIẾT
*(Áp dụng Đề cương 15 tuần & Khung Rubric đánh giá 10 điểm của Bộ môn KHDL - HUIT)*

| STT | Họ và Tên | Mã Số SV | Vai Trò Đảm Nhận | Nhiệm Vụ Chi Tiết Trong Toàn Bộ Dự Án | Chuẩn Đầu Ra (Rubric) | Tỷ Lệ Đóng Góp |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: |
| 1 | **Võ Tấn Đạt**<br>*(Nhóm Trưởng)* | **2045240050** | Trưởng nhóm & Kiến trúc sư hệ thống | • Quản lý tiến độ 15 tuần theo đề cương HUIT.<br>• Thiết kế cấu trúc kiến trúc phần mềm 3 tầng phân tách (Data - Logic - Web).<br>• Xây dựng và kiểm định Pipeline đóng gói nguyên khối `ColumnTransformer` + `RandomForestClassifier` xuất ra `models/kidney_disease_pipeline.joblib`.<br>• Tích hợp toàn bộ mã nguồn, điều phối kịch bản báo cáo và chủ trì thuyết trình bảo vệ. | **CLO2, CLO3**<br>*(3.0đ / 10đ)* | **100%** |
| 2 | **Triệu Thị Thu Ngân** | **2405240179** | Chuyên viên Khám phá & Trực quan hóa Dữ liệu | • Thu thập, kiểm tra tính toàn vẹn 400 mẫu bệnh án Kaggle/UCI CKD.<br>• Phân tích thống kê mô tả 24 biến lâm sàng, đánh giá mất cân bằng nhãn ($250/150$).<br>• Thiết lập hệ thống biểu đồ EDA chuyên sâu: "Tam giác vàng sinh hóa" (Creatinine, Hemo, Albumin), Heatmap tương quan Pearson đa biến.<br>• Phụ trách biên soạn Mục 5 báo cáo (Mô tả & Trực quan hóa dữ liệu). | **CLO1**<br>*(1.0đ / 10đ)* | **100%** |
| 3 | **Vũ Thế Quang** | **2045240253** | Kỹ sư Tiền xử lý & Kiểm chuẩn Phần mềm (QA) | • Làm sạch ký tự rác (`\t`, `?`), kiểm toán dữ liệu đầu vào (`duplicated`, `nunique`, cột hằng số, `id`), chuẩn hóa chuỗi phân loại nhãn và danh mục.<br>• Thiết kế Pipeline tiền xử lý chuẩn y khoa chống Data Leakage: SimpleImputer (Median/Mode), One-Hot Encoder, StandardScaler (`24 -> 35` chiều sạch).<br>• Xây dựng trọn bộ 17 ca kiểm thử đơn vị tự động (`test/MainTest_*.py`) kiểm tra dữ liệu, kiểm toán EDA, mô hình và độ an toàn API.<br>• Phụ trách biên soạn Mục 6 báo cáo (Quy trình tiền xử lý dữ liệu chuẩn y khoa). | **CLO1, CLO2**<br>*(2.0đ / 10đ)* | **100%** |
| 4 | **Nguyễn Đình Bảo Tấn** | **2405240270** | Kỹ sư Mô hình Học máy & Tinh chỉnh Siêu tham số | • Nghiên cứu cơ sở toán học 6 thuật toán phân lớp (RF, SVM, LR, DT, GNB, k-NN) và phương pháp giảm chiều PCA.<br>• Cài đặt thực nghiệm huấn luyện mô hình Baseline và so sánh hiệu năng.<br>• Tinh chỉnh siêu tham số tối ưu bằng `GridSearchCV` 5-Fold Stratified CV, phân tích đường cong ROC-AUC và ma trận nhầm lẫn ưu tiên độ nhạy Recall.<br>• Phụ trách biên soạn Mục 4 (Lý thuyết toán học) và Mục 7-8 (Huấn luyện & Đánh giá). | **CLO1, CLO4**<br>*(2.0đ / 10đ)* | **100%** |
| 5 | **Nguyễn Thanh Nhàn** | **2405240198** | Kỹ sư Ứng dụng Web & Trí tuệ Giải thích được (XAI) | • Phát triển ứng dụng Web lâm sàng hiện đại HUIT Hospital CDSS (`src/app.py`, `templates/`, `static/`).<br>• Xây dựng trung tâm trực quan hóa: Đồng hồ đo nguy cơ Half-Gauge, biểu đồ Radar sinh hóa, biểu đồ cột so sánh mô hình.<br>• Tích hợp khối Explainable AI (XAI): Diễn giải công thức lọc cầu thận eGFR MDRD KDIGO 2024, bảng đối chiếu 24 chỉ số bình thường Bullet Bar và Dataset Explorer 400 ca bệnh.<br>• Phụ trách biên soạn Mục 9 báo cáo (Ứng dụng minh họa) và Phụ lục. | **CLO1, CLO2, CLO3**<br>*(3.0đ / 10đ)* | **100%** |

---

### MỤC LỤC TỔNG QUAN BỘ TÀI LIỆU MARKDOWN

```
markdown/
├── README.md                                         # Tài liệu điều hướng tổng quan & Phân công nhiệm vụ (File này)
├── 01_Bao_Cao_Kich_Thuoc_Ly_Thuyet_Toan_Hoc.md       # Báo cáo Kích thước lý thuyết, Công thức toán học & Ví dụ tính tay
├── 02_Bao_Cao_Thiet_Ke_Va_Quy_Trinh_8_Buoc.md        # Báo cáo Thiết kế hệ thống & Quy trình 8 bước (Chuẩn Trường Đại Học Công Nghệ Thông Tin(UIT) - Đại Học Quốc Gia Thành Phố Hồ Chí Minh(VNUHCM))
├── 03_Cau_Truc_Thu_Muc_Va_Kien_Truc_He_Thong.md      # Cấu trúc thư mục chuẩn hóa, Sơ đồ thiết kế Mermaid & Hợp đồng API
├── 04_Huong_Dan_Ky_Thuat_Lap_Trinh_Sach_3_Tang.md    # Hướng dẫn Kỹ thuật Lập trình sạch Clean Code, Kiến trúc 3 tầng & XAI
├── 05_Kich_Ban_Thuyet_Trinh_Va_Slide_Bao_Ve.md       # Kịch bản thuyết trình 12-14 phút cho 5 thành viên & dàn ý 14 slide
└── 06_Bao_Cao_Giai_Thich_Toan_Bo_Bieu_Do_Output.md    # Giải thích chi tiết toàn bộ 10 đồ thị output y khoa & học máy
```

---

### MA TRẬN ĐỐI CHIẾU CHUẨN ĐẦU RA (CLO) & RUBRIC ĐÁNH GIÁ HUIT (THANG ĐIỂM 10)

| Tiêu Chí Đánh Giá HUIT | Chuẩn Đầu Ra | Trọng Số | Điểm | Tài Liệu Tham Chiếu Trực Tiếp | Thành Viên Phụ Trách Chính |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Tìm hiểu thuật toán học máy phù hợp** (có ví dụ minh họa) | PLO2 / CLO1 | 10% | **1.0đ** | `01_Bao_Cao_Kich_Thuoc_Ly_Thuyet_Toan_Hoc.md` *(Mục 5 & 6)* | **Nguyễn Đình Bảo Tấn** |
| **Tìm bộ dữ liệu, phân tích & trực quan hóa** (EDA) | PLO2 / CLO1 | 10% | **1.0đ** | `02_Bao_Cao_Thiet_Ke_Va_Quy_Trinh_8_Buoc.md` *(Bước 2 & 3)* | **Triệu Thị Thu Ngân** |
| **Tiền xử lý dữ liệu** (thiếu, mã hóa, chuẩn hóa, train/test) | PLO2 / CLO1 | 10% | **1.0đ** | `01_Bao_Cao...md` *(Mục 3)*, `04_Huong_Dan...md` *(Mục 2)* | **Vũ Thế Quang** |
| **Chọn thuật toán học máy giải quyết bài toán** | PLO2 / CLO1 | 10% | **1.0đ** | `01_Bao_Cao...md` *(Mục 8)*, `02_Bao_Cao...md` *(Mục 7.1)* | **Nguyễn Đình Bảo Tấn** |
| **Chia dữ liệu, xây dựng & lưu mô hình** (.joblib nguyên khối) | PLO2 / CLO2 | 20% | **2.0đ** | `02_Bao_Cao...md` *(Bước 6 & 8)*, `src/model_logic.py` | **Võ Tấn Đạt, Vũ Thế Quang** |
| **Xây dựng ứng dụng minh họa** (Web HUIT Hospital CDSS) | PLO2 / CLO1 | 20% | **2.0đ** | `03_Cau_Truc...md`, `04_Huong_Dan...md`, `src/app.py` | **Nguyễn Thanh Nhàn** |
| **Tự học & vận dụng tài liệu chuyên ngành** (KDIGO 2024, XAI) | PLO4 / CLO2 | 10% | **1.0đ** | `data/mo-ta-bo-du-lieu...md`, `04_Huong_Dan...md` | **Nguyễn Thanh Nhàn** |
| **Hình thức trình bày bài báo cáo** (chuẩn mực, không lỗi) | PLO6 / CLO3 | 10% | **1.0đ** | Bộ 5 tài liệu hoàn chỉnh tại thư mục `markdown/` | **Toàn Nhóm** |
| **Tham gia tổ chức & phối hợp làm việc nhóm** (15 tuần, thuyết trình) | PLO6 / CLO3 | 10% | **1.0đ** | `02_Bao_Cao...md` *(Kế hoạch 15 tuần)*, `05_Kich_Ban...md` | **Võ Tấn Đạt (Leader)** |
| **TỔNG CỘNG ĐIỂM TOÀN DIỆN** | **PLO1 - PLO6** | **100%** | **10.0đ** | **Đạt chuẩn xuất sắc cả 2 Giai đoạn (Tuần 8 & 14-15)** | **Cả 5 Thành Viên (100%)** |

---

### HƯỚNG DẪN XUẤT BẢN SANG FILE PDF / DOCX KHI CẦN NỘP

Các tệp tài liệu Markdown đều sử dụng cú pháp chuẩn GitHub Flavored Markdown và biểu thức toán học KaTeX/LaTeX. Sinh viên có thể:
1. Đọc trực tiếp trên GitHub / GitLab / VS Code Markdown Preview.
2. Xuất sang PDF chất lượng cao bằng tiện ích mở rộng **Markdown PDF** hoặc lệnh `pandoc`:
   ```bash
   pandoc 01_Bao_Cao_Kich_Thuoc_Ly_Thuyet_Toan_Hoc.md -o Bao_Cao_Ly_Thuyet.pdf --pdf-engine=xelatex
   ```
