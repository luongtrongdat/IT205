parking_lot = []
next_id = 1

MOTORBIKE_PRICE = 5000
CAR_PRICE = 10000


def find_vehicle(parking_lot, plate):
    """Tìm xe theo biển số."""
    for vehicle in parking_lot:
        if vehicle["plate"] == plate:
            return vehicle

    return None


def check_in(parking_lot, next_id):
    """Đăng ký xe vào bãi."""

    while True:
        plate = input("Nhập biển số: ").strip().upper()

        if plate == "":
            print("[Lỗi]: Biển số không được để trống!")
            continue

        if find_vehicle(parking_lot, plate) is not None:
            print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
            continue

        break

    while True:
        try:
            vehicle_type = int(
                input("Nhập loại xe (1: Xe máy, 2: Ô tô): ")
            )

            if vehicle_type not in [1, 2]:
                print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
                continue

            break

        except ValueError:
            print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")

    while True:
        try:
            entry_time = int(input("Nhập giờ vào (0-24): "))

            if 0 <= entry_time <= 24:
                break

            print("[Lỗi]: Giờ vào phải từ 0 đến 24!")

        except ValueError:
            print("[Lỗi]: Giờ vào phải là số nguyên!")

    vehicle = {
        "id": next_id,
        "plate": plate,
        "type": vehicle_type,
        "entry_time": entry_time
    }

    parking_lot.append(vehicle)

    print(f"[Thành công]: Xe {plate} đã được đăng ký vào bãi.")

    return next_id + 1


def display_vehicles(parking_lot):
    """Hiển thị danh sách xe."""

    if len(parking_lot) == 0:
        print("[Thông báo]: Bãi xe hiện đang trống.")
        return

    print("\n===== DANH SÁCH XE ĐANG ĐỖ =====")
    print(f"{'ID':<5}{'BIỂN SỐ':<15}{'LOẠI XE':<12}{'GIỜ VÀO':<10}")

    for vehicle in parking_lot:
        vehicle_name = "Xe máy"

        if vehicle["type"] == 2:
            vehicle_name = "Ô tô"

        print(
            f"{vehicle['id']:<5}"
            f"{vehicle['plate']:<15}"
            f"{vehicle_name:<12}"
            f"{vehicle['entry_time']:<10}"
        )

    print("=" * 42)


def search_vehicle(parking_lot):
    """Tìm kiếm xe."""

    plate = input("Nhập biển số cần tìm: ").strip().upper()

    vehicle = find_vehicle(parking_lot, plate)

    if vehicle is None:
        print(f"[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")
        return

    vehicle_name = "Xe máy"

    if vehicle["type"] == 2:
        vehicle_name = "Ô tô"

    print("\n===== THÔNG TIN XE =====")
    print(vehicle)
    print("Loại xe:", vehicle_name)


def check_out(parking_lot):
    """Xe ra bãi."""

    plate = input("Nhập biển số cần check-out: ").strip().upper()

    vehicle = find_vehicle(parking_lot, plate)

    if vehicle is None:
        print(f"[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")
        return

    while True:
        try:
            exit_time = int(input("Nhập giờ ra (0-24): "))

            if not (0 <= exit_time <= 24):
                print("[Lỗi]: Giờ ra phải từ 0 đến 24!")
                continue

            if exit_time < vehicle["entry_time"]:
                print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
                continue

            break

        except ValueError:
            print("[Lỗi]: Giờ ra phải là số nguyên!")

    duration = exit_time - vehicle["entry_time"]

    if vehicle["type"] == 1:
        price_per_hour = MOTORBIKE_PRICE
    else:
        price_per_hour = CAR_PRICE

    fee = duration * price_per_hour

    parking_lot.remove(vehicle)

    print("\n===== HÓA ĐƠN THANH TOÁN =====")
    print("Biển số:", plate)
    print("Số giờ gửi:", duration)
    print("Tổng phí:", fee, "VNĐ")
    print(f"[Thành công]: Xe {plate} đã check-out khỏi bãi.")


while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Check-in")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out")
    print("5. Thoát chương trình")
    print("================================")

    try:
        choice = int(input("Chọn chức năng (1-5): "))

    except ValueError:
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue

    if choice == 1:
        next_id = check_in(parking_lot, next_id)

    elif choice == 2:
        display_vehicles(parking_lot)

    elif choice == 3:
        search_vehicle(parking_lot)

    elif choice == 4:
        check_out(parking_lot)

    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")