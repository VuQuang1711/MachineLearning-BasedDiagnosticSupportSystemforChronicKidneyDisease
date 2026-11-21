# BÁO CÁO TIẾN ĐỘ TUẦN 11 — THIẾT KẾ KIẾN TRÚC & XÂY DỰNG ỨNG DỤNG MINH HỌA (GIAI ĐOẠN ĐẦU)

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Giai đoạn 2 (Tuần 11–12)
- **Liên hệ Rubric:** Xây dựng ứng dụng — Giai đoạn đầu (PLO2 / CLO1 — Trọng số: 20% / Điểm: 2.0)
- **Thành viên chủ trì:** Nguyễn Thanh Nhàn (`2405240198`) — *Hỗ trợ:* Võ Tấn Đạt (`2045240050`)
- **Trạng thái:** Hoàn thành 100%

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 11)
1. **Thiết kế và lựa chọn nền tảng ứng dụng minh họa:**
   - Lựa chọn nền tảng: Xây dựng **ứng dụng Web tương tác trên nền tảng Python Flask** kết hợp HTML5/CSS3/JavaScript hiện đại, cho phép truy cập linh hoạt qua trình duyệt máy tính và thiết bị di động mà không cần cài đặt phức tạp.
   - Thiết kế kiến trúc phần mềm sạch 3 tầng (3-Tier Clean Architecture) để tách bạch hoàn toàn giữa giao diện, nghiệp vụ máy học và cấu hình dữ liệu.
2. **Tích hợp bước đầu mô hình đã lưu vào ứng dụng:**
   - Xây dựng lớp trung gian nạp mô hình (`src/model_logic.py`) đọc tệp `models/kidney_disease_pipeline.joblib`.
   - Thiết lập các điểm cuối dịch vụ Web RESTful API (`/api/predict`, `/api/health`).
   - Xây dựng khung giao diện Web tiếp nhận thông tin bệnh nhân và gửi yêu cầu suy luận đến mô hình.

---

## 2. Kiến Trúc Ứng Dụng & Kết Quả Tích Hợp Ban Đầu

### 2.1. Thiết kế kiến trúc 3 tầng sạch (Clean Architecture)
- **Tầng 1 — Cấu hình & Dữ liệu (Data & Configuration Layer):**
  - `src/config.py`: Khai báo danh mục 24 biến, dải giá trị chuẩn y tế, đường dẫn tệp.
  - `src/data_loader.py`: Tải và tiền xử lý dữ liệu chuẩn hóa.
- **Tầng 2 — Xử lý nghiệp vụ máy học (Business Logic Layer):**
  - `src/model_logic.py`: Chứa lớp `CKDPredictor`, thực hiện nạp tệp `.joblib` dạng Singleton, tiếp nhận từ điển 24 trường dữ liệu thô, chuyển thành DataFrame và gọi `.predict()` / `.predict_proba()`.
  - `src/xai_explainer.py`: Khởi tạo module giải trình quyết định lâm sàng.
- **Tầng 3 — Trình diễn & Giao tiếp người dùng (Presentation Layer):**
  - `src/app.py`: Bộ định tuyến Flask xử lý các yêu cầu HTTP.
  - `templates/index.html` & `static/`: Giao diện Web tương tác.

### 2.2. Kiểm thử kết nối giữa Ứng dụng Web và Mô hình `.joblib`
- Nhóm đã khởi chạy thành công máy chủ Flask cục bộ tại địa chỉ `http://127.0.0.1:5000`.
- Kiểm thử luồng gửi nhận dữ liệu qua API:
  - Gửi dữ liệu JSON gồm 24 chỉ số lâm sàng qua phương thức `POST /api/predict`.
  - Mô hình `.joblib` tiếp nhận, tự động điền khuyết các trường còn trống, chuẩn hóa và trả về kết quả dự đoán cùng xác suất theo thời gian thực ($< 50\text{ ms}$).

---

## 3. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Khung ứng dụng minh họa ban đầu (nền tảng Web Flask) đã kết nối thành công với file model đã lưu.
  - [x] Giao diện nhập liệu ban đầu và các API cơ sở hoạt động ổn định.
- **Kế hoạch Tuần 12 tiếp theo:** Hoàn thiện toàn bộ giao diện và chức năng ứng dụng minh họa (**HUIT Hospital CDSS**), tích hợp khối XAI + eGFR KDIGO 2024 và kiểm thử ứng dụng với nhiều trường hợp dữ liệu khác nhau (17 Unit Tests).
