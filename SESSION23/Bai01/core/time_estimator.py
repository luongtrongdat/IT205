"""Module dự đoán thời gian di chuyển của các chuyến xe hành trình."""

import datetime


def predict_eta(departure_str: str, distance_km: float, speed: float = 60.0) -> datetime.datetime:
    """Tính toán thời gian dự kiến đến nơi (ETA) dựa trên vận tốc vận chuyển hành trình."""
    # Ép kiểu chuỗi string cấu trúc chuẩn sang đối tượng datetime chuyên dụng
    dep_time = datetime.datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")

    # Tính toán số giờ di chuyển cần thiết
    hours_needed = distance_km / speed

    # Cộng dồn thời gian bằng cách dùng timedelta
    eta = dep_time + datetime.timedelta(hours=hours_needed)
    return eta
