"""
1.Nếu khai báo trong __init__:self.point_value_vnd = 1000
    thì mỗi đối tượng sẽ có một bản sao riêng.
    Khi ban giám đốc đổi tỷ giá từ 1000 lên 2000 VNĐ ở chức năng 5,
    hệ thống phải cập nhật từng thẻ một, rất khó quản lý và dễ gây sai lệch dữ liệu
2.is_valid_card_id() dùng @staticmethod vì Hàm này chỉ kiểm tra định dạng mã thẻ:RC01,RC99

"""

class MemberCard:

    # Class Attribute
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()

        self.__points = 0
        self.__tier = "Standard"

    # ==========================
    # Properties (Read Only)
    # ==========================

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    # ==========================
    # Static Method
    # ==========================

    @staticmethod
    def is_valid_card_id(card_id):

        if len(card_id) != 4:
            return False

        if not card_id.startswith("RC"):
            return False

        if not card_id[2:].isdigit():
            return False

        return True

    # ==========================
    # Class Method
    # ==========================

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value

    # ==========================
    # Instance Methods
    # ==========================

    def earn_points(self, bill_amount):

        earned_points = bill_amount // 10000

        self.__points += earned_points

        upgraded = False

        if self.__points >= 100 and self.__tier == "Standard":
            self.__tier = "VIP"
            upgraded = True

        return earned_points, upgraded

    def redeem_points(self, points_to_use):

        if points_to_use <= 0:
            return False, 0

        if points_to_use > self.__points:
            return False, 0

        self.__points -= points_to_use

        discount = points_to_use * MemberCard.point_value_vnd

        return True, discount


cards_database = []


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card

    return None


def show_cards():
    print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")

    if len(cards_database) == 0:
        print("Chưa có dữ liệu.")
        return

    for index, card in enumerate(cards_database, start=1):
        print(
            f"{index}. Mã: {card.card_id} | "
            f"Tên: {card.name} | "
            f"Điểm: {card.points} | "
            f"Hạng: {card.tier}")


def register_card():
    print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")

    card_id = input("Nhập mã thẻ: ").strip()

    if not MemberCard.is_valid_card_id(card_id):
        print("Mã thẻ không hợp lệ!")
        return

    if find_card(card_id):
        print("\nMã thẻ đã tồn tại trong hệ thống!")
        print("Vui lòng kiểm tra lại.")
        return

    name = input("Nhập tên khách hàng: ")

    card = MemberCard(card_id, name)

    cards_database.append(card)

    print("\nĐăng ký thẻ thành viên thành công!")
    print(f"Mã thẻ: {card.card_id}")
    print(f"Tên khách hàng: {card.name}")
    print(f"Điểm ban đầu: {card.points}")
    print(f"Hạng thẻ: {card.tier}")


def earn_points():
    print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")

    card_id = input("Nhập mã thẻ: ")

    card = find_card(card_id)

    if card is None:
        print("Không tìm thấy thẻ.")
        return

    try:
        bill_amount = int(input("Nhập tổng tiền hóa đơn: "))

        if bill_amount <= 0:
            print("Hóa đơn phải lớn hơn 0.")
            return

        earned, upgraded = card.earn_points(bill_amount)

        print(f"\nKhách hàng: {card.name}")
        print(f"Hóa đơn: {bill_amount:,} VNĐ")
        print(f"Số điểm được tích: {earned}")
        print(f"Tổng điểm hiện tại: {card.points}")

        if upgraded:
            print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")

        print(f"Hạng thẻ hiện tại: {card.tier}")

    except ValueError:
        print("Dữ liệu không hợp lệ.")


def redeem_points():
    print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")

    card_id = input("Nhập mã thẻ: ")

    card = find_card(card_id)

    if card is None:
        print("Không tìm thấy thẻ.")
        return

    try:
        points_to_use = int(input("Nhập số điểm muốn sử dụng: "))

        success, discount = card.redeem_points(points_to_use)

        if not success:
            print("\nKhông thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {card.points}")
            print("Điểm cũ được giữ nguyên:")
            print(f"Số điểm sau giao dịch: {card.points}")
            return

        print(f"\nĐã trừ {points_to_use} điểm.")
        print(f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!")
        print(f"Số điểm còn lại: {card.points}")
        print(f"Hạng thẻ hiện tại: {card.tier}")

    except ValueError:
        print("Dữ liệu không hợp lệ.")


def update_exchange_rate():
    print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")

    print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

    try:
        new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))

        if new_value <= 0:
            print("Tỷ giá phải lớn hơn 0.")
            return

        MemberCard.update_point_value(new_value)

        print("\nCập nhật tỷ giá thành công!")
        print(
            f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

    except ValueError:
        print("Dữ liệu không hợp lệ.")



while True:

    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        show_cards()

    elif choice == "2":
        register_card()

    elif choice == "3":
        earn_points()

    elif choice == "4":
        redeem_points()

    elif choice == "5":
        update_exchange_rate()

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ.")