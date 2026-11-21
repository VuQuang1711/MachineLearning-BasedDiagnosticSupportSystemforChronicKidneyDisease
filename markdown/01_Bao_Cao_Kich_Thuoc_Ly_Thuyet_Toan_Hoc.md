# BÁO CÁO KÍCH THƯỚC LÝ THUYẾT, CƠ SỞ TOÁN HỌC VÀ CÁC THUẬT TOÁN HỌC MÁY CHẨN ĐOÁN BỆNH THẬN MÃN TÍNH (CKD)

**Mã đề tài:** BT04 — Chẩn đoán Bệnh Thận (Kidney Disease Diagnosis)  
**Học phần:** Học Máy (Machine Learning) — Năm học: 2026–2027  
**Lớp học phần:** 15DHKHDL04  
**Giảng viên hướng dẫn (GVHD):** ThS. Nguyễn Thị Huyền Trang  
**Bộ môn:** Khoa học Dữ liệu (KHDL) — Khoa Công Nghệ Thông Tin — Trường Đại học Công Thương TP.HCM (HUIT)  
**Bộ dữ liệu:** Kaggle / UCI Chronic Kidney Disease Dataset ($N = 400$, $D = 24$)  
**Chuẩn đầu ra đáp ứng:** CLO1 (Cơ sở toán học & thuật toán phân lớp), CLO2 (Tiền xử lý & Xây dựng mô hình), CLO4 (Đánh giá & Tối ưu hóa)

### THÀNH VIÊN THỰC HIỆN & PHÂN CÔNG CHUYÊN ĐỀ TOÁN HỌC
- **Nguyễn Đình Bảo Tấn** (MSSV: `2405240270`): Chịu trách nhiệm chính — Nghiên cứu giải tích toán học 6 thuật toán, đạo hàm hàm mất mát, xác suất Naïve Bayes, và trực tiếp giải chi tiết 3 ví dụ tính tay (Hand Calculation).
- **Triệu Thị Thu Ngân** (MSSV: `2405240179`): Phân tích kích thước không gian ma trận dữ liệu $\mathbf{X} \in \mathbb{R}^{400 \times 24}$, miền giá trị 24 thuộc tính và ma trận tương quan Pearson.
- **Vũ Thế Quang** (MSSV: `2045240253`): Xây dựng không gian tiền xử lý sau mã hóa $\mathbf{X}_{\text{proc}} \in \mathbb{R}^{400 \times 35}$, chuẩn hóa Z-Score và One-Hot.
- **Võ Tấn Đạt** (MSSV: `2045240050` - Trưởng nhóm): Thẩm định công thức toán học, liên kết cơ sở lý thuyết vào Pipeline nguyên khối và điều phối báo cáo.
- **Nguyễn Thanh Nhàn** (MSSV: `2405240198`): Mô hình hóa toán học công thức lâm sàng eGFR MDRD (KDIGO 2024) và chuyển đổi toán học sang Explainable AI.

---

## 1. TỔNG QUAN BÀI TOÁN VÀ KHÔNG GIAN TOÁN HỌC DỮ LIỆU BỆNH THẬN

### 1.1. Bối cảnh Lâm sàng và Bài toán Học máy
Bệnh thận mãn tính (*Chronic Kidney Disease* - CKD) là tình trạng tổn thương thận tiến triển không hồi phục qua nhiều tháng hoặc nhiều năm, dẫn đến suy giảm mức lọc cầu thận (*Estimated Glomerular Filtration Rate* - eGFR). Việc phát hiện sớm bệnh thận qua các xét nghiệm máu, nước tiểu và tiền sử bệnh lý đóng vai trò sống còn để ngăn chặn bệnh nhân chuyển sang giai đoạn suy thận cuối (*End-Stage Renal Disease* - ESRD) phải chạy thận nhân tạo định kỳ hoặc ghép thận.

Dưới góc độ Học máy, bài toán được định nghĩa là **Phân lớp nhị phân có giám sát (Supervised Binary Classification)**:
* Cho tập dữ liệu quan sát $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$, mục tiêu là học một ánh xạ giả thuyết $f: \mathcal{X} \to \mathcal{Y}$ sao cho cực tiểu hóa hàm mất mát kỳ vọng trên phân phối dữ liệu chưa từng thấy.
* Không gian đầu vào: $\mathcal{X} \subseteq \mathbb{R}^D$ với $D = 24$ thuộc tính đặc trưng lâm sàng.
* Không gian nhãn mục tiêu: $\mathcal{Y} = \{0, 1\}$, trong đó:
  * $y_i = 1$ đại diện cho ca bệnh: mắc bệnh thận mãn tính (`ckd`).
  * $y_i = 0$ đại diện cho ca đối chứng: không mắc bệnh thận (`notckd`).

### 1.2. Kích thước Không gian Dữ liệu Ma trận (Matrix Dimensions)
Tập dữ liệu hoàn chỉnh được biểu diễn dưới dạng ma trận đặc trưng hai chiều và vector nhãn:

$$\mathbf{X} \in \mathbb{R}^{N \times D}, \quad \mathbf{y} \in \{0, 1\}^N$$

Trong đó:
* Kích thước mẫu: $N = 400$ bệnh nhân quan sát lâm sàng.
* Số chiều đặc trưng ban đầu: $D = 24$ chiều.
* Phân phối nhãn: $N_1 = 250$ mẫu nhãn `ckd` ($62.5\%$) và $N_0 = 150$ mẫu nhãn `notckd` ($37.5\%$).

Không gian vector đầu vào ban đầu là không gian hỗn hợp (*Heterogeneous Feature Space*), bao gồm:
1. Không gian đặc trưng định lượng (Numerical): $\mathbf{X}_{\text{num}} \in \mathbb{R}^{N \times 11}$ ($d_{\text{num}} = 11$).
2. Không gian đặc trưng định tính (Categorical/Ordinal): $\mathbf{X}_{\text{cat}} \in \mathcal{S}^{N \times 13}$ ($d_{\text{cat}} = 13$).

Sau khi áp dụng mã hóa One-Hot Encoding cho các biến danh mục (với kỹ thuật loại bỏ cột đầu `drop='first'` để tránh hiện tượng đa cộng tuyến *Multicollinearity*), số chiều không gian đặc trưng thực tế đưa vào các mô hình học máy tăng lên:

$$D^* = d_{\text{num}} + d_{\text{onehot}} = 11 + 24 = 35 \text{ chiều}$$

Do đó, ma trận dữ liệu chuẩn hóa nạp vào giải thuật tối ưu có kích thước:

$$\mathbf{X}^* \in \mathbb{R}^{400 \times 35}$$

---

## 2. PHÂN LOẠI CHI TIẾT 24 ĐẶC TRƯNG LÂM SÀNG & Ý NGHĨA SINH HÓA

### 2.1. Nhóm 11 Đặc trưng Định lượng Liên tục / Đếm ($\mathbf{X}_{\text{num}}$)

