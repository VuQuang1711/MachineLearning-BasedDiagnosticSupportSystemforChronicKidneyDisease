# BÁO CÁO MÔ TẢ VÀ PHÂN TÍCH CHI TIẾT BỘ DỮ LIỆU BỆNH THẬN MÃN TÍNH (CHRONIC KIDNEY DISEASE - CKD)

Bộ dữ liệu Chẩn đoán Bệnh thận Mãn tính (Chronic Kidney Disease Dataset) thu thập từ UCI Machine Learning Repository và Kaggle đại diện cho một tập dữ liệu y tế lâm sàng đa chiều, phức tạp và mang tính thực tiễn cao trong các bài toán phân lớp y khoa. Việc hiểu rõ cấu trúc, đặc tính phân phối, tỷ lệ khuyết thiếu dữ liệu cũng như ý nghĩa sinh hóa của 24 thuộc tính đầu vào là điều kiện tiên quyết để xây dựng quy trình tiền xử lý chống rò rỉ dữ liệu (Data Leakage) và huấn luyện các mô hình học máy đạt hiệu năng tối ưu.

---

## 1. Tổng Quan Về Bộ Dữ Liệu Bệnh Thận Mãn Tính (UCI / Kaggle CKD Dataset)

Bộ dữ liệu bệnh thận mãn tính được thu thập từ các bệnh viện lâm sàng với mục tiêu hỗ trợ chẩn đoán sớm nguy cơ suy thận ở bệnh nhân thông qua các xét nghiệm máu, nước tiểu và tiền sử bệnh lý. 

Tập dữ liệu chứa tổng cộng 400 mẫu bệnh nhân ($N = 400$), trong đó mỗi mẫu dữ liệu bao gồm 24 đặc trưng đầu vào (features) và 1 thuộc tính nhãn mục tiêu (target class).

| Thông số Tổng quan | Giá trị Chi tiết | Ý nghĩa Lâm sàng & Khoa học Dữ liệu |
| :--- | :--- | :--- |
| **Số lượng mẫu bệnh nhân ($N$)** | 400 mẫu | Kích thước dữ liệu vừa phải, đòi hỏi các mô hình phân lớp có khả năng kiểm soát Overfitting cao. |
| **Số thuộc tính đầu vào ($d$)** | 24 đặc trưng | Không gian đặc trưng đa chiều gồm cả định lượng (liên tục) và định tính (rời rạc). |
| **Nhãn mục tiêu (`classification`)** | 2 lớp nhị phân (`ckd` / `notckd`) | Bài toán phân lớp nhị phân có giám sát (Supervised Binary Classification). |
| **Phân bố nhãn mục tiêu** | 250 `ckd` (62.5%) vs 150 `notckd` (37.5%) | Dữ liệu mất cân bằng nhẹ (Imbalanced Dataset), cần chú ý các chỉ số Recall và F1-Score. |
| **Tỷ lệ giá trị khuyết (Missing Rate)** | **24/24 cột** chứa ô khuyết (`1,012 / 9,600` ô = `10.54%`) | Thách thức lớn trong khâu Imputation (điền giá trị thiếu) trước khi huấn luyện. |
| **Kiểm toán toàn vẹn dữ liệu** | **0 dòng trùng lặp**, **0 cột hằng số**, loại bỏ cột `id` (`400/400` duy nhất) | Dữ liệu sạch cấu trúc, không chứa bản ghi trùng hay thuộc tính vô nghĩa. |

---

## 2. Cấu Trúc Chi Tiết 24 Thuộc Tính Lâm Sàng & Phân Loại Dữ Liệu

Tập dữ liệu được chia làm hai nhóm chính: 11 đặc trưng định lượng liên tục (Numerical Features) và 13 đặc trưng định tính phân loại (Categorical Features).

### 2.1. Nhóm 11 Đặc Trưng Định Lượng (Numerical Features)

Các đặc trưng định lượng đo lường các chỉ số sinh hóa máu, huyết áp và tế bào học. Việc chuẩn hóa thang đo cho nhóm này là bắt buộc đối với các thuật toán nhạy cảm với khoảng cách như k-NN và SVM.

