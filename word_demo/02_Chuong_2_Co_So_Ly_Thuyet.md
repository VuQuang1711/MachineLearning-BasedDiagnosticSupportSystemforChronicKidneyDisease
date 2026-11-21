# CHƯƠNG 2. CƠ SỞ LÝ THUYẾT VÀ CÁC THUẬT TOÁN ĐỀ XUẤT

## 2.1. BÀI TOÁN PHÂN LỚP (CLASSIFICATION) CHẨN ĐOÁN BỆNH THẬN

Trong bài toán chẩn đoán Bệnh thận mãn tính (CKD), mỗi bệnh nhân được biểu diễn bởi một vector đặc trưng $\mathbf{x} = (x_1, x_2, \dots, x_d)^T \in \mathbb{R}^d$ (với $d = 35$ chiều sau tiền xử lý) và một nhãn mục tiêu nhị phân $y \in \{0, 1\}$, trong đó $y = 1$ tương ứng với **Bệnh thận mãn tính (`ckd`)** và $y = 0$ tương ứng với **Khỏe mạnh (`notckd`)**. Mục tiêu là học một hàm ánh xạ $f: \mathbb{R}^d \to \{0, 1\}$ sao cho sai số tổng quát hóa là nhỏ nhất và độ nhạy phát hiện bệnh (Recall) đạt mức tối đa.

### 2.1.1. Mô hình Hồi quy Logistic (Logistic Regression)

#### 1. Khái niệm và mô hình toán học
Mặc dù mang tên "Hồi quy", Logistic Regression là thuật toán học có giám sát kinh điển cho bài toán phân lớp nhị phân. Mô hình ước lượng xác suất hậu nghiệm $p = P(y = 1 \mid \mathbf{x})$ bằng cách đưa tổ hợp tuyến tính $z$ đi qua **hàm kích hoạt Sigmoid**:

$$z = \mathbf{w}^T\mathbf{x} + b = \sum_{j=1}^{d} w_j x_j + b$$

$$p = \sigma(z) = \frac{1}{1 + e^{-z}} \in (0, 1)$$

Hàm Sigmoid liên tục, khả vi mọi nơi và thỏa mãn tính chất đạo hàm đẹp $\sigma'(z) = \sigma(z)(1 - \sigma(z))$. Khi lấy logarit tự nhiên của tỷ lệ Odds, ta thu được hàm Logit tuyến tính:

$$\ln\left(\frac{p}{1 - p}\right) = \mathbf{w}^T\mathbf{x} + b$$

Với ngưỡng quyết định $\tau = 0.5$, ranh giới phân tách hai lớp là siêu phẳng tuyến tính $\mathbf{w}^T\mathbf{x} + b = 0$.

#### 2. Hàm mất mát Binary Cross-Entropy và Tối ưu hóa
Áp dụng phương pháp Ước lượng Cực đại Khả năng (*Maximum Likelihood Estimation — MLE*) trên $N$ mẫu huấn luyện độc lập, ta thu được hàm mất mát **Binary Cross-Entropy (Log Loss)** kèm điều chuẩn L2 (Ridge) chống quá khớp:

$$J(\mathbf{w}, b) = -\frac{1}{N} \sum_{i=1}^{N} \Big[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \Big] + \frac{\lambda}{2}\|\mathbf{w}\|_2^2$$

Vì $J(\mathbf{w}, b)$ là hàm lồi chặt, thuật toán Gradient Descent (hoặc L-BFGS) đảm bảo hội tụ về cực tiểu toàn cục với đạo hàm:

$$\nabla_{\mathbf{w}} J = \frac{1}{N} \sum_{i=1}^{N} (p_i - y_i)\mathbf{x}_i + \lambda \mathbf{w}$$