| Ký hiệu | Tên Thuộc tính (Tiếng Anh) | Tên Chỉ số Lâm sàng (Tiếng Việt) | Miền giá trị thực tế | Đơn vị đo | Ý nghĩa Y khoa Chẩn đoán Thận |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `age` | Age | Tuổi bệnh nhân | $2 - 90$ | Năm | Tuổi cao làm xơ hóa mạch máu thận và suy giảm eGFR tự nhiên. |
| `bp` | Blood Pressure | Huyết áp lúc nghỉ | $50 - 180$ | mmHg | Tăng huyết áp phá hủy mao mạch cầu thận; vừa là nguyên nhân vừa là hệ quả của CKD. |
| `bgr` | Blood Glucose Random | Đường huyết ngẫu nhiên | $22 - 490$ | mg/dL | Đường huyết cao mạn tính gây tổn thương màng đáy cầu thận (*Đái tháo đường biến chứng thận*). |
| `bu` | Blood Urea | Urê máu | $1.5 - 391$ | mg/dL | Sản phẩm thoái hóa protein; thận suy giảm bài tiết làm Urê máu tích tụ gây nhiễm độc ure huyết. |
| `sc` | Serum Creatinine | Creatinine huyết thanh | $0.4 - 76.0$ | mg/dL | **Chỉ số sinh hóa vàng**: Creatinine là chỉ báo nhạy nhất của chức năng lọc cầu thận. |
| `sod` | Sodium | Nồng độ Natri máu | $4.5 - 163$ | mEq/L | Thận điều hòa tái hấp thu nước và Natri; mất cân bằng gây phù nề và rối loạn điện giải. |
| `pot` | Potassium | Nồng độ Kali máu | $2.5 - 47.0$ | mEq/L | Tăng Kali máu (*Hyperkalemia*) ở bệnh nhân suy thận cấp/mạn là nguy cơ ngừng tim đột ngột. |
| `hemo` | Hemoglobin | Huyết sắc tố Hemoglobin | $3.1 - 17.8$ | g/dL | Thận tiết hoocmon *Erythropoietin* kích thích sinh hồng cầu; CKD gây thiếu máu trầm trọng. |
| `pcv` | Packed Cell Volume | Dung tích hồng cầu | $9 - 54$ | $\%$ | Tỷ lệ thể tích hồng cầu trên thể tích máu toàn phần; tương quan thuận chặt chẽ với `hemo`. |
| `wc` | White Blood Cell Count | Số lượng bạch cầu | $2,200 - 26,400$ | cells/$\mu$L | Bạch cầu tăng cao là dấu hiệu viêm mạn tính hoặc nhiễm trùng hệ tiết niệu. |
| `rc` | Red Blood Cell Count | Số lượng hồng cầu | $2.1 - 8.0$ | triệu/$\mu$L | Giảm số lượng hồng cầu trực tiếp phản ánh mức độ thiếu máu do suy tủy thứ phát ở bệnh thận. |

### 2.2. Nhóm 13 Đặc trưng Định tính & Tiền sử Bệnh lý ($\mathbf{X}_{\text{cat}}$)

| Ký hiệu | Thuộc tính | Giá trị hợp lệ | Kiểu mã hóa | Ý nghĩa Lâm sàng & Xét nghiệm nước tiểu |
| :--- | :--- | :--- | :--- | :--- |
| `sg` | Specific Gravity | $1.005, 1.010, 1.015, 1.020, 1.025$ | Thứ tự / One-Hot | Tỷ trọng nước tiểu; phản ánh khả năng cô đặc nước tiểu của ống thận. |
| `al` | Albumin | $0, 1, 2, 3, 4, 5$ | Thứ tự / One-Hot | Đạm niệu; màng lọc cầu thận bị rách cho phép protein lọt vào nước tiểu. |
| `su` | Sugar | $0, 1, 2, 3, 4, 5$ | Thứ tự / One-Hot | Đường niệu; xuất hiện khi đường huyết vượt quá ngưỡng tái hấp thu của thận. |
| `rbc` | Red Blood Cells | `normal`, `abnormal` | Nhị phân ($0/1$) | Hồng cầu niệu; tổn thương đài bể thận hoặc viêm cầu thận cấp. |
| `pc` | Pus Cell | `normal`, `abnormal` | Nhị phân ($0/1$) | Tế bào mủ trong nước tiểu; báo hiệu nhiễm khuẩn đường tiết niệu (*UTI*). |
| `pcc` | Pus Cell Clumps | `present`, `notpresent` | Nhị phân ($0/1$) | Đám tế bào mủ; nhiễm trùng thận nặng hoặc viêm bể thận mạn. |
| `ba` | Bacteria | `present`, `notpresent` | Nhị phân ($0/1$) | Vi khuẩn niệu; xác nhận tình trạng nhiễm khuẩn thận - tiết niệu. |
| `htn` | Hypertension | `yes`, `no` | Nhị phân ($0/1$) | Tiền sử tăng huyết áp mạn tính. |
| `dm` | Diabetes Mellitus | `yes`, `no` | Nhị phân ($0/1$) | Tiền sử bệnh đái tháo đường týp 1 hoặc 2. |
| `cad` | Coronary Artery Disease | `yes`, `no` | Nhị phân ($0/1$) | Bệnh mạch vành tim (bệnh tim mạch đồng mắc nguy hiểm). |
| `appet` | Appetite | `good`, `poor` | Nhị phân ($0/1$) | Cảm giác thèm ăn; chán ăn là triệu chứng của hội chứng tăng ure huyết. |
| `pe` | Pedal Edema | `yes`, `no` | Nhị phân ($0/1$) | Phù mắt cá chân/mu bàn chân do ứ trệ dịch và giảm áp lực keo huyết tương. |
| `ane` | Anemia | `yes`, `no` | Nhị phân ($0/1$) | Hội chứng thiếu máu lâm sàng (da xanh xao, mệt mỏi mạn tính). |

---

## 3. CƠ SỞ TOÁN HỌC TIỀN XỬ LÝ DỮ LIỆU & CHỐNG RÒ RỈ DỮ LIỆU (DATA LEAKAGE)

### 3.1. Phân tích Hiện trạng Ô khuyết (Missing Data Mechanism)
Trong 400 mẫu bệnh nhân, toàn bộ $24/24$ thuộc tính đều chứa giá trị khuyết (*Missing Values*, tổng $1,012 / 9,600$ ô = $10.54\%$), rải rác từ $0.25\%$ đến $38.0\%$ (ví dụ `rbc` thiếu 152 mẫu, `rc` thiếu 131 mẫu, `wc` thiếu 106 mẫu), trong khi kiểm toán xác nhận $0$ dòng trùng lặp và $0$ cột hằng số. Cơ chế khuyết thuộc dạng **MAR (Missing At Random)** do quy trình khám lâm sàng không bắt buộc bệnh nhân làm toàn bộ xét nghiệm chuyên sâu nếu không có chỉ định đặc thù.

### 3.2. Công thức Điền Giá trị Khuyết (Imputation Formula)
Nhằm triệt tiêu nguy cơ rò rỉ dữ liệu (*Data Leakage*), quy tắc vàng là: **Mọi tham số thống kê chỉ được học trên tập huấn luyện $\mathcal{D}_{\text{train}}$ và áp dụng nguyên vẹn sang tập kiểm thử $\mathcal{D}_{\text{test}}$**.

