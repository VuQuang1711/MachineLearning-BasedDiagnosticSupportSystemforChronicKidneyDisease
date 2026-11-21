# BÁO CÁO TIẾN ĐỘ TUẦN 08 — ĐÁNH GIÁ SƠ BỘ BASELINE & NỘP BÁO CÁO TIẾN ĐỘ GIAI ĐOẠN 1

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** ★ **MỐC BẮT BUỘC GIAI ĐOẠN 1 — Báo cáo tiến độ đồ án (Tuần 8)**
- **Liên hệ Rubric:** Đánh giá theo **CLO2, CLO3 (Chiếm 20% tổng điểm đồ án)**, tập trung vào: Dữ liệu đã xác nhận, trực quan hóa EDA, định hướng thuật toán rõ ràng, tự học và phối hợp nhóm.
- **Thành viên chủ trì:** Võ Tấn Đạt (`2045240050`) & Toàn bộ 5 thành viên nhóm
- **Trạng thái:** Hoàn thành 100% — Đã nộp báo cáo đúng hạn

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 8)
1. **Đánh giá sơ bộ mô hình baseline và xác định các điểm cần cải thiện:**
   - Đánh giá toàn diện kết quả thực nghiệm 7 tuần đầu (Bộ dữ liệu, trực quan hóa EDA, tiền xử lý và 6 mô hình Baseline).
   - Chỉ ra các nguy cơ tiềm ẩn: Mô hình Baseline chưa được kiểm tra chéo (Cross-Validation) nên có thể bị Overfitting; chưa khảo sát giảm số chiều dữ liệu (PCA); chưa đóng gói tự động hóa để tái sử dụng; chưa có giao diện minh họa cho người dùng cuối.
   - Lập danh mục cải tiến chi tiết cho Giai đoạn 2 (Tuần 9 đến Tuần 14).
2. **Tổng hợp và nộp Báo cáo tiến độ thực hiện đồ án — Giai đoạn 1:**
   - Biên tập hoàn chỉnh tài liệu báo cáo tiến độ Giai đoạn 1 phản ánh đầy đủ: Bộ dữ liệu chính thức, kết quả trực quan hóa EDA, pipeline tiền xử lý và định hướng thuật toán lựa chọn.
   - Nộp báo cáo đúng thời hạn quy định của Bộ môn KHDL (Tuần 8).

---

## 2. Kiểm Điểm Mức Độ Hoàn Thành Yêu Cầu Mốc Tuần 8 (Giai Đoạn 1)

Theo quy định tại Mục V (Một số lưu ý) trong văn bản của Bộ môn KHDL: *"Tuần 8 (nộp báo cáo tiến độ) là mốc bắt buộc, chiếm 20% điểm đồ án — nhóm cần đảm bảo tại thời điểm này đã có tối thiểu: bộ dữ liệu, kết quả EDA/trực quan hóa, và định hướng thuật toán rõ ràng"*.

| Yêu Cầu Bắt Buộc Của Bộ Môn | Tình Trạng | Bằng Chứng Kỹ Thuật Đạt Được |
| :--- | :---: | :--- |
| **1. Bộ dữ liệu chính thức đã xác nhận** | **ĐẠT** | Dataset $N=400, D=24$ tại `DatasetForProject/MLDataset/kidney_disease.csv` |
| **2. Kết quả EDA / Trực quan hóa dữ liệu** | **ĐẠT** | 4 biểu đồ phân tích (`missing_values`, `target_distribution`, `golden_biomarkers`, `correlation_matrix`) |
| **3. Định hướng thuật toán rõ ràng** | **ĐẠT** | Hoàn thành Baseline 6 mô hình, chốt thuật toán chủ lực **Random Forest** |
| **4. Tự học & Vận dụng tài liệu (CLO2)** | **ĐẠT** | Lý thuyết 6 mô hình + PCA + **Bộ 3 ví dụ tính toán thủ công từng bước (Hand Calculation)** |
| **5. Phối hợp làm việc trong nhóm (CLO3)** | **ĐẠT** | Bảng phân công 5 thành viên rõ ràng, minh bạch, đạt tiến độ 100% |

---

## 3. Xác Định Các Điểm Cần Cải Thiện Ở Giai Đoạn 2 (Tuần 9 – 14)
1. **Kiểm tra chéo và Tinh chỉnh siêu tham số (Tuần 9):**
   - Áp dụng **Stratified 5-Fold Cross-Validation** để đo lường độ lệch chuẩn và tính ổn định thực sự của mô hình.
   - Tinh chỉnh siêu tham số bằng **`GridSearchCV`** (`max_depth`, `min_samples_leaf`, `n_estimators`) để chủ động kiểm soát Overfitting.
   - Thực nghiệm kỹ thuật giảm chiều **PCA** để khảo sát phương sai tích lũy và cấu trúc 2D.
2. **Lưu trữ mô hình sau huấn luyện (Tuần 10):**
   - Đóng gói nguyên khối cả tiền xử lý và phân lớp thành một tệp duy nhất (`.joblib`) và kiểm thử load lại.
3. **Xây dựng ứng dụng minh họa hoàn chỉnh (Tuần 11 – 12):**
   - Triển khai ứng dụng Web tương tác trên nền tảng Python Flask (**HUIT Hospital CDSS**), tích hợp khối giải trình XAI và tính eGFR MDRD KDIGO 2024, kèm bộ 17 Unit Tests tự động.
4. **Biên soạn báo cáo hoàn chỉnh và slide thuyết trình (Tuần 13 – 14).**

---

## 4. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Bảng kết quả đánh giá sơ bộ mô hình baseline và kế hoạch cải thiện Giai đoạn 2.
  - [x] **Báo cáo tiến độ thực hiện đồ án Giai đoạn 1 đã nộp đúng hạn Tuần 8** (đảm bảo hoàn thành chuẩn đầu ra CLO2, CLO3 chiếm 20% điểm đồ án).
- **Kế hoạch Tuần 09 tiếp theo:** Bắt tay vào tinh chỉnh mô hình (`GridSearchCV`), kiểm định chéo Stratified 5-Fold CV và thực nghiệm giảm chiều dữ liệu PCA.
