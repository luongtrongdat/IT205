"""Module xử lý tính toán khoảng cách địa lý toàn cầu."""

import math


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Tính toán khoảng cách đường chim bay giữa 2 điểm dựa trên công thức Haversine.

    Đơn vị trả về: Kilomet (km).
    """
    # Bán kính Trái Đất trung bình (km)
    earth_radius = 6371.0

    # Chuyển đổi tọa độ từ độ (Degree) sang Radian
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    # Áp dụng công thức hình học Haversine để triệt tiêu sai số bề mặt cong
    a = (math.sin(d_lat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius * c
