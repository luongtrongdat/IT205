
class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name

        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")
            return

        self.__base_price = new_price

    @property
    def is_available(self):
        return self.__is_available


    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return int(
            self.__base_price
            + self.__base_price * MenuItem.service_charge)

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate


    @staticmethod
    def is_valid_item_id(item_code):
        if len(item_code) != 4:
            return False

        return (
            item_code[:2].isalpha()
            and item_code[:2].isupper()
            and item_code[2:].isdigit())

menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]



def find_item(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None


def show_menu_items():
    print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")

    if len(menu_db) == 0:
        print("Chưa có món nào trong menu.")
        return

    for index, item in enumerate(menu_db, start=1):

        status = (
            "Đang bán"
            if item.is_available
            else "Hết hàng")

        print(
            f"{index}. Mã: {item.item_id} | "
            f"Tên: {item.item_name} | "
            f"Trạng thái: {status} | "
            f"Giá niêm yết: {item.calculate_selling_price():,} VNĐ")


def add_new_item():
    print("\n--- THÊM MÓN MỚI VÀO MENU ---")

    item_id = input("Nhập mã món: ")

    if not MenuItem.is_valid_item_id(item_id):
        print("\nMã món không hợp lệ!")
        print("Mã món phải gồm 2 chữ cái in hoa ""và 2 chữ số. Ví dụ: CF01.")
        return

    if find_item(item_id):
        print("Mã món đã tồn tại!")
        return

    item_name = input("Nhập tên món: ")

    try:
        base_price = int(input("Nhập giá gốc: "))

        if base_price <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            return

        menu_db.append(
            MenuItem(
                item_id,
                item_name,
                base_price
            )
        )

        print("\nThêm món mới thành công!")

    except ValueError:
        print("Giá phải là số nguyên!")


def update_status():
    print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")

    item_id = input("Nhập mã món cần cập nhật: ")

    item = find_item(item_id)

    if item is None:
        print("Không tìm thấy món!")
        return

    item.toggle_availability()

    status = (
        "ĐANG BÁN"
        if item.is_available
        else "HẾT HÀNG")

    print(
        f">> Đã cập nhật "
        f"{item.item_name} thành {status}!")


def update_price():
    print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")

    item_id = input("Nhập mã món cần đổi giá: ")

    item = find_item(item_id)

    if item is None:
        print("Không tìm thấy món!")
        return

    try:
        new_price = int(input("Nhập giá tiền mới: "))

        old_price = item.base_price

        item.base_price = new_price

        if item.base_price != old_price:
            print("Cập nhật giá gốc thành công!")

    except ValueError:
        print("Giá phải là số nguyên!")


def update_service_charge():
    print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")

    print(
        f"Phụ phí hiện tại: "
        f"{MenuItem.service_charge * 100:.0f}%")

    try:
        new_rate = float(input("Nhập phụ phí mới. ""Ví dụ 0.1 tương ứng 10%: "))

        if new_rate < 0:
            print("Phụ phí không được âm!")
            return

        MenuItem.update_service_charge(new_rate)

        print("Cập nhật phụ phí dịch vụ ""thành công!")

    except ValueError:
        print("Dữ liệu không hợp lệ!")



while True:

    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN ""RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        show_menu_items()

    elif choice == "2":
        add_new_item()

    elif choice == "3":
        update_status()

    elif choice == "4":
        update_price()

    elif choice == "5":
        update_service_charge()

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng ""hệ thống Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ!")