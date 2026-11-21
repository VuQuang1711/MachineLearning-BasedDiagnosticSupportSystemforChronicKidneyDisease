<div align="center">

**BỘ CÔNG THƯƠNG**  
**TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG THÀNH PHỐ HỒ CHÍ MINH**  
**KHOA CÔNG NGHỆ THÔNG TIN — BỘ MÔN KHOA HỌC DỮ LIỆU**

<br>

<img src="../static/images/huit_logo.png" alt="Logo Trường Đại học Công Thương TP.HCM (HUIT)" width="150"/>

<br>

# BÁO CÁO ĐỒ ÁN KẾT THÚC HỌC PHẦN
## HỌC PHẦN: HỌC MÁY (MACHINE LEARNING)

<br>

### ĐỀ TÀI SỐ 04:
# HỆ THỐNG MÁY HỌC HỖ TRỢ CHẨN ĐOÁN BỆNH THẬN MÃN TÍNH (CHRONIC KIDNEY DISEASE — CKD)

<br>

| Thông tin học phần | Chi tiết |
| :--- | :--- |
| **Lớp học phần** | `15DHKHDL04` |
| **Năm học** | `2026 – 2027` |
| **Giảng viên hướng dẫn (GVHD)** | **ThS. Nguyễn Thị Huyền Trang** |
| **Bộ môn** | Khoa học Dữ liệu (KHDL) |

<br>

*Thành phố Hồ Chí Minh, tháng 11 năm 2026*

</div>

---

## BẢNG PHÂN CÔNG NHIỆM VỤ THÀNH VIÊN NHÓM

| STT | Họ và Tên | MSSV | Vai Trò | Nội Dung Thực Hiện Chi Tiết | Tỷ Lệ Hoàn Thành |
| :---: | :--- | :---: | :--- | :--- | :---: |
| 1 | **Võ Tấn Đạt** *(Nhóm Trưởng)* | `2045240050` | Trưởng nhóm & Kiến trúc sư hệ thống | • Điều phối kế hoạch 15 tuần theo đề cương Bộ môn KHDL – HUIT.<br>• Thiết kế kiến trúc phần mềm 3 tầng độc lập (Data – Business – Presentation).<br>• Đóng gói Pipeline nguyên khối (`ColumnTransformer` + `RandomForestClassifier`) thành tệp `models/kidney_disease_pipeline.joblib`.<br>• Tổng hợp báo cáo, rà soát chất lượng toàn dự án và chủ trì thuyết trình bảo vệ. | **100%** |
| 2 | **Triệu Thị Thu Ngân** | `2405240179` | Chuyên viên Phân tích & Trực quan hóa Dữ liệu (EDA) | • Thu thập và thẩm định bộ dữ liệu 400 mẫu bệnh án Kaggle/UCI CKD (24 đặc trưng).<br>• Phân tích thống kê mô tả, khảo sát mất cân bằng nhãn ($250/150$).<br>• Xây dựng hệ thống biểu đồ EDA: tỷ lệ khuyết thiếu, "Tam giác vàng sinh hóa" (`sc`, `hemo`, `al`, `sg`), ma trận tương quan Pearson.<br>• Biên soạn Chương 1 và Mục 3.1 – 3.2 của báo cáo. | **100%** |
| 3 | **Vũ Thế Quang** | `2045240253` | Kỹ sư Tiền xử lý & Kiểm chuẩn Chất lượng (QA) | • Làm sạch ký tự rác (`\t`, `?`), kiểm toán dữ liệu đầu vào (`duplicated`, `nunique`, cột hằng số, `id`), chuẩn hóa nhãn mục tiêu và kiểu dữ liệu.<br>• Xây dựng Pipeline tiền xử lý chống rò rỉ dữ liệu (*Data Leakage*): `SimpleImputer` (Median/Mode), `OneHotEncoder`, `StandardScaler` (`24 -> 35` chiều sạch).<br>• Thiết kế và chạy bộ 17 ca kiểm thử tự động (`test/MainTest_0` đến `MainTest_4`).<br>• Biên soạn Mục 3.3 và phần Kiểm thử trong Chương 5. | **100%** |
| 4 | **Nguyễn Đình Bảo Tấn** | `2405240270` | Kỹ sư Mô hình Học máy & Tối ưu hóa | • Nghiên cứu cơ sở toán học 6 thuật toán phân lớp (LR, RF, SVM, DT, GNB, k-NN) và giảm chiều PCA.<br>• Thực nghiệm huấn luyện mô hình Baseline, kiểm định chéo Stratified 5-Fold CV.<br>• Tinh chỉnh siêu tham số bằng `GridSearchCV`, phân tích Confusion Matrix, ROC-AUC và Error Analysis.<br>• Biên soạn Chương 2, Chương 4 và Mục 5.1 của báo cáo. | **100%** |
| 5 | **Nguyễn Thanh Nhàn** | `2405240198` | Kỹ sư Ứng dụng Web & Clinical XAI | • Xây dựng ứng dụng Web lâm sàng **HUIT Hospital CDSS** (`src/app.py`, `templates/`, `static/`).<br>• Thiết kế giao diện nhập 24 chỉ số, đồng hồ nguy cơ Half-Gauge, biểu đồ Radar sinh hóa và Dataset Explorer 400 ca bệnh.<br>• Tích hợp khối giải trình Explainable AI (XAI) và công thức lọc cầu thận eGFR MDRD chuẩn KDIGO 2024.<br>• Biên soạn Mục 5.3, Chương 6 và Tài liệu tham khảo. | **100%** |