#### A. Đối với 11 biến định lượng liên tục ($j \in \text{Numerical}$):
Sử dụng giá trị **Trung vị (Median)** thay vì Trung bình cộng (Mean) để kháng lại độ lệch ngoại lai (*Robust to Outliers*):

$$\hat{x}_{j} = \text{Median}\left(\{x_{i,j}\}_{i \in \text{Train}}\right)$$

Nếu phần tử thứ $j$ của mẫu bệnh nhân $i$ bị khuyết:

$$x_{i,j} \leftarrow \hat{x}_{j}$$

#### B. Đối với 13 biến định tính danh mục ($j \in \text{Categorical}$):
Sử dụng giá trị **Yếu vị (Mode)** — nhãn xuất hiện nhiều nhất trong tập huấn luyện:

$$\hat{x}_{j} = \arg\max_{c \in \mathcal{C}_j} \sum_{i \in \text{Train}} \mathbb{I}(x_{i,j} = c)$$

Trong đó $\mathbb{I}(\cdot)$ là hàm chỉ thị (*Indicator Function*), $\mathcal{C}_j$ là tập các giá trị hợp lệ của thuộc tính $j$.

### 3.3. Công thức Chuẩn hóa Thang đo Z-score (StandardScaler)
Các thuật toán dựa trên khoảng cách ($k\text{-NN}, \text{SVM}$) và tối ưu hóa Gradient Descent ($\text{Logistic Regression}$) cực kỳ nhạy cảm với thang đo của thuộc tính. Thuật toán Z-score đưa mỗi đặc trưng liên tục về phân phối có trung bình $\mu = 0$ và độ lệch chuẩn $\sigma = 1$:

$$\mu_j = \frac{1}{N_{\text{train}}} \sum_{i \in \text{Train}} x_{i,j}, \quad \sigma_j = \sqrt{\frac{1}{N_{\text{train}}} \sum_{i \in \text{Train}} (x_{i,j} - \mu_j)^2 + \epsilon}$$

Ánh xạ chuẩn hóa cho mọi mẫu $x_{i,j}$ (trên cả Train và Test):

$$z_{i,j} = \frac{x_{i,j} - \mu_j}{\sigma_j}$$

Trong đó $\epsilon = 10^{-8}$ là số cực tiểu dương ngăn chặn lỗi chia cho 0 khi thuộc tính có phương sai triệt tiêu.

### 3.4. Công thức Mã hóa One-Hot Encoding
Với biến định tính $x_j$ nhận một trong các trạng thái $\{c_1, c_2, \dots, c_K\}$, ánh xạ mã hóa tạo ra $K-1$ biến chỉ thị nhị phân:

$$\mathbf{v}(x_j) = \left[ \mathbb{I}(x_j = c_2), \mathbb{I}(x_j = c_3), \dots, \mathbb{I}(x_j = c_K) \right]^T \in \{0, 1\}^{K-1}$$

Cột đầu tiên $c_1$ đóng vai trò là mốc tham chiếu (*Reference Category*), giúp loại bỏ hoàn toàn ma trận suy biến do đa cộng tuyến tuyến tính hoàn hảo.

---

## 4. CƠ SỞ TOÁN HỌC GIẢM CHIỀU DỮ LIỆU: PCA VÀ LDA (ĐÁP ỨNG CHUẨN ĐẦU RA CLO1)

Để đáp ứng câu chữ của chuẩn đầu ra môn học CLO1 (*"Áp dụng các phương pháp giảm chiều dữ liệu vào tối ưu các phương pháp phân lớp"*), hệ thống nghiên cứu 2 phương pháp giảm chiều tiêu biểu: PCA (học không giám sát) và LDA (học có giám sát).

### 4.1. Phân tích Thành phần Chính (Principal Component Analysis - PCA)

#### Mục tiêu toán học:
Tìm phép chiếu trực giao chiếu ma trận dữ liệu chuẩn hóa $\mathbf{Z} \in \mathbb{R}^{N \times D^*}$ (với $D^* = 35$) sang không gian con $k$ chiều ($k \ll D^*$) sao cho bảo toàn tối đa phương sai của dữ liệu.

```
Ma trận dữ liệu Z (N x 35) ──> Ma trận Hiệp phương sai Σ (35 x 35) ──> Giải Trị riêng/Vector riêng ──> Giữ k=19 thành phần (95% phương sai)
```

#### Quy trình tính toán ma trận:
1. **Tính ma trận hiệp phương sai mẫu $\boldsymbol{\Sigma} \in \mathbb{R}^{D^* \times D^*}$:**

   $$\boldsymbol{\Sigma} = \frac{1}{N_{\text{train}}} \mathbf{Z}_{\text{train}}^T \mathbf{Z}_{\text{train}}$$

2. **Giải bài toán phân rã phổ (Eigendecomposition):**

   $$\boldsymbol{\Sigma} \mathbf{v}_m = \lambda_m \mathbf{v}_m, \quad \forall m \in \{1, 2, \dots, D^*\}$$

   Trong đó $\lambda_m \ge 0$ là trị riêng (*eigenvalue*), $\mathbf{v}_m \in \mathbb{R}^{D^*}$ là vector riêng trực chuẩn tương ứng ($\|\mathbf{v}_m\|_2 = 1, \mathbf{v}_m^T \mathbf{v}_l = 0$ khi $m \neq l$).

3. **Sắp xếp trị riêng giảm dần và chọn $k$ thành phần chính:**

   $$\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_{D^*}$$

   Xác định $k$ nhỏ nhất thỏa mãn tiêu chuẩn tỷ lệ phương sai tích lũy (*Cumulative Explained Variance Ratio*) đạt tối thiểu $95\%$:

   $$\text{CEVR}(k) = \frac{\sum_{m=1}^k \lambda_m}{\sum_{j=1}^{D^*} \lambda_j} \ge 0.95$$

   *Thực nghiệm thực tế trên tập CKD Train:* Để đạt $95\%$ phương sai tích lũy, hệ thống nén từ $D^* = 35$ chiều xuống còn $k = 19$ thành phần chính.

4. **Ma trận chiếu trực giao:**

   $$\mathbf{W}_{\text{PCA}} = [\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k] \in \mathbb{R}^{D^* \times k}$$

   Tọa độ mới của bệnh nhân: $\mathbf{z}_{\text{new\_pca}} = \mathbf{W}_{\text{PCA}}^T \mathbf{z} \in \mathbb{R}^k$.

### 4.2. Phân tích Biệt thức Tuyến tính (Linear Discriminant Analysis - LDA)

Khác với PCA, LDA là phương pháp chiếu có giám sát (*Supervised Dimensionality Reduction*), tìm kiếm siêu phẳng tối đa hóa khả năng phân tách giữa hai lớp bệnh nhân (`ckd` vs `notckd`).

#### Tiêu chuẩn Fisher (Fisher's Criterion):
Tối đa hóa tỷ số giữa phương sai liên lớp (*Between-class Scatter*) và phương sai nội lớp (*Within-class Scatter*):