| Ký hiệu | Tên Thuộc tính (Tiếng Anh) | Tên Chỉ số Lâm sàng (Tiếng Việt) | Đơn vị Đo | Khoảng Giá trị Thống kê | Ý nghĩa Y khoa Chẩn đoán |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `age` | Age | Tuổi bệnh nhân | Năm | 2 - 90 | Tuổi tác càng cao, nguy cơ suy giảm chức năng lọc của cầu thận càng lớn. |
| `bp` | Blood Pressure | Huyết áp lúc nghỉ | mmHg | 50 - 180 | Tăng huyết áp vừa là nguyên nhân vừa là biến chứng của bệnh thận mãn tính. |
| `bgr` | Blood Glucose Random | Đường huyết ngẫu nhiên | mg/dl | 22 - 490 | Chỉ số đường huyết cao phản ảnh nguy cơ biến chứng thận do đái tháo đường. |
| `bu` | Blood Urea | Hàm lượng Urê trong máu | mg/dl | 1.5 - 391 | Urê là sản phẩm chuyển hóa đạm; nồng độ bu cao cảnh báo khả năng đào thải kém của thận. |
| `sc` | Serum Creatinine | Creatinine huyết thanh | mg/dl | 0.4 - 76.0 | **Chỉ số sinh hóa quan trọng nhất**; sc tăng cao trực tiếp phản ánh mức lọc cầu thận (eGFR) giảm. |
| `sod` | Sodium | Hàm lượng Natri trong máu | mEq/L | 4.5 - 163 | Rối loạn điện giải Natri ảnh hưởng đến cân bằng áp suất thẩm thấu nội bào. |
| `pot` | Potassium | Hàm lượng Kali trong máu | mEq/L | 2.5 - 47.0 | Tăng Kali máu (Hyperkalemia) là nguy cơ cấp cứu tim mạch nghiêm trọng ở bệnh nhân CKD. |
| `hemo` | Hemoglobin | Huyết sắc tố Hemoglobin | g/dl | 3.1 - 17.8 | Thận tiết ra Erythropoietin kích thích tạo máu; hemo giảm sâu báo hiệu thiếu máu do suy thận. |
| `pcv` | Packed Cell Volume | Thể tích khối hồng cầu | % | 9 - 54 | Tỷ lệ thể tích hồng cầu trên toàn bộ thể tích máu; tương quan thuận với Hemoglobin. |
| `wc` | White Blood Cell Count | Số lượng bạch cầu | cells/cumm | 2200 - 26400 | Bạch cầu tăng cao phản ánh tình trạng viêm nhiễm hoặc nhiễm trùng đường tiết niệu. |
| `rc` | Red Blood Cell Count | Số lượng hồng cầu | millions/cmm | 2.1 - 8.0 | Số lượng hồng cầu giảm trực tiếp gây ra hội chứng thiếu máu ở bệnh nhân suy thận. |

### 2.2. Nhóm 13 Đặc Trưng Định Tính (Categorical Features)

Các đặc trưng định tính phản ánh kết quả phân tích nước tiểu tổng quát và tiền sử bệnh lý đi kèm của bệnh nhân.

