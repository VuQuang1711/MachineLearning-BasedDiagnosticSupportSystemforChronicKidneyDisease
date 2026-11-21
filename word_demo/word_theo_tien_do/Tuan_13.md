# BÁO CÁO TIẾN ĐỘ TUẦN 13 — VIẾT BẢN NHÁP BÁO CÁO 12 MỤC & RÀ SOÁT NỘI DUNG

- **Đề tài:** Đề tài số 04 — Hệ Thống Máy Học Hỗ Trợ Chẩn Đoán Bệnh Thận Mãn Tính (Chronic Kidney Disease — CKD)
- **Lớp:** `15DHKHDL04` — **GVHD:** ThS. Nguyễn Thị Huyền Trang
- **Giai đoạn:** Giai đoạn 2 (Tuần 13–14)
- **Liên hệ Rubric:** Hình thức trình bày bài báo cáo — Phần chuẩn bị (PLO6 / CLO3 — Trọng số: 10% / Điểm: 1.0)
- **Thành viên chủ trì:** Võ Tấn Đạt (`2045240050`) & Toàn bộ 5 thành viên nhóm
- **Trạng thái:** Hoàn thành 100%

---

## 1. Nội Dung Công Việc Thực Hiện (Theo Yêu Cầu Kế Hoạch Tuần 13)
1. **Viết báo cáo (bản nháp):**
   - Tổng hợp toàn diện toàn bộ kết quả của 12 tuần thực hiện: Cơ sở lý thuyết toán học, dữ liệu và trực quan hóa EDA, quy trình tiền xử lý chống rò rỉ dữ liệu, kết quả thực nghiệm 6 mô hình baseline, tinh chỉnh `GridSearchCV`, kiểm tra chéo 5-Fold CV, giảm chiều PCA, đóng gói `.joblib` và ứng dụng Web CDSS.
   - Biên soạn theo **đúng cấu trúc 12 mục** quy định tại Mục II.3 trong văn bản của Bộ môn KHDL – HUIT:
     1. Trang bìa (Tên đề tài, danh sách thành viên, phân công công việc)
     2. Mục lục
     3. Giới thiệu đề tài (Bối cảnh, mục tiêu, phạm vi bài toán)
     4. Cơ sở lý thuyết (Mô tả các thuật toán sử dụng, có ví dụ minh họa)
     5. Mô tả và trực quan hóa bộ dữ liệu (Nguồn, số lượng mẫu, đặc trưng, thống kê mô tả)
     6. Tiền xử lý dữ liệu (Các bước thực hiện, lý do lựa chọn phương pháp)
     7. Xây dựng, huấn luyện và tinh chỉnh mô hình (Thuật toán, tham số, so sánh baseline và hoàn thiện)
     8. Kết quả và đánh giá mô hình (Bảng kết quả, phân tích, nhận xét)
     9. Xây dựng ứng dụng minh họa (Nền tảng, chức năng, hướng dẫn sử dụng, hình ảnh minh họa)
     10. Kết luận (Tóm tắt kết quả, hạn chế, hướng phát triển)
     11. Tài liệu tham khảo
     12. Phụ lục (Bảng phân công chi tiết, hướng dẫn cài đặt/chạy ứng dụng)
2. **Rà soát nội dung, đảm bảo đúng cấu trúc yêu cầu:**
   - Đối chiếu chéo số liệu giữa Notebook, mã nguồn Python, biểu đồ xuất ra và bản nháp báo cáo để bảo đảm tính chính xác và nhất quán 100%.

---

## 2. Kết Quả Biên Soạn Bản Nháp Báo Cáo 12 Mục

Nhóm đã hoàn thành việc biên soạn hệ thống báo cáo thành 7 tệp Markdown tương ứng với các chương chuẩn tại thư mục `word_demo/`:

| Tệp Báo Cáo | Chương / Mục Tương Ứng | Nội Dung Cốt Lõi |
| :--- | :--- | :--- |
| `00_Trang_Bia_Phan_Cong_Muc_Luc.md` | Mục 1, 2 | Trang bìa đại học chuẩn HUIT, bảng phân công 5 thành viên (RACI), Mục lục và Danh mục 10 hình vẽ, 5 bảng biểu. |
| `01_Chuong_1_Gioi_Thieu_Bai_Toan.md` | Mục 3 | Tính cấp thiết của chẩn đoán CKD sớm, 5 nhóm chỉ số lâm sàng, mục tiêu định lượng (Recall $\ge 96\%$) và phạm vi đề tài. |
| `02_Chuong_2_Co_So_Ly_Thuyet.md` | Mục 4 | Toán học của 6 thuật toán phân lớp + PCA + **Bộ 3 ví dụ tính toán thủ công từng bước**. |
| `03_Chuong_3_Du_Lieu_Va_Tien_Xu_Ly.md` | Mục 5, 6 | Nguồn Apollo/UCI ($N=400, D=24$), 4 biểu đồ EDA, nguyên lý chống Data Leakage, cấu trúc `ColumnTransformer`, Z-Score. |
| `04_Chuong_4_Ket_Qua_Baseline_Va_Danh_Gia.md` | Mục 7, 8 (Phần 1) | So sánh 6 mô hình Baseline, phân tích lý do chọn Random Forest, kết quả kiểm tra chéo Stratified 5-Fold CV và thực nghiệm PCA. |
| `05_Chuong_5_Toi_Uu_Hoa_Va_Trien_Khai_Ung_Dung.md` | Mục 7, 8 (Phần 2), Mục 9 | Tinh chỉnh `GridSearchCV` (`criterion='entropy'`), đánh giá Test (Accuracy 96.25%, Recall 96.00%), Error Analysis, Feature Importance, đóng gói `.joblib` (`187.43 KB`), kiến trúc Web 3 tầng và bộ 17 Unit Tests. |
| `06_Chuong_6_Ket_Luan_Va_Tai_Lieu_Tham_Khao.md` | Mục 10, 11, 12 | Đánh giá đóng góp, hạn chế, hướng mở rộng, danh mục tài liệu tham khảo chuẩn IEEE và Phụ lục hướng dẫn chạy lệnh. |

---

## 3. Sản Phẩm Cần Đạt & Mức Độ Hoàn Thành
- **Sản phẩm theo quy định:**
  - [x] Bản nháp báo cáo hoàn chỉnh đầy đủ các phần chính theo cấu trúc 12 mục.
  - [x] Bảng số liệu được rà soát đồng bộ tuyệt đối giữa code và báo cáo.
- **Kế hoạch Tuần 14 tiếp theo:** Hoàn thiện báo cáo cuối cùng, rà soát lỗi chính tả/định dạng, chuẩn bị slide thuyết trình và **NỘP BÁO CÁO HOÀN CHỈNH — Giai đoạn 2 (80% điểm đồ án)**.
