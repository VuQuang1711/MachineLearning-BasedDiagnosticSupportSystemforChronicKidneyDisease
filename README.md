# HỆ THỐNG MÁY HỌC HỖ TRỢ CHẨN ĐOÁN BỆNH THẬN MÃN TÍNH (CKD)

**Mã đề tài:** BT04 — Chẩn Đoán Bệnh Thận (Kidney Disease Diagnosis)  
**Học phần:** Học Máy (Machine Learning) — Năm học: 2026–2027  
**Lớp học phần:** 15DHKHDL04  
**Giảng viên hướng dẫn (GVHD):** ThS. Nguyễn Thị Huyền Trang  
**Bộ môn:** Khoa học Dữ liệu (KHDL) — Khoa Công Nghệ Thông Tin — Trường Đại học Công Thương TP.HCM (HUIT)  
**Tập dữ liệu:** Kaggle / UCI Chronic Kidney Disease Dataset ($N = 400$, $D = 24$)

---

## 👥 THÀNH VIÊN NHÓM & BẢNG PHÂN CÔNG NHIỆM VỤ CHI TIẾT

*(Thiết kế theo Đề cương chi tiết học phần 15 tuần & Khung đánh giá Rubric 10 điểm của Bộ môn Khoa học Dữ liệu - HUIT)*

### 1. Bảng Phân Công Nhiệm Vụ & Đánh Giá Đóng Góp

| STT | Họ và Tên | Mã Số SV | Vai Trò Đảm Nhận | Nhiệm Vụ Chi Tiết Trong Toàn Bộ Dự Án | Chuẩn Đầu Ra (Rubric) | Tỷ Lệ Hoàn Thành |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: |
| 1 | **Võ Tấn Đạt**<br>*(Nhóm Trưởng)* | **2045240___** | Trưởng nhóm & Kiến trúc sư hệ thống *(Team Lead & System Architect)* | • Điều phối tiến độ 15 tuần theo đúng kế hoạch đề cương HUIT.<br>• Thiết kế cấu trúc kiến trúc phần mềm 3 tầng phân tách độc lập (Data - Logic - Web).<br>• Xây dựng và kiểm chuẩn Pipeline đóng gói nguyên khối `ColumnTransformer` + `RandomForestClassifier` xuất file `models/kidney_disease_pipeline.joblib`.<br>• Tích hợp toàn bộ mã nguồn, điều phối kịch bản báo cáo và chủ trì thuyết trình bảo vệ đồ án. | **CLO2, CLO3**<br>*(3.0đ / 10đ)* | **100%** |
| 2 | **Triệu Thị Thu Ngân** | **2405240___** | Chuyên viên Khám phá & Trực quan hóa Dữ liệu *(Data Analyst & EDA)* | • Thu thập, kiểm tra tính toàn vẹn 400 mẫu bệnh án Kaggle/UCI CKD.<br>• Phân tích thống kê mô tả 24 biến lâm sàng, đánh giá mất cân bằng nhãn ($250/150$).<br>• Thiết lập hệ thống biểu đồ EDA chuyên sâu: "Tam giác vàng sinh hóa" (Creatinine, Hemo, Albumin), Heatmap tương quan Pearson đa biến.<br>• Phụ trách biên soạn Mục 5 báo cáo (Mô tả & Trực quan hóa dữ liệu). | **CLO1**<br>*(1.0đ / 10đ)* | **100%** |
| 3 | **Vũ Thế Quang** | **2045240___** | Kỹ sư Tiền xử lý & Kiểm chuẩn Phần mềm *(Data Preprocessing & QA Engineer)* | • Làm sạch ký tự rác (`\t`, `?`), kiểm toán dữ liệu đầu vào (`duplicated`, `nunique`, cột hằng số, `id`), chuẩn hóa chuỗi phân loại nhãn và danh mục.<br>• Thiết kế Pipeline tiền xử lý chuẩn y khoa chống rò rỉ dữ liệu (*Data Leakage*): SimpleImputer (Median/Mode), One-Hot Encoder, StandardScaler (`24 -> 35` chiều sạch).<br>• Xây dựng trọn bộ 17 ca kiểm thử đơn vị tự động (`test/MainTest_*.py`) kiểm tra dữ liệu, kiểm toán EDA, mô hình và độ an toàn API.<br>• Phụ trách biên soạn Mục 6 báo cáo (Quy trình tiền xử lý dữ liệu chuẩn y khoa). | **CLO1, CLO2**<br>*(2.0đ / 10đ)* | **100%** |
| 4 | **Nguyễn Đình Bảo Tấn** | **2405240___** | Kỹ sư Mô hình Học máy & Tối ưu hóa Siêu tham số *(ML Modeling & Tuning)* | • Nghiên cứu cơ sở toán học 6 thuật toán phân lớp (RF, SVM, LR, DT, GNB, k-NN) và phương pháp giảm chiều PCA.<br>• Cài đặt thực nghiệm huấn luyện mô hình Baseline và so sánh hiệu năng.<br>• Tinh chỉnh siêu tham số tối ưu bằng `GridSearchCV` 5-Fold Stratified CV, phân tích đường cong ROC-AUC và ma trận nhầm lẫn ưu tiên độ nhạy Recall.<br>• Phụ trách biên soạn Mục 4 (Lý thuyết toán học) và Mục 7-8 (Huấn luyện & Đánh giá). | **CLO1, CLO4**<br>*(2.0đ / 10đ)* | **100%** |
| 5 | **Nguyễn Thanh Nhàn** | **2405240___** | Kỹ sư Ứng dụng & Trí tuệ Nhân tạo Giải thích được *(Fullstack Web & Clinical XAI)* | • Phát triển ứng dụng Web lâm sàng hiện đại HUIT Hospital CDSS (`src/app.py`, `templates/`, `static/`).<br>• Xây dựng trung tâm trực quan hóa: Đồng hồ đo nguy cơ Half-Gauge, biểu đồ Radar sinh hóa, biểu đồ cột so sánh mô hình.<br>• Tích hợp khối Explainable AI (XAI): Diễn giải công thức lọc cầu thận eGFR MDRD KDIGO 2024, bảng đối chiếu 24 chỉ số bình thường Bullet Bar và Dataset Explorer 400 ca bệnh.<br>• Phụ trách biên soạn Mục 9 báo cáo (Ứng dụng minh họa) và Phụ lục. | **CLO1, CLO2, CLO3**<br>*(3.0đ / 10đ)* | **100%** |

