# module thực hiện chức năng duyệt qua và in ra danh sách
import math


def display_flights(flights: list):
    print(f"{' DANH SÁCH CHUYẾN BAY & HẬU CẦN '.center(40, "-")}")

    for position, flight in enumerate(flights, start=1):
        print(
            f"{position}. Mã: {flight['flight_id']} | Khởi hành: {flight['depart_time']} | Số khách: {flight['passengers']} | Dự phòng: {math.ceil((flight['passengers']) / 10)} thùng nước")
