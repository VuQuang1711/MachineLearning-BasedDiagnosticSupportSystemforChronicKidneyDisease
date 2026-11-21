# KỊCH BẢN THUYẾT TRÌNH VÀ CẤU TRÚC SLIDE BẢO VỆ ĐỒ ÁN HỌC MÁY (12-14 PHÚT)

**Mã đề tài:** BT04 — Hệ Thống Máy Học Chẩn Đoán Bệnh Thận Mãn Tính (CKD)  
**Học phần:** Học Máy (Machine Learning) — Năm học: 2026–2027  
**Lớp học phần:** 15DHKHDL04  
**Giảng viên hướng dẫn (GVHD):** ThS. Nguyễn Thị Huyền Trang  
**Bộ môn:** Khoa học Dữ liệu (KHDL) — Khoa Công Nghệ Thông Tin — Trường Đại học Công Thương TP.HCM (HUIT)  
**Mục tiêu tài liệu:** Cung cấp dàn ý chi tiết 14 Slide trình chiếu chuẩn học thuật, phân bổ thời gian nói chặt chẽ (12-14 phút tránh trừ điểm quá giờ) cho đầy đủ **5 thành viên nhóm**, và lời thoại mẫu (Script) tự tin thuyết phục hội đồng chấm thi đạt điểm 10/10.

---

## 1. BẢNG PHÂN BỔ THỜI LƯỢNG THUYẾT TRÌNH (TỔNG: 13-14 PHÚT — 5 THÀNH VIÊN)

| Phần | Nội Dung Trình Bày | Số Slide | Người Trình Bày Chính | Thời Lượng |
| :---: | :--- | :---: | :--- | :---: |
| **Phần 1** | Giới thiệu, Bối cảnh Lâm sàng, Mục tiêu Đề tài & Kiến trúc 3 Tầng | Slide 1 - 3 | **Võ Tấn Đạt** *(Nhóm Trưởng / Lead)* | 2.5 phút |
| **Phần 2** | Khám phá Dữ liệu (EDA) & Tam Giác Vàng Sinh Hóa Thận | Slide 4 - 5 | **Triệu Thị Thu Ngân** *(EDA Specialist)* | 2.5 phút |
| **Phần 3** | Quy trình Tiền xử lý Chống Data Leakage & Hệ thống 17 Unit Tests | Slide 6 - 7 | **Vũ Thế Quang** *(Data Preprocessing & QA)* | 2.5 phút |
| **Phần 4** | Cơ sở Toán học, Huấn luyện 6 Mô hình, Tuning GridSearchCV & PCA | Slide 8 - 9 | **Nguyễn Đình Bảo Tấn** *(ML & Tuning)* | 3.0 phút |
| **Phần 5** | Phân tích Lỗi Lâm sàng, Demo Web HUIT Hospital CDSS & Khối XAI | Slide 10 - 12 | **Nguyễn Thanh Nhàn** *(Web App & XAI)* | 2.5 phút |
| **Phần 6** | Tổng kết 4 Nội dung Bước 7, Kế hoạch 15 Tuần & Chủ trì Q&A | Slide 13 - 14 | **Võ Tấn Đạt & Toàn Nhóm** | 1.0 phút |

---

## 2. CHI TIẾT NỘI DUNG 14 SLIDE & LỜI THOẠI MẪU (SCRIPT)

### Slide 1: Trang Bìa Đề Tài & Danh Sách 5 Thành Viên Nhóm
* **Nội dung Slide:**
  * **TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP.HCM (HUIT)** — KHOA CNTT — BỘ MÔN KHOA HỌC DỮ LIỆU
  * Tên đề tài: **HỆ THỐNG MÁY HỌC HỖ TRỢ CHẨN ĐOÁN BỆNH THẬN MÃN TÍNH (CKD)**
  * Mã đề tài: **BT04** — Lớp học phần: **15DHKHDL04** — Năm học: **2026–2027**
  * Giảng viên hướng dẫn: **ThS. Nguyễn Thị Huyền Trang**
  * Danh sách thành viên & Vai trò:
    1. **Võ Tấn Đạt** (MSSV: `2045240050`) — Nhóm Trưởng & Kiến trúc sư hệ thống
    2. **Triệu Thị Thu Ngân** (MSSV: `2405240179`) — Chuyên viên EDA & Trực quan hóa dữ liệu
    3. **Vũ Thế Quang** (MSSV: `2045240253`) — Kỹ sư Tiền xử lý dữ liệu & Kiểm chuẩn QA
    4. **Nguyễn Đình Bảo Tấn** (MSSV: `2405240270`) — Kỹ sư Mô hình học máy & Tinh chỉnh siêu tham số
    5. **Nguyễn Thanh Nhàn** (MSSV: `2405240198`) — Kỹ sư Ứng dụng Web & Trí tuệ giải thích được (XAI)
