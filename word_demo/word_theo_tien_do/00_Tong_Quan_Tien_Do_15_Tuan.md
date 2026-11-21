# TỔNG QUAN BÁO CÁO TIẾN ĐỘ THỰC HIỆN ĐỒ ÁN 15 TUẦN

**Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)  
**Học phần:** Học Máy (Machine Learning) — Năm học: 2026–2027  
**Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang  
**Đơn vị:** Bộ môn Khoa học Dữ liệu (KHDL) — Trường Đại học Công Thương TP.HCM (HUIT)  

---

## 1. CĂN CỨ VÀ QUY ĐỊNH ĐÁNH GIÁ (THEO VĂN BẢN YÊU CẦU BỘ MÔN KHDL)

Theo văn bản **"Yêu cầu chung và Kế hoạch thực hiện đồ án kết thúc học phần: Học máy — Năm học 2026–2027"** của Bộ môn KHDL – HUIT:
- **Tính chất đồ án:** Đồ án thuộc phần **CUỐI KỲ (chiếm 70% tổng điểm học phần)**, thể hiện đầy đủ vòng đời của một dự án học máy (*Machine Learning Lifecycle*).
- **Hai mốc nộp bắt buộc:**
  1. **★ Mốc 1 — Giai đoạn 1 (Tuần 8, chiếm 20% điểm đồ án):** Nộp Báo cáo tiến độ thực hiện đồ án. Đánh giá theo **CLO2, CLO3**, tập trung vào: Dữ liệu đã xác nhận, kết quả trực quan hóa EDA, định hướng thuật toán rõ ràng và kế hoạch tự học/phối hợp nhóm.
  2. **★ Mốc 2 — Giai đoạn 2 (Tuần 14, chiếm 80% điểm đồ án):** Nộp trọn bộ hồ sơ đồ án hoàn chỉnh gồm: File code (Jupyter Notebook/.py), File mô hình đã lưu (`.joblib`), Mã nguồn và hướng dẫn chạy ứng dụng minh họa, Báo cáo Word/PDF theo cấu trúc 12 mục, Slide thuyết trình. Đánh giá toàn diện theo **CLO1, CLO2, CLO3, CLO4**.
  3. **Thuyết trình bảo vệ (Tuần 15):** Thuyết trình trước lớp và trả lời câu hỏi phản biện, đánh giá gộp trong tiêu chí *"Tham gia tổ chức và phối hợp làm việc trong nhóm"*.

### Ma trận 8 Tiêu chí đánh giá theo Rubric Đồ án Cuối kỳ (Thang điểm 10):

| Tiêu Chí Đánh Giá (Rubric HUIT) | PLO | CLO | Trọng Số | Điểm Tối Đa | Tuần Trọng Tâm |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Thu thập dữ liệu, trực quan hóa dữ liệu** | PLO2 | CLO1 | 10% | 1.0 đ | Tuần 4, Tuần 5 |
| **2. Tiền xử lý dữ liệu, đánh giá độ tương quan của các feature** | PLO2 | CLO1 | 10% | 1.0 đ | Tuần 5, Tuần 6 |
| **3. Chọn thuật toán để giải quyết yêu cầu phân lớp hay gom cụm** | PLO2 | CLO1 | 10% | 1.0 đ | Tuần 7 |
| **4. Chia dữ liệu, xây dựng mô hình, lưu mô hình (nếu có)** | PLO2 | CLO1 | 20% | 2.0 đ | Tuần 9, Tuần 10 |
| **5. Xây dựng ứng dụng** | PLO2 | CLO1 | 20% | 2.0 đ | Tuần 11, Tuần 12 |
| **6. Tự học và vận dụng tài liệu chuyên ngành trong bài tập nhóm** | PLO4 | CLO2 | 10% | 1.0 đ | Tuần 2, Tuần 3 |
| **7. Hình thức trình bày bài báo cáo** | PLO6 | CLO3 | 10% | 1.0 đ | Tuần 13, Tuần 14 |
| **8. Tham gia tổ chức và phối hợp làm việc trong nhóm** | PLO6 | CLO3 | 10% | 1.0 đ | Tuần 1, Tuần 8, Tuần 15 |
| **TỔNG ĐIỂM ĐỒ ÁN** | | | **100%** | **10.0 đ** | **Toàn bộ 15 Tuần** |

---

## 2. BẢNG TIẾN ĐỘ CHI TIẾT 15 TUẦN THEO ĐÚNG KẾ HOẠCH BỘ MÔN

