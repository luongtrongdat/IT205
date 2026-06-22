import logging


def show_devices(devices):
    if len(devices) == 0:
        print("He thong chua co thiet bi nao!")
        return

    print("-" * 90)
    print(
        f"{'Ma':<8}{'Vi tri':<25}{'Chi so cu':<15}{'Chi so moi':<15}{'Trang thai':<15}"
    )
    print("-" * 90)

    for device in devices:
        print(
            f"{device['id']:<8}"
            f"{device['location']:<25}"
            f"{device['old_index']:<15}"
            f"{device['new_index']:<15}"
            f"{device['status']:<15}"
        )


def update_indices(devices):
    device_id = input("Nhap ma thiet bi: ").strip()

    for device in devices:
        if device["id"] == device_id:

            while True:
                try:
                    old_index = float(input("Nhap chi so cu: "))
                    if old_index < 0:
                        print("Chi so phai >= 0!")
                        continue
                    break
                except ValueError:
                    print("Du lieu khong hop le!")

            while True:
                try:
                    new_index = float(input("Nhap chi so moi: "))
                    if new_index < 0:
                        print("Chi so phai >= 0!")
                        continue

                    if new_index < old_index:
                        print("ERR-E02: Chi so moi khong duoc nho hon chi so cu!")
                        continue

                    break
                except ValueError:
                    print("Du lieu khong hop le!")

            device["old_index"] = old_index
            device["new_index"] = new_index

            logging.info(f"Cap nhat chi so cho thiet bi {device_id}")
            print("Cap nhat thanh cong!")
            return

    print("ERR-E01: Khong tim thay ma thiet bi!")


def activate_overload(devices):
    device_id = input("Nhap ma thiet bi can canh bao: ").strip()

    for device in devices:

        if device["id"] == device_id:

            if device["status"] == "Overload":
                print("ERR-E04: Thiet bi da o trang thai Overload!")
                return

            consumption = device["new_index"] - device["old_index"]

            if consumption > 5000:
                device["status"] = "Overload"
                logging.warning(
                    f"Thiet bi {device_id} vuot nguong 5000 kWh, chuyen sang Overload"
                )
                print("Kich hoat canh bao thanh cong!")
            else:
                print("Thiet bi chua vuot nguong 5000 kWh.")

            return

    print("ERR-E01: Khong tim thay ma thiet bi!")


def calculate_energy_financials(devices):
    total_consumption = 0

    for device in devices:
        total_consumption += device["new_index"] - device["old_index"]

    total_cost = total_consumption * 3000

    discount_percent = 0

    if total_consumption >= 50000:
        discount_percent = 3

    final_cost = total_cost * (1 - discount_percent / 100)

    return total_consumption, discount_percent, final_cost


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    devices = [
        {
            "id": "M01",
            "location": "Mechanical Shop A",
            "old_index": 1200,
            "new_index": 4500,
            "status": "Normal"
        },
        {
            "id": "M02",
            "location": "Assembly Line B",
            "old_index": 2300,
            "new_index": 8500,
            "status": "Overload"
        },
        {
            "id": "M03",
            "location": "Packaging Area",
            "old_index": 1000,
            "new_index": 7000,
            "status": "Normal"
        }
    ]

    while True:
        print("\n===== SMART ENERGY MONITOR =====")
        print("1. Xem danh sach thiet bi")
        print("2. Cap nhat chi so dien")
        print("3. Kich hoat canh bao qua tai")
        print("4. Tinh tong dien va chi phi")
        print("5. Thoat")

        try:
            choice = int(input("Nhap lua chon: "))

            if choice == 1:
                show_devices(devices)

            elif choice == 2:
                update_indices(devices)

            elif choice == 3:
                activate_overload(devices)

            elif choice == 4:
                total_consumption, discount_percent, final_cost = (
                    calculate_energy_financials(devices)
                )

                print("\n===== BAO CAO NANG LUONG =====")
                print(f"Tong dien tieu thu: {total_consumption} kWh")
                print(f"Chiet khau ap dung: {discount_percent}%")
                print(f"Tong tien sau chiet khau: {final_cost:,.0f} VND")

            elif choice == 5:
                print("Tam biet!")
                break

            else:
                print("Lua chon khong hop le!")

        except ValueError:
            print("Vui long nhap so!")


if __name__ == "__main__":
    main()