#### 3. Ưu điểm và nhược điểm
- **Ưu điểm:** Đầu ra có ý nghĩa xác suất trực quan, tốc độ huấn luyện nhanh, ít tham số, dễ diễn giải dấu của trọng số $w_j$ và phù hợp làm mô hình cơ sở (Baseline).
- **Nhược điểm:** Ranh giới quyết định bị giới hạn là siêu phẳng tuyến tính và dễ chịu ảnh hưởng bởi hiện tượng đa cộng tuyến giữa các chỉ số xét nghiệm (như `hemo` và `pcv`).

---

### 2.1.2. Mô hình Rừng ngẫu nhiên (Random Forest)

#### 1. Khái niệm và cơ chế hoạt động
**Random Forest** là thuật toán học kết hợp (*Ensemble Learning*) xây dựng một tập hợp gồm $B$ cây quyết định độc lập $\{T_1, T_2, \dots, T_B\}$ dựa trên hai cơ chế cốt lõi:
- **Bootstrap Aggregating (Bagging):** Rút ngẫu nhiên có hoàn lại $N$ mẫu từ tập huấn luyện để tạo ra $B$ tập con huấn luyện khác nhau. Khoảng $63.2\%$ mẫu xuất hiện trong mỗi tập bootstrap, phần còn lại ($\approx 36.8\%$) tạo thành tập *Out-Of-Bag (OOB)* dùng để đánh giá nội bộ.
- **Chọn ngẫu nhiên đặc trưng (Feature Randomization):** Tại mỗi nút phân chia của cây, thay vì duyệt toàn bộ $d$ đặc trưng, thuật toán chỉ chọn ngẫu nhiên $m = \lfloor \sqrt{d} \rfloor$ đặc trưng để tìm ngưỡng cắt tối ưu. Cơ chế này làm giảm mạnh tương quan giữa các cây (*de-correlation*), từ đó giảm phương sai (Variance) và chống quá khớp hiệu quả.

#### 2. Tiêu chí phân nhánh Gini Impurity và Luật tổng hợp dự đoán
Tại mỗi nút $t$, thuật toán chọn cặp đặc trưng và ngưỡng chia sao cho **Độ vẩn đục Gini (Gini Impurity)** giảm nhiều nhất:

$$\text{Gini}(t) = 1 - \sum_{c \in \{0, 1\}} p(c \mid t)^2 = 2p(1 \mid t)\big(1 - p(1 \mid t)\big)$$

Khi dự đoán cho một bệnh nhân mới $\mathbf{x}$, xác suất mắc bệnh được tổng hợp bằng biểu quyết mềm (*Soft Voting*) — lấy trung bình xác suất dự đoán của cả $B$ cây:

$$\hat{P}(y = 1 \mid \mathbf{x}) = \frac{1}{B} \sum_{b=1}^{B} P_b(y = 1 \mid \mathbf{x})$$

#### 3. Khả năng giải thích đặc trưng (Feature Importance)
Random Forest tự động tính toán tầm quan trọng của từng đặc trưng thông qua **Mean Decrease in Impurity (MDI)** — tổng mức giảm Gini mà đặc trưng đó đóng góp trên toàn bộ $B$ cây. Điều này đặc biệt quý giá trong chẩn đoán y khoa để giải thích cho bác sĩ chỉ số nào đang chi phối quyết định của AI.

#### 4. Ưu điểm và nhược điểm
- **Ưu điểm:** Độ chính xác và độ ổn định rất cao, xử lý xuất sắc mối quan hệ phi tuyến giữa 24 chỉ số sinh hóa, kháng đa cộng tuyến, chống quá khớp tốt khi kiểm soát `max_depth`, `min_samples_leaf` và hỗ trợ trực tiếp XAI.
- **Nhược điểm:** Chi phí bộ nhớ lớn hơn mô hình đơn lẻ; không thể đọc trực tiếp thành một luật IF-THEN duy nhất như một cây quyết định đơn.

---

### 2.1.3. Máy vector hỗ trợ (Support Vector Machine — SVM)

