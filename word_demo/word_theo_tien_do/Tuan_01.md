# BÁO CÁO TIẾN ĐỘ TUẦN 01 — ĐĂNG KÝ ĐỀ TÀI, THÀNH LẬP NHÓM & LẬP KẾ HOẠCH 15 TUẦN

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Khởi động đồ án
- **Liên hệ Rubric:** Tham gia tổ chức và phối hợp làm việc trong nhóm (PLO6 / CLO3 — Trọng số: 10% / Điểm: 1.0)
- **Trạng thái:** Hoàn thành 100%

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 1)
1. **Đăng ký đề tài:** Chọn và đăng ký chính thức Đề tài 04 trong danh sách gợi ý của Bộ môn Khoa học Dữ liệu – HUIT: bài toán phân lớp chẩn đoán bệnh thận mãn tính (`akshayksingh/kidney-disease-dataset`), được giảng viên phê duyệt trên Google Classroom.
2. **Thành lập nhóm và phân công vai trò:**
   - Quy mô: Nhóm 5 sinh viên chính thức.
   - Thống nhất cơ chế phối hợp: Bầu Võ Tấn Đạt làm Nhóm trưởng, điều phối tiến độ chung.
   - Phân chia vai trò rõ ràng, công bằng theo năng lực chuyên môn để bảo đảm điểm số thành viên minh bạch.
3. **Lập kế hoạch làm việc chi tiết cho 15 tuần:**
   - Xây dựng lộ trình bám sát 2 mốc nộp bắt buộc: Tuần 8 (Báo cáo tiến độ Giai đoạn 1 — 20%) và Tuần 14 (Báo cáo hoàn chỉnh Giai đoạn 2 — 80%).
   - Thiết lập hạ tầng làm việc: Kho lưu trữ mã nguồn chung, phân vùng thư mục chuẩn và thư mục Google Drive đồng bộ dữ liệu.

---

## 2. Bảng Phân Công Vai Trò & Trách Nhiệm 5 Thành Viên

| STT | Họ và Tên | Mã Số Sinh Viên | Vai Trò Đảm Nhiệm | Nhiệm Vụ Trọng Tâm Trong 15 Tuần |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Võ Tấn Đạt** *(Trưởng Nhóm)* | `2045240050` | Quản lý dự án & Kiến trúc hệ thống | Quản lý tiến độ 15 tuần, thiết kế kiến trúc 3 tầng, đóng gói Pipeline `.joblib`, biên tập báo cáo tổng hợp và điều phối bảo vệ. |
| 2 | **Triệu Thị Thu Ngân** | `2405240179` | Phân tích & Trực quan hóa dữ liệu | Thu thập dữ liệu $N=400, D=24$, kiểm toán chất lượng dữ liệu, thực hiện EDA và xuất bộ 4 biểu đồ phân tích. |
| 3 | **Vũ Thế Quang** | `2045240253` | Tiền xử lý dữ liệu & Đảm bảo chất lượng | Kiểm toán dữ liệu đầu vào, thiết kế quy trình tiền xử lý chống Data Leakage (`ColumnTransformer`), chuẩn hóa Z-Score và xây dựng 17 Unit Tests tự động. |
| 4 | **Nguyễn Đình Bảo Tấn** | `2405240270` | Nghiên cứu thuật toán & Huấn luyện mô hình | Nghiên cứu toán học 6 thuật toán & PCA, huấn luyện Baseline, tinh chỉnh `GridSearchCV`, 5-Fold Cross-Validation và phân tích lỗi. |
| 5 | **Nguyễn Thanh Nhàn** | `2405240198` | Phát triển ứng dụng Web & XAI | Lập trình ứng dụng Web Flask **HUIT Hospital CDSS**, trực quan hóa giao diện tương tác Chart.js, tích hợp khối XAI và eGFR MDRD KDIGO 2024. |

---

## 3. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Đề tài 04 đã đăng ký thành công trên Google Classroom và được GV duyệt.
  - [x] Bản kế hoạch làm việc chi tiết 15 tuần của nhóm gắn với chuẩn đầu ra CLO và Rubric 8 tiêu chí.
- **Kế hoạch Tuần 02 tiếp theo:** Tìm hiểu lý thuyết các thuật toán học máy phân lớp chủ lực (Logistic Regression, Random Forest, SVM) và đọc tài liệu chuyên ngành KDIGO.
