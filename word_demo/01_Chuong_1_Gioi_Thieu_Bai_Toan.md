# CHƯƠNG 1. GIỚI THIỆU VỀ BÀI TOÁN CHẨN ĐOÁN BỆNH THẬN MÃN TÍNH (CKD)

## 1.1. TỔNG QUAN VỀ BÀI TOÁN VÀ BỐI CẢNH Y TẾ

### 1.1.1. Tầm quan trọng của phân tích dữ liệu y tế và phát hiện sớm CKD

Trong bối cảnh chuyển đổi số y tế hiện nay, Bệnh thận mãn tính (*Chronic Kidney Disease — CKD*) đang trở thành một trong những gánh nặng sức khỏe cộng đồng nghiêm trọng nhất trên toàn cầu. Theo các thống kê dịch tễ học quốc tế và Tổ chức Y tế Thế giới (WHO), ước tính có khoảng **10% dân số trưởng thành trên toàn thế giới** đang sống chung với bệnh thận mãn tính ở nhiều giai đoạn khác nhau.

Điểm nguy hiểm nhất của CKD là **diễn tiến âm thầm, không triệu chứng rõ ràng ở các giai đoạn sớm (Giai đoạn 1 – 3)**. Phần lớn bệnh nhân chỉ phát hiện bệnh khi chức năng lọc cầu thận đã suy giảm trên 70%, lúc này thận mất khả năng hồi phục và buộc phải bước vào giai đoạn suy thận mạn cuối (ESRD — End-Stage Renal Disease). Chi phí điều trị thay thế thận (chạy thận nhân tạo chu kỳ 3 lần/tuần hoặc ghép thận) tạo ra gánh nặng tài chính khổng lồ cho gia đình người bệnh và quỹ bảo hiểm y tế, đồng thời làm suy giảm nghiêm trọng chất lượng sống và tỷ lệ sống còn.

Trước đây, việc sàng lọc bệnh thận phụ thuộc hoàn toàn vào kinh nghiệm đọc kết quả xét nghiệm đơn lẻ của bác sĩ chuyên khoa thận. Tại các cơ sở y tế tuyến dưới hoặc phòng khám đa khoa đông bệnh nhân, việc phải tổng hợp đồng thời hàng chục chỉ số huyết học, sinh hóa máu, xét nghiệm nước tiểu và bệnh lý nền rất dễ dẫn đến bỏ sót các trường hợp tiềm ẩn. Chính vì vậy, ứng dụng **Học máy (Machine Learning)** và **Hệ thống hỗ trợ ra quyết định lâm sàng (CDSS — Clinical Decision Support System)** để phân tích đa biến, phát hiện sớm nguy cơ CKD và giải thích nguyên nhân cho bác sĩ là yêu cầu cấp thiết, mang lại giá trị nhân văn và kinh tế to lớn.

### 1.1.2. Các nhóm yếu tố lâm sàng liên quan đến Bệnh thận mãn tính

Bệnh thận mãn tính hiếm khi xuất phát từ một nguyên nhân đơn lẻ mà là hệ quả tích lũy từ sự suy giảm chức năng lọc cầu thận, tổn thương ống thận và các bệnh lý nền chuyển hóa. Bộ dữ liệu lâm sàng **Chronic Kidney Disease (CKD)** cung cấp hệ thống **24 đặc trưng y khoa đa chiều** phản ánh toàn diện 5 nhóm yếu tố cốt lõi:

1. **Nhóm chỉ số chức năng lọc cầu thận và chuyển hóa nitơ:** Bao gồm nồng độ Creatinine huyết thanh (`sc` — Serum Creatinine) và Urê máu (`bu` — Blood Urea). Đây là các sản phẩm thải của quá trình chuyển hóa cơ và protein; khi cầu thận suy giảm khả năng lọc, các chất độc này tích tụ tăng cao trong máu.
2. **Nhóm chỉ số xét nghiệm nước tiểu (Urinalysis):** Bao gồm tỷ trọng nước tiểu (`sg`), đạm niệu Albumin (`al`), đường niệu (`su`), tế bào hồng cầu (`rbc`), tế bào mủ (`pc`), đám tế bào mủ (`pcc`) và vi khuẩn (`ba`). Sự xuất hiện của Albumin trong nước tiểu (đạm niệu) cùng tỷ trọng nước tiểu giảm thấp là dấu hiệu trực tiếp cho thấy màng lọc cầu thận đã bị tổn thương và ống thận mất khả năng cô đặc.
3. **Nhóm chỉ số huyết học và thiếu máu:** Bao gồm huyết sắc tố Hemoglobin (`hemo`), dung tích khối hồng cầu (`pcv`), số lượng hồng cầu (`rc`) và số lượng bạch cầu (`wc`). Thận khỏe mạnh tiết ra hormone *Erythropoietin (EPO)* kích thích tủy xương tạo hồng cầu; khi thận suy, lượng EPO giảm mạnh gây ra hội chứng thiếu máu mạn đặc trưng.
4. **Nhóm chỉ số điện giải và chuyển hóa đường:** Bao gồm Natri (`sod`), Kali (`pot`) và đường huyết ngẫu nhiên (`bgr`). Rối loạn điện giải (đặc biệt tăng Kali máu) là biến chứng nguy hiểm trực tiếp đe dọa tính mạng bệnh nhân suy thận.
5. **Nhóm yếu tố nhân khẩu học, bệnh lý nền và triệu chứng lâm sàng:** Bao gồm tuổi (`age`), huyết áp (`bp`), tiền sử tăng huyết áp (`htn`), đái tháo đường (`dm`), bệnh mạch vành (`cad`), cảm giác thèm ăn (`appet`), phù ngoại biên (`pe`) và hội chứng thiếu máu (`ane`). Tăng huyết áp và đái tháo đường là hai nguyên nhân hàng đầu gây xơ hóa mạch máu thận.