---

## MỤC LỤC

- **DANH MỤC HÌNH ẢNH**
- **DANH MỤC BẢNG BIỂU**
- **[CHƯƠNG 1. GIỚI THIỆU VỀ BÀI TOÁN CHẨN ĐOÁN BỆNH THẬN MÃN TÍNH (CKD)](./01_Chuong_1_Gioi_Thieu_Bai_Toan.md)**
  - 1.1. Tổng quan về bài toán và bối cảnh y tế
    - 1.1.1. Tầm quan trọng của phân tích dữ liệu y tế và phát hiện sớm CKD
    - 1.1.2. Các nhóm yếu tố lâm sàng liên quan đến Bệnh thận mãn tính
  - 1.2. Mục tiêu và phạm vi nghiên cứu
    - 1.2.1. Mục tiêu phân tích đặc trưng sinh hóa và dự đoán CKD
    - 1.2.2. Phạm vi nghiên cứu trên bộ dữ liệu Kaggle / UCI CKD
- **[CHƯƠNG 2. CƠ SỞ LÝ THUYẾT VÀ CÁC THUẬT TOÁN ĐỀ XUẤT](./02_Chuong_2_Co_So_Ly_Thuyet.md)**
  - 2.1. Bài toán Phân lớp (Classification) chẩn đoán bệnh thận
    - 2.1.1. Mô hình Hồi quy Logistic (Logistic Regression)
    - 2.1.2. Mô hình Rừng ngẫu nhiên (Random Forest)
    - 2.1.3. Máy vector hỗ trợ (Support Vector Machine — SVM)
    - 2.1.4. Cây quyết định (Decision Tree — CART), Gaussian Naïve Bayes và k-NN
  - 2.2. Bài toán Giảm chiều dữ liệu (PCA)
  - 2.3. Các độ đo đánh giá mô hình trong y tế
    - 2.3.1. Ma trận nhầm lẫn và các độ đo Accuracy, Precision, Recall, F1-Score
    - 2.3.2. Đường cong ROC và chỉ số ROC-AUC
- **[CHƯƠNG 3. THIẾT LẬP THỰC NGHIỆM: BỘ DỮ LIỆU VÀ TIỀN XỬ LÝ](./03_Chuong_3_Du_Lieu_Va_Tien_Xu_Ly.md)**
  - 3.1. Mô tả bộ dữ liệu Chronic Kidney Disease (CKD)
    - 3.1.1. Nguồn gốc dữ liệu
    - 3.1.2. Tổng quan cấu trúc và phân loại 24 thuộc tính (Numerical, Categorical)
    - 3.1.3. Phân tích biến mục tiêu (`classification`)
    - 3.1.4. Đánh giá chất lượng dữ liệu (Missing values, ký tự rác, cột định danh `id`)
  - 3.2. Trực quan hóa dữ liệu (Data Visualization — EDA)
    - 3.2.1. Thống kê dữ liệu khuyết thiếu trên 24 thuộc tính
    - 3.2.2. Phân phối biến mục tiêu CKD vs Not-CKD
    - 3.2.3. Phân tích "Tam giác vàng sinh hóa" (`sc`, `hemo`, `al`, `sg`)
    - 3.2.4. Ma trận tương quan tuyến tính Pearson (Correlation Heatmap)
  - 3.3. Quy trình tiền xử lý dữ liệu chuẩn y khoa chống rò rỉ dữ liệu
    - 3.3.1. Làm sạch chuỗi rác và loại bỏ cột định danh `id`
    - 3.3.2. Chia tập dữ liệu phân tầng (Stratified Train/Test Split 80/20)
    - 3.3.3. Xử lý giá trị khuyết thiếu (Median / Mode Imputation)
    - 3.3.4. Mã hóa biến phân loại (One-Hot Encoding) và chuẩn hóa Z-Score (StandardScaler)
    - 3.3.5. Kiểm chứng phân bố dữ liệu trước và sau tiền xử lý
- **[CHƯƠNG 4. ĐÁNH GIÁ VÀ PHÂN TÍCH KẾT QUẢ SƠ BỘ (BASELINE)](./04_Chuong_4_Ket_Qua_Baseline_Va_Danh_Gia.md)**
  - 4.1. Kết quả so sánh 6 mô hình phân lớp Baseline trên tập kiểm thử
  - 4.2. Kiểm định độ ổn định bằng Stratified 5-Fold Cross-Validation
  - 4.3. Thực nghiệm phân tích thành phần chính (PCA)