$$J(\mathbf{w}) = \frac{\mathbf{w}^T \mathbf{S}_B \mathbf{w}}{\mathbf{w}^T \mathbf{S}_W \mathbf{w}}$$

Trong đó:
* **Ma trận tán xạ nội lớp $\mathbf{S}_W$:**

  $$\mathbf{S}_W = \sum_{c \in \{0, 1\}} \sum_{i \in \text{Class } c} (\mathbf{x}_i - \boldsymbol{\mu}_c)(\mathbf{x}_i - \boldsymbol{\mu}_c)^T$$

* **Ma trận tán xạ liên lớp $\mathbf{S}_B$:**

  $$\mathbf{S}_B = (\boldsymbol{\mu}_1 - \boldsymbol{\mu}_0)(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_0)^T$$

* Vector trọng số tối ưu là nghiệm của bài toán trị riêng tổng quát:

  $$\mathbf{S}_W^{-1} \mathbf{S}_B \mathbf{w} = \lambda \mathbf{w} \implies \mathbf{w}^* \propto \mathbf{S}_W^{-1} (\boldsymbol{\mu}_1 - \boldsymbol{\mu}_0)$$

---

## 5. CÔNG THỨC TOÁN HỌC VÀ THUẬT TOÁN TỐI ƯU CỦA 6 MÔ HÌNH HỌC MÁY

### 5.1. Mô hình 1: Logistic Regression (Hồi quy Logistic)

#### Biểu diễn toán học:
Logistic Regression mô hình hóa xác suất hậu nghiệm bệnh nhân mắc bệnh thận mãn tính ($y=1$) thông qua hàm kích hoạt Sigmoid chuẩn:

$$P(y=1|\mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$

Trong đó $\mathbf{w} \in \mathbb{R}^{D^*}$ là vector trọng số (*weights*), $b \in \mathbb{R}$ là hệ số điều chỉnh (*bias*).

#### Hàm mục tiêu mất mát với điều hòa $L_2$ (Ridge Regularization):
Để ngăn ngừa Overfitting khi không gian đặc trưng lớn, hàm mất mát Binary Cross-Entropy kết hợp đại lượng phạt chuẩn $L_2$:

$$\mathcal{J}(\mathbf{w}, b) = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \ln \hat{y}_i + (1 - y_i) \ln (1 - \hat{y}_i) \right] + \frac{\lambda}{2} \|\mathbf{w}\|_2^2$$

Với $\hat{y}_i = \sigma(\mathbf{w}^T \mathbf{x}_i + b)$ và $\lambda = \frac{1}{C}$ là tham số phạt.

#### Đạo hàm và Quy tắc cập nhật Gradient Descent:

$$\frac{\partial \mathcal{J}}{\partial \mathbf{w}} = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i) \mathbf{x}_i + \lambda \mathbf{w}, \quad \frac{\partial \mathcal{J}}{\partial b} = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i)$$

$$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \eta \frac{\partial \mathcal{J}}{\partial \mathbf{w}}, \quad b^{(t+1)} = b^{(t)} - \eta \frac{\partial \mathcal{J}}{\partial b}$$

Trong đó $\eta > 0$ là tốc độ học (*learning rate*).

---

### 5.2. Mô hình 2: Support Vector Machine (SVM)

#### Bài toán tối ưu lề cực đại biên mềm (Soft-Margin SVM):
Trong dữ liệu y sinh thực tế, hai lớp thường không tách biệt tuyến tính tuyệt đối. Soft-margin SVM cho phép một số điểm rơi vào vùng vi phạm lề qua biến bù $\xi_i \ge 0$:

$$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \left\{ \frac{1}{2} \|\mathbf{w}\|_2^2 + C \sum_{i=1}^N \xi_i \right\}$$

Ràng buộc:

$$y_i (\mathbf{w}^T \phi(\mathbf{x}_i) + b) \ge 1 - \xi_i, \quad \xi_i \ge 0, \quad \forall i \in \{1, \dots, N\}$$

Trong đó:
* $y_i \in \{-1, +1\}$ (quy ước nhãn SVM).
* $C > 0$: Siêu tham số kiểm soát sự đánh đổi giữa tối đa hóa độ rộng lề $\frac{2}{\|\mathbf{w}\|}$ và tối thiểu hóa tổng sai số phạt.
* $\phi(\mathbf{x})$: Ánh xạ phi tuyến biến đổi không gian đặc trưng vào không gian Hilbert vô hạn chiều.

#### Hàm nhân RBF Kernel (Radial Basis Function):
Thay vì tính toán trực tiếp $\phi(\mathbf{x})$, kỹ thuật Kernel Trick áp dụng hàm nhân RBF:

$$K(\mathbf{x}_i, \mathbf{x}_j) = \exp\left( -\gamma \|\mathbf{x}_i - \mathbf{x}_j\|_2^2 \right), \quad \gamma = \frac{1}{2\sigma^2} > 0$$

#### Bài toán đối ngẫu Lagrange (Dual Formulation):

$$\max_{\boldsymbol{\alpha}} \left\{ \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j K(\mathbf{x}_i, \mathbf{x}_j) \right\}$$

Thỏa mãn: $0 \le \alpha_i \le C$ và $\sum_{i=1}^N \alpha_i y_i = 0$.  
Hàm quyết định phân loại cho bệnh nhân mới $\mathbf{x}^*$:

$$\hat{y}^* = \text{sign}\left( \sum_{i \in \text{Support Vectors}} \alpha_i y_i K(\mathbf{x}_i, \mathbf{x}^*) + b \right)$$

---

### 5.3. Mô hình 3: Decision Tree (Cây Quyết Định - Thuật toán CART)

Cây quyết định phân chia không gian đặc trưng thành các siêu hình hộp chữ nhật trực giao thông qua các câu hỏi nhị phân dạng $x_j \le \theta$.

#### Độ đo bất thuần Gini (Gini Impurity) tại nút $m$:

$$G(m) = 1 - \sum_{k \in \{0, 1\}} p_{m,k}^2$$

Trong đó $p_{m,k} = \frac{1}{|m|} \sum_{i \in m} \mathbb{I}(y_i = k)$ là tỷ lệ bệnh nhân thuộc lớp $k$ tại nút $m$.

#### Độ đo hỗn loạn Entropy và Mức tăng thông tin (Information Gain):

$$H(m) = -\sum_{k \in \{0, 1\}} p_{m,k} \log_2(p_{m,k})$$

$$\text{Gain}(m, j, \theta) = H(m) - \left( \frac{|m_L|}{|m|} H(m_L) + \frac{|m_R|}{|m|} H(m_R) \right)$$

#### Tiêu chuẩn tách nhánh tối ưu (Split Criterion):
Tại mỗi bước phân nhánh, thuật toán CART duyệt qua toàn bộ thuộc tính $j \in \{1, \dots, D\}$ và ngưỡng cắt $\theta$ để tìm điểm chia làm giảm tối đa độ bất thuần:

$$(j^*, \theta^*) = \arg\min_{j, \theta} \left\{ \frac{|m_L|}{|m|} G(m_L) + \frac{|m_R|}{|m|} G(m_R) \right\}$$

---

### 5.4. Mô hình 4: Random Forest (Rừng Ngẫu Nhiên)

Random Forest là mô hình học kết hợp (*Ensemble Learning*) dựa trên nguyên lý **Bagging (Bootstrap Aggregating)** và **Không gian con ngẫu nhiên (Random Subspaces)**.

```
Tập dữ liệu D (N mẫu) ──> Bootstrap Sample 1 ──> Tree 1 (max_features = √D) ──┐
                     ──> Bootstrap Sample 2 ──> Tree 2 (max_features = √D) ──┼──> Majority Voting / Soft Voting
                     ──> Bootstrap Sample T ──> Tree T (max_features = √D) ──┘
```

#### Quy trình toán học:
1. **Lấy mẫu có hoàn lại (Bootstrap Sampling):** Tạo ra $T$ tập dữ liệu con $\mathcal{D}_1, \mathcal{D}_2, \dots, \mathcal{D}_T$, mỗi tập có kích thước $N$ lấy ngẫu nhiên có lặp lại từ $\mathcal{D}_{\text{train}}$. Xác suất một mẫu không được chọn vào tập bootstrap (*Out-Of-Bag - OOB*):

   $$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = \frac{1}{e} \approx 36.8\%$$

2. **Chọn tập con đặc trưng ngẫu nhiên (Feature Subsampling):** Tại mỗi nút của cây thứ $t$, chỉ xét ngẫu nhiên $d_{\text{sub}} = \lfloor \sqrt{D} \rfloor = \lfloor \sqrt{35} \rfloor \approx 5$ thuộc tính để tìm điểm tách nhánh tốt nhất. Kỹ thuật này làm giảm phương sai (*Variance Reduction*) bằng cách làm giảm hệ số tương quan giữa các cây:

   $$\text{Var}\left(\frac{1}{T} \sum_{t=1}^T f_t(\mathbf{x})\right) = \rho \sigma^2 + \frac{1 - \rho}{T} \sigma^2$$

   Khi $T \to \infty$ và $\rho \to 0$, phương sai của toàn rừng giảm sâu về 0 mà không làm tăng độ chệch (*Bias*).

3. **Kết hợp dự đoán (Soft Voting):**

   $$P(y=1|\mathbf{x}) = \frac{1}{T} \sum_{t=1}^T P_t(y=1|\mathbf{x})$$

   Quyết định chẩn đoán: $\hat{y} = \mathbb{I}\left(P(y=1|\mathbf{x}) \ge 0.5\right)$.

---

### 5.5. Mô hình 5: Gaussian Naïve Bayes

#### Định lý Bayes tổng quát:

$$P(y=k|\mathbf{x}) = \frac{P(y=k) P(\mathbf{x}|y=k)}{P(\mathbf{x})} \propto P(y=k) \prod_{j=1}^{D^*} P(x_j | y=k)$$

Giả định tiên quyết: Toàn bộ $D^*$ đặc trưng hoàn toàn **độc lập có điều kiện** khi biết nhãn lớp bệnh nhân ($y=k$).

#### Mật độ xác suất Gaussian cho biến liên tục:

$$P(x_j | y=k) = \frac{1}{\sqrt{2\pi \sigma_{k,j}^2}} \exp\left( -\frac{(x_j - \mu_{k,j})^2}{2\sigma_{k,j}^2} \right)$$

Trong đó $\mu_{k,j}$ và $\sigma_{k,j}^2$ là kỳ vọng và phương sai mẫu của đặc trưng $j$ thuộc lớp $k \in \{0, 1\}$.

Quy tắc gán nhãn Maximum A Posteriori (MAP):

$$\hat{y} = \arg\max_{k \in \{0, 1\}} \left\{ \ln P(y=k) + \sum_{j=1}^{D^*} \ln P(x_j | y=k) \right\}$$

---

### 5.6. Mô hình 6: k-Nearest Neighbors (k-NN)

k-NN là thuật toán học lười (*Lazy Learning / Instance-Based Learning*), không có pha huấn luyện tham số mà lưu trữ toàn bộ dữ liệu mẫu trong bộ nhớ.

#### Hàm khoảng cách Euclidean trong không gian $D^*$ chiều:

$$d(\mathbf{x}_{\text{query}}, \mathbf{x}_i) = \|\mathbf{z}_{\text{query}} - \mathbf{z}_i\|_2 = \sqrt{\sum_{j=1}^{D^*} (z_{\text{query}, j} - z_{i, j})^2}$$

#### Quy tắc bỏ phiếu đa số theo trọng số khoảng cách (Weighted Majority Voting):
Tập $K$ láng giềng gần nhất là $\mathcal{N}_K(\mathbf{x}_{\text{query}})$. Trọng số mỗi láng giềng:

$$w_i = \frac{1}{d(\mathbf{x}_{\text{query}}, \mathbf{x}_i) + \epsilon}$$

Xác suất dự đoán mắc bệnh CKD:

$$P(y=1|\mathbf{x}_{\text{query}}) = \frac{\sum_{i \in \mathcal{N}_K, y_i=1} w_i}{\sum_{i \in \mathcal{N}_K} w_i}$$

---

## 6. VÍ DỤ TÍNH TOÁN BẰNG TAY MINH HỌA CHI TIẾT (HAND CALCULATION)

Theo yêu cầu chuẩn mực của Đề cương môn học và Danh sách đề tài (chiếm trọn vẹn **1.0 điểm** trong rubric lý thuyết: *"Cho ví dụ minh họa từng nội dung, tính toán từng bước rõ ràng"*), dưới đây là ví dụ minh họa bằng tay thực hiện trên tập mẫu thu nhỏ gồm 4 bệnh nhân huấn luyện và 1 bệnh nhân mới cần chẩn đoán.

### 6.1. Bảng Dữ liệu Lâm sàng Mẫu Thu Nhỏ (4 Bệnh nhân Huấn luyện)
Xét 4 chỉ số sinh hóa then chốt: Tuổi (`age`), Creatinine huyết thanh (`sc`), Huyết sắc tố Hemoglobin (`hemo`), và Albumin nước tiểu (`al`).

| Mã BN | Tuổi (`age`) | Creatinine `sc` (mg/dL) | Hemoglobin `hemo` (g/dL) | Albumin `al` | Nhãn thực tế ($y$) | Trạng thái chẩn đoán |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **B1** | 48 | 1.2 | 15.4 | 0 | **0** | `notckd` (Khỏe mạnh) |
| **B2** | 60 | 6.8 | 9.6 | 3 | **1** | `ckd` (Suy thận mạn) |
| **B3** | 55 | 3.4 | 10.5 | 2 | **1** | `ckd` (Suy thận mạn) |
| **B4** | 42 | 0.9 | 16.0 | 0 | **0** | `notckd` (Khỏe mạnh) |

**Bệnh nhân mới cần chẩn đoán ($\mathbf{x}_{\text{new}}$):**
$$\mathbf{x}_{\text{new}} = [\text{age} = 50, \text{sc} = 2.5, \text{hemo} = 11.0, \text{al} = 1]$$