* **Lời thoại của Võ Tấn Đạt (Script - 45s):**
  > *"Kính thưa cô Nguyễn Thị Huyền Trang và quý Thầy/Cô trong Hội đồng chấm đồ án môn học Học máy. Hôm nay nhóm sinh viên Lớp 15DHKHDL04 gồm 5 thành viên chúng em xin phép được báo cáo đồ án kết thúc học phần với đề tài: 'Xây dựng hệ thống máy học hỗ trợ chẩn đoán bệnh thận mãn tính CKD dựa trên 24 chỉ số xét nghiệm cận lâm sàng'. Đồ án được nhóm nghiên cứu và triển khai bám sát 100% chuẩn đầu ra môn học CLO1 đến CLO4, từ cơ sở đại số ma trận, quy trình tiền xử lý chống rò rỉ dữ liệu, tối ưu hóa các thuật toán phân lớp y tế, đến đóng gói kiến trúc 3 tầng và xuất bản cổng thông tin Web Bệnh viện HUIT Hospital CDSS."*

---

### Slide 2: Đặt Vấn Đề & Bối Cảnh Lâm Sàng Bệnh Thận Mãn Tính
* **Nội dung Slide:**
  * Tỷ lệ mắc CKD toàn cầu: Chiếm khoảng $10-12\%$ dân số trưởng thành.
  * Tính chất nguy hiểm: "Kẻ giết người thầm lặng" — Các giai đoạn khởi phát hầu như không có triệu chứng rõ rệt.
  * Khi bệnh bộc lộ (phù chân, thiếu máu nặng), thận thường đã xơ hóa ở giai đoạn 4 hoặc 5, chi phí chạy thận nhân tạo và ghép thận vô cùng tốn kém.
  * Vai trò của Machine Learning: Tự động hóa tầm soát sớm dựa trên các xét nghiệm máu và nước tiểu định kỳ với chi phí thấp.
* **Lời thoại (Script - 1 phút):**
  > *"Như Thầy/Cô đã biết, bệnh thận mãn tính là một trong những nguyên nhân gây tử vong hàng đầu hiện nay. Điểm nguy hiểm nhất của CKD là ở giai đoạn sớm, bệnh nhân không hề cảm thấy đau đớn hay mệt mỏi. Đa số chỉ đến bệnh viện khi chức năng lọc cầu thận đã suy giảm trên 70%. Nếu ứng dụng Học máy để phân tích tự động 24 chỉ số sinh hóa thông thường, chúng ta hoàn toàn có thể cảnh báo sớm nguy cơ với độ nhạy tiệm cận 100%, giúp bệnh nhân có cơ hội điều trị bảo tồn kịp thời."*

---

### Slide 3: Mục Tiêu Đồ Án & Chuẩn Đầu Ra (CLO)
* **Nội dung Slide:**
  * **CLO1:** Nắm vững bản chất toán học của 6 thuật toán phân lớp (Logistic, SVM, Decision Tree, Random Forest, Naïve Bayes, $k$-NN) và kỹ thuật giảm chiều PCA/LDA.
  * **CLO2:** Xây dựng quy trình tiền xử lý y tế chuẩn mực: kiểm toán `duplicated`/`nunique`, xử lý 24/24 cột ô khuyết (`1,012` ô `NaN`) bằng Median/Mode, chuẩn hóa Z-Score, One-Hot Encoding (`24 -> 35` chiều sạch), tuyệt đối không gây Data Leakage.
  * **CLO3:** Đóng gói Pipeline nguyên khối bằng Joblib (`187.43 KB`), thiết kế phần mềm 3 tầng và phân công làm việc nhóm 15 tuần khoa học.
  * **CLO4:** Tối ưu hóa thước đo y tế: Đặt **Recall (Độ nhạy phát hiện bệnh)** làm mục tiêu cốt lõi ($\text{Recall} \ge 96\%$, triệt tiêu False Negative).