Mối quan hệ giữa 24 đặc trưng này với nguy cơ mắc CKD mang tính **phi tuyến cao và có tương tác chéo phức tạp** (ví dụ: một bệnh nhân có mức Creatinine chỉ tăng nhẹ ở ngưỡng ranh giới $1.3\text{ mg/dL}$ nhưng kèm theo tiểu đường, tăng huyết áp, thiếu máu và đạm niệu vẫn có nguy cơ suy thận rất cao). Do đó, việc áp dụng các thuật toán Học máy là phương pháp tối ưu để mô hình hóa chính xác bức tranh lâm sàng đa chiều này.

---

## 1.2. MỤC TIÊU VÀ PHẠM VI NGHIÊN CỨU

### 1.2.1. Mục tiêu phân tích đặc trưng sinh hóa và dự đoán CKD

Mục tiêu tổng quát của đề tài là xây dựng một **hệ thống Học máy hoàn chỉnh theo vòng đời chuẩn (ML Lifecycle)** — từ lý thuyết toán học, phân tích dữ liệu, tiền xử lý chống rò rỉ dữ liệu, huấn luyện – tối ưu mô hình đến đóng gói và triển khai ứng dụng Web hỗ trợ bác sĩ chẩn đoán sớm Bệnh thận mãn tính.

Các mục tiêu cụ thể bao gồm:

1. **Khám phá và trực quan hóa dữ liệu y tế (EDA):** Kiểm toán toàn vẹn chất lượng bộ dữ liệu 400 bệnh nhân (dòng trùng lặp, cột hằng số, cột định danh `id`), phân tích cơ chế khuyết thiếu trên 24/24 cột (`1,012` ô `NaN` = `10.54%`), khảo sát mất cân bằng nhãn và xác định nhóm "Tam giác vàng sinh hóa" (`sc`, `hemo`, `al`, `sg`).
2. **Thiết kế quy trình tiền xử lý chuẩn y khoa chống Data Leakage:** Làm sạch ký tự rác, chia tập dữ liệu phân tầng (*Stratified Split 80/20*), xử lý giá trị khuyết bằng Median/Mode Imputation, mã hóa One-Hot và chuẩn hóa Z-Score đóng gói trọn vẹn trong `ColumnTransformer`.
3. **Huấn luyện, so sánh và tối ưu hóa mô hình phân lớp:** Cài đặt thực nghiệm 6 thuật toán phân lớp tiêu biểu (Random Forest, SVM, Logistic Regression, Decision Tree, Gaussian Naïve Bayes, k-NN) kết hợp khảo sát giảm chiều PCA; tối ưu hóa siêu tham số bằng `GridSearchCV` qua Stratified 5-Fold Cross-Validation với ưu tiên y khoa hàng đầu là **độ nhạy Recall $\ge 96\%$** nhằm giảm thiểu tối đa nguy cơ bỏ sót bệnh nhân (*False Negative*).
4. **Đóng gói mô hình và xây dựng ứng dụng minh họa CDSS tích hợp XAI:** Lưu Pipeline nguyên khối dạng `.joblib`, phát triển ứng dụng Web **HUIT Hospital CDSS** (Flask + Chart.js) hỗ trợ nhập 24 chỉ số lâm sàng, hiển thị trực quan xác suất nguy cơ, giải thích các yếu tố tác động (Explainable AI) và tự động tính mức lọc cầu thận ước tính **eGFR theo công thức MDRD chuẩn KDIGO 2024**.

### 1.2.2. Phạm vi nghiên cứu trên bộ dữ liệu Kaggle / UCI CKD

- **Bộ dữ liệu thực nghiệm:** Bộ dữ liệu công khai *Chronic Kidney Disease Dataset* do Bệnh viện Apollo (Ấn Độ) thu thập và công bố trên kho lưu trữ UCI Machine Learning Repository / Kaggle (`akshayksingh/kidney-disease-dataset`), gồm **$N = 400$ mẫu bệnh nhân**, **$D = 24$ thuộc tính đầu vào** và 1 nhãn phân lớp nhị phân `classification` (`ckd` / `notckd`).
- **Phạm vi phương pháp luận:** Tập trung vào bài toán **Phân lớp nhị phân có giám sát (Supervised Binary Classification)** kết hợp **Giảm chiều dữ liệu (PCA)** và **Giải thích mô hình (Feature Importance / Clinical XAI)**.
- **Giới hạn và lưu ý y khoa:** Hệ thống được thiết kế với vai trò là **công cụ hỗ trợ sàng lọc và ra quyết định lâm sàng (CDSS)** giúp tham khảo nhanh cho y bác sĩ, không thay thế phán quyết y khoa cuối cùng của bác sĩ chuyên khoa thận. Do kích thước mẫu ở mức vừa phải ($N = 400$), mô hình cần được tái thẩm định và hiệu chỉnh trên dữ liệu bệnh viện địa phương trước khi đưa vào vận hành thương mại thực tế.
