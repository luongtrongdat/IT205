"""File điều hướng chính phối hợp phân hệ quản lý Rikkei Logistics."""

import datetime

# Import tường minh từ các package và module tự xây dựng
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
from utils.helper import create_log_dir

# Bộ dữ liệu giả lập các chuyến xe đẩy về hệ thống
shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285, "from_lon": 105.8542,
        "to_lat": 10.8231, "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285, "from_lon": 105.8542,
        "to_lat": 16.0544, "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    },
]


def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

    # Gọi hàm an toàn kiểm tra và tạo thư mục logs
    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)

    for s in shipments:
        # 1. Gọi module tính khoảng cách Haversine chuẩn xác
        distance = calculate_distance(
            s["from_lat"], s["from_lon"],
            s["to_lat"], s["to_lon"]
        )

        # 2. Gọi module dự báo thời gian ETA
        eta = predict_eta(s["depart"], distance, speed=60.0)

        # 3. Ép kiểu hạn chót (deadline) để so sánh đối chiếu logic thời gian
        deadline_time = datetime.datetime.strptime(
            s["deadline"], "%Y-%m-%d %H:%M:%S")

        # Phân loại trạng thái giao hàng dựa trên đối tượng datetime
        if eta <= deadline_time:
            status = "🟢 AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            status = f"🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_time.strftime('%H:%M:%S')})"

        # Hiển thị kết quả nghiệm thu ra màn hình Terminal
        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" + Trạng thái: {status}\n")

    print("=" * 56)


if __name__ == "__main__":
    main()