---

### 2. Kế Hoạch Triển Khai 15 Tuần Chuẩn Đề Cương HUIT

```mermaid
gantt
    title KẾ HOẠCH THỰC HIỆN ĐỒ ÁN HỌC MÁY 15 TUẦN — LỚP 15DHKHDL04
    dateFormat  YYYY-MM-DD
    section Giai đoạn 1: Khởi động & Nộp Báo cáo Tiến độ (20%)
    Tuần 1 - 3: Nghiên cứu đề tài & Tìm hiểu lý thuyết 6 thuật toán      :2026-09-01, 21d
    Tuần 4 - 6: Thu thập dữ liệu, EDA trực quan & Tiền xử lý chống rò rỉ:2026-09-22, 21d
    Tuần 7 - 8: Huấn luyện Baseline & NỘP BÁO CÁO TIẾN ĐỘ TUẦN 8 (20%)  :2026-10-13, 14d
    section Giai đoạn 2: Tối ưu hóa, Triển khai & Báo cáo Hoàn chỉnh (80%)
    Tuần 9 - 10: Tinh chỉnh GridSearchCV, 5-Fold CV & Lưu mô hình Joblib :2026-10-27, 14d
    Tuần 11 - 12: Xây dựng Web App HUIT Hospital CDSS & Khối giải trình XAI:2026-11-10, 14d
    Tuần 13 - 14: Bộ kiểm thử tự động, Viết báo cáo & NỘP BÀI TUẦN 14  :2026-11-24, 14d
    Tuần 15: THUYẾT TRÌNH & BẢO VỆ ĐỒ ÁN TRƯỚC HỘI ĐỒNG                 :2026-12-08, 7d
```

---

## 1. GIỚI THIỆU TỔNG QUAN HỆ THỐNG

Bệnh thận mãn tính (*Chronic Kidney Disease* - CKD) là bệnh lý nguy hiểm tiến triển âm thầm, thường chỉ bộc lộ triệu chứng khi thận đã tổn thương nặng. Đồ án xây dựng một hệ thống học máy toàn diện hỗ trợ sàng lọc và phát hiện sớm nguy cơ CKD dựa trên 24 chỉ số xét nghiệm sinh hóa máu, phân tích nước tiểu và tiền sử bệnh lý, tích hợp giao diện quản lý bệnh viện **HUIT HOSPITAL** (Trường Đại học Công Thương TP.HCM).