---

### Slide 4: Khám Phá Dữ Liệu (EDA) & Tam Giác Vàng Sinh Hóa
* **Nội dung Slide:**
  * Tập dữ liệu chuẩn: Kaggle / UCI Chronic Kidney Disease ($N = 400$ bệnh nhân, $D = 24$ thuộc tính).
  * Phân phối nhãn: 250 ca bệnh (`ckd` - $62.5\%$) và 150 ca đối chứng (`notckd` - $37.5\%$).
  * Biểu đồ ma trận tương quan: Khám phá "Tam giác vàng sinh hóa" chi phối mạnh nhất nguy cơ bệnh thận:
    * `Serum Creatinine (sc)`: Tương quan dương mạnh ($r = +0.54$) — Thận hỏng không lọc được Creatinine.
    * `Hemoglobin (hemo)`: Tương quan âm mạnh ($r = -0.76$) — Suy thận gây thiếu máu nặng.
    * `Albumin niệu (al)`: Tương quan dương mạnh ($r = +0.62$) — Tổn thương màng đáy rò rỉ đạm vào nước tiểu.
* **Lời thoại (Script - 1.5 phút):**
  > *"Đi sâu vào dữ liệu, nhóm phát hiện ra một mối tương quan lâm sàng cực kỳ chặt chẽ giữa 3 chỉ số sinh hóa cốt lõi. Ở nhóm bệnh nhân suy thận, Creatinine huyết thanh trung bình đo được lên tới 4.41 mg/dL, gấp 5 lần người bình thường; nồng độ Hemoglobin tụt xuống 10.6 g/dL; và có tới 74.2% bệnh nhân xuất hiện đạm trong nước tiểu. Ba chỉ số này đóng vai trò như 'mắt xích' quyết định giúp các thuật toán học máy tìm ra ranh giới phân tách hai nhóm đối tượng."*

---

### Slide 5: Quy Trình Tiền Xử Lý Chống Rò Rỉ Dữ Liệu (Data Leakage)
* **Nội dung Slide:**
  * Sơ đồ luồng: Làm sạch chuỗi $\to$ Stratified Split (80/20) $\to$ ColumnTransformer Pipeline.
  * Kiểm toán dữ liệu & hiện trạng ô khuyết: `0` dòng trùng lặp, `0` cột hằng số, loại bỏ cột định danh `id` (`400/400` duy nhất); `24/24` cột thiếu dữ liệu (`1,012` ô `NaN` = `10.54%`, trong đó `rbc` thiếu $38.0\%$, `rc` thiếu $32.75\%$).
  * Giải pháp toán học:
    * Biến định lượng: Áp dụng `SimpleImputer(strategy='median')` để kháng các giá trị ngoại lai y tế cực lớn.
    * Biến định tính: Áp dụng `SimpleImputer(strategy='most_frequent')` (Mode).
  * **Nguyên tắc chống rò rỉ dữ liệu:** Hàm `.fit()` chỉ thực thi duy nhất trên tập Train (320 mẫu). Khi sang tập Test (80 mẫu), chỉ gọi `.transform()`.
* **Lời thoại (Script - 1.5 phút):**
  > *"Thưa Thầy/Cô, trong dữ liệu y tế thực tế, ô khuyết là điều không thể tránh khỏi. Nhóm giải quyết vấn đề này bằng cách kết hợp SimpleImputer và ColumnTransformer. Tuy nhiên, điểm mấu chốt để đạt chuẩn khoa học dữ liệu là nhóm đã phân tách tập Train và Test độc lập trước tiên. Toàn bộ giá trị trung vị và yếu vị chỉ được tính toán trên 320 mẫu của tập Train, đảm bảo tập Test hoàn toàn là dữ liệu chưa từng thấy, loại bỏ 100% hiện tượng học vẹt và thổi phồng độ chính xác giả tạo."*

---