| Tuần | Nội Dung Công Việc (Chuẩn Văn Bản HUIT) | Sản Phẩm Cần Đạt | Thành Viên Chủ Trì | Liên Hệ Điểm / Rubric | Tệp Báo Cáo Chi Tiết |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **Tuần 1** | • Đăng ký đề tài trên Google Classroom<br>• Thành lập nhóm, phân công vai trò, lập kế hoạch chi tiết 15 tuần | • Đề tài đã duyệt trên Google Classroom<br>• Bản kế hoạch làm việc 15 tuần của nhóm | Võ Tấn Đạt (Leader) & Cả nhóm | Tham gia tổ chức và phối hợp làm việc trong nhóm (10%) | [Tuan_01.md](./Tuan_01.md) |
| **Tuần 2** | • Tìm hiểu lý thuyết các thuật toán học máy phân lớp (Logistic Regression, Random Forest, SVM)<br>• Đọc tài liệu y khoa chuyên ngành KDIGO | • Tài liệu tóm tắt lý thuyết 3 thuật toán chủ lực<br>• Bảng xác định hàm mất mát & điều chuẩn | Nguyễn Đình Bảo Tấn (Phối hợp: Tấn Đạt) | Tự học và vận dụng tài liệu chuyên ngành (10% — Phần 1) | [Tuan_02.md](./Tuan_02.md) |
| **Tuần 3** | • Tìm hiểu lý thuyết Decision Tree, Naïve Bayes, k-NN, giảm chiều PCA<br>• Xây dựng các ví dụ minh họa cách hoạt động của thuật toán | • Tài liệu tóm tắt đầy đủ 6 thuật toán & PCA<br>• **Bộ 3 ví dụ tính toán thủ công từng bước (Hand Calculation)** | Nguyễn Đình Bảo Tấn | Tự học và vận dụng tài liệu chuyên ngành (10% — Phần 2) | [Tuan_03.md](./Tuan_03.md) |
| **Tuần 4** | • Tìm bộ dữ liệu phù hợp với bài toán (Kaggle/UCI CKD)<br>• Phân tích sơ bộ, mô tả các đặc trưng (feature) của dữ liệu | • Bộ dữ liệu đã được xác nhận ($N=400, D=24$)<br>• Bản mô tả tổng quan (số dòng, số cột, kiểu dữ liệu) | Triệu Thị Thu Ngân | Thu thập dữ liệu, trực quan hóa dữ liệu (10% — phần thu thập) | [Tuan_04.md](./Tuan_04.md) |
| **Tuần 5** | • Trực quan hóa dữ liệu: phân bố, tương quan giữa các đặc trưng, phát hiện bất thường<br>• Viết nhận xét ban đầu về đặc điểm dữ liệu, định hướng tiền xử lý | • Biểu đồ trực quan hóa dữ liệu (missing values, target distribution, golden biomarkers, correlation heatmap)<br>• Bản nhận xét sơ bộ về dữ liệu | Triệu Thị Thu Ngân | Thu thập dữ liệu, trực quan hóa dữ liệu (10% — phần trực quan hóa) | [Tuan_05.md](./Tuan_05.md) |
| **Tuần 6** | • Tiền xử lý dữ liệu: xử lý giá trị thiếu, mã hóa biến phân loại, chuẩn hóa/scale<br>• Đánh giá độ tương quan giữa các đặc trưng, chia tập huấn luyện/kiểm tra | • Pipeline tiền xử lý chống rò rỉ dữ liệu (`ColumnTransformer`)<br>• Bộ dữ liệu đã qua tiền xử lý sẵn sàng huấn luyện | Vũ Thế Quang | Tiền xử lý dữ liệu, đánh giá độ tương quan của các feature (10%) | [Tuan_06.md](./Tuan_06.md) |
| **Tuần 7** | • Chọn thuật toán học máy phù hợp giải quyết yêu cầu phân lớp (dựa trên lý thuyết Tuần 2–3)<br>• Cài đặt thực nghiệm mô hình cơ sở (baseline) ban đầu | • 6 mô hình baseline chạy được và có bảng kết quả đo lường<br>• Giải thích lý do chọn thuật toán phù hợp (Random Forest) | Nguyễn Đình Bảo Tấn | Chọn thuật toán để giải quyết yêu cầu phân lớp (10%) | [Tuan_07.md](./Tuan_07.md) |
| **Tuần 8** | • Đánh giá sơ bộ mô hình baseline, xác định điểm cần cải thiện<br>• **NỘP BÁO CÁO TIẾN ĐỘ THỰC HIỆN ĐỒ ÁN — Giai đoạn 1** | • Bảng kết quả đánh giá baseline & danh mục cải thiện Giai đoạn 2<br>• **Báo cáo tiến độ Giai đoạn 1 nộp đúng hạn** | Võ Tấn Đạt & Cả nhóm | **★ Giai đoạn 1: Báo cáo tiến độ (CLO2, CLO3) — 20% điểm đồ án** | [Tuan_08.md](./Tuan_08.md) |
| **Tuần 9** | • Tinh chỉnh mô hình: hyperparameter tuning (`GridSearchCV`), thử nghiệm kỹ thuật giảm chiều PCA để so sánh<br>• Kiểm tra chéo (Stratified 5-Fold Cross-Validation) đánh giá độ ổn định | • Mô hình đã được tinh chỉnh, kết quả cải thiện so với baseline (CV Recall: $98.50\% \pm 1.22\%$)<br>• Biểu đồ phân tích phương sai tích lũy PCA | Nguyễn Đình Bảo Tấn | Chia dữ liệu, xây dựng mô hình, lưu mô hình (20% — phần xây dựng mô hình) | [Tuan_09.md](./Tuan_09.md) |
| **Tuần 10** | • Hoàn thiện mô hình cuối cùng, đánh giá kết quả tổng thể trên tập kiểm tra (CM, ROC-AUC, Feature Importance)<br>• Lưu mô hình sau huấn luyện (`.joblib`) và kiểm tra việc load lại mô hình | • Bộ đo lường tập Test hoàn chỉnh ($TP=48, TN=29, FP=1, FN=2$)<br>• **File model đã lưu (`.joblib`), load và dự đoán thử thành công** | Võ Tấn Đạt & Nguyễn Đình Bảo Tấn | Chia dữ liệu, xây dựng mô hình, lưu mô hình (20% — phần lưu mô hình) | [Tuan_10.md](./Tuan_10.md) |
| **Tuần 11** | • Thiết kế và bắt đầu xây dựng ứng dụng minh họa (chọn nền tảng: Web Flask)<br>• Tích hợp bước đầu mô hình đã lưu vào ứng dụng qua REST API | • Kiến trúc phần mềm 3 tầng phân tách độc lập<br>• Khung ứng dụng Web ban đầu đã kết nối được với model `.joblib` | Nguyễn Thanh Nhàn (Phối hợp: Tấn Đạt) | Xây dựng ứng dụng (20% — giai đoạn đầu) | [Tuan_11.md](./Tuan_11.md) |
| **Tuần 12** | • Hoàn thiện giao diện và chức năng ứng dụng minh họa (HUIT Hospital CDSS)<br>• Kiểm thử ứng dụng với nhiều trường hợp dữ liệu đầu vào khác nhau | • Ứng dụng Web hoàn chỉnh tích hợp Clinical XAI & eGFR MDRD KDIGO<br>• **Bộ 17 Unit Tests tự động đạt 100% tỷ lệ vượt qua** | Nguyễn Thanh Nhàn & Vũ Thế Quang | Xây dựng ứng dụng (20% — hoàn thiện) | [Tuan_12.md](./Tuan_12.md) |
| **Tuần 13** | • Viết báo cáo (bản nháp): tổng hợp lý thuyết, dữ liệu, quy trình thực nghiệm, kết quả<br>• Rà soát nội dung, đảm bảo đúng cấu trúc 12 mục yêu cầu | • Bản nháp báo cáo hoàn chỉnh đầy đủ 12 mục theo cấu trúc đề cương HUIT<br>• Bảng kiểm tra tính nhất quán của số liệu | Võ Tấn Đạt & Cả nhóm | Hình thức trình bày bài báo cáo (10% — chuẩn bị) | [Tuan_13.md](./Tuan_13.md) |
| **Tuần 14** | • Hoàn thiện báo cáo cuối cùng, rà soát lỗi chính tả và định dạng<br>• Chuẩn bị slide thuyết trình (14 slide)<br>• **NỘP BÁO CÁO HOÀN CHỈNH — Giai đoạn 2** | • Báo cáo hoàn chỉnh (Word/PDF không lỗi chính tả)<br>• Slide thuyết trình 14 trang<br>• **Trọn bộ hồ sơ đã nộp đầy đủ theo quy định** | Võ Tấn Đạt & Cả nhóm | **★ Giai đoạn 2: Báo cáo hoàn chỉnh (CLO1–4) — 80% điểm đồ án** | [Tuan_14.md](./Tuan_14.md) |
| **Tuần 15** | • Thuyết trình trước lớp (đúng thời gian quy định 12–14 phút)<br>• Trao đổi, trả lời tốt các câu hỏi phản biện của giảng viên và các nhóm khác | • Buổi thuyết trình bảo vệ hoàn chỉnh, đúng giờ<br>• Trả lời xuất sắc toàn bộ câu hỏi phản biện chuyên môn | Toàn bộ 5 thành viên (Điều phối: Võ Tấn Đạt) | Tham gia tổ chức và phối hợp làm việc trong nhóm (10% — thuyết trình & Q&A) | [Tuan_15.md](./Tuan_15.md) |
