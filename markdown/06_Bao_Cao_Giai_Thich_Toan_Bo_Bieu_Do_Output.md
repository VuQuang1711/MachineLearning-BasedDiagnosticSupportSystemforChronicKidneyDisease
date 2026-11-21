# BÁO CÁO GIẢI THÍCH CHI TIẾT TOÀN BỘ 10 BIỂU ĐỒ OUTPUT DỰ ÁN HỌC MÁY (CKD)

**Đề tài:** BT04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease - CKD)  
**Học phần:** Học Máy (Machine Learning) — Năm học: 2026–2027  
**Lớp học phần:** 15DHKHDL04 — **Bộ môn:** Khoa học Dữ liệu (KHDL)  
**Đơn vị đào tạo:** Trường Đại học Công Thương TP.HCM (HUIT) kết hợp bài giảng chuẩn Trường Đại Học Công Nghệ Thông Tin(UIT) - Đại Học Quốc Gia Thành Phố Hồ Chí Minh(VNUHCM)  
**Giảng viên hướng dẫn:** ThS. Nguyễn Thị Huyền Trang  
**Thư mục lưu trữ biểu đồ:** [`OutputForProject/MLOutput/`](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/)  

---

## 📑 MỤC LỤC TỔNG QUAN HỆ THỐNG BIỂU ĐỒ