#### 1. Cơ sở toán học và kỹ thuật Kernel RBF
SVM tìm kiếm siêu phẳng $\mathbf{w}^T\mathbf{x} + b = 0$ sao cho **khoảng lề hình học (Margin)** $\frac{2}{\|\mathbf{w}\|_2}$ giữa hai lớp bệnh nhân là lớn nhất. Với dữ liệu thực tế có nhiễu (Soft-Margin SVM), bài toán tối ưu có dạng:

$$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2}\|\mathbf{w}\|_2^2 + C \sum_{i=1}^{N} \xi_i \quad \text{sao cho } y_i(\mathbf{w}^T\mathbf{x}_i + b) \ge 1 - \xi_i, \;\; \xi_i \ge 0$$

Trong đó $C > 0$ kiểm soát sự đánh đổi giữa độ rộng lề và mức phạt sai số phân lớp. Để tách dữ liệu phi tuyến, nhóm sử dụng hàm nhân **Radial Basis Function (RBF)**:

$$K(\mathbf{x}_i, \mathbf{x}_j) = \exp\left(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|_2^2\right)$$

#### 2. Ưu điểm và nhược điểm
- **Ưu điểm:** Cực kỳ hiệu quả trong không gian nhiều chiều (35 chiều sau One-Hot), ổn định tốt trên tập dữ liệu cỡ vừa ($N = 400$).
- **Nhược điểm:** Nhạy cảm với thang đo dữ liệu (bắt buộc phải dùng `StandardScaler`) và khó diễn giải trực quan lý do chẩn đoán hơn Random Forest.

---

### 2.1.4. Các thuật toán phân lớp so sánh khác (Decision Tree, Gaussian Naïve Bayes, k-NN)

Để đánh giá khách quan trước khi chọn mô hình triển khai, nhóm đối chiếu thêm 3 thuật toán nền tảng trong chương trình Học máy:

1. **Cây quyết định (Decision Tree — CART):** Phân chia không gian đặc trưng theo cấu trúc cây bằng chỉ số Gini Impurity. Dễ trực quan hóa thành luật lâm sàng nhưng dễ bị quá khớp (Overfitting) nếu không cắt tỉa độ sâu.
2. **Gaussian Naïve Bayes (GNB):** Áp dụng định lý Bayes với giả định các đặc trưng độc lập có điều kiện và tuân theo phân phối chuẩn $\mathcal{N}(\mu_{c,j}, \sigma_{c,j}^2)$:
   $$P(y = c \mid \mathbf{x}) \propto P(y = c) \prod_{j=1}^{d} \frac{1}{\sqrt{2\pi\sigma_{c,j}^2}} \exp\left(-\frac{(x_j - \mu_{c,j})^2}{2\sigma_{c,j}^2}\right)$$
   Tốc độ cực nhanh nhưng giả định độc lập giữa các chỉ số máu (như `hemo` và `pcv`) không đúng về mặt sinh lý học.
3. **k-Láng giềng gần nhất (k-Nearest Neighbors — k-NN):** Thuật toán học lười (*Lazy Learning*), phân lớp bệnh nhân mới dựa trên biểu quyết đa số của $k = 5$ bệnh nhân gần nhất theo khoảng cách Euclid $d(\mathbf{x}, \mathbf{x}_i) = \sqrt{\sum_{j=1}^{d}(x_j - x_{ij})^2}$. Dễ bị suy giảm độ nhạy trong không gian nhiều chiều (*Curse of Dimensionality*).

---

## 2.2. BÀI TOÁN GIẢM CHIỀU DỮ LIỆU (PCA)

**Phân tích thành phần chính (Principal Component Analysis — PCA)** là kỹ thuật học không giám sát tuyến tính nhằm chiếu tập dữ liệu từ không gian gốc $d = 35$ chiều sang không gian mới $k < d$ chiều gồm các trục trực giao (thành phần chính) bảo toàn tối đa lượng phương sai (thông tin) của dữ liệu.

