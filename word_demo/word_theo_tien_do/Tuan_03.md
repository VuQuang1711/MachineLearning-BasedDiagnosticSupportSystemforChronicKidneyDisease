# BÁO CÁO TIẾN ĐỘ TUẦN 03 — LÝ THUYẾT THUẬT TOÁN HỌC MÁY (PHẦN 2) & VÍ DỤ MINH HỌA

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Giai đoạn 1 (Tuần 2–3)
- **Liên hệ Rubric:** Tự học và vận dụng tài liệu chuyên ngành trong bài tập nhóm (PLO4 / CLO2 — Trọng số: 10% / Điểm: 1.0)
- **Thành viên chủ trì:** Nguyễn Đình Bảo Tấn (`2405240270`)
- **Trạng thái:** Hoàn thành 100%

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 3)
1. **Tìm hiểu lý thuyết các thuật toán học máy bổ sung & giảm chiều dữ liệu:**
   - Hoàn thiện cơ sở lý thuyết toán học cho: **Cây quyết định (Decision Tree — CART)**, **Gaussian Naïve Bayes (GNB)**, và **k-Láng giềng gần nhất (k-NN)**.
   - Nghiên cứu kỹ thuật giảm số chiều không giám sát **Phân tích thành phần chính (PCA)** nhằm khảo sát khả năng nén đặc trưng và trực quan hóa dữ liệu trong không gian 2D.
2. **Xây dựng ví dụ minh họa cách hoạt động của thuật toán (Hand Calculation):**
   - Thiết kế các bài toán mẫu tính toán thủ công từng bước trên tập dữ liệu y tế giả lập thu nhỏ để thể hiện sinh viên hiểu sâu sắc bản chất vận hành của giải thuật, đáp ứng đúng yêu cầu của Bộ môn KHDL.

---

## 2. Kết Quả Nghiên Cứu Lý Thuyết Bổ Sung

### 2.1. Cây quyết định (Decision Tree — CART)
- **Cơ chế:** Phân chia không gian đặc trưng bằng các lát cắt trực giao nhị phân sao cho độ vẩn đục Gini giảm nhiều nhất:
  $$\Delta \text{Gini} = \text{Gini}(t) - \left( \frac{n_L}{n} \text{Gini}(t_L) + \frac{n_R}{n} \text{Gini}(t_R) \right)$$
- Cực kỳ trực quan, dễ diễn giải nhưng có nguy cơ bị quá khớp (overfitting) nếu cây phát triển quá sâu.

### 2.2. Bộ phân lớp Bayes ngây thơ Gauss (Gaussian Naïve Bayes — GNB)
- **Nguyên lý:** Áp dụng định lý Bayes với giả định ngây thơ các đặc trưng độc lập có điều kiện theo từng lớp:
  $$P(y = c \mid \mathbf{x}) \propto P(y = c) \prod_{j=1}^{d} \mathcal{N}(x_j; \mu_{c,j}, \sigma_{c,j}^2)$$
- Tốc độ tính toán tức thời nhưng nhạy cảm nếu dữ liệu vi phạm giả định độc lập (ví dụ tương quan mạnh giữa Hemoglobin và PCV).

### 2.3. k-Láng giềng gần nhất (k-Nearest Neighbors — k-NN)
- **Nguyên lý:** Phân lớp dựa trên khoảng cách Euclid trong không gian đặc trưng sau khi đã chuẩn hóa Z-Score:
  $$d(\mathbf{x}, \mathbf{x}_i) = \sqrt{\sum_{j=1}^d (x_j - x_{ij})^2}$$
- Không có pha huấn luyện tham số tường minh (Lazy Learning), thời gian suy luận phụ thuộc trực tiếp vào kích thước tập dữ liệu mẫu.

### 2.4. Phân tích thành phần chính (PCA)
- Chiếu dữ liệu sang hệ tọa độ trực giao mới của các vector riêng ma trận hiệp phương sai $\mathbf{\Sigma} = \frac{1}{N-1}\mathbf{Z}^T\mathbf{Z}$, sắp xếp theo trị riêng giảm dần để giữ lại thành phần mang phương sai lớn nhất.

---

## 3. Bộ 3 Ví Dụ Tính Toán Thủ Công Từng Bước (Hand Calculation)

Nhóm đã xây dựng tập mẫu giả lập 4 bệnh nhân với 3 thuộc tính xét nghiệm: Tuổi (`age`), Serum Creatinine (`sc`), Hemoglobin (`hemo`):
- **Bệnh nhân 1:** `age=48, sc=1.2, hemo=15.4` $\to$ Lớp 0 (Khỏe mạnh).
- **Bệnh nhân 2:** `age=62, sc=3.8, hemo=9.6` $\to$ Lớp 1 (Suy thận CKD).
- **Bệnh nhân 3:** `age=50, sc=1.0, hemo=14.0` $\to$ Lớp 0 (Khỏe mạnh).
- **Bệnh nhân 4:** `age=70, sc=4.5, hemo=8.2` $\to$ Lớp 1 (Suy thận CKD).

### Ba ví dụ tính toán thủ công chi tiết đã hoàn thành:
1. **Ví dụ 1 (Chuẩn hóa Z-Score & Phân lớp k-NN $k=3$):** Tính tay giá trị trung bình $\mu$, độ lệch chuẩn $\sigma$ cho từng cột, chuẩn hóa vector bệnh nhân mới (`age=55, sc=2.5, hemo=10.5`), đo khoảng cách Euclid đến 4 mẫu và suy luận ra kết quả $y=1$ (CKD) với xác suất $2/3$.
2. **Ví dụ 2 (Chọn nút gốc Cây quyết định CART):** Tính chỉ số Gini gốc của tập mẫu, duyệt qua điểm cắt `sc = 2.5 mg/dL` và chứng minh $\Delta \text{Gini} = 0.5$, chia hoàn hảo hai nhóm mà không còn vẩn đục.
3. **Ví dụ 3 (Tính xác suất hậu nghiệm Gaussian Naïve Bayes):** Tính hàm mật độ Gauss cho từng biến và áp dụng công thức tích để tìm xác suất hậu nghiệm $P(\text{CKD} \mid \mathbf{x})$.

---

## 4. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Tài liệu tóm tắt đầy đủ lý thuyết 6 thuật toán phân lớp và kỹ thuật giảm chiều PCA.
  - [x] Bộ 3 ví dụ tính toán thủ công từng bước minh họa rõ ràng cách hoạt động của thuật toán (được tích hợp trong cả Notebook và Báo cáo).
- **Kế hoạch Tuần 04 tiếp theo:** Tìm và xác nhận bộ dữ liệu chuẩn, kiểm toán số lượng mẫu, đặc trưng và các lỗi dữ liệu thô.
