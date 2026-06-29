class BaseAccount(ABC):
    pass

class CreaditAccount(BaseAccount):
    def __init__(self):
        super().__init__()

class DigitalPreinumMixin:
    @staticmethod
    def cashback_reward():
        pass

"""
INPUT:
    menubar và lựa chọn của người dùng.
OUTPUT:
    với mỗi chức năng trả về thông tin tương ứng.

1. Mở tài khoản mới (Chọn loại tài khoản)
2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)
3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)
4. Tích lũy / Áp dụng lãi suất định kỳ
5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)
6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)
7. Thoát chương trình
"""