Quy trình toán học gồm 3 bước trên ma trận dữ liệu đã chuẩn hóa $\mathbf{Z}$:
1. Tính ma trận hiệp phương sai: $\mathbf{\Sigma} = \frac{1}{N - 1}\mathbf{Z}^T\mathbf{Z}$.
2. Phân rã trị riêng và vector riêng: $\mathbf{\Sigma}\mathbf{v}_j = \lambda_j \mathbf{v}_j$, sắp xếp giảm dần $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d \ge 0$.
3. Tỷ lệ phương sai tích lũy giữ lại bởi $k$ thành phần đầu tiên:

$$\text{EVR}(k) = \frac{\sum_{j=1}^{k} \lambda_j}{\sum_{j=1}^{d} \lambda_j} \times 100\%$$

Trong đề tài, PCA được sử dụng để khảo sát khả năng nén chiều (tìm số thành phần tối thiểu giữ $\ge 95\%$ phương sai) và trực quan hóa mức độ phân tách giữa 2 nhóm bệnh nhân trên mặt phẳng 2D ($PC_1, PC_2$).

---

## 2.3. CÁC ĐỘ ĐO ĐÁNH GIÁ MÔ HÌNH TRONG Y TẾ

### 2.3.1. Ma trận nhầm lẫn và các độ đo Accuracy, Precision, Recall, F1-Score

Hiệu năng phân lớp nhị phân được thiết lập từ **Ma trận nhầm lẫn (Confusion Matrix)**:

| Thực tế \ Dự đoán | Dự đoán Bệnh thận — CKD (1) | Dự đoán Khỏe mạnh — Not-CKD (0) |
| :--- | :---: | :---: |
| **Thực tế Bệnh thận — CKD (1)** | **TP** *(Dương tính thật)* | **FN** *(Âm tính giả — Bỏ sót bệnh)* |
| **Thực tế Khỏe mạnh — Not-CKD (0)** | **FP** *(Dương tính giả — Báo động nhầm)* | **TN** *(Âm tính thật)* |

Từ 4 đại lượng cốt lõi trên, ta định nghĩa 4 chỉ số đánh giá:

- **Accuracy (Độ chính xác tổng thể):**
  $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
- **Precision (Độ chính xác dự đoán dương):**
  $$\text{Precision} = \frac{TP}{TP + FP}$$
- **Recall / Sensitivity (Độ nhạy — Tiêu chí ưu tiên số 1 trong y tế):**
  $$\text{Recall} = \frac{TP}{TP + FN}$$
  Trong chẩn đoán bệnh thận, lỗi **Âm tính giả (FN)** cực kỳ nguy hiểm vì khiến bệnh nhân suy thận bị bỏ sót và lỡ giai đoạn điều trị vàng. Do đó, nhóm đặt mục tiêu bắt buộc **Recall $\ge 96.0\%$**.
- **F1-Score (Trung bình điều hòa giữa Precision và Recall):**
  $$F_1 = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}$$

### 2.3.2. Đường cong ROC và chỉ số ROC-AUC

Đường cong **ROC (Receiver Operating Characteristic)** biểu diễn mối quan hệ đánh đổi giữa tỷ lệ dương tính thật ($\text{TPR} = \text{Recall}$) và tỷ lệ dương tính giả ($\text{FPR} = \frac{FP}{FP + TN}$) khi thay đổi ngưỡng cắt xác suất $\tau \in [0, 1]$.

Diện tích dưới đường cong ROC — **AUC (Area Under Curve)** — đo lường tổng quát năng lực phân tách hai lớp của mô hình ($\text{AUC} \in [0.5, 1.0]$). Giá trị $\text{AUC}$ càng tiệm cận $1.0$ chứng tỏ mô hình xếp hạng xác suất rủi ro của bệnh nhân mắc CKD cao hơn người khỏe mạnh càng chính xác, không phụ thuộc vào một ngưỡng cắt cố định nào.
