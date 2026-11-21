# BÁO CÁO TIẾN ĐỘ TUẦN 14 — HOÀN THIỆN BÁO CÁO, SLIDE & NỘP HỒ SƠ HOÀN CHỈNH GIAI ĐOẠN 2

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** ★ **MỐC BẮT BUỘC GIAI ĐOẠN 2 — Nộp Báo Cáo Hoàn Chỉnh (Tuần 14)**
- **Liên hệ Rubric:** Đánh giá toàn diện theo **CLO1, CLO2, CLO3, CLO4 (Chiếm 80% tổng điểm đồ án)**, bao gồm toàn bộ 8 tiêu chí chấm điểm của Rubric.
- **Thành viên chủ trì:** Võ Tấn Đạt (`2045240050`) & Toàn bộ 5 thành viên nhóm
- **Trạng thái:** Hoàn thành 100% — Đã nộp đầy đủ hồ sơ theo quy định

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 14)
1. **Hoàn thiện báo cáo cuối cùng:**
   - Rà soát toàn bộ lỗi chính tả, kiểm tra định dạng trang, phông chữ chuẩn (Times New Roman), căn lề 1 inch chuẩn học thuật, số thứ tự hình vẽ và bảng biểu.
   - Xuất tài liệu ra các định dạng chuẩn theo yêu cầu: file Word (`Bao_Cao_Do_An_CKD.docx`, `Bao_Cao_Tien_Do_15_Tuan_CKD.docx`) và file PDF hoàn chỉnh.
2. **Chuẩn bị slide thuyết trình:**
   - Xây dựng bộ trình chiếu PowerPoint 14 slide tinh gọn, cô đọng nội dung, làm nổi bật các đóng góp kỹ thuật cốt lõi và hình ảnh trực quan sinh động.
   - Biên soạn kịch bản phân vai thuyết trình chi tiết cho 5 thành viên nhóm trong khung thời gian 12–14 phút.
3. **NỘP BÁO CÁO HOÀN CHỈNH — Giai đoạn 2:**
   - Nộp đầy đủ bộ hồ sơ gồm 5 sản phẩm bắt buộc theo Mục II.4 văn bản của Bộ môn KHDL – HUIT.

---

## 2. Bảng Kiểm Tra Bộ Hồ Sơ Sản Phẩm Nộp Giai Đoạn 2 (Checklist Đạt Chuẩn)

Theo quy định tại Mục II.4 (Sản phẩm cần nộp) và Mục IV (Kế hoạch thực hiện Tuần 14): Nhóm phải nộp đầy đủ bộ hồ sơ hoàn chỉnh vào Tuần 14.

| STT | Sản Phẩm Cần Nộp (Quy Định HUIT) | Tệp Mã Nguồn / Báo Cáo Thực Tế | Tình Trạng | Đánh Giá Đáp Ứng |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **File code (Jupyter Notebook/.py)**<br>Huấn luyện mô hình có chú thích rõ ràng | • `notebooks/Kidney_Disease_EDA_and_Modeling.ipynb`<br>• `src/*.py` | **ĐẠT 100%** | Code sạch sẽ, 36 cells chạy tuần tự từ đầu đến cuối không lỗi, chú thích Markdown song ngữ rõ ràng. |
| **2** | **File mô hình đã huấn luyện và lưu lại**<br>(Định dạng phù hợp: `.joblib`) | • `models/kidney_disease_pipeline.joblib`<br>• `models/model_metadata.json` | **ĐẠT 100%** | Mô hình nguyên khối (Preprocessor + Random Forest), load lại và suy luận tức thì. |
| **3** | **Mã nguồn & hướng dẫn chạy ứng dụng**<br>Minh họa trên ít nhất 1 nền tảng | • `src/app.py`, `templates/`, `static/`<br>• `README.md` | **ĐẠT 100%** | Ứng dụng Web Flask hoàn chỉnh, có hướng dẫn cài đặt và chạy chi tiết từng bước. |
| **4** | **Báo cáo (Word/PDF)**<br>Theo đúng cấu trúc 12 mục ở Mục II.3 | • `Bao_Cao_Do_An_CKD.docx`<br>• `Bao_Cao_Tien_Do_15_Tuan_CKD.docx`<br>• `word_demo/*.md` | **ĐẠT 100%** | Đúng 12 mục, căn lề chuẩn, font Times New Roman, không lỗi chính tả, có mục lục & hình vẽ. |
| **5** | **Slide thuyết trình** | • `markdown/05_Kich_Ban_Thuyet_Trinh_Va_Slide_Bao_Ve.md`<br>• File Slide PowerPoint | **ĐẠT 100%** | Bộ 14 slide trực quan, có biểu đồ và giao diện thực tế. |

---

## 3. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Báo cáo hoàn chỉnh (không lỗi chính tả, đúng cấu trúc 12 mục).
  - [x] Slide thuyết trình 14 trang.
  - [x] **Đã nộp đầy đủ trọn bộ hồ sơ theo quy định vào Tuần 14** (Đảm bảo đánh giá Giai đoạn 2: CLO1–4 chiếm 80% điểm đồ án).
- **Kế hoạch Tuần 15 tiếp theo:** Chạy tổng duyệt thuyết trình đúng khung thời gian quy định, chuẩn bị trang thiết bị máy chiếu và ôn luyện bộ câu hỏi phản biện bảo vệ trước Hội đồng.