### Slide 6: Cơ Sở Toán Học & 6 Thuật Toán Phân Lớp Cốt Lõi
* **Nội dung Slide:**
  * 6 trường phái thuật toán được nghiên cứu và so sánh:
    1. **Logistic Regression:** Hàm Sigmoid $\sigma(z)$, Binary Cross-Entropy Loss kết hợp điều hòa $L_2$ Ridge.
    2. **SVM (Support Vector Machine):** Tối ưu lề cực đại Soft-margin với hàm nhân RBF Kernel phi tuyến.
    3. **Decision Tree (CART):** Tách nhánh tối ưu hóa độ bất thuần Gini Impurity.
    4. **Random Forest:** Ensemble Bagging 100 cây với kỹ thuật chọn tập con đặc trưng ngẫu nhiên.
    5. **Gaussian Naïve Bayes:** Xác suất hậu nghiệm dựa trên phân phối chuẩn có điều kiện.
    6. **k-NN ($k=5$):** Phân loại theo khoảng cách Euclidean trong không gian đa chiều.
  * Nhấn mạnh: Có phần ví dụ tính toán thủ công từng bước (Hand Calculation) cho cả 4 thuật toán trong báo cáo lý thuyết.

---

### Slide 7: Thực Nghiệm Giảm Chiều Dữ Liệu PCA / LDA (Chuẩn Đầu Ra CLO1)
* **Nội dung Slide:**
  * Sau khi mã hóa One-Hot, không gian đặc trưng tăng từ 24 lên 35 chiều.
  * **PCA (Học không giám sát):**
    * Phân rã trị riêng và vector riêng ma trận hiệp phương sai $\boldsymbol{\Sigma} \in \mathbb{R}^{35 \times 35}$.
    * Đồ thị tỷ lệ phương sai tích lũy: Cần đúng **19 thành phần chính** để giải thích $95.12\%$ phương sai dữ liệu ban đầu.
  * **LDA (Học có giám sát):** Nén về 1 chiều phân tách cực đại theo tiêu chuẩn tỷ số phương sai Fisher.

---

### Slide 8: Bảng Kết Quả Thực Nghiệm & So Sánh Đa Chiều
* **Nội dung Slide:**
  * Bảng so sánh 6 mô hình trên tập Test độc lập (80 mẫu: 30 `notckd`, 50 `ckd`):
    * **Random Forest:** Accuracy $97.50\%$, Precision $98.00\%$, **Recall $98.00\%$**, F1-Score $98.00\%$, ROC-AUC $0.9987$.
    * **SVM (RBF):** Accuracy $98.75\%$, Precision $100.00\%$, **Recall $98.00\%$**, F1-Score $98.99\%$, ROC-AUC $0.9993$.
    * **Logistic Regression:** Recall $96.00\%$, F1 $97.96\%$.
    * **Decision Tree:** Recall $94.00\%$, F1 $95.92\%$.
    * **k-NN ($k=5$):** Recall $88.00\%$ (Thấp nhất do bị loãng khoảng cách).
  * Đồ thị đường cong ROC so sánh 6 mô hình và Ma trận nhầm lẫn của Random Forest (`[[29, 1], [1, 49]]`).
* **Lời thoại (Script - 2 phút):**
  > *"Trên tập kiểm thử độc lập 80 bệnh nhân, Random Forest và SVM đã chứng minh hiệu năng vượt trội. Cả hai mô hình đều đạt độ nhạy Recall 98.0% đối với nhóm bệnh nhân suy thận, tức là trong 50 người có bệnh, mô hình phát hiện chính xác 49 người và chỉ sót 1 ca ranh giới cực kỳ khó. Ngược lại, thuật toán k-NN bộc lộ rõ hạn chế của lời nguyền số chiều khi Recall tụt xuống 88%, bỏ sót tới 6 bệnh nhân. Do đó, nhóm đã chọn Random Forest làm mô hình đóng gói chính thức vì tính ổn định cao và khả năng trích xuất thuộc tính quan trọng."*

---

### Slide 9: Phân Tích Lỗi Chuyên Sâu (Error Analysis / Case Studies)
* **Nội dung Slide:**
  * Phân tích 2 ca bệnh án cụ thể bị mô hình dự đoán sai:
    * **Ca Test #12 (Âm tính giả của SVM):** Bệnh nhân 17 tuổi, huyết áp bình thường, không tiểu đường, không phù chân, nhưng Creatinine huyết thanh tăng vọt $2.1\text{ mg/dL}$. Vì có tới 22/24 chỉ số mang đặc điểm khỏe mạnh nên tổ hợp tuyến tính của SVM đã bị kéo về lớp 0. Giải pháp: Thêm quy tắc cảnh báo ghi đè khi `sc > 1.8`.
    * **Ca Test #47 (Âm tính giả của Random Forest):** Bệnh nhân có đạm niệu `al = 1.0` nhưng Creatinine bình thường và bị khuyết nhiều xét nghiệm máu.