---

### 6.2. Bước 1: Tính toán Tham số Thống kê và Chuẩn hóa Z-Score Thủ công

#### 1. Tính Trung bình cộng ($\mu$) trên 4 bệnh nhân Train:
* $\mu_{\text{age}} = \frac{48 + 60 + 55 + 42}{4} = \frac{205}{4} = \mathbf{51.25}$
* $\mu_{\text{sc}} = \frac{1.2 + 6.8 + 3.4 + 0.9}{4} = \frac{12.3}{4} = \mathbf{3.075}$
* $\mu_{\text{hemo}} = \frac{15.4 + 9.6 + 10.5 + 16.0}{4} = \frac{51.5}{4} = \mathbf{12.875}$
* $\mu_{\text{al}} = \frac{0 + 3 + 2 + 0}{4} = \frac{5}{4} = \mathbf{1.25}$

#### 2. Tính Độ lệch chuẩn mẫu ($\sigma$) trên 4 bệnh nhân Train:
* $\sigma_{\text{age}} = \sqrt{\frac{(48 - 51.25)^2 + (60 - 51.25)^2 + (55 - 51.25)^2 + (42 - 51.25)^2}{4}} = \sqrt{\frac{10.5625 + 76.5625 + 14.0625 + 85.5625}{4}} = \sqrt{46.6875} \approx \mathbf{6.833}$
* $\sigma_{\text{sc}} = \sqrt{\frac{(1.2 - 3.075)^2 + (6.8 - 3.075)^2 + (3.4 - 3.075)^2 + (0.9 - 3.075)^2}{4}} = \sqrt{\frac{3.5156 + 13.8756 + 0.1056 + 4.7306}{4}} = \sqrt{5.5569} \approx \mathbf{2.357}$
* $\sigma_{\text{hemo}} = \sqrt{\frac{(15.4 - 12.875)^2 + (9.6 - 12.875)^2 + (10.5 - 12.875)^2 + (16.0 - 12.875)^2}{4}} = \sqrt{\frac{6.3756 + 10.7256 + 5.6406 + 9.7656}{4}} = \sqrt{8.1269} \approx \mathbf{2.851}$
* $\sigma_{\text{al}} = \sqrt{\frac{(0 - 1.25)^2 + (3 - 1.25)^2 + (2 - 1.25)^2 + (0 - 1.25)^2}{4}} = \sqrt{\frac{1.5625 + 3.0625 + 0.5625 + 1.5625}{4}} = \sqrt{1.6875} \approx \mathbf{1.299}$

#### 3. Chuẩn hóa Vector Bệnh nhân mới $\mathbf{x}_{\text{new}}$:
* $z_{\text{new, age}} = \frac{50 - 51.25}{6.833} = \mathbf{-0.183}$
* $z_{\text{new, sc}} = \frac{2.5 - 3.075}{2.357} = \mathbf{-0.244}$
* $z_{\text{new, hemo}} = \frac{11.0 - 12.875}{2.851} = \mathbf{-0.658}$
* $z_{\text{new, al}} = \frac{1 - 1.25}{1.299} = \mathbf{-0.192}$

$$\mathbf{z}_{\text{new}} = [-0.183, -0.244, -0.658, -0.192]$$

#### 4. Chuẩn hóa 4 Vector trong tập Huấn luyện:
* $\mathbf{z}_1 = \left[\frac{48-51.25}{6.833}, \frac{1.2-3.075}{2.357}, \frac{15.4-12.875}{2.851}, \frac{0-1.25}{1.299}\right] = [-0.476, -0.795, +0.886, -0.962]$
* $\mathbf{z}_2 = \left[\frac{60-51.25}{6.833}, \frac{6.8-3.075}{2.357}, \frac{9.6-12.875}{2.851}, \frac{3-1.25}{1.299}\right] = [+1.281, +1.580, -1.149, +1.347]$
* $\mathbf{z}_3 = \left[\frac{55-51.25}{6.833}, \frac{3.4-3.075}{2.357}, \frac{10.5-12.875}{2.851}, \frac{2-1.25}{1.299}\right] = [+0.549, +0.138, -0.833, +0.577]$
* $\mathbf{z}_4 = \left[\frac{42-51.25}{6.833}, \frac{0.9-3.075}{2.357}, \frac{16.0-12.875}{2.851}, \frac{0-1.25}{1.299}\right] = [-1.354, -0.923, +1.096, -0.962]$

---

### 6.3. Bước 2: Dự đoán bằng Thuật toán k-NN ($k=3$) Thủ công

Tính khoảng cách Euclidean từ $\mathbf{z}_{\text{new}}$ đến 4 điểm huấn luyện:

1. **Khoảng cách tới B1 ($y=0$):**
   $$d(\mathbf{z}_{\text{new}}, \mathbf{z}_1) = \sqrt{(-0.183 - (-0.476))^2 + (-0.244 - (-0.795))^2 + (-0.658 - 0.886)^2 + (-0.192 - (-0.962))^2}$$
   $$= \sqrt{(0.293)^2 + (0.551)^2 + (-1.544)^2 + (0.770)^2} = \sqrt{0.0858 + 0.3036 + 2.3839 + 0.5929} = \sqrt{3.3662} \approx \mathbf{1.835}$$

2. **Khoảng cách tới B2 ($y=1$):**
   $$d(\mathbf{z}_{\text{new}}, \mathbf{z}_2) = \sqrt{(-0.183 - 1.281)^2 + (-0.244 - 1.580)^2 + (-0.658 - (-1.149))^2 + (-0.192 - 1.347)^2}$$
   $$= \sqrt{(-1.464)^2 + (-1.824)^2 + (0.491)^2 + (-1.539)^2} = \sqrt{2.1433 + 3.3270 + 0.2411 + 2.3685} = \sqrt{8.0799} \approx \mathbf{2.843}$$

3. **Khoảng cách tới B3 ($y=1$):**
   $$d(\mathbf{z}_{\text{new}}, \mathbf{z}_3) = \sqrt{(-0.183 - 0.549)^2 + (-0.244 - 0.138)^2 + (-0.658 - (-0.833))^2 + (-0.192 - 0.577)^2}$$
   $$= \sqrt{(-0.732)^2 + (-0.382)^2 + (0.175)^2 + (-0.769)^2} = \sqrt{0.5358 + 0.1459 + 0.0306 + 0.5914} = \sqrt{1.3037} \approx \mathbf{1.142}$$

4. **Khoảng cách tới B4 ($y=0$):**
   $$d(\mathbf{z}_{\text{new}}, \mathbf{z}_4) = \sqrt{(-0.183 - (-1.354))^2 + (-0.244 - (-0.923))^2 + (-0.658 - 1.096)^2 + (-0.192 - (-0.962))^2}$$
   $$= \sqrt{(1.171)^2 + (0.679)^2 + (-1.754)^2 + (0.770)^2} = \sqrt{1.3712 + 0.4610 + 3.0765 + 0.5929} = \sqrt{5.5016} \approx \mathbf{2.346}$$

