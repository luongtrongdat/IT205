from datetime import datetime, timedelta


def predict_eta(departure_str, distance_km, speed=60):
    """
    Tính thời gian dự kiến đến nơi (ETA).
    """

    depart_time = datetime.strptime(
        departure_str,
        "%Y-%m-%d %H:%M:%S"
    )

    hours_needed = distance_km / speed

    eta = depart_time + timedelta(hours=hours_needed)

    return eta