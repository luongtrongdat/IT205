"""
1.Việc gán trực tiếp order_table1.total_amount = 0 từ bên ngoài đang vi phạm tính chất : tính đóng gói
2.Để kích hoạt cơ chế Name Mangling:cần đổi tên thành :__total_amount
3.Để cho phép đọc nhưng không cho phép sửa:ta dùng @property
4.Python sẽ tạo ra một Instance Attribute mới tên là:self.vat_rate chỉ tồn tại ở đối tượng hiện tại
5.Phải dùng:@classmethod
    thay self bằng:cls
"""

class CoffeeOrder:
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number

        self.__total_amount = 0

    @property
    def total_amount(self):
        return self.__total_amount

    def add_item(self, price):

        if price > 0:
            self.__total_amount += price

    def calculate_final_bill(self):

        return self.__total_amount + (
            self.__total_amount * CoffeeOrder.vat_rate
        )

    @classmethod
    def update_vat_rate(cls, new_rate):

        cls.vat_rate = new_rate

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

try:
    order_table1.total_amount = 0
except AttributeError:
    print("Không thể chỉnh sửa trực tiếp tổng tiền hóa đơn!")

CoffeeOrder.update_vat_rate(0.08)

print("\n===== THÔNG TIN HÓA ĐƠN =====")

print(
    f"Bàn 1 - Tổng tiền sau VAT: {order_table1.calculate_final_bill():,.0f} VNĐ"
)

print(
    f"Bàn 2 - Tổng tiền sau VAT: {order_table2.calculate_final_bill():,.0f} VNĐ"
)

print(f"VAT Bàn 1: {order_table1.vat_rate}")
print(f"VAT Bàn 2: {order_table2.vat_rate}")

print(f"Tổng tiền Bàn 1: {order_table1.total_amount:,.0f} VNĐ")
print(f"Tổng tiền Bàn 2: {order_table2.total_amount:,.0f} VNĐ")