#### Bảng Xếp hạng Khoảng cách:
| Hạng | Mẫu BN | Khoảng cách Euclidean ($d$) | Nhãn thực tế ($y$) |
| :---: | :---: | :---: | :---: |
| **1** | **B3** | $\mathbf{1.142}$ | $1$ (`ckd`) |
| **2** | **B1** | $\mathbf{1.835}$ | $0$ (`notckd`) |
| **3** | **B4** | $\mathbf{2.346}$ | $0$ (`notckd`) |
| 4 | B2 | $2.843$ | $1$ (`ckd`) |

* Với $k=3$, tập láng giềng gần nhất là $\{\text{B3}, \text{B1}, \text{B4}\}$.
* Số phiếu bầu:
  * Lớp $y = 0$ (`notckd`): $2$ phiếu (B1, B4).
  * Lớp $y = 1$ (`ckd`): $1$ phiếu (B3).
* **Kết luận thuật toán $k\text{-NN}$ ($k=3$):** Bệnh nhân mới được dự đoán **Không mắc bệnh thận mãn tính (`notckd`)** theo quy tắc đa số phiếu bình đẳng.
* *Nhận định y khoa:* Mặc dù nhãn gán là 0, nhưng láng giềng gần nhất tuyệt đối lại là B3 ($d=1.142$ rất nhỏ, chỉ số creatinine bắt đầu tăng ở mức $2.5$). Điều này cho thấy nếu áp dụng hàm khoảng cách có trọng số nghịch đảo $w_i = \frac{1}{d}$, bệnh nhân này nằm ở ranh giới nguy cơ cần theo dõi sát sao!

---

### 6.4. Bước 3: Dự đoán bằng Thuật toán Gaussian Naïve Bayes Thủ công

#### 1. Tính Tham số Phân phối Từng Lớp:
* **Lớp 0 (`notckd`, gồm B1 và B4, $N_0 = 2$):**
  * $P(y=0) = \frac{2}{4} = 0.5$
  * `sc`: $\mu_{0, \text{sc}} = \frac{1.2 + 0.9}{2} = 1.05$; $\sigma_{0, \text{sc}}^2 = \frac{(1.2-1.05)^2 + (0.9-1.05)^2}{2} = \frac{0.0225 + 0.0225}{2} = \mathbf{0.0225}$ ($\sigma = 0.15$)
  * `hemo`: $\mu_{0, \text{hemo}} = \frac{15.4 + 16.0}{2} = 15.7$; $\sigma_{0, \text{hemo}}^2 = \frac{(-0.3)^2 + (0.3)^2}{2} = \mathbf{0.09}$ ($\sigma = 0.30$)

* **Lớp 1 (`ckd`, gồm B2 và B3, $N_1 = 2$):**
  * $P(y=1) = \frac{2}{4} = 0.5$
  * `sc`: $\mu_{1, \text{sc}} = \frac{6.8 + 3.4}{2} = 5.10$; $\sigma_{1, \text{sc}}^2 = \frac{(6.8-5.1)^2 + (3.4-5.1)^2}{2} = \frac{2.89 + 2.89}{2} = \mathbf{2.89}$ ($\sigma = 1.70$)
  * `hemo`: $\mu_{1, \text{hemo}} = \frac{9.6 + 10.5}{2} = 10.05$; $\sigma_{1, \text{hemo}}^2 = \frac{(-0.45)^2 + (0.45)^2}{2} = \mathbf{0.2025}$ ($\sigma = 0.45$)

#### 2. Tính Mật độ Xác suất Hàng dọc cho Bệnh nhân mới ($x_{\text{new, sc}} = 2.5, x_{\text{new, hemo}} = 11.0$):
* **Xét điều kiện $y=0$ (`notckd`):**
  $$P(\text{sc}=2.5 | y=0) = \frac{1}{\sqrt{2\pi (0.0225)}} \exp\left( -\frac{(2.5 - 1.05)^2}{2 \times 0.0225} \right) = \frac{1}{0.376} \exp\left( -\frac{2.1025}{0.045} \right) = 2.66 \times e^{-46.72} \approx \mathbf{0}$$
  *(Do nồng độ Creatinine $2.5$ vượt quá xa ngưỡng sinh lý bình thường $1.05 \pm 0.15$ của nhóm khỏe mạnh).*

* **Xét điều kiện $y=1$ (`ckd`):**
  $$P(\text{sc}=2.5 | y=1) = \frac{1}{\sqrt{2\pi (2.89)}} \exp\left( -\frac{(2.5 - 5.10)^2}{2 \times 2.89} \right) = \frac{1}{4.26} \exp\left( -\frac{6.76}{5.78} \right) = 0.235 \times e^{-1.17} \approx 0.235 \times 0.310 = \mathbf{0.0728}$$

  $$P(\text{hemo}=11.0 | y=1) = \frac{1}{\sqrt{2\pi (0.2025)}} \exp\left( -\frac{(11.0 - 10.05)^2}{2 \times 0.2025} \right) = \frac{1}{1.128} \exp\left( -\frac{0.9025}{0.405} \right) = 0.886 \times e^{-2.228} \approx 0.886 \times 0.1077 = \mathbf{0.0954}$$

#### 3. Tính Điểm Xác suất Hậu nghiệm (Posterior Score):
* $\text{Score}(y=0) = P(y=0) \times P(\text{sc}|y=0) \times P(\text{hemo}|y=0) \approx 0.5 \times 0 \times \dots = \mathbf{0}$
* $\text{Score}(y=1) = P(y=1) \times P(\text{sc}|y=1) \times P(\text{hemo}|y=1) = 0.5 \times 0.0728 \times 0.0954 = \mathbf{0.00347}$

* **Kết luận thuật toán Gaussian Naïve Bayes:** $\text{Score}(y=1) \gg \text{Score}(y=0) \implies$ Bệnh nhân mới được chẩn đoán **MẮC BỆNH THẬN MÃN TÍNH (`ckd`)** với xác suất hậu nghiệm tiệm cận $100\%$. Đây là minh chứng rõ nét cho thấy Naïve Bayes phản ứng rất nhạy với các chỉ số sinh hóa vượt ngưỡng bất thường.

---

### 6.5. Bước 4: Tính toán Độ bất thuần Gini cho Nút Gốc Decision Tree

Tại nút gốc $m_0$ chứa cả 4 bệnh nhân (2 `ckd`, 2 `notckd`):
$$G(m_0) = 1 - \left( \left(\frac{2}{4}\right)^2 + \left(\frac{2}{4}\right)^2 \right) = 1 - (0.25 + 0.25) = \mathbf{0.500}$$

#### Xét Thuộc tính Albumin (`al`) với câu hỏi phân nhánh: $\text{al} \le 0.5$:
* **Nhánh Trái ($\text{al} \le 0.5$, gồm B1 và B4):** Cả 2 đều có $y=0$.
  $$G(m_L) = 1 - \left( \left(\frac{2}{2}\right)^2 + \left(\frac{0}{2}\right)^2 \right) = 1 - 1 = \mathbf{0.000} \quad (\text{Nút lá thuần khiết tuyệt đối!})$$
