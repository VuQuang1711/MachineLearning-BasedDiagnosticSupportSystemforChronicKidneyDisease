# CHƯƠNG 6. KẾT LUẬN, HƯỚNG PHÁT TRIỂN VÀ TÀI LIỆU THAM KHẢO

## 6.1. KẾT LUẬN

Qua 15 tuần triển khai bài bản theo đúng đề cương học phần Học máy (Bộ môn KHDL — Trường Đại học Công Thương TP.HCM) và quy trình 8 bước phát triển dự án Học máy (tham chiếu chuẩn bài giảng Học máy — Trường Đại Học Công Nghệ Thông Tin(UIT) - Đại Học Quốc Gia Thành Phố Hồ Chí Minh(VNUHCM)), nhóm đã hoàn thành trọn vẹn toàn bộ các mục tiêu đề ra của **Đề tài số 04: Chẩn đoán Bệnh thận mãn tính (CKD)**.

Tổng kết 4 nội dung cốt lõi của giai đoạn đánh giá giải pháp:

1. **Những khám phá chính từ dữ liệu y tế:**
   - Xác định thành công nhóm chỉ số huyết học và lọc cầu thận cốt lõi (`hemo` $22.45\%$, `pcv` $20.22\%$, `sc` $9.51\%$, `htn_yes` $7.98\%$, `rc` $7.75\%$, `dm_yes` $5.22\%$) đóng góp $73.13\%$ sức mạnh phân loại, hoàn toàn khớp với y văn thận học KDIGO 2024; đồng thời chứng minh bằng bảng crosstab rằng 100% ca có `al >= 1.0`, `sg <= 1.015`, `htn='yes'`, `dm='yes'`, `pe='yes'`, `ane='yes'` đều mắc CKD.
   - Kiểm toán toàn vẹn 400 ca bệnh: `0` dòng trùng lặp, `0` cột hằng số, loại bỏ cột định danh `id`, phát hiện cơ chế khuyết dữ liệu MAR trên 24/24 cột (`1,012` ô `NaN` = `10.54%`) và đa cộng tuyến mạnh giữa `hemo` – `pcv` ($r = 0.895$).
2. **Các kỹ thuật đã thử nghiệm — Hiệu quả và Không hiệu quả:**
   - **Hiệu quả:** Đóng gói `ColumnTransformer` (Median/Mode Imputer + OneHotEncoder + StandardScaler, chuyển `24 -> 35` chiều sạch) chống hoàn toàn Data Leakage; sử dụng **Random Forest** tinh chỉnh bằng `GridSearchCV` (`criterion='entropy', max_depth=5, min_samples_split=6, min_samples_leaf=3`) đạt **Accuracy $96.25\%$**, **Precision $97.96\%$**, **Recall $96.00\%$**, **F1-Score $96.97\%$**, **ROC-AUC $0.9980$** và **Stratified 5-Fold CV Recall $98.50\% \pm 1.22\%$**.
   - **Kém hiệu quả:** Thuật toán `k-NN` bị loãng khoảng cách trong không gian 35 chiều nên Recall tụt xuống $88.0\%$ (bỏ sót 6 ca bệnh); cây quyết định đơn `Decision Tree` không giới hạn độ sâu dễ bị quá khớp; dùng PCA trực tiếp làm đầu vào mô hình làm mất khả năng giải thích y khoa cho bác sĩ.
3. **Các giả định của hệ thống:**
   - Dữ liệu khuyết tuân theo cơ chế MAR (có thể ước lượng đại diện bằng Trung vị / Yếu vị của tập huấn luyện).
   - Các mẫu bệnh nhân trong tương lai có phân phối sinh hóa tương đồng với tập dữ liệu huấn luyện (cần hiệu chỉnh lại nếu áp dụng cho nhóm đối tượng đặc thù như trẻ em hoặc phụ nữ mang thai).
