# BÁO CÁO TIẾN ĐỘ TUẦN 02 — TÌM HIỂU LÝ THUYẾT THUẬT TOÁN HỌC MÁY (PHẦN 1)

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Giai đoạn 1 (Tuần 2–3)
- **Liên hệ Rubric:** Tự học và vận dụng tài liệu chuyên ngành trong bài tập nhóm (PLO4 / CLO2 — Trọng số: 10% / Điểm: 1.0)
- **Thành viên chủ trì:** Nguyễn Đình Bảo Tấn (`2405240270`) — *Hỗ trợ:* Võ Tấn Đạt (`2045240050`)
- **Trạng thái:** Hoàn thành 100%

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 2)
1. **Tìm hiểu lý thuyết các thuật toán học máy phân lớp:**
   - Nghiên cứu cơ sở toán học, hàm mất mát và cơ chế tối ưu của 3 thuật toán phân lớp cốt lõi: **Logistic Regression**, **Random Forest (Ensemble Learning)**, và **Support Vector Machine (SVM)**.
   - Phân tích ưu/nhược điểm của từng thuật toán đối với dữ liệu y tế dạng bảng (tabular medical data) có cả biến số và biến phân loại.
2. **Đọc tài liệu chuyên ngành và hướng dẫn lâm sàng:**
   - Đọc các bài báo khoa học về ứng dụng máy học chẩn đoán bệnh thận mãn tính (CKD) trên cơ sở dữ liệu UCI.
   - Nghiên cứu hướng dẫn lâm sàng **KDIGO 2024** (*Kidney Disease: Improving Global Outcomes*) để hiểu định nghĩa, các tiêu chí xét nghiệm (Creatinine máu, Albumin niệu, Hemoglobin) và tầm quan trọng của việc tối thiểu hóa lỗi âm tính giả (False Negative).

---

## 2. Kết Quả Nghiên Cứu Lý Thuyết Các Thuật Toán

### 2.1. Hồi quy Logistic (Logistic Regression — Mô hình tuyến tính cơ sở)
- **Mô hình xác suất:** Ánh xạ tổ hợp tuyến tính $z = \mathbf{w}^T\mathbf{x} + b$ sang không gian xác suất thông qua hàm Sigmoid:
  $$p = \sigma(z) = \frac{1}{1 + e^{-z}} \in (0, 1)$$
- **Hàm mất mát Binary Cross-Entropy với điều chuẩn $L_2$:**
  $$J(\mathbf{w}, b) = -\frac{1}{N} \sum_{i=1}^{N} \Big[y_i \ln(p_i) + (1 - y_i)\ln(1 - p_i)\Big] + \frac{\lambda}{2}\|\mathbf{w}\|_2^2$$
- **Nhận định ứng dụng:** Đóng vai trò là mô hình Baseline đơn giản, tốc độ huấn luyện nhanh và cung cấp xác suất tự nhiên.

### 2.2. Rừng ngẫu nhiên (Random Forest — Mô hình tổ hợp đa cây)
- **Nguyên lý hoạt động:** Kết hợp $B$ cây quyết định độc lập bằng kỹ thuật **Bootstrap Aggregating (Bagging)** và ngẫu nhiên hóa không gian đặc trưng (**Feature Randomization**, chọn $m = \lfloor\sqrt{d}\rfloor$ đặc trưng tại mỗi nút chia).
- **Tiêu chuẩn phân nhánh:** Sử dụng độ vẩn đục Gini Impurity:
  $$\text{Gini}(t) = 1 - \sum_{c=0}^{1} p(c \mid t)^2$$
- **Đầu ra:** Tổng hợp qua cơ chế Soft-Voting: $\hat{P}(y = 1 \mid \mathbf{x}) = \frac{1}{B}\sum_{b=1}^B P_b(y = 1 \mid \mathbf{x})$.
- **Ưu thế y khoa:** Kháng đa cộng tuyến cao, xử lý tốt cả biến định lượng lẫn định tính, hỗ trợ trích xuất thuộc tính quan trọng (`feature_importances_`) phục vụ giải thích quyết định.

### 2.3. Máy vector hỗ trợ (Support Vector Machine — SVM)
- **Nguyên lý:** Tìm siêu phẳng phân tách $f(\mathbf{x}) = \mathbf{w}^T\phi(\mathbf{x}) + b$ sao cho độ mở lề hình học (Margin) giữa hai lớp là lớn nhất:
  $$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2}\|\mathbf{w}\|_2^2 + C \sum_{i=1}^N \xi_i \quad \text{với } y_i(\mathbf{w}^T\phi(\mathbf{x}_i) + b) \ge 1 - \xi_i, \ \xi_i \ge 0$$
- **Nhân phi tuyến (RBF Kernel):** $K(\mathbf{x}_i, \mathbf{x}_j) = \exp(-\gamma\|\mathbf{x}_i - \mathbf{x}_j\|^2)$, phân chia ranh giới phi tuyến phức tạp trong không gian nhiều chiều.

---

## 3. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Tài liệu tóm tắt lý thuyết 3 thuật toán phân lớp dự kiến sử dụng (lưu trữ trong `word_demo/02_Chuong_2_Co_So_Ly_Thuyet.md`).
  - [x] Bảng xác định bài toán y tế: Ưu tiên chỉ số **Recall $\ge 96.0\%$** và **ROC-AUC $\ge 0.99$** để tránh bỏ sót bệnh nhân suy thận.
- **Kế hoạch Tuần 03 tiếp theo:** Nghiên cứu Decision Tree, Naïve Bayes, k-NN, kỹ thuật giảm chiều PCA và xây dựng **bộ ví dụ tính toán thủ công từng bước**.