* **Lời thoại (Script - 1.5 phút):**
  > *"Bám sát tinh thần của môn học, nhóm không chỉ dừng lại ở việc khoe điểm số cao mà đã tiến hành 'Phân tích lỗi chuyên sâu' trên từng ca bệnh bị nhầm lẫn. Điển hình như ca bệnh nhân số 12, đây là một thanh niên 17 tuổi với 22 chỉ số đều hoàn hảo như người khỏe mạnh, nhưng nồng độ Creatinine lại tăng bất thường ở mức 2.1 mg/dL. Việc mô hình dự đoán nhầm ca này đã giúp nhóm nhận ra rằng: trong y tế, cần phải có cơ chế cảnh báo quy tắc độc lập cho các chỉ số sinh mạng để hỗ trợ tối đa cho bác sĩ."*

---

### Slide 10: Kiến Trúc Phần Mềm 3 Tầng (3-Tier Architecture)
* **Nội dung Slide:**
  * Sơ đồ kiến trúc 3 tầng:
    * **Data Layer:** `src/data_loader.py` (Làm sạch chuỗi, ColumnTransformer Pipeline, nạp CSV).
    * **Business / Model Layer:** `src/model_logic.py` (Lớp `CKDPredictor`, Joblib Serializer) & `src/xai_explainer.py`.
    * **Presentation Layer:** `src/app.py` (Flask RESTful API) + `templates/index.html` + `static/`.
  * Hợp đồng giao tiếp JSON API chuẩn RESTful (`POST /api/predict`).

---

### Slide 11: Demo Ứng Dụng Web & Khối Giải Trình Lâm Sàng (Clinical XAI)
* **Nội dung Slide:**
  * Ảnh chụp màn hình ứng dụng Web: Biểu mẫu đầy đủ **24 thông số xét nghiệm** chia 3 nhóm khoa học.
  * Nút "Nạp Mẫu Bệnh Án Điển Hình" phục vụ thao tác demo nhanh chỉ trong 3 giây.
  * Khối kết quả trực quan:
    * Nhãn chẩn đoán màu đỏ cảnh báo nguy cơ.
    * Thanh đo phần trăm xác suất rủi ro bệnh thận.
    * **Widget XAI y tế:** Liệt kê tường minh các nguyên nhân sinh hóa (Creatinine cao, Đạm niệu mức 3, Thiếu máu, Tiền sử Tăng huyết áp + Đái tháo đường).
* **Lời thoại (Script - 1.5 phút):**
  > *"Nhóm đã triển khai hoàn chỉnh một ứng dụng Web lâm sàng trực quan. Giao diện được thiết kế tối giản, phân nhóm 24 chỉ số thành Sinh hóa máu, Phân tích nước tiểu và Tiền sử bệnh. Điểm đặc biệt là ứng dụng tích hợp khối giải trình XAI: thay vì chỉ đưa ra một xác suất khô khan, hệ thống giải thích rõ ràng cho bác sĩ biết vì sao bệnh nhân này có nguy cơ cao, ví dụ do nồng độ Creatinine vượt 1.4 mg/dL kết hợp với sự xuất hiện của Protein niệu."*

---

### Slide 12: Kế Hoạch Làm Việc Nhóm 15 Tuần & Phân Công Trách Nhiệm (CLO3)
* **Nội dung Slide:**
  * Bảng tiến độ 15 tuần thực hiện đồ án môn học theo đúng đề cương Bộ môn KHDL - HUIT.
  * Ma trận phân công trách nhiệm RACI chi tiết 5 thành viên (Mức độ đóng góp: 100% tất cả thành viên):
    * **Võ Tấn Đạt (Trưởng nhóm):** Quản trị tiến độ, thiết kế kiến trúc 3 tầng, Pipeline đóng gói Joblib, tổng hợp mã nguồn & kịch bản.
    * **Triệu Thị Thu Ngân:** Thu thập, kiểm toán 400 mẫu UCI/Kaggle, phân tích thống kê mô tả và trực quan hóa EDA Tam giác vàng sinh hóa.
    * **Vũ Thế Quang:** Kiểm toán dữ liệu đầu vào, tiền xử lý dữ liệu chuẩn y khoa chống Data Leakage (Median/Mode/OneHot/Scale), xây dựng trọn bộ 17 ca kiểm thử tự động `test/`.
    * **Nguyễn Đình Bảo Tấn:** Cơ sở toán học 6 thuật toán, thực nghiệm Baseline, tinh chỉnh siêu tham số `GridSearchCV` 5-Fold, tối ưu độ nhạy Recall $\ge 96\%$.
    * **Nguyễn Thanh Nhàn:** Phát triển Web App HUIT Hospital CDSS, giải trình eGFR MDRD KDIGO 2024, biểu đồ Radar/Gauge, Dataset Explorer 400 ca và bảng đối chiếu chuẩn sinh lý.
  * Hệ thống kiểm thử tự động với 17 Unit Tests trong thư mục `test/` đạt tỷ lệ vượt qua $100\%$.