* **Nhánh Phải ($\text{al} > 0.5$, gồm B2 và B3):** Cả 2 đều có $y=1$.
  $$G(m_R) = 1 - \left( \left(\frac{0}{2}\right)^2 + \left(\frac{2}{2}\right)^2 \right) = 1 - 1 = \mathbf{0.000} \quad (\text{Nút lá thuần khiết tuyệt đối!})$$

#### Độ bất thuần trung bình sau phép tách:
$$G_{\text{split}}(\text{al} \le 0.5) = \frac{2}{4} G(m_L) + \frac{2}{4} G(m_R) = 0.5 \times 0 + 0.5 \times 0 = \mathbf{0.000}$$

* Mức giảm độ bất thuần (*Gini Reduction*): $\Delta G = 0.500 - 0.000 = \mathbf{0.500}$ (Cực đại tuyệt đối).
* **Kết luận Decision Tree:** Thuộc tính Đạm niệu (`al`) đóng vai trò là một trong những đặc trưng phân tách mạnh mẽ nhất, hoàn toàn cô lập bệnh nhân suy thận khỏi người khỏe mạnh ngay tại tầng đầu tiên của cây.

---

## 7. CÔNG THỨC VÀ MA TRẬN ĐÁNH GIÁ MÔ HÌNH Y TẾ LÂM SÀNG

### 7.1. Cấu trúc Ma trận Nhầm lẫn Y tế (Clinical Confusion Matrix)
Trong chẩn đoán y tế, một dự đoán sai không đơn thuần là một con số mà liên quan trực tiếp đến sinh mạng bệnh nhân.

| Thực tế lâm sàng \ Dự đoán mô hình | Dự đoán Mắc bệnh ($\hat{y} = 1$ - CKD) | Dự đoán Khỏe mạnh ($\hat{y} = 0$ - NOTCKD) |
| :--- | :---: | :---: |
| **Thực tế Bệnh ($y = 1$ - CKD)** | **True Positive (TP)**<br>*(Chẩn đoán đúng người bệnh)* | **False Negative (FN)**<br>⚠️ **HẬU QUẢ NGHIÊM TRỌNG NHẤT**<br>*(Bỏ sót người suy thận)* |
| **Thực tế Khỏe ($y = 0$ - NOTCKD)** | **False Positive (FP)**<br>*(Báo động nhầm người khỏe)* | **True Negative (TN)**<br>*(Xác định đúng người khỏe)* |

### 7.2. Các Công thức Đo lường Hiệu năng Cốt lõi

1. **Độ chính xác tổng thể (Accuracy):**
   $$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$$

2. **Độ nhạy / Tỷ lệ phát hiện bệnh (Recall / Sensitivity):**
   $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
   *Ý nghĩa y tế:* Đo lường trong số tất cả bệnh nhân thực sự bị bệnh thận, mô hình phát hiện được bao nhiêu $\%$. **Mục tiêu đồ án bắt buộc tối ưu hóa $\text{Recall} \to 100\%$ để $\text{FN} \to 0$**.

3. **Độ đặc hiệu (Specificity):**
   $$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$$
   *Ý nghĩa y tế:* Tỷ lệ xác định chính xác người thực sự không mắc bệnh thận.

4. **Độ chuẩn xác (Precision / Positive Predictive Value):**
   $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$

5. **Chỉ số F1-Score (Điều hòa giữa Precision và Recall):**
   $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$

6. **Diện tích dưới đường cong ROC (ROC-AUC):**
   Tích phân diện tích dưới đường cong biểu diễn mối quan hệ đánh đổi giữa $\text{TPR}$ (*True Positive Rate = Recall*) và $\text{FPR}$ (*False Positive Rate = $1 - \text{Specificity}$*) khi ngưỡng quyết định phân loại thay đổi liên tục từ $0$ đến $1$:

   $$\text{ROC-AUC} = \int_0^1 \text{TPR}(\tau) \, d(\text{FPR}(\tau))$$

---

## 8. BẢNG TỔNG KẾT SO SÁNH CÁC THUẬT TOÁN HỌC MÁY TRONG ĐỒ ÁN

| Thuật toán | Ưu điểm cốt lõi | Nhược điểm / Rủi ro | Biện pháp kỹ thuật khắc phục |
| :--- | :--- | :--- | :--- |
| **Random Forest** | Kiểm soát Overfitting tuyệt vời, xếp hạng thuộc tính tự động, xử lý tốt phi tuyến. | Mô hình dạng hộp đen (*Black-box*), tốn tài nguyên tính toán hơn cây đơn. | Tích hợp thư viện giải trình XAI trích xuất trọng số thuộc tính quan trọng. |
| **SVM (RBF Kernel)** | Tối ưu hóa cực đại lề phân cách, độ chính xác rất cao trong không gian đa chiều. | Nhạy cảm với nhiễu và thang đo, thời gian huấn luyện tỷ lệ bậc 2 với số mẫu. | Bắt buộc chuẩn hóa StandardScaler và dùng 5-Fold Cross Validation tuning $C, \gamma$. |
| **Logistic Regression** | Đơn giản, tốc độ thực thi nano-giây, cung cấp xác suất mượt mà, dễ diễn giải hệ số trọng số. | Không nắm bắt tốt các ranh giới phi tuyến phức tạp nếu không tạo đa thức. | Kết hợp chuẩn hóa $L_2$ Ridge để ổn định trọng số các biến tương quan. |
| **Decision Tree** | Cực kỳ trực quan, dễ diễn giải dưới dạng các quy tắc logic y khoa (*If-Then*). | Dễ bị quá khớp (Overfitting) nghiêm trọng trên tập dữ liệu kích thước nhỏ. | Giới hạn độ sâu tối đa (`max_depth = 4`), quy định số mẫu tối thiểu ở nút lá (`min_samples_leaf = 5`). |
| **k-NN** | Không giả định phân phối dữ liệu, tự nhiên và dễ hiểu. | Chi phí dự đoán cao khi dữ liệu lớn, suy giảm hiệu năng do lời nguyền số chiều. | Giảm chiều bằng PCA/LDA và tiền xử lý chuẩn hóa Z-score toàn bộ biến. |
| **Gaussian Naïve Bayes** | Tốc độ cực nhanh, huấn luyện ổn định ngay cả với tập mẫu nhỏ, tính toán trực tiếp. | Giả định các biến độc lập có điều kiện là phi thực tế trong y sinh học. | Dùng làm Baseline chuẩn mực đối chứng với các thuật toán phi tuyến phức tạp. |

---

> [!IMPORTANT]
> **Kết luận chương lý thuyết:** Toàn bộ cơ sở đại số ma trận, giải tích hàm mất mát, xác suất thống kê và ví dụ tính toán thủ công từng bước trên đây là nền tảng toán học vững chắc, giải quyết trọn vẹn yêu cầu học thuật của học phần Học máy tại Trường Đại học Công Thương TP.HCM (HUIT) và Trường Đại Học Công Nghệ Thông Tin(UIT) - Đại Học Quốc Gia Thành Phố Hồ Chí Minh(VNUHCM).

