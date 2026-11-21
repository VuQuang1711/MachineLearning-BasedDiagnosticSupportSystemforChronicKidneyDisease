"""
src/app.py
Máy chủ Flask RESTful Web Server phục vụ API chẩn đoán bệnh thận.
"""

import sys
sys.dont_write_bytecode = True
from datetime import datetime, timezone
from pathlib import Path
from flask import Flask, jsonify, render_template, request

# Đảm bảo thư mục gốc dự án luôn nằm trong PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    from src.config import ALL_FEATURES, MODEL_PIPELINE_PATH
    from src.data_loader import CKDDataLoader
    from src.model_logic import CKDPredictor
except ModuleNotFoundError:
    from config import ALL_FEATURES, MODEL_PIPELINE_PATH
    from data_loader import CKDDataLoader
    from model_logic import CKDPredictor

app = Flask(
    __name__,
    template_folder=str(ROOT_DIR / "templates"),
    static_folder=str(ROOT_DIR / "static"),
)
app.config["TEMPLATES_AUTO_RELOAD"] = True

predictor = CKDPredictor()

# Bộ đệm dữ liệu 400 ca bệnh án gốc
_dataset_cache = None


def get_cached_dataset():
    global _dataset_cache
    if _dataset_cache is None:
        loader = CKDDataLoader()
        _dataset_cache = loader.get_raw_dataset_for_table()
    return _dataset_cache


# Khởi tạo mô hình khi server bật
try:
    predictor.load_model()
    print("[INFO] Đã nạp mô hình từ đĩa cứng thành công.")
except Exception:
    print("[WARN] Chưa có mô hình đã lưu! Tiến hành huấn luyện tự động từ file dữ liệu gốc...")
    loader = CKDDataLoader()
    df_clean = loader.load_and_clean_raw_data()
    X_train, X_test, y_train, y_test = loader.split_data(df_clean)
    predictor.train_and_save(X_train, y_train)


@app.route("/")
def index():
    """Hiển thị giao diện Web chính của bác sĩ."""
    return render_template("index.html")


@app.route("/api/health", methods=["GET"])
def health_check():
    """Endpoint kiểm tra trạng thái hoạt động của hệ thống."""
    return jsonify({
        "status": "healthy",
        "service": "Kidney Disease Diagnosis API (BT04)",
        "model_loaded": predictor.pipeline is not None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/api/benchmarks", methods=["GET"])
def get_benchmarks():
    """Endpoint trả về bảng giá trị khoảng chuẩn sinh lý người bình thường."""
    try:
        from src.config import CLINICAL_BENCHMARKS
    except ModuleNotFoundError:
        from config import CLINICAL_BENCHMARKS

    return jsonify({
        "status": "success",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data": CLINICAL_BENCHMARKS,
    })


@app.route("/api/dataset", methods=["GET"])
def get_dataset():
    """
    Endpoint trả về toàn bộ dữ liệu 400 ca bệnh án phục vụ Dataset Explorer.
    Hỗ trợ tìm kiếm, lọc theo nhãn phân loại (CKD / NotCKD) và phân trang mượt mà.
    """
    try:
        data = get_cached_dataset()
        records = data["records"]

        # 1. Lọc theo nhãn chẩn đoán thực tế
        filter_class = request.args.get("classification", "all").strip().lower()
        if filter_class in ["ckd", "notckd"]:
            filtered_records = [
                r for r in records if str(r.get("classification", "")).strip().lower() == filter_class
            ]
        else:
            filtered_records = records

        # 2. Tìm kiếm theo từ khóa (ID, tuổi, huyết áp, creatinine...)
        query = request.args.get("search", "").strip().lower()
        if query:
            filtered_records = [
                r for r in filtered_records
                if query in str(r.get("id", "")).lower()
                or query in str(r.get("age", "")).lower()
                or query in str(r.get("classification", "")).lower()
                or query in str(r.get("bp", "")).lower()
                or query in str(r.get("sc", "")).lower()
            ]

        # 3. Phân trang
        page = int(request.args.get("page", 1))
        page_size_param = request.args.get("page_size", "15").strip().lower()
        if page_size_param in ["all", "-1"]:
            page_size = len(filtered_records) if filtered_records else 15
            page = 1
        else:
            page_size = max(1, int(page_size_param))

        total_filtered = len(filtered_records)
        total_pages = max(1, (total_filtered + page_size - 1) // page_size) if page_size else 1
        page = min(max(1, page), total_pages)

        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paged_records = filtered_records[start_idx:end_idx]

        return jsonify({
            "status": "success",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "summary": {
                "total_count": data["total_count"],
                "ckd_count": data["ckd_count"],
                "notckd_count": data["notckd_count"],
                "ckd_pct": data["ckd_pct"],
                "notckd_pct": data["notckd_pct"],
            },
            "pagination": {
                "current_page": page,
                "page_size": page_size,
                "total_records": total_filtered,
                "total_pages": total_pages,
            },
            "records": paged_records,
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Lỗi nạp dữ liệu: {str(e)}"
        }), 500


@app.route("/api/predict", methods=["POST"])
def predict():
    """
    Endpoint tiếp nhận dữ liệu bệnh nhân và trả về chẩn đoán kèm XAI.
    """
    try:
        data = request.get_json(force=True)
        if not data or not isinstance(data, dict):
            return jsonify({
                "status": "error",
                "message": "Payload không hợp lệ! Vui lòng truyền JSON object chứa các thuộc tính lâm sàng."
            }), 400

        result = predictor.predict_single_patient(data)
        return jsonify({
            "status": "success",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "data": result,
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Lỗi hệ thống khi dự báo: {str(e)}"
        }), 500


if __name__ == "__main__":
    print("[HUIT HOSPITAL] Khởi động máy chủ Web tại http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
