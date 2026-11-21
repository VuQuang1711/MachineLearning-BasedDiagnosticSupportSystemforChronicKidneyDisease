# BÁO CÁO TIẾN ĐỘ TUẦN 15 — THUYẾT TRÌNH BẢO VỆ ĐỒ ÁN & TRẢ LỜI PHẢN BIỆN (Q&A)

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Thuyết trình bảo vệ kết thúc học phần
- **Liên hệ Rubric:** Tham gia tổ chức và phối hợp làm việc trong nhóm — Trình bày báo cáo và trả lời câu hỏi rõ ràng, mạch lạc (PLO6 / CLO3 — Trọng số: 10% / Điểm: 1.0)
- **Thành viên chủ trì:** Toàn bộ 5 thành viên (Điều phối chung: Võ Tấn Đạt — `2045240050`)
- **Trạng thái:** Hoàn thành xuất sắc

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 15)
1. **Thuyết trình trước lớp:**
   - Trình bày toàn bộ kết quả đồ án trước Giảng viên hướng dẫn và các bạn sinh viên trong lớp đúng thời gian quy định (12 – 14 phút).
   - Phân chia vai trò đồng đều cho cả 5 thành viên nhóm, mỗi người phụ trách một phần chuyên môn tương ứng với vai trò đã đảm nhiệm trong suốt 15 tuần.
   - Thao tác trực tiếp (Live Demo) ứng dụng Web **HUIT Hospital CDSS** tại chỗ với các ca bệnh mẫu lâm sàng.
2. **Trao đổi, trả lời tốt các câu hỏi phản biện của giảng viên và các nhóm khác:**
   - Trả lời rõ ràng, mạch lạc, lập luận khoa học dựa trên số liệu thực nghiệm và kiến thức y tế đã nghiên cứu.
   - Làm nổi bật tinh thần làm việc nhóm gắn kết, hiểu sâu về mô hình và quy trình học máy.

---

## 2. Kịch Bản Phân Vai Thuyết Trình Chi Tiết (12 – 14 Phút)

| STT | Nội Dung Trình Bày | Slide | Thành Viên Phụ Trách | Thời Lượng |
| :---: | :--- | :---: | :--- | :---: |
| **1** | Mở đầu, lý do chọn đề tài BT04, tính cấp thiết y tế và phạm vi giải quyết | Slide 1 – 3 | **Võ Tấn Đạt** *(Nhóm trưởng)* | 2.0 phút |
| **2** | Phân tích tập dữ liệu 400 mẫu bệnh án, 24 đặc trưng và 4 phát hiện EDA cốt lõi | Slide 4 – 5 | **Triệu Thị Thu Ngân** *(Data Analyst)* | 2.0 phút |
| **3** | Thiết kế quy trình tiền xử lý chống rò rỉ dữ liệu và bộ 17 ca kiểm thử tự động | Slide 6 – 7 | **Vũ Thế Quang** *(QA & Preprocessing)* | 2.0 phút |
| **4** | Cơ sở toán học 6 mô hình, kiểm tra chéo 5-Fold CV, tinh chỉnh siêu tham số và PCA | Slide 8 – 9 | **Nguyễn Đình Bảo Tấn** *(Modeling & Tuning)* | 2.5 phút |
| **5** | Phân tích lỗi, Live Demo ứng dụng Web HUIT CDSS và khối giải trình XAI + eGFR | Slide 10 – 12 | **Nguyễn Thanh Nhàn** *(Fullstack Web)* | 3.0 phút |
| **6** | Tổng kết thành quả, định hướng phát triển và chủ trì phần hỏi đáp phản biện | Slide 13 – 14 | **Võ Tấn Đạt & Cả nhóm** | 1.5 phút |

---

## 3. Nội Dung Trả Lời Các Câu Hỏi Phản Biện Chuyên Sâu Đã Chuẩn Bị

1. **Câu hỏi 1: Vì sao nhóm không đưa thẳng các quy tắc ngưỡng y tế của WHO/KDIGO vào làm luật phân loại mà phải dùng thuật toán học máy?**
   - **Trả lời:** Học máy học quy luật khách quan từ 400 ca bệnh án thực tế mà không áp đặt định kiến chủ quan; các mối liên hệ phi tuyến phức tạp giữa 24 chỉ số (ví dụ sự kết hợp giữa tụt Hemoglobin và tăng nhẹ Creatinine ở người trẻ) là điều mà các ngưỡng đơn lẻ không thể bao quát hết. Ngưỡng WHO/KDIGO được nhóm tích hợp ở tầng hậu xử lý XAI để giải thích quyết định của mô hình và tính eGFR hỗ trợ bác sĩ.
2. **Câu hỏi 2: Nhóm làm cách nào để chứng minh không bị rò rỉ dữ liệu (Data Leakage)?**
   - **Trả lời:** Dữ liệu được chia tập Stratified Train/Test (80/20) ngay từ đầu trước mọi thao tác tính toán; `ColumnTransformer` chỉ được `.fit()` trên 320 mẫu huấn luyện để học giá trị Median/Mode/Scale, sau đó chỉ `.transform()` trên tập kiểm tra. Điều này đã được kiểm chứng tự động bằng ca kiểm thử `test/MainTest_0_Preprocess.py`.
3. **Câu hỏi 3: Vì sao Gaussian Naïve Bayes đạt 100% nhưng nhóm vẫn chọn Random Forest?**
   - **Trả lời:** Biểu đồ tương quan ở Tuần 5 chỉ ra `hemo` và `pcv` có tương quan $r = 0.895$, vi phạm giả định độc lập biến của Naïve Bayes, rất dễ suy giảm hiệu năng khi gặp dữ liệu thực tế mới. Random Forest kháng đa cộng tuyến, đạt Recall cực kỳ ổn định qua 5-Fold CV ($98.50\% \pm 1.22\%$) và cung cấp thuộc tính quan trọng phục vụ XAI.
4. **Câu hỏi 4: Trong bài toán y tế này, nhóm ưu tiên độ đo nào nhất? Vì sao?**
   - **Trả lời:** Ưu tiên hàng đầu là **Recall (Độ nhạy)** đạt trên $96.0\%$. Việc bỏ sót bệnh nhân suy thận (Âm tính giả) có thể dẫn đến việc bệnh nhân không được can thiệp kịp thời, nguy hiểm đến tính mạng; trong khi Dương tính giả chỉ yêu cầu làm thêm xét nghiệm chuyên sâu để khẳng định lại.

---

## 4. Tổng Kết Đánh Giá Hoàn Thành Đồ Án
- **Sản phẩm theo quy định:**
  - [x] Buổi thuyết trình bảo vệ đồ án diễn ra hoàn chỉnh, chuyên nghiệp và đúng giờ.
  - [x] Trả lời lưu loát, tự tin, mạch lạc toàn bộ các câu hỏi phản biện của giảng viên và người nghe.
  - [x] Đạt điểm tối đa tiêu chí "Tham gia tổ chức và phối hợp làm việc trong nhóm" (10%).
- **Đánh giá chung:** Cả 5 thành viên nhóm `15DHKHDL04` đã nỗ lực hoàn thành xuất sắc 100% khối lượng công việc của đồ án suốt 15 tuần, tạo ra sản phẩm hoàn chỉnh từ lý thuyết, dữ liệu, mô hình máy học đã lưu đến ứng dụng Web CDSS thực tiễn.