- **[CHƯƠNG 5. TỐI ƯU HÓA MÔ HÌNH, GIẢI THÍCH XAI VÀ TRIỂN KHAI ỨNG DỤNG](./05_Chuong_5_Toi_Uu_Hoa_Va_Trien_Khai_Ung_Dung.md)**
  - 5.1. Tinh chỉnh siêu tham số và đánh giá chuyên sâu mô hình Random Forest
    - 5.1.1. Tối ưu hóa với `GridSearchCV`
    - 5.1.2. Ma trận nhầm lẫn, đường cong ROC-AUC và phân tích lỗi (Error Analysis)
    - 5.1.3. Độ quan trọng đặc trưng (Feature Importance — XAI)
  - 5.2. Đóng gói Pipeline `.joblib` và Kiểm thử tự động (17 Unit Tests)
  - 5.3. Triển khai ứng dụng minh họa Web HUIT Hospital CDSS
    - 5.3.1. Kiến trúc 3 tầng và giao diện người dùng (Flask + Chart.js)
    - 5.3.2. Luồng xử lý dự đoán và hậu xử lý lâm sàng eGFR MDRD (KDIGO 2024)
- **[CHƯƠNG 6. KẾT LUẬN, HƯỚNG PHÁT TRIỂN VÀ TÀI LIỆU THAM KHẢO](./06_Chuong_6_Ket_Luan_Va_Tai_Lieu_Tham_Khao.md)**
  - 6.1. Kết luận (Tổng kết 4 nội dung cốt lõi Bước 7)
  - 6.2. Hạn chế và hướng phát triển
  - 6.3. Tài liệu tham khảo
  - 6.4. Phụ lục hướng dẫn cài đặt và vận hành hệ thống

---

## DANH MỤC HÌNH ẢNH

| STT | Tên Hình Ảnh | Đường Dẫn Tệp | Chương |
| :---: | :--- | :--- | :---: |
| Hình 3.1 | Biểu đồ thống kê tỷ lệ dữ liệu khuyết thiếu trên 24 thuộc tính | `OutputForProject/MLOutput/missing_values.png` | Chương 3 |
| Hình 3.2 | Phân phối nhãn mục tiêu CKD vs Not-CKD ($N = 400$) | `OutputForProject/MLOutput/target_distribution.png` | Chương 3 |
| Hình 3.3 | Trực quan hóa 4 chỉ số sinh hóa vàng (`sc`, `hemo`, `al`, `sg`) | `OutputForProject/MLOutput/golden_biomarkers.png` | Chương 3 |
| Hình 3.4 | Ma trận tương quan Pearson giữa 11 đặc trưng định lượng và nhãn | `OutputForProject/MLOutput/correlation_matrix.png` | Chương 3 |
| Hình 3.5 | Kiểm chứng phân bố dữ liệu trước và sau chuẩn hóa Z-Score | `OutputForProject/MLOutput/data_after_preprocessing.png` | Chương 3 |
| Hình 4.1 | So sánh đa tiêu chí hiệu năng 6 mô hình học máy | `OutputForProject/MLOutput/models_comparison.png` | Chương 4 |
| Hình 4.2 | Biểu đồ phương sai tích lũy PCA (Scree Plot) và không gian 2D | `OutputForProject/MLOutput/pca_variance.png` | Chương 4 |
| Hình 5.1 | Ma trận nhầm lẫn (Confusion Matrix) của Random Forest trên 80 mẫu Test | `OutputForProject/MLOutput/confusion_matrix.png` | Chương 5 |
| Hình 5.2 | Đường cong ROC và chỉ số AUC so sánh 6 thuật toán phân lớp | `OutputForProject/MLOutput/roc_curves.png` | Chương 5 |
| Hình 5.3 | Top 10 đặc trưng lâm sàng quan trọng nhất (Feature Importance) | `OutputForProject/MLOutput/feature_importance.png` | Chương 5 |

---

## DANH MỤC BẢNG BIỂU

| STT | Tên Bảng Biểu | Chương |
| :---: | :--- | :---: |
| Bảng 0.1 | Bảng phân công nhiệm vụ 5 thành viên nhóm | Trang bìa |
| Bảng 2.1 | Ma trận nhầm lẫn nhị phân (Confusion Matrix) | Chương 2 |
| Bảng 3.1 | Mô tả chi tiết 11 thuộc tính định lượng (Numerical Features) | Chương 3 |
| Bảng 3.2 | Mô tả chi tiết 13 thuộc tính định tính (Categorical Features) | Chương 3 |
| Bảng 4.1 | Kết quả thực nghiệm so sánh 6 mô hình phân lớp trên tập Test ($n = 80$) | Chương 4 |
| Bảng 5.1 | Không gian tìm kiếm và siêu tham số tối ưu của Random Forest | Chương 5 |
| Bảng 5.2 | Top 10 đặc trưng quan trọng nhất và ý nghĩa sinh lý thận | Chương 5 |
| Bảng 5.3 | Phân độ giai đoạn suy thận mạn theo chỉ số eGFR (KDIGO 2024) | Chương 5 |
| Bảng 5.4 | Kết quả kiểm thử tự động toàn hệ thống (17 Unit Tests) | Chương 5 |
