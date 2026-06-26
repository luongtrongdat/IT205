"""
1.Nếu để points là thuộc tính public: thì dữ liệu sẽ bị mất tính toàn vẹn
    hậu quả :Điểm thưởng có thể âm
        Điểm thưởng có thể là chuỗi thay vì số
        Các phép tính cộng/trừ điểm sẽ cho kết quả sai
        Có thể gây lỗi chương trình
2.Để kiểm tra dữ liệu trước khi cho phép gán giá trị mới vào thuộc tính private __points, ta dùng:@points.setter
3.Hàm:def is_eligible_for_voucher(self, bill_amount):
    return bill_amount >= 200000
không sử dụng:
    self.customer_name
    self.points
=> nên việc dùng self là ko cần thiết 
4.Ta nên dùng:@staticmethod
    @staticmethod	                    @classmethod
    Không nhận self	                    Không nhận self
    Không nhận cls	                    Nhận cls
    Không truy cập thuộc tính class	    Có thể truy cập thuộc tính class
   
"""


class MemberCard:

    def __init__(self, customer_name, points=0):

        self.customer_name = customer_name

        self.__points = 0

        self.points = points


    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):

        if not isinstance(value, int) or value < 0:
            print("Dữ liệu điểm không hợp lệ!")
            return

        self.__points = value


    def add_points(self, amount):

        if isinstance(amount, int) and amount > 0:
            self.__points += amount

    @staticmethod
    def is_eligible_for_voucher(bill_amount):

        return bill_amount >= 200000


card1 = MemberCard("Le Van C", 100)

print("Điểm ban đầu:", card1.points)

card1.points = -50

print("Điểm sau khi nhập sai:", card1.points)

card1.points = "mot tram"

print("Điểm hiện tại:", card1.points)

card1.add_points(50)

print("Điểm sau khi cộng:", card1.points)

result = MemberCard.is_eligible_for_voucher(250000)

print("Hóa đơn 250000 có được tặng voucher không?", result)