| Ký hiệu | Tên Thuộc tính | Các Giá trị Hợp lệ | Dạng Mã hóa Chuẩn | Ý nghĩa Y khoa Lâm sàng |
| :--- | :--- | :--- | :--- | :--- |
| `sg` | Specific Gravity | 1.005, 1.010, 1.015, 1.020, 1.025 | Ordinal / Categorical | Tỷ trọng nước tiểu; cô đặc hay pha loãng phản ánh khả năng cô đặc của ống thận. |
| `al` | Albumin | 0, 1, 2, 3, 4, 5 | Ordinal / Categorical | Đạm trong nước tiểu; chỉ số al $\ge 1$ báo hiệu màng lọc cầu thận bị tổn thương. |
| `su` | Sugar | 0, 1, 2, 3, 4, 5 | Ordinal / Categorical | Đường trong nước tiểu; phản ánh ngưỡng tái hấp thu đường của ống thận bị vượt quá. |
| `rbc` | Red Blood Cells | `normal`, `abnormal` | Binary (`0` / `1`) | Hồng cầu trong nước tiểu; xuất hiện hồng cầu bất thường cảnh báo viêm cầu thận. |
| `pc` | Pus Cell | `normal`, `abnormal` | Binary (`0` / `1`) | Tế bào mủ trong nước tiểu; sự xuất hiện tế bào mủ báo hiệu nhiễm trùng đường tiết niệu. |
| `pcc` | Pus Cell Clumps | `present`, `notpresent` | Binary (`0` / `1`) | Cụm tế bào mủ; nhiễm trùng thận nặng hoặc viêm đài bể thận. |
| `ba` | Bacteria | `present`, `notpresent` | Binary (`0` / `1`) | Vi khuẩn trong nước tiểu; sự hiện diện của vi khuẩn khẳng định nhiễm khuẩn tiết niệu. |
| `htn` | Hypertension | `yes`, `no` | Binary (`0` / `1`) | Tiền sử tăng huyết áp; yếu tố rủi ro và biến chứng tim mạch hàng đầu ở bệnh nhân CKD. |
| `dm` | Diabetes Mellitus | `yes`, `no` | Binary (`0` / `1`) | Tiền sử đái tháo đường; nguyên nhân hàng đầu gây ra bệnh thận giai đoạn cuối. |
| `cad` | Coronary Artery Disease | `yes`, `no` | Binary (`0` / `1`) | Bệnh động mạch vành; biến chứng tim mạch nguy hiểm đi kèm suy thận. |
| `appet` | Appetite | `good`, `poor` | Binary (`0` / `1`) | Cảm giác thèm ăn; chán ăn (poor) là triệu chứng của hội chứng ure huyết cao. |
| `pe` | Pedal Edema | `yes`, `no` | Binary (`0` / `1`) | Phù chân; hậu quả của tình trạng ứ trệ nước và Natri do thận giảm chức năng lọc. |
| `ane` | Anemia | `yes`, `no` | Binary (`0` / `1`) | Tình trạng thiếu máu; biến chứng mãn tính do giảm tiết Erythropoietin từ thận. |

---

## 3. Phân Tích Hiện Trạng Giá Trị Khuyết (Missing Values Analysis) & Kỹ Thuật Làm Sạch

Một trong những đặc điểm nổi bật của tập dữ liệu `kidney_disease.csv` là mật độ giá trị bị khuyết rất cao do điều kiện thực tế của quá trình xét nghiệm lâm sàng (bệnh nhân không làm đầy đủ tất cả các danh mục xét nghiệm).

```
Tỷ lệ khuyết thiếu (Missing Rate) trên toàn bộ 400 mẫu bệnh nhân:
+-----------------------------------------------------------------------+
| Thuộc tính continuous | Mẫu thiếu | Thuộc tính categorical | Mẫu thiếu|
+-----------------------------------------------------------------------+
| age                   | 9 (2.25%) | sg                     | 47(11.8%)|
| bp                    | 12(3.00%) | al                     | 46(11.5%)|
| bgr                   | 44(11.0%) | su                     | 49(12.2%)|
| bu                    | 19(4.75%) | rbc                    |152(38.0%)|
| sc                    | 17(4.25%) | pc                     | 65(16.2%)|
| sod                   | 87(21.7%) | pcc                    |  4(1.00%)|
| pot                   | 88(22.0%) | ba                     |  4(1.00%)|
| hemo                  | 52(13.0%) | htn                    |  2(0.50%)|
| pcv                   | 71(17.7%) | dm                     |  2(0.50%)|
| wc                    |106(26.5%) | cad                    |  2(0.50%)|
| rc                    |131(32.7%) | appet, pe, ane         |  1(0.25%)|
+-----------------------------------------------------------------------+
```

### 3.1. Kỹ Thuật Làm Sạch Ký Tự Rác (String Cleaning)

Trong tệp CSV thô, một số cột số (`pcv`, `wc`, `rc`) và cột phân loại (`dm`, `cad`, `classification`) bị lẫn các ký tự khoảng trắng không chuẩn (`\t`), hoặc ký tự rác.

1. **Chuẩn hóa chuỗi nhãn mục tiêu (`classification`)**:
   - Nhãn thô chứa các giá trị dính ký tự `\t`: `'ckd\t'` $\rightarrow$ `'ckd'`.
   - Chuyển đổi về dạng binary: `'ckd'` $\rightarrow 1$ (Có bệnh thận), `'notckd'` $\rightarrow 0$ (Không bị bệnh thận).
2. **Ép kiểu số cho biến liên tục bị lẫn chuỗi**:
   - Cột `pcv`, `wc`, `rc` trong file thô chứa chuỗi rác như `'?` hoặc `'\t43'`.
   - Cần áp dụng hàm làm sạch chuỗi và ép về dạng số thực (`float64`).

### 3.2. Chiến Lược Điền Giá Trị Khuyết Chống Rò Rỉ Dữ Liệu (Imputation Strategy)

Để đảm bảo không vi phạm nguyên tắc Data Leakage, bộ điền giá trị khuyết (Imputer) chỉ được phép học các tham số thống kê trên tập huấn luyện (Train set) và áp dụng lên tập kiểm thử (Test set):

- **Đối với 11 biến liên tục (Numerical)**: Áp dụng `SimpleImputer(strategy='median')`. Sử dụng trung vị (Median) giúp tránh bị ảnh hưởng bởi các giá trị ngoại lệ (Outliers) trong các chỉ số xét nghiệm y tế như `sc` hay `bgr`.
  $$\hat{x}_{i,j} = \text{Median}\left(\mathbf{x}_{:,j}^{\text{train}}\right)$$
- **Đối với 13 biến phân loại (Categorical)**: Áp dụng `SimpleImputer(strategy='most_frequent')`. Sử dụng yếu vị (Mode) để thay thế các giá trị khuyết bằng nhãn xuất hiện phổ biến nhất trong tập huấn luyện.
  $$\hat{x}_{i,j} = \text{Mode}\left(\mathbf{x}_{:,j}^{\text{train}}\right)$$

---

## 4. Phân Phối Nhãn Mùa Vụ & Thống Kê Mô Tả Lâm Sàng

Phân tích thống kê mô tả giữa hai nhóm bệnh nhân `ckd` ($y=1$) và `notckd` ($y=0$) thể hiện sự khác biệt rõ rệt ở các chỉ số sinh hóa then chốt.

```
So sánh chỉ số trung bình giữa nhóm Bệnh Thận (CKD) và Nhóm Khỏe Mạnh (NOTCKD):
+----------------------------------------------------------------------------+
| Chỉ số Lâm Sàng               | Nhóm CKD (y=1)     | Nhóm NOTCKD (y=0)    |
+----------------------------------------------------------------------------+
| Tuổi trung bình (age)          | 54.5 tuổi          | 46.5 tuổi            |
| Huyết áp trung bình (bp)       | 79.6 mmHg          | 71.3 mmHg            |
| Creatinine huyết thanh (sc)    | 4.41 mg/dl (Rất cao)| 0.87 mg/dl (Bình thường)|
| Urê máu (bu)                   | 72.4 mg/dl (Cao)   | 32.7 mg/dl (Bình thường)|
| Huyết sắc tố (hemo)            | 10.6 g/dl (Thiếu)  | 15.2 g/dl (Bình thường)|
| Thể tích khối hồng cầu (pcv)   | 32.9% (Thấp)       | 46.3% (Bình thường)  |
| Albumin nước tiểu (al >= 1)    | 74.2% bệnh nhân    | 0.0% bệnh nhân       |
| Tăng huyết áp (htn = yes)      | 58.8% bệnh nhân    | 0.0% bệnh nhân       |
| Đái tháo đường (dm = yes)      | 54.4% bệnh nhân    | 0.0% bệnh nhân       |
+----------------------------------------------------------------------------+
```

Sự khác biệt vượt trội ở các chỉ số Creatinine (`sc`), Albumin (`al`), Huyết sắc tố (`hemo`) và tiền sử Tăng huyết áp (`htn`) cho thấy các thuật toán học máy dựa trên cây quyết định (Decision Tree, Random Forest) hoặc ranh giới phân tách (SVM, Logistic Regression) sẽ dễ dàng tìm thấy các ngưỡng cắt (Split Thresholds) để phân loại chính xác hai nhóm bệnh nhân này.

---

## 5. Tương Quan Đặc Trưng & Ý Nghĩa Y Khoa Chẩn Đoán

Phân tích ma trận tương quan Pearson giữa các thuộc tính định lượng và nhãn mục tiêu cho thấy các mối tương quan lâm sàng mạnh mẽ:

1. **Tương quan âm mạnh với nhãn CKD**:
   - `hemo` (Hemoglobin, $r = -0.769 \approx -0.77$): Huyết sắc tố càng giảm thì nguy cơ bị bệnh thận mãn tính càng cao.
   - `pcv` (Packed Cell Volume, $r = -0.741 \approx -0.74$): Tỷ lệ khối hồng cầu giảm phản ánh mức độ thiếu máu mãn tính do suy thận.
   - `rc` (Red Blood Cell Count, $r = -0.699 \approx -0.70$): Mật độ hồng cầu suy giảm mạnh khi thận thiếu hụt Erythropoietin.
   - `sod` (Sodium, $r = -0.376 \approx -0.38$): Hạ natri máu thường gặp trong suy thận ứ dịch.
2. **Tương quan dương rõ rệt với nhãn CKD**:
   - `bgr` (Blood Glucose Random, $r = +0.420 \approx +0.42$): Đường huyết tăng cao làm tăng nguy cơ biến chứng thận đái tháo đường.
   - `bu` (Blood Urea, $r = +0.381 \approx +0.38$): Urê tích tụ trong máu do thận không đào thải được.
   - `sc` (Serum Creatinine, $r = +0.300$): Nồng độ Creatinine tăng vọt (lệch phải mạnh đến `76.0 mg/dL`) khi mức lọc cầu thận suy giảm.
   - `bp` (Blood Pressure, $r = +0.294$): Tăng huyết áp gây tổn thương mạch máu cầu thận.
3. **Đa cộng tuyến nội tại:** Cặp `hemo` – `pcv` có tương quan tuyến tính rất cao ($r = +0.895$) và cặp `bu` – `sc` đạt $r = +0.586$.

---

## 6. Quy Trình Chuẩn Hóa & Chuẩn Bị Dữ Liệu Cho Mô Hình Học Máy

Để chuyển đổi bộ dữ liệu thô `kidney_disease.csv` thành ma trận đặc trưng chuẩn hóa $\mathbf{X} \in \mathbb{R}^{N \times d^*}$ sẵn sàng đưa vào huấn luyện mô hình, quy trình tiền xử lý được thực thi nghiêm ngặt theo các bước sau:

```
Tóm tắt Pipeline Tiền Xử Lý Dữ Liệu Bệnh Thận (Data Pipeline Architecture):

 [File CSV Thô: kidney_disease.csv]
                 │
                 ▼
 ┌───────────────────────────────────────────────────────────┐
 │ Step 1: String Cleaning & Type Conversion                 │
 │ - Xóa khoảng trắng rác ('\t'), gán nhãn ckd=1, notckd=0    │
 │ - Ép kiểu float cho pcv, wc, rc                           │
 └───────────────────────────────────────────────────────────┘
                 │
                 ▼
 ┌───────────────────────────────────────────────────────────┐
 │ Step 2: Stratified Train/Test Split (80/20)               │
 │ - Tách độc lập tập Train (320 mẫu) và Test (80 mẫu)       │
 └───────────────────────────────────────────────────────────┘
                 │
                 ├──────────────────────────────┐
                 ▼                              ▼
 ┌───────────────────────────────┐ ┌──────────────────────────┐
 │ Step 3a: Numerical Imputer    │ │ Step 3b: Categorical Impr│
 │ - SimpleImputer(median)       │ │ - SimpleImputer(mode)    │
 └───────────────────────────────┘ └──────────────────────────┘
                 │                              │
                 ▼                              ▼
 ┌───────────────────────────────┐ ┌──────────────────────────┐
 │ Step 4a: Z-Score Scaling      │ │ Step 4b: One-Hot Encoding│
 │ - StandardScaler()            │ │ - OneHotEncoder()        │
 └───────────────────────────────┘ └──────────────────────────┘
                 │                              │
                 └──────────────┬───────────────┘
                                ▼
 ┌───────────────────────────────────────────────────────────┐
 │ Step 5: Feature Matrix Fusion                             │
 │ - Kết hợp ma trận đặc trưng sẵn sàng nạp vào Model ML     │
 └───────────────────────────────────────────────────────────┘
```

Quy trình chuẩn hóa này đảm bảo toàn bộ dữ liệu đầu vào đáp ứng đúng tiêu chí khoa học dữ liệu, loại bỏ hiện tượng rò rỉ thông tin từ tập kiểm thử và cung cấp bộ đặc trưng giàu thông tin nhất cho các mô hình chẩn đoán y tế.