| STT | Tên Tệp Biểu Đồ | Nhóm Giai Đoạn | Loại Đồ Thị Chính | Ý Nghĩa Kỹ Thuật & Y Học Lâm Sàng |
| :---: | :--- | :--- | :--- | :--- |
| **01** | [`missing_values.png`](#1-missing_valuespng--ty-le-khuyet-thieu-du-lieu-tren-24-thuoc-tinh) | Tiền xử lý (EDA) | Ngang Bar Chart (`barh`) | Kiểm toán 24/24 biến thiếu (`1,012` ô `NaN` = `10.54%`), phân tầng Imputation (Median/Mode). |
| **02** | [`target_distribution.png`](#2-target_distributionpng--phan-phoi-nhan-muc-tieu-va-mat-can-bang) | Khám phá dữ liệu | Cột kép & Biểu đồ Donut | Đánh giá tỷ lệ bệnh nhân $250:150$ ($62.5\% : 37.5\%$), định hướng Stratified Split. |
| **03** | [`golden_biomarkers.png`](#3-golden_biomarkerspng--tam-giac-vang-sinh-hoa-lam-sang) | Sinh học y tế | KDE + Boxplot + Countplot | Khảo sát phân phối 4 chỉ số vàng: Creatinine, Hemo, Albumin, Tỷ trọng niệu kèm bảng `groupby` & `crosstab`. |
| **04** | [`correlation_matrix.png`](#4-correlation_matrixpng--ma-tran-tuong-quan-pearson-da-bien) | Phân tích quan hệ | Heatmap tương quan ($12 \times 12$) | Phát hiện tương quan đa biến, xác định $r(\text{hemo, target}) = -0.77$, $r(\text{bgr, target}) = +0.42$, $r(\text{sc, target}) = +0.30$. |
| **05** | [`data_after_preprocessing.png`](#5-data_after_preprocessingpng--kiem-chung-pipeline-truoc-va-sau-z-score) | Kiểm chuẩn Pipeline | Boxplot đối sánh Trước vs Sau | Minh chứng loại bỏ rò rỉ dữ liệu, đồng nhất thang đo Z-score ($\mu \approx 0, \sigma \approx 1$) trên đúng 4 biến `bp`, `bu`, `hemo`, `sc`. |
| **06** | [`models_comparison.png`](#6-models_comparisonpng--so-sanh-da-tieu-chi-6-thuat-toan-hoc-may) | Đánh giá mô hình | Grouped Bar Chart (4 chỉ số) | Đối chiếu Accuracy, Recall, F1, ROC-AUC của 6 thuật toán; khẳng định ưu thế Random Forest. |
| **07** | [`confusion_matrix.png`](#7-confusion_matrixpng--ma-tran-nham-lan-kiem-dinh-80-benh-nhan) | Kiểm định chẩn đoán | Heatmap Ma trận nhầm lẫn ($2 \times 2$) | Đo lường độ nhạy thực tế trên 80 ca test: $TP=48$, $TN=29$, $FP=1$, $FN=2$ (Recall $96.0\%$). |
| **08** | [`roc_curves.png`](#8-roc_curvespng--duong-cong-roc-va-nang-luc-phan-tach-auc) | Năng lực phân loại | Multi-Line ROC Curve | Đo diện tích dưới đường cong AUC: Random Forest đạt $0.9980$, tiệm cận tuyệt đối $1.0000$. |
| **09** | [`feature_importance.png`](#9-feature_importancepng--top-10-dac-trung-quan-trong-nhat) | Giải thích AI (XAI) | Ngang Bar Chart trọng số (%) | Minh bạch hóa "hộp đen": `hemo` ($22.45\%$), `pcv` ($20.22\%$), `sc` ($9.51\%$), `htn_yes` ($7.98\%$). |
| **10** | [`pca_variance.png`](#10-pca_variancepng--phan-tich-thanh-phan-chinh-pca-scree--2d) | Giảm chiều dữ liệu | Scree Plot & 2D Scatter | Xác định 19/35 thành phần giữ $95.26\%$ ($\ge 95\%$) phương sai ($PC1=31.18\%$, $PC2=10.69\%$). |

---

## 1. `missing_values.png` — Tỷ Lệ Khuyết Thiếu Dữ Liệu Trên 24 Thuộc Tính

![missing_values.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/missing_values.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 7 (Giai đoạn Khám phá dữ liệu EDA).
- **Thư viện thực hiện:** `matplotlib.pyplot`, `pandas`.
- **Dạng đồ thị:** Horizontal Bar Chart (`barh`), đường tham chiếu ngưỡng khuyết cao tại $20\%$ (`axvline`).

### B. Phân tích số liệu thực tế
1. **Tổng thể:** Sau khi ép kiểu chuẩn và chuyển các chuỗi rác `"?"` về `NaN`, cả **24/24 thuộc tính lâm sàng** đều tồn tại giá trị khuyết (`NaN`), tổng cộng **`1,012 / 9,600` ô trống (`10.54%`)** trên toàn bộ 400 ca bệnh (trong khi có `0` dòng trùng lặp và `0` cột hằng số).
2. **Nhóm khuyết trầm trọng ($>20\%$):**
   - Tế bào hồng cầu niệu (`rbc`): Khuyết $38.0\%$ (152/400 ca).
   - Thể tích khối hồng cầu (`rc`): Khuyết $32.75\%$ (131/400 ca).
   - Số lượng bạch cầu (`wc`): Khuyết $26.5\%$ (106/400 ca).
   - Dung tích hồng cầu (`pcv`): Khuyết $17.75\%$ (71 ca).
   - Kali máu (`pot`) và Natri máu (`sod`): Khuyết lần lượt $22.0\%$ và $21.75\%$.
3. **Nhóm khuyết thấp ($<10\%$):**
   - Huyết áp (`bp`): $3.0\%$.
   - Tuổi (`age`): $2.25\%$.
   - Các biến phân loại như Tăng huyết áp (`htn`), Đái tháo đường (`dm`): $\le 0.5\%$.

### C. Ý nghĩa Y học & Quyết định Kỹ thuật Machine Learning
- **Bản chất Y sinh (Cơ chế MAR - Missing At Random):** Trong thực tế bệnh viện, bác sĩ không chỉ định tràn lan tất cả xét nghiệm. Những bệnh nhân có triệu chứng nhẹ thường không làm sinh thiết cặn nước tiểu (`rbc`, `pc`) hoặc điện giải đồ chuyên sâu (`sod`, `pot`). Đây là cơ chế khuyết phụ thuộc bối cảnh lâm sàng, không phải do lỗi ghi nhận ngẫu nhiên.
- **Quyết định thuật toán:** Tuyệt đối không xóa dòng (`dropna`), vì xóa dòng sẽ làm mất hơn $60\%$ dữ liệu quý giá (từ 400 mẫu tụt xuống còn chưa đầy 160 mẫu). Nhóm quyết định thiết kế kiến trúc Pipeline 2 nhánh:
  - Điền khuyết bằng **Trung vị (Median)** cho 11 biến định lượng để chống lệch ngoại lai.
  - Điền khuyết bằng **Yếu vị (Mode)** cho 13 biến định tính để bảo toàn tần suất xuất hiện tự nhiên.

---

## 2. `target_distribution.png` — Phân Phối Nhãn Mục Tiêu Và Mất Cân Bằng

![target_distribution.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/target_distribution.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 9.
- **Thư viện thực hiện:** `seaborn.barplot` kết hợp `matplotlib.pyplot.pie` (Donut chart với lỗ rỗng trung tâm $45\%$).
- **Màu sắc chuẩn y tế:** Đỏ cảnh báo (`#dc2626`) biểu thị ca bệnh CKD; Xanh lá an toàn (`#16a34a`) biểu thị ca khỏe mạnh.

### B. Phân tích số liệu thực tế
- **Số ca mắc bệnh thận mạn (CKD - Nhãn 1):** 250 bệnh nhân, chiếm **$62.5\%$**.
- **Số ca không mắc bệnh (Not CKD - Nhãn 0):** 150 bệnh nhân, chiếm **$37.5\%$**.
- **Tỷ lệ mất cân bằng:** $\approx 1.67 : 1$.

### C. Ý nghĩa Y học & Quyết định Kỹ thuật Machine Learning
- **Đánh giá mức độ lệch lớp:** Tỷ lệ $62.5\% / 37.5\%$ thuộc nhóm **mất cân bằng nhẹ (Mild Imbalance)**, chưa đến mức cực đoan như bài toán phát hiện gian lận thẻ tín dụng hay ung thư hiếm ($99:1$). Do đó, không cần thiết phải dùng kỹ thuật sinh mẫu nhân tạo quá đà như SMOTE (vốn dễ tạo ra các ca bệnh nhân "ảo" không đúng sinh lý thận).
- **Quyết định phân chia tập dữ liệu:**
  - Bắt buộc áp dụng **Stratified Train-Test Split (Tỷ lệ 80/20)** và **Stratified 5-Fold Cross Validation**.
  - Việc phân tầng đảm bảo cả tập Train (320 mẫu) và tập Test (80 mẫu) đều giữ nguyên chính xác tỷ lệ $62.5\%$ bệnh nhân CKD và $37.5\%$ người bình thường, triệt tiêu hoàn toàn hiện tượng lệch phân phối (*Distribution Shift*).

---

## 3. `golden_biomarkers.png` — Tam Giác Vàng Sinh Hóa Lâm Sàng

![golden_biomarkers.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/golden_biomarkers.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 11.
- **Cấu trúc khung hình:** Lưới $2 \times 3$ gồm đồ thị ước lượng mật độ nhân Kernel Density Estimation (`sns.kdeplot`), đồ thị hộp (`sns.boxplot`) và biểu đồ đếm tần số (`sns.countplot`).

### B. Phân tích 4 chỉ số sinh hóa cốt lõi
1. **Serum Creatinine (`sc` - mg/dL):**
   - *Nhóm khỏe mạnh:* Phân phối tập trung cực hẹp tại dải an toàn $0.6 - 1.2\text{ mg/dL}$ (đúng chuẩn sinh lý người bình thường).
   - *Nhóm CKD:* Đường phân bố lệch phải rất dài (Right-skewed), kéo dài từ $0.50$ lên tới $76.00\text{ mg/dL}$, trung bình đạt mức báo động **$4.41\text{ mg/dL}$** (trung vị **$2.25\text{ mg/dL}$**).
2. **Hemoglobin (`hemo` - g/dL):**
   - *Nhóm khỏe mạnh:* Đỉnh phân bố cao tại $13.5 - 17.0\text{ g/dL}$ (sắc tố máu hồng hào).
   - *Nhóm CKD:* Tụt dốc sâu xuống dưới ngưỡng thiếu máu $12.0\text{ g/dL}$, phổ biến trong khoảng $7.0 - 10.5\text{ g/dL}$.
3. **Đạm niệu Albumin (`al`):**
   - *Nhóm khỏe mạnh:* $100\%$ bệnh nhân nằm ở mức $0$ (nước tiểu hoàn toàn không có đạm).
   - *Nhóm CKD:* Phân bố trải đều từ mức $1$ đến $5$ (protein niệu từ vi thể đến ồ ạt).
4. **Tỷ trọng nước tiểu (`sg`):**
   - *Nhóm khỏe mạnh:* Tỷ trọng cao ($1.020 - 1.025$), chứng tỏ ống thận cô đặc nước tiểu tốt.
   - *Nhóm CKD:* Tỷ trọng giảm thấp cố định quanh $1.005 - 1.015$ do thận mất khả năng cô đặc.

### C. Ý nghĩa Y học & Đóng góp cho mô hình
- Đồ thị chứng minh sự tồn tại của **"Tam giác vàng sinh hóa"**: Bộ ba `sc - hemo - al` tạo nên ranh giới phân tách sinh học cực kỳ sâu sắc giữa người bệnh và người lành.
- Đây là cơ sở khoa học giải thích vì sao các thuật toán dạng cây (Random Forest, Decision Tree) lại đạt độ chính xác cao vượt trội: cây chỉ cần 2 đến 3 nhát cắt phân nhánh trên các biến này là đã phân loại chính xác trên $90\%$ ca bệnh.

---

## 4. `correlation_matrix.png` — Ma Trận Tương Quan Pearson Đa Biến

![correlation_matrix.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/correlation_matrix.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 13.
- **Thư viện thực hiện:** `sns.heatmap` với dải màu tương phản đối xứng `coolwarm`, thang đo từ $-1.0$ đến $+1.0$, hiển thị số liệu thập phân 2 chữ số (`fmt=".2f"`).

### B. Các phát hiện tương quan then chốt

```
Hệ số tương quan Pearson: r = Cov(X, Y) / (σ_X * σ_Y)
```

1. **Tương quan mạnh nhất với biến mục tiêu (`target`):**
   - **Hemoglobin (`hemo`):** $r = -0.769 \approx -0.77$ (Tương quan nghịch rất mạnh). Nồng độ huyết sắc tố càng thấp thì xác suất mắc bệnh thận càng cao.
   - **Dung tích hồng cầu (`pcv`):** $r = -0.741 \approx -0.74$ (Tương quan nghịch rất mạnh).
   - **Số lượng hồng cầu (`rc`):** $r = -0.699 \approx -0.70$ (Tương quan nghịch mạnh).
   - **Đường huyết (`bgr`):** $r = +0.420 \approx +0.42$ (Tương quan thuận).
   - **Urê máu (`bu`):** $r = +0.381 \approx +0.38$ (Tương quan thuận).
   - **Serum Creatinine (`sc`):** $r = +0.300$ (Tương quan thuận, có giá trị ngoại lai lệch phải tới `76.0 mg/dL`).
2. **Hiện tượng đa cộng tuyến giữa các biến lâm sàng nội tại:**
   - Cặp `hemo` và `pcv` có hệ số tương quan đạt tới **$r = +0.895$**.
   - Cặp `bu` và `sc` có tương quan dương mạnh **$r = +0.586$**.

### C. Quyết định kỹ thuật Machine Learning
- Sự xuất hiện của hiện tượng cộng tuyến mạnh ($r = 0.89$ giữa `hemo` và `pcv`) sẽ làm cho các thuật toán tuyến tính đơn giản (như Logistic Regression không điều chuẩn) bị bất ổn định trọng số giải thích.
- Điều này củng cố quyết định lựa chọn **Random Forest**: Thuật toán rừng cây chọn ngẫu nhiên tập con đặc trưng tại mỗi nút (`max_features = 'sqrt'`), nhờ đó triệt tiêu tác động tiêu cực của đa cộng tuyến và giữ vững độ bền phân loại.

---

## 5. `data_after_preprocessing.png` — Kiểm Chứng Pipeline Trước Và Sau Z-Score

![data_after_preprocessing.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/data_after_preprocessing.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 17.
- **Dạng đồ thị:** Boxplot song song 2 đồ thị con (Trái: Dữ liệu thô; Phải: Dữ liệu sau biến đổi Z-score qua Pipeline).

### B. Phân tích đối sánh Trước vs Sau
1. **Nửa bên trái (Dữ liệu gốc):**
   - Thang đo chênh lệch hàng trăm lần: Huyết áp `bp` dao động $50 - 180\text{ mmHg}$, Urê máu `bu` dao động $10 - 390\text{ mg/dL}$, trong khi Creatinine `sc` chỉ từ $0.4 - 15.0\text{ mg/dL}$.
   - Nếu đưa trực tiếp vào các mô hình nhạy cảm khoảng cách (như SVM, k-NN), biến `bu` với giá trị hàng trăm sẽ hoàn toàn "đè bẹp" biến `sc`, khiến mô hình bỏ qua dấu hiệu suy thận then chốt.
2. **Nửa bên phải (Sau Pipeline StandardScaler):**
   - Toàn bộ các biến số được quy chuẩn hóa về cùng phân phối chuẩn:
     $$z = \frac{x - \mu}{\sigma} \quad (\mu \approx 0, \sigma \approx 1)$$
   - Đường trung bình màu đỏ ($z = 0$) làm mốc cân bằng; biên độ dao động của mọi chỉ số được kéo về dải $[-2, +4]$.
   - Các giá trị ngoại lai bệnh lý cực độ (Outliers như bệnh nhân ngộ độc urê) vẫn được giữ nguyên dạng hình học mà không làm sai lệch không gian đặc trưng.

### C. Ý nghĩa kiểm chuẩn kỹ thuật phần mềm (QA)
- Khẳng định $100\%$ không còn giá trị `NaN` nào lọt qua tập huấn luyện và kiểm thử.
- Chứng minh nguyên tắc **Chống rò rỉ dữ liệu (No Data Leakage)**: Bộ `ColumnTransformer` chỉ học thống kê $\mu, \sigma$ trên tập `X_train`, sau đó dùng lại nguyên vẹn để `transform` cho `X_test` và dữ liệu bệnh nhân mới từ Web EMR.

---

## 6. `models_comparison.png` — So Sánh Đa Tiêu Chí 6 Thuật Toán Học Máy

![models_comparison.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/models_comparison.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 20.
- **Thư viện thực hiện:** Grouped Bar Chart với 4 cột chỉ số song song cho mỗi thuật toán:
  - Cột đỏ: **Recall (Độ nhạy y tế ★ - Tiêu chí số 1)**
  - Cột xanh dương: **Accuracy (Độ chính xác tổng thể)**
  - Cột xanh lá: **F1-Score (Trung bình điều hòa Precision & Recall)**
  - Cột vàng cam: **ROC-AUC (Năng lực phân tách)**

### B. Bảng số liệu chi tiết đối chiếu 6 thuật toán

| Thuật Toán | Recall (%) | Accuracy (%) | F1-Score (%) | ROC-AUC | Đánh Giá Kỹ Thuật |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Gaussian Naïve Bayes** | **100.00%** | **100.00%** | **100.00%** | **1.0000** | Hiệu năng phân tách tuyệt đối trên mẫu thử. |
| **SVM (RBF Kernel)** | **98.00%** | **98.75%** | **98.99%** | **0.9993** | Siêu phẳng phân cách tối ưu, cực kỳ ổn định. |
| **Random Forest** | **96.00%** | **96.25%** | **96.97%** | **0.9980** | **Toàn diện nhất:** Kháng nhiễu, không quá khớp, hỗ trợ XAI. |
| **Logistic Regression** | **96.00%** | **97.50%** | **97.96%** | **0.9987** | Mô hình cơ sở (Baseline) tuyến tính vững chắc. |
| **Decision Tree (CART)** | **94.00%** | **95.00%** | **95.92%** | **0.9687** | Dễ quá khớp nếu không khống chế độ sâu (`max_depth`). |
| **k-NN ($k=5$)** | **88.00%** | **92.50%** | **93.62%** | **0.9887** | Bị loãng khoảng cách do không gian 35 chiều (*Curse of Dimensionality*). |

### C. Triết lý Y tế & Lý giải lựa chọn kiến trúc
- **Tại sao chọn Recall $\ge 96.0\%$ làm kim chỉ nam?** Trong chẩn đoán y khoa, lỗi **Âm tính giả (False Negative - Bỏ sót bệnh)** mang lại hậu quả chết người: bệnh nhân suy thận bị trả về nhà với kết luận "khỏe mạnh", mất cơ hội điều trị lọc máu sớm. Ngược lại, Dương tính giả chỉ tốn thêm chi phí làm xét nghiệm khẳng định lại.
- **Lý do chọn Random Forest thay vì Naïve Bayes dù Naïve Bayes đạt 100%:** Naïve Bayes giả định ngây thơ rằng 24 chỉ số lâm sàng độc lập hoàn toàn với nhau (điều này trái ngược hoàn toàn với sinh lý học, vì `hemo` và `pcv` tương quan tới $0.89$). Random Forest phản ánh chân thực tương tác phi tuyến giữa các cơ quan trong cơ thể và cung cấp được trọng số đặc trưng phục vụ bác sĩ giải trình.

---

## 7. `confusion_matrix.png` — Ma Trận Nhầm Lẫn Kiểm Định 80 Bệnh Nhân

![confusion_matrix.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/confusion_matrix.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 26 (Ghép cùng đồ thị ROC curve).
- **Thư viện thực hiện:** `sns.heatmap` hiển thị 4 góc phần tư nhị phân với định dạng số nguyên (`fmt='d'`).

### B. Bóc tách từng ô trong ma trận kiểm định (80 bệnh nhân tập Test độc lập)

```
                       NHÃN DỰ ĐOÁN (PREDICTED)
                     Khỏe mạnh (0)      Bệnh thận (1)
THỰC TẾ  Khỏe mạnh (0)   TN = 29           FP = 1
(TRUE)   Bệnh thận (1)   FN = 2            TP = 48
```

1. **True Positive ($TP = 48$):** 48 ca bệnh nhân suy thận thực sự đã được mô hình phát hiện chính xác, cảnh báo kịp thời nguy cơ cho bác sĩ.
2. **True Negative ($TN = 29$):** 29 ca người khỏe mạnh được mô hình kết luận an toàn.
3. **False Positive ($FP = 1$):** Chỉ có duy nhất 1 ca người khỏe mạnh bị dự đoán nhầm thành có bệnh (chiếm tỷ lệ cực thấp $1.25\%$).
4. **False Negative ($FN = 2$):** Chỉ có 2 ca bệnh nhân suy thận nhẹ bị bỏ sót (đạt chỉ tiêu y tế khắt khe với **Recall $= \frac{48}{48+2} = 96.00\%$**).

### C. Ý nghĩa thực tiễn lâm sàng
- Ma trận nhầm lẫn chứng minh mô hình không chỉ học vẹt mà có khả năng tổng quát hóa xuất sắc trên các ca bệnh hoàn toàn chưa từng thấy trong quá trình huấn luyện.
- Tỷ lệ chính xác tổng thể: $\text{Accuracy} = \frac{29 + 48}{80} = \frac{77}{80} = 96.25\%$.
- Tỷ lệ giá trị dự đoán dương: $\text{Precision} = \frac{48}{48 + 1} = 97.96\%$.

---

## 8. `roc_curves.png` — Đường Cong ROC Và Năng Lực Phân Tách (AUC)

![roc_curves.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/roc_curves.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 26.
- **Thư viện thực hiện:** `sklearn.metrics.roc_curve` và `roc_auc_score`.
- **Hệ tọa độ:**
  - Trục hoành ($X$): Tỷ lệ dương tính giả $\text{FPR} = \frac{FP}{FP + TN} = 1 - \text{Specificity}$.
  - Trục tung ($Y$): Tỷ lệ dương tính thật $\text{TPR} = \frac{TP}{TP + FN} = \text{Recall / Sensitivity}$.
  - Đường chéo đứt nét màu đen: Ngưỡng phân loại ngẫu nhiên không có giá trị ($\text{AUC} = 0.5000$).

### B. Phân tích diện tích dưới đường cong (AUC) của các mô hình
- **Gaussian Naïve Bayes:** $\text{AUC} = 1.0000$ (Đường cong ôm trọn góc trên bên trái).
- **SVM (RBF Kernel):** $\text{AUC} = 0.9993$.
- **Random Forest:** $\text{AUC} = 0.9980$ (Đường cong dựng đứng cực nhanh lên tiệm cận $1.0$ ngay khi FPR mới ở mức $0.03$).
- **Logistic Regression:** $\text{AUC} = 0.9987$.
- **k-NN:** $\text{AUC} = 0.9887$.
- **Decision Tree:** $\text{AUC} = 0.9687$.

### C. Ý nghĩa ứng dụng trong phần mềm y tế
- Chỉ số $\text{AUC} = 0.9980$ của Random Forest khẳng định: Nếu rút ngẫu nhiên 1 bệnh nhân CKD và 1 người khỏe mạnh, xác suất để mô hình chấm điểm rủi ro của người bệnh cao hơn người khỏe mạnh lên tới **$99.80\%$**.
- Điều này cho phép bác sĩ có thể linh hoạt điều chỉnh ngưỡng cắt quyết định (Classification Threshold $\tau$): Nếu muốn triệt tiêu hoàn toàn 2 ca bỏ sót (Recall $100\%$), bác sĩ chỉ cần hạ ngưỡng cắt xác suất từ $0.5$ xuống $0.35$ trên giao diện Web EMR.

---

## 9. `feature_importance.png` — Top 10 Đặc Trưng Quan Trọng Nhất (XAI)

![feature_importance.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/feature_importance.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 28.
- **Phương pháp toán học:** Mean Decrease in Impurity (MDI) trích xuất từ 100 cây quyết định của `best_rf.feature_importances_`.

### B. Bảng xếp hạng Top 10 đặc trưng quyết định bệnh

| Thứ Hạng | Tên Thuộc Tính | Tên Y Học Đầy Đủ | Trọng Số Quan Trọng (%) | Ý Nghĩa Chức Năng Thận |
| :---: | :--- | :--- | :---: | :--- |
| **1** | `hemo` | Huyết sắc tố Hemoglobin | **$22.45\%$** | Thận hư suy giảm bài tiết Erythropoietin $\rightarrow$ Thiếu máu mạn. |
| **2** | `pcv` | Dung tích hồng cầu Packed Cell Volume | **$20.22\%$** | Tỷ lệ thể tích hồng cầu, biến tương quan song hành với Hemoglobin ($r=0.895$). |
| **3** | `sc` | Serum Creatinine huyết thanh | **$9.51\%$** | Sản phẩm thoái hóa cơ, chỉ số vàng đo mức lọc cầu thận eGFR. |
| **4** | `htn_yes` | Tiền sử tăng huyết áp | **$7.98\%$** | Vừa là nguyên nhân vừa là biến chứng phá hủy mao mạch cầu thận. |
| **5** | `rc` | Số lượng tế bào hồng cầu | **$7.75\%$** | Suy giảm trực tiếp do tủy xương thiếu kích thích từ thận. |
| **6** | `dm_yes` | Tiền sử bệnh đái tháo đường | **$5.22\%$** | Bệnh lý nền kinh điển tiến triển thành hội chứng suy thận mạn. |
| **7** | `sg_1.015` | Tỷ trọng nước tiểu $1.015$ | **$3.63\%$** | Thước đo khả năng cô đặc nước tiểu của hệ thống ống lượn thận. |
| **8** | `bgr` | Đường huyết ngẫu nhiên | **$3.35\%$** | Căn nguyên hàng đầu gây xơ hóa cầu thận do đái tháo đường. |
| **9** | `sod` | Natri huyết thanh (Sodium) | **$3.35\%$** | Phản ánh rối loạn cân bằng điện giải và ứ dịch trong suy thận. |
| **10** | `bu` | Urê máu (Blood Urea) | **$3.33\%$** | Độc chất chuyển hóa protein ứ đọng khi thận suy giảm bài tiết. |

### C. Giá trị Explainable AI (XAI)
- **Minh bạch hóa "Hộp đen":** Biểu đồ cung cấp bằng chứng thuyết phục cho Hội đồng chấm đồ án và y bác sĩ rằng mô hình Random Forest không hề đưa ra kết quả ngẫu nhiên mà ra quyết định hoàn toàn dựa trên các triệu chứng sinh lý kinh điển được công nhận bởi Hiệp hội Thận học Quốc tế (KDIGO).
- Khối XAI trên giao diện Web [templates/index.html](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/templates/index.html) sử dụng chính dữ liệu trọng số này để tô màu cảnh báo nguy cơ sinh hóa cho bệnh nhân.

---

## 10. `pca_variance.png` — Phân Tích Thành Phần Chính PCA (Scree & 2D)

![pca_variance.png](file:///e:/15DHKHDL03/2026-2027/HKI_26_27/MachineLearning/Final_Project/OutputForProject/MLOutput/pca_variance.png)

### A. Vị trí & Thông số kỹ thuật
- **Nguồn xuất phát:** Jupyter Notebook Cell 30.
- **Cấu trúc khung hình:** Đồ thị kép:
  - Bên trái: Đồ thị phương sai tích lũy (Scree Plot) với đường kẻ ngưỡng $95\%$ (`axhline`).
  - Bên phải: Biểu đồ tán xạ 2D chiếu dữ liệu 80 ca kiểm thử lên mặt phẳng tạo bởi 2 thành phần chính đầu tiên ($PC1$ và $PC2$).

### B. Phân tích toán học & Hình học dữ liệu
1. **Phương sai tích lũy (Scree Plot):**
   - Từ 35 chiều sau mã hóa One-Hot, thành phần chính đầu tiên ($PC1$) giải thích **$31.18\%$** và $PC2$ giải thích **$10.69\%$** tổng phương sai của toàn bộ dữ liệu.
   - Để bảo toàn **$\ge 95\%$ lượng thông tin (phương sai)** của toàn bộ tập dữ liệu y tế, hệ thống chỉ cần tối thiểu **19 thành phần chính** (đạt **$95.26\%$** phương sai tích lũy, giảm gần $46\%$ số chiều).
2. **Không gian tán xạ 2 chiều ($PC1$ vs $PC2$):**
   - Các điểm màu xanh dương (Người khỏe mạnh) cụm chặt chẽ ở nửa bên trái ($PC1 < 0$).
   - Các điểm màu đỏ cam (Bệnh nhân CKD) phân tán rộng ở nửa bên phải ($PC1 > 0$).
   - **Nhận định hình học:** Không gian dữ liệu có ranh giới phân tách tự nhiên cực kỳ rõ ràng, giải thích vì sao các mô hình học máy đều đạt điểm số AUC trên $0.98$.

### C. Quyết định kiến trúc hệ thống
- **Vì sao không dùng PCA để huấn luyện mô hình triển khai thực tế?**
  Mặc dù PCA giảm chiều rất tốt và chứng minh dữ liệu phân tách đẹp, trong bài toán y sinh học, các thành phần $PC1, PC2$ là tổ hợp tuyến tính trừu tượng của 35 biến (ví dụ: $PC1 = 0.35 \times \text{hemo} - 0.28 \times \text{sc} + \dots$). Bác sĩ lâm sàng **không thể hiểu được ý nghĩa sinh học của một thành phần trừu tượng**.
- Do đó, nhóm quyết định giữ nguyên không gian đặc trưng gốc 35 chiều để phục vụ trọn vẹn yêu cầu giải thích được (**Explainable AI**) theo đúng định hướng Y tế thông minh 4.0.

---

## 11. BẢNG TỔNG HỢP ÁNH XẠ CHUẨN ĐẦU RA (CLO & RUBRIC CHẤM ĐIỂM)

| Tên Biểu Đồ | Chuẩn Đầu Ra (CLO) | Tiêu Chí Rubric Đáp Ứng | Điểm Số Tối Đa | Thành Viên Phụ Trách |
| :--- | :---: | :--- | :---: | :--- |
| `missing_values.png` | **CLO1, CLO2** | Tiền xử lý & Xử lý dữ liệu khuyết thiếu y tế | 1.0đ | **Vũ Thế Quang** |
| `target_distribution.png` | **CLO1** | Khám phá dữ liệu & Phân tích mất cân bằng nhãn | 1.0đ | **Triệu Thị Thu Ngân** |
| `golden_biomarkers.png` | **CLO1** | Trực quan hóa phân phối biến sinh hóa then chốt | 1.0đ | **Triệu Thị Thu Ngân** |
| `correlation_matrix.png` | **CLO1** | Phân tích ma trận tương quan đa biến Pearson | 1.0đ | **Triệu Thị Thu Ngân** |
| `data_after_preprocessing.png` | **CLO2** | Thiết kế quy trình tiền xử lý chống Data Leakage | 2.0đ | **Vũ Thế Quang** |
| `models_comparison.png` | **CLO1, CLO4** | Huấn luyện & Đánh giá so sánh 6 thuật toán | 1.0đ | **Nguyễn Đình Bảo Tấn** |
| `confusion_matrix.png` | **CLO4** | Kiểm định hiệu năng trên tập test (Recall, CM) | 1.0đ | **Nguyễn Đình Bảo Tấn** |
| `roc_curves.png` | **CLO4** | Phân tích đường cong ROC và chỉ số AUC | 1.0đ | **Nguyễn Đình Bảo Tấn** |
| `feature_importance.png` | **CLO1, CLO3** | Trích xuất mức độ quan trọng đặc trưng (XAI) | 1.0đ | **Nguyễn Thanh Nhàn** |
| `pca_variance.png` | **CLO1** | Áp dụng thuật toán giảm chiều dữ liệu PCA | 1.0đ | **Võ Tấn Đạt (Leader)** |
| **TỔNG CỘNG ĐỒ ÁN** | **CLO1 - CLO4** | **Trọn vẹn 10 biểu đồ trực quan hóa chuẩn mực** | **10.0đ** | **Toàn Bộ 5 Thành Viên** |