4. **Sản phẩm bàn giao hoàn chỉnh:**
   - Jupyter Notebook thực nghiệm 36 cells chạy mượt trên cả Google Colab (tích hợp Google Drive) và máy cục bộ (0 lỗi, 0 cảnh báo), xuất tự động 10 biểu đồ phân tích độ phân giải cao.
   - Tệp Pipeline đóng gói `models/kidney_disease_pipeline.joblib` (`187.43 KB`) vượt qua **17/17 ca kiểm thử tự động**.
   - Ứng dụng Web lâm sàng **HUIT Hospital CDSS** hoạt động ổn định, kết hợp dự đoán AI và giải trình sinh hóa XAI theo chuẩn KDIGO 2024.

---

## 6.2. HẠN CHẾ VÀ HƯỚNG PHÁT TRIỂN

### Hạn chế hiện tại
- **Quy mô mẫu còn khiêm tốn ($N = 400$):** Số lượng bệnh nhân chưa đủ lớn để bao phủ toàn bộ các biến thể lâm sàng hiếm gặp hoặc phân lớp chi tiết trực tiếp theo từng giai đoạn G1–G5 bằng Học máy thuần túy.
- **Dữ liệu tĩnh tại một thời điểm:** Bộ dữ liệu chưa có chuỗi thời gian (longitudinal data) để theo dõi tốc độ sụt giảm chức năng thận của cùng một bệnh nhân qua nhiều quý liên tiếp.

### Hướng phát triển trong tương lai
1. **Mở rộng dữ liệu và thuật toán:** Thu thập thêm dữ liệu bệnh án đa trung tâm (chuẩn hóa ẩn danh), thử nghiệm thêm các thuật toán Gradient Boosting hiện đại như **XGBoost**, **LightGBM**, **CatBoost** kết hợp **SHAP Values** cục bộ cho từng bệnh nhân.
2. **Nâng cấp công thức lâm sàng:** Tích hợp thêm phương trình **CKD-EPI 2021** (không phụ thuộc chủng tộc) song song với MDRD để tăng độ chính xác ước lượng eGFR ở người có chức năng thận bình thường hoặc suy giảm nhẹ.
3. **Tích hợp hạ tầng bệnh viện:** Phát triển API chuẩn hóa theo giao thức **HL7 FHIR** để kết nối trực tiếp với hệ thống quản lý bệnh viện (HIS) và hệ thống xét nghiệm (LIS), tự động đẩy kết quả xét nghiệm vào mô hình sàng lọc cảnh báo sớm.

---

## 6.3. TÀI LIỆU THAM KHẢO

1. Rubini, L., Soundarapandian, P., & Eswaran, P. (2015). *Chronic Kidney Disease Dataset*. UCI Machine Learning Repository. https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease
2. Singh, A. K. *Kidney Disease Dataset*. Kaggle. https://www.kaggle.com/datasets/akshayksingh/kidney-disease-dataset
3. KDIGO (2024). *KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease*. Kidney International, 105(4S), S117–S314.
4. Breiman, L. (2001). *Random Forests*. Machine Learning, 45(1), 5–32.
5. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825–2830.
6. Bộ môn Khoa học Dữ liệu — Trường Đại học Công Thương TP.HCM (HUIT) (2026). *Đề cương chi tiết và Yêu cầu thực hiện Đồ án kết thúc học phần Học máy năm học 2026–2027*.
7. Tài liệu bài giảng môn Học máy — *Quy trình 8 bước phát triển dự án Máy học*, Trường Đại Học Công Nghệ Thông Tin(UIT) - Đại Học Quốc Gia Thành Phố Hồ Chí Minh(VNUHCM).

---

## 6.4. PHỤ LỤC: HƯỚNG DẪN CÀI ĐẶT VÀ VẬN HÀNH ỨNG DỤNG

### 1. Cài đặt môi trường Python
```powershell
# Cài đặt đầy đủ thư viện phụ thuộc
pip install -r requirements.txt
```

### 2. Chạy bộ 17 ca kiểm thử tự động (Unit Tests)
```powershell
python -B -m unittest discover -s test -p "MainTest_*.py" -v
```

### 3. Khởi động ứng dụng Web HUIT Hospital CDSS
```powershell
python -B src/app.py
```
Sau khi khởi chạy thành công, mở trình duyệt và truy cập địa chỉ: **`http://127.0.0.1:5000`**.
