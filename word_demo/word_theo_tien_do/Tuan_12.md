# BÁO CÁO TIẾN ĐỘ TUẦN 12 — HOÀN THIỆN ỨNG DỤNG MINH HỌA (HUIT HOSPITAL CDSS) & KIỂM THỬ

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Giai đoạn 2 (Tuần 11–12)
- **Liên hệ Rubric:** Xây dựng ứng dụng — Hoàn thiện (PLO2 / CLO1 — Trọng số: 20% / Điểm: 2.0)
- **Thành viên chủ trì:** Nguyễn Thanh Nhàn (`2405240198`) & Vũ Thế Quang (`2045240253`)
- **Trạng thái:** Hoàn thành 100%

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 12)
1. **Hoàn thiện giao diện và chức năng ứng dụng minh họa:**
   - Xây dựng hoàn chỉnh giao diện chuyên nghiệp cho hệ thống **HUIT Hospital CDSS** (*Clinical Decision Support System*).
   - Tích hợp 5 hồ sơ bệnh nhân mẫu đa dạng trường hợp lâm sàng do 5 thành viên nhóm trực tiếp phụ trách.
   - Trực quan hóa kết quả dự đoán bằng thư viện Chart.js hoạt động ngoại tuyến (Offline 100%): Đồng hồ đo rủi ro Half-Gauge, Biểu đồ mạng nhện Radar so sánh và Bảng đối chiếu 24 chỉ số lâm sàng.
   - Tích hợp khối **Explainable AI (XAI)** đối chiếu ngưỡng lâm sàng WHO/KDIGO 2024 và tự động tính tốc độ lọc cầu thận ước tính (**eGFR theo công thức MDRD**) phân giai đoạn suy thận từ G1 đến G5.
2. **Kiểm thử ứng dụng với nhiều trường hợp dữ liệu đầu vào khác nhau:**
   - Kiểm thử các trường hợp dữ liệu bình thường, dữ liệu bệnh nhân nặng, dữ liệu thiếu nhiều trường và dữ liệu ngoại lai cực trị.
   - Tự động hóa kiểm thử bằng bộ **17 ca kiểm thử đơn vị (Unit Tests)** chuẩn unittest của Python.

---

## 2. Các Chức Năng Nổi Bật Của Ứng Dụng HUIT Hospital CDSS

### 2.1. Trạm tiếp nhận bệnh án điện tử (EMR Station)
- Biểu mẫu nhập liệu 24 chỉ số lâm sàng phân theo 5 tab trực quan, có giá trị gợi ý và kiểm tra ràng buộc nhập liệu.
- Tích hợp sẵn 5 ca bệnh mẫu để bác sĩ thử nghiệm nhanh với 1 cú click chuột:
  - Ca 1: Bệnh nhân suy thận giai đoạn cuối ($P > 95\%$).
  - Ca 2: Người khỏe mạnh bình thường ($P < 5\%$).
  - Ca 3: Người cao tuổi có bệnh nền tăng huyết áp ($P \approx 50\%$).
  - Ca 4: Bệnh nhân thiếu máu nặng ($P > 85\%$).
  - Ca 5: Bệnh nhân viêm cầu thận cấp tính ($P > 90\%$).

### 2.2. Khối chẩn đoán thông minh, XAI & eGFR MDRD KDIGO 2024
- **Đồng hồ bán nguyệt (Half-Gauge):** Hiển thị xác suất rủi ro $P(\text{CKD})$ với dải màu cảnh báo Xanh lá ($<30\%$), Vàng cam ($30-70\%$), Đỏ ($>70\%$).
- **Tính toán eGFR tự động (MDRD Study Equation):**
  $$\text{eGFR} = 175 \times (\text{SC})^{-1.154} \times (\text{Age})^{-0.203} \times (0.742 \text{ nếu Nữ})$$
  Tự động xếp loại giai đoạn suy thận: G1 (Bình thường $\ge 90$), G2 (Giảm nhẹ $60-89$), G3a/G3b (Giảm trung bình $30-59$), G4 (Giảm nặng $15-29$), G5 (Suy thận giai đoạn cuối $<15\text{ mL/min/1.73m}^2$).
- **Giải trình XAI:** Liệt kê các chỉ số vượt ngưỡng nguy cơ xếp theo mức độ ảnh hưởng của Random Forest.

### 2.3. Dataset Explorer 400 ca bệnh
- Tích hợp màn hình khám phá toàn bộ 400 ca bệnh án với tính năng tìm kiếm, phân trang và xem chi tiết ngay trên giao diện Web.

---

## 3. Kết Quả Kiểm Thử Toàn Diện (Bộ 17 Unit Tests Tự Động)

Nhóm đã xây dựng bộ 17 ca kiểm thử đơn vị trong thư mục `test/` và thực thi tự động qua dòng lệnh:

```powershell
python -B -m unittest discover -s test -p "MainTest_*.py" -v
```

| Tệp Kiểm Thử | Số Lượng Test | Nội Dung Kiểm Thử | Kết Quả |
| :--- | :---: | :--- | :---: |
| `MainTest_0_Preprocess.py` | 5 tests | Kiểm tra làm sạch, kiểm toán `duplicated`/`nunique`/`id`, `eda_summary`, đối chiếu `24 -> 35` chiều (`0 NaN`) và chống Data Leakage | **PASSED (5/5)** |
| `MainTest_1_ModelMetrics.py` | 1 test | Kiểm tra huấn luyện, lưu/load tệp `.joblib`, kiểm chứng Recall $\ge 96\%$, F1 $\ge 95\%$ và ROC-AUC $\ge 0.98$ | **PASSED (1/1)** |
| `MainTest_2_XAI_Explain.py` | 2 tests | Kiểm tra khối XAI sinh cảnh báo Creatinine cao ($> 1.4\text{ mg/dL}$) và Albumin niệu ($\text{al} \ge 1$) | **PASSED (2/2)** |
| `MainTest_3_StressTest.py` | 2 tests | Kiểm thử lập trình phòng thủ: Dữ liệu khuyết 21/24 trường và payload hoàn toàn rỗng (`{}`) | **PASSED (2/2)** |
| `MainTest_4_ClinicalBenchmarks.py` | 7 tests | Kiểm chuẩn 24 ngưỡng sinh lý KDIGO 2024, API `/api/benchmarks`, `/api/dataset`, `/api/predict` và `detailed_xai` | **PASSED (7/7)** |
| **TỔNG CỘNG** | **17 tests** | **Thời gian thực thi: < 1 giây — Tỷ lệ đạt: 100% (0 lỗi, 0 cảnh báo)** | **OK (17/17)** |

---

## 4. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Ứng dụng minh họa hoàn chỉnh, chạy ổn định trên nền tảng Web Flask tại `http://127.0.0.1:5000`.
  - [x] Bộ mã nguồn ứng dụng tổ chức sạch sẽ trong thư mục `src/`, giao diện HTML/CSS/JS tại `templates/` và `static/`.
  - [x] Kết quả kiểm thử với nhiều trường hợp dữ liệu đạt 100% (17/17 Unit Tests pass).
- **Kế hoạch Tuần 13 tiếp theo:** Viết bản nháp báo cáo tổng hợp đầy đủ theo cấu trúc 12 mục yêu cầu và rà soát số liệu.
