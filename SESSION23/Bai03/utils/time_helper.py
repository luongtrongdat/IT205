# *** Chức năng 3: Tính thời gian hạ cánh dự kiến (ETA)
from datetime import datetime, timedelta
# hàm phụ trợ tìm id
from core.manager import find_flight_by_id


format_time = "%Y-%m-%d %H:%M:%S"


print(f"{' TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) '.center(40, "-")}")


def calculate_arrive_predict_time(flights: list):
    while True:
        flight_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
        index = find_flight_by_id(flight_id, flights)
        if not flight_id:
            print("Không được để trống!")
            continue

        if index == -1:
            print(f"Không tìm thấy id: {flight_id}")
            return
        break

    # tính toán thời gian hạ cánh
    depart_time = datetime.strptime(flights[index]['depart_time'], format_time)

    landing_time = depart_time + \
        timedelta(minutes=flights[index]['duration_min'])

    print(
        f"-> Chuyến bay {flight_id} cất cánh lúc: {flights[index]['depart_time']}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {landing_time}")
