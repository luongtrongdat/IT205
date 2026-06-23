# *** Chức năng 2: Tiếp nhận chuyến bay mới

from datetime import datetime

# helper function

# kiểm tra ngày giờ đúng định dạng


def is_valid_date(depart_time: str) -> bool:
    format = "%Y-%m-%d %H:%M:%S"

    try:
        datetime.strptime(depart_time, format)
        return True
    except ValueError:
        return False


# kiểm tra id trùng

def check_duplicate_id(flight_id: str, flights: list) -> bool:
    for flight in flights:
        if flight['flight_id'] == flight_id:
            return True
    return False


# tìm chuyến bay theo mã
def find_flight_by_id(flight_id: str, flights: list) -> int:
    for index, flight in enumerate(flights):
        if flight['flight_id'] == flight_id:
            return index
    return -1


# chức năng nhập chính
def add_flight(flights: list):

    # Nhập vào id chuyến bay
    while True:
        flight_id = input("Mã chuyến bay: ").strip().upper()

        if not flight_id:
            print("k được để trống!")
            continue

        # check trùng
        if check_duplicate_id(flight_id, flights):
            print(f"Trùng id: {flight_id}")
            continue
        break

    # nhập ngày giờ khởi hành
    while True:
        depart_time = input("Thời gian khởi hành (YYYY-MM-DD HH:MM:SS): ")

        if not depart_time:
            print("K được để trống!")
            continue

        if not is_valid_date(depart_time):
            print("Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
            continue
        break

    # nhập số lượng hành khách
    while True:
        try:
            passengers = int(input("Nhập số hành khách: "))

            if passengers <= 0:
                print("Số lượng hành khách phải là số nguyên và lớn hơn 0")
                continue
            break
        except ValueError:
            print("Số lượng hành khách phải là số nguyên và lớn hơn 0")

    # nhập thời lượng
    while True:
        try:
            duration_mins = int(input("Nhập thời lượng bay: "))

            if duration_mins <= 0:
                print("thời lượng bay phải là số nguyên và lớn hơn 0")
                continue
            break
        except ValueError:
            print("thời lượng bay phải là số nguyên và lớn hơn 0")

    # nhập hợp lệ thì đóng gói thành 1 dict và thêm
    new_flight = {
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time,
        "duration_min": duration_mins
    }

    flights.append(new_flight)
    print(f"Thêm chuyến bay {flight_id} thành công!")