Hệ thống được thiết kế theo chuẩn kỹ thuật công nghiệp & y tế:
- **Kiến trúc phần mềm 3 tầng (3-Tier Architecture):** Tách biệt rạch ròi giữa Data Layer, Business/Model Logic Layer và Presentation Layer (Flask Web API).
- **Hệ thống Quản lý Bệnh viện (HIS & CDSS):** Quản lý danh sách 5 bệnh nhân tiếp nhận mẫu, hồ sơ hành chính EMR, phân tích 24 chỉ số cận lâm sàng và in ấn bệnh án điện tử chuẩn y tế.
- **Trực quan hóa Dữ liệu Hiện đại (Data Visualization):**
  - **Đồng hồ đo nguy cơ CKD (Half-Gauge Chart):** Kim đo xác suất động với dải màu an toàn $\to$ cảnh báo.
  - **Biểu đồ Radar đa chiều sinh hóa (Biomarker Radar):** Đối chiếu 6 chỉ số sinh tồn của bệnh nhân với ngưỡng an toàn.
  - **Trung tâm Phân tích Trực quan (Visual Analytics Hub):** Biểu đồ so sánh 6 mô hình ML, biểu đồ tầm quan trọng đặc trưng (Feature Importance), thư viện đồ thị ROC / Confusion Matrix / PCA với cửa sổ phóng to Lightbox Modal.
- **Quy trình chuẩn hóa chống rò rỉ dữ liệu (Data Leakage):** Pipeline `ColumnTransformer` tích hợp `SimpleImputer` (Median cho biến số, Mode cho biến danh mục), `StandardScaler` và `OneHotEncoder`.
- **Đóng gói mô hình nguyên khối:** Xuất bản mô hình thành tệp nhị phân duy nhất `models/kidney_disease_pipeline.joblib`.
- **Trí tuệ Nhân tạo Giải thích được (Clinical XAI Engine — Tại sao có kết quả này?):** Phân tích cơ chế suy luận 3 cấp độ (Màng lọc cầu thận, Tốc độ lọc eGFR, Biến chứng toàn thân), diễn giải từng bước thế số công thức MDRD, và biểu đồ thanh đo trọng số tác động của từng chỉ số lâm sàng (Feature Impact Waterfall).
- **Đối chiếu 24 Chỉ số Lâm sàng với Khoảng chuẩn Sinh lý:** Bảng đối chiếu tự động so sánh từng giá trị của người bệnh với ngưỡng chuẩn người bình thường (KDIGO 2024 & Bộ Y Tế), tính toán phần trăm độ lệch và hiển thị thanh đo trực quan Bullet Range Bar.
- **Kho Dữ liệu Gốc 400 Ca Bệnh án (Dataset Explorer):** Trình duyệt toàn bộ 400 mẫu bệnh án với bộ lọc phân loại (CKD / NotCKD), tìm kiếm nhanh và nút bấm **"⚡ Chọn Phân Tích"** trên từng dòng để nạp và dự đoán tức thì.
- **Kê đơn thuốc & Phác đồ điều trị KDIGO:** Tự động gợi ý đơn thuốc thông minh (Losartan, Forxiga, Sắt/EPO, Furosemide) và chế độ ăn nhạt, giảm đạm.

---

## 2. KẾT QUẢ THỰC NGHIỆM ĐÁNH GIÁ 6 MÔ HÌNH

Đo đạc thực tế trên tập kiểm thử độc lập ($80$ bệnh nhân, gồm $30$ ca đối chứng và $50$ ca bệnh):

| Thuật toán Phân lớp | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | ROC-AUC | Đánh giá Lâm sàng |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gaussian Naïve Bayes** | 100.00% | 100.00% | **100.00%** | 100.00% | 1.0000 | Phân tách xuất sắc trên mẫu Test (nhưng vi phạm giả định độc lập) |
| **SVM (RBF Kernel)** | 98.75% | 100.00% | **98.00%** | 98.99% | 0.9993 | Không có báo động giả (FP=0), 1 FN |
| **Logistic Regression** | 97.50% | 100.00% | **96.00%** | 97.96% | 0.9987 | Hệ số tường minh, suy luận siêu nhanh |
| **Random Forest (Selected)** | 96.25% | 97.96% | **96.00%** | 96.97% | 0.9980 | **Mô hình triển khai chính thức (CV Recall 98.50% ± 1.22%, hỗ trợ XAI)** |
| **Decision Tree (CART)** | 95.00% | 97.92% | **94.00%** | 95.92% | 0.9687 | Trực quan dạng cây, 3 FN |
| **k-NN ($k=5$)** | 92.50% | 100.00% | **88.00%** | 93.62% | 0.9887 | Bị loãng khoảng cách do 35 chiều |

> [!IMPORTANT]
> Trong y tế, chỉ số **Recall** (Độ nhạy phát hiện bệnh) được ưu tiên hàng đầu để triệt tiêu lỗi bỏ sót bệnh nhân suy thận (*False Negative*). Toàn bộ các mô hình chính đều đạt $\text{Recall} \ge 96.0\%$.

---

## 3. HƯỚNG DẪN CÀI ĐẶT & KHỞI CHẠY HỆ THỐNG

### 3.1. Cài đặt Môi trường
Yêu cầu Python $\ge 3.10$ (khuyến nghị Python 3.11 hoặc 3.13).