* **Lời thoại của Võ Tấn Đạt (Script - 45s):**
  > *"Kính thưa Thầy/Cô, để đạt được kết quả trên, nhóm em đã phân bổ công việc công bằng và rõ ràng theo tiến trình 15 tuần của đề cương. Cả 5 thành viên đều phát huy tối đa thế mạnh chuyên môn, từ thu thập dữ liệu, cơ sở toán học, lập trình tiền xử lý, kiểm thử tự động, đến triển khai Web và XAI. Mức độ tham gia và hoàn thành của từng thành viên trong nhóm đều đạt 100%."*

---

### Slide 13: Bốn Nội Dung Tổng Kết Bước 7 (Chuẩn Trường Đại Học Công Nghệ Thông Tin(UIT) - Đại Học Quốc Gia Thành Phố Hồ Chí Minh(VNUHCM)) & Hướng Phát Triển
* **Nội dung Slide:**
  * **1. Khám phá:** Tam giác vàng `sc - hemo - al` chi phối $>65\%$ quyết định phân lớp.
  * **2. Hiệu quả:** SimpleImputer Median cho biến số; Random Forest cho độ ổn định cao nhất. Không hiệu quả: k-NN bị loãng trong không gian 35 chiều; Decision Tree không tỉa cành dễ bị quá khớp.
  * **3. Giả định:** Dữ liệu khuyết thuộc dạng MAR; biến liên tục tuân theo phân phối chuẩn.
  * **4. Hạn chế & Hướng phát triển:** Kích thước mẫu 400 còn khiêm tốn; định hướng mở rộng thêm các thuật toán Gradient Boosting (XGBoost, LightGBM) và tích hợp chỉ số mức lọc cầu thận eGFR tự động theo công thức CKD-EPI.

---

### Slide 14: Lời Cảm Ơn & Sẵn Sàng Trả Lời Câu Hỏi Phản Biện (Q&A)
* **Nội dung Slide:**
  * Thông điệp kết thúc: *"Nhóm xin chân thành cảm ơn quý Thầy/Cô đã lắng nghe!"*
  * Nhóm đã chuẩn bị sẵn sàng giải trình toàn bộ các câu hỏi chuyên sâu về:
    * Bản chất toán học của các thuật toán phân lớp.
    * Cơ chế chống rò rỉ dữ liệu (Data Leakage) trong tiền xử lý.
    * Sự đánh đổi giữa Recall và Precision trong bài toán y sinh học.
    * Quy trình vận hành và kiểm soát suy thoái mô hình (Model Drift).
* **Lời thoại (Script - 30s):**
  > *"Bài báo cáo của nhóm em đến đây là kết thúc. Nhóm em xin chân thành cảm ơn quý Thầy/Cô đã chú ý theo dõi. Rất mong nhận được những góp ý quý báu từ Thầy/Cô và nhóm em xin sẵn sàng tiếp nhận các câu hỏi phản biện!"*

---

> [!TIP]
> **Lời khuyên khi thuyết trình:**
> 1. Trưởng nhóm mở đầu dõng dạc, chào hỏi lễ phép, giới thiệu nhanh tên đề tài và từng thành viên.
> 2. Luôn bám sát thời lượng của bảng phân bổ để không bị ngắt lời giữa chừng.
> 3. Khi giảng viên hỏi về mặt toán học, hãy mở ngay tệp `01_Bao_Cao_Kich_Thuoc_Ly_Thuyet_Toan_Hoc.md` và dẫn chứng phần tính toán bằng tay (Hand Calculation) để chứng minh sự hiểu biết sâu sắc.

