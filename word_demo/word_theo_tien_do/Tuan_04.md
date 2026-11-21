# BÁO CÁO TIẾN ĐỘ TUẦN 04 — THU THẬP & MÔ TẢ ĐẶC TRƯNG BỘ DỮ LIỆU

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Giai đoạn 1 (Tuần 4–5)
- **Liên hệ Rubric:** Thu thập dữ liệu, trực quan hóa dữ liệu — Phần thu thập dữ liệu (PLO2 / CLO1 — Trọng số: 10% / Điểm: 1.0)
- **Thành viên chủ trì:** Triệu Thị Thu Ngân (`2405240179`)
- **Trạng thái:** Hoàn thành 100%

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 4)
1. **Tìm bộ dữ liệu phù hợp với bài toán:**
   - Khảo sát và tải về bộ dữ liệu chẩn đoán bệnh thận mãn tính chính thức từ kho lưu trữ uy tín: Kaggle (`akshayksingh/kidney-disease-dataset`) có nguồn gốc từ Bệnh viện Apollo (Ấn Độ) công bố trên UCI Machine Learning Repository.
   - Kiểm tra và đảm bảo bộ dữ liệu khớp đúng với chủ đề Đề tài 04 đã được GV duyệt.
2. **Phân tích sơ bộ, mô tả các đặc trưng (feature) của dữ liệu:**
   - Thống kê quy mô tổng quan: Số dòng (bệnh nhân), số cột (thuộc tính xét nghiệm), kiểu dữ liệu nguyên thủy trong tệp CSV.
   - Lập bảng đặc tả y khoa cho 24 đặc trưng đầu vào, phân nhóm thành 5 nhóm chỉ số lâm sàng (Thông tin chung, Huyết áp, Chức năng thận & Điện giải, Huyết học tế bào máu, Bệnh sử kết hợp).
   - Rà soát các bất thường thô trong dữ liệu thô (chuỗi ký tự rác, định dạng số bị lỗi do dấu cách/tab).

---

## 2. Kết Quả Thu Thập & Thống Kê Tổng Quan Dữ Liệu

| Chỉ Số Thống Kê | Chi Tiết Ghi Nhận | Ý Nghĩa / Đánh Giá |
| :--- | :--- | :--- |
| **Nguồn dữ liệu** | UCI / Kaggle (`kidney_disease.csv`) | Thu thập tại bệnh viện lâm sàng thực tế |
| **Kích thước dữ liệu thô** | **400 dòng $\times$ 26 cột** | Gồm 400 ca bệnh nhân, 1 cột ID, 24 đặc trưng lâm sàng và 1 cột nhãn |
| **Phân loại đặc trưng** | **11 biến định lượng** (Continuous)<br>**13 biến định tính** (Categorical) | Biến định lượng: `age`, `bp`, `bgr`, `bu`, `sc`, `sod`, `pot`, `hemo`, `pcv`, `wc`, `rc`<br>Biến định tính: `sg`, `al`, `su`, `rbc`, `pc`, `pcc`, `ba`, `htn`, `dm`, `cad`, `appet`, `pe`, `ane` |
| **Nhãn mục tiêu (`classification`)** | 250 ca `ckd` (62.5%)<br>150 ca `notckd` (37.5%) | Bài toán phân lớp nhị phân có độ mất cân bằng nhẹ, không cần áp dụng kỹ thuật tạo mẫu tổng hợp SMOTE |
| **Chất lượng dữ liệu thô** | Sau ép kiểu chuẩn: **24/24 cột** bị khuyết giá trị (tổng **`1,012 / 9,600` ô `NaN` = `10.54%`**) | Cần phương pháp điền khuyết (Imputation) phù hợp, không được xóa dòng |
| **Kiểm toán toàn vẹn (Audit)** | **0 dòng trùng lặp** (`duplicated=0`), **0 cột hằng số** (`nunique<=1`), cột `id` có `400/400` giá trị duy nhất | Chứng minh không có dữ liệu trùng/vô nghĩa; loại bỏ cột định danh `id` để tránh học vẹt |
| **Bất thường kiểu dữ liệu** | Ký tự ẩn `\t?`, `\tno`, `\tyes`, `ckd\t` | Làm cho 3 cột số thực (`pcv`, `wc`, `rc`) bị pandas đọc nhầm thành kiểu `object` |

---

## 3. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Bộ dữ liệu đã được xác nhận và đồng bộ tại `DatasetForProject/MLDataset/kidney_disease.csv`.
  - [x] Tài liệu mô tả tổng quan về dữ liệu (số dòng, số đặc trưng, kiểu dữ liệu, ý nghĩa y học của 24 thuộc tính) lưu tại `data/mo-ta-bo-du-lieu-benh-than-ckd.md` và `word_demo/03_Chuong_3_Du_Lieu_Va_Tien_Xu_Ly.md`.
- **Kế hoạch Tuần 05 tiếp theo:** Trực quan hóa dữ liệu đa biến (EDA), phát hiện bất thường và viết nhận xét sơ bộ để định hướng cho khâu tiền xử lý dữ liệu.