```bash
# Cài đặt toàn bộ thư viện phụ thuộc
pip install -r requirements.txt
```

Notebook thực nghiệm cũng dùng cùng bộ thư viện trên. Mở notebook bằng Jupyter:
```bash
python -m notebook notebooks/Kidney_Disease_EDA_and_Modeling.ipynb
```

Nếu thiếu dữ liệu cục bộ, ứng dụng/notebook có thể tải dữ liệu qua KaggleHub; khi đó cần kết nối Internet.

### 3.2. Khởi chạy Ứng dụng Web Lâm sàng
```bash
# Khởi động máy chủ Flask
python src/app.py
```
Sau đó truy cập trình duyệt tại địa chỉ: **`http://localhost:5000`**

- Giao diện hỗ trợ điền đầy đủ **24 thông số lâm sàng** chia làm 3 nhóm trực quan.
- Có sẵn danh sách tiếp nhận 5 bệnh nhân và bảng **Dataset Explorer 400 ca** để nạp phân tích 1-click.
- Xem bảng thông tin thành viên và phân công nhiệm vụ ngay tại menu bên trái hoặc chân trang.
- Hiển thị nhãn chẩn đoán, thanh đo phần trăm xác suất rủi ro, khối giải trình y khoa XAI và xuất phiếu khám bệnh A4.

### 3.3. Chạy Toàn bộ Bộ Kiểm thử Tự động (Unit Test Suites)
```bash
# Chạy toàn bộ 17 ca kiểm thử đơn vị tự động trong thư mục test/
python -B -m unittest discover -s test -p "MainTest_*.py" -v
```

---

## 4. BỘ HỒ SƠ TÀI LIỆU HỌC THUẬT (MARKDOWN)

Toàn bộ các bản báo cáo học thuật chuyên sâu đáp ứng chuẩn đầu ra môn học CLO1, CLO2, CLO3, CLO4 được lưu tại thư mục [`markdown/`](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown):

- **[markdown/README.md](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown/README.md)**: Bảng ma trận đối chiếu ánh xạ 100% tiêu chí Rubric chấm thi 10 điểm của HUIT.
- **[01_Bao_Cao_Kich_Thuoc_Ly_Thuyet_Toan_Hoc.md](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown/01_Bao_Cao_Kich_Thuoc_Ly_Thuyet_Toan_Hoc.md)**: Báo cáo ma trận kích thước, công thức toán học 6 thuật toán, PCA/LDA và **ví dụ tính toán bằng tay (Hand Calculation)** chi tiết cho $k$-NN, Naïve Bayes, Gini Tree.
- **[02_Bao_Cao_Thiet_Ke_Va_Quy_Trinh_8_Buoc.md](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown/02_Bao_Cao_Thiet_Ke_Va_Quy_Trinh_8_Buoc.md)**: Quy trình 8 bước phát triển dự án Máy học theo chuẩn Trường Đại Học Công Nghệ Thông Tin(UIT) - Đại Học Quốc Gia Thành Phố Hồ Chí Minh(VNUHCM), **4 câu hỏi bắt buộc của Bước 7**, phân tích lỗi chuyên sâu (*Error Analysis*) trên 3 ca bệnh án cụ thể, kế hoạch nhóm 15 tuần.
- **[03_Cau_Truc_Thu_Muc_Va_Kien_Truc_He_Thong.md](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown/03_Cau_Truc_Thu_Muc_Va_Kien_Truc_He_Thong.md)**: Sơ đồ kiến trúc 3 tầng, Activity Diagram, Sequence Diagram, Class Diagram và hợp đồng giao tiếp API.
- **[04_Huong_Dan_Ky_Thuat_Lap_Trinh_Sach_3_Tang.md](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown/04_Huong_Dan_Ky_Thuat_Lap_Trinh_Sach_3_Tang.md)**: Hướng dẫn Clean Code, mã nguồn Web 24 trường lâm sàng, bộ test tự động và cẩm nang câu hỏi phản biện bảo vệ đồ án.
- **[05_Kich_Ban_Thuyet_Trinh_Va_Slide_Bao_Ve.md](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown/05_Kich_Ban_Thuyet_Trinh_Va_Slide_Bao_Ve.md)**: Kịch bản thuyết trình từng phút (12-14 phút), phân vai 5 thành viên nhóm và cấu trúc chi tiết 14 slide bảo vệ đồ án trước Hội đồng chấm thi.
- **[06_Bao_Cao_Giai_Thich_Toan_Bo_Bieu_Do_Output.md](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/markdown/06_Bao_Cao_Giai_Thich_Toan_Bo_Bieu_Do_Output.md)**: Báo cáo giải thích chi tiết toàn bộ 10 biểu đồ output y khoa và học máy (Missing Values, EDA, ROC Curves, Confusion Matrix, Feature Importance, PCA).
