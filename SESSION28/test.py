class Product:
    def __init__(self, product_id, name, price, quantity_sold, discount):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ""

        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        revenue = self.price * self.quantity_sold - self.discount
        if revenue < 0:
            revenue = 0
        self.total_revenue = revenue

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"


class ProductManager:
    def __init__(self):
        self.products = []
    def find_by_id(self, product_id):
        for product in self.products:
            if product.id.lower() == product_id.lower():
                return product
        return None
    def input_positive_number(self, message):
        while True:
            try:
                value = float(input(message))
                if value < 0:
                    print("Giá trị phải lớn hơn hoặc bằng 0!")
                    continue
                return value
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

    def input_quantity(self):
        while True:
            try:
                quantity = int(input("Nhập số lượng đã bán: "))
                if 0 <= quantity <= 10000:
                    return quantity
                print("Số lượng phải nằm trong khoảng từ 0 đến 10000!")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")

    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm đang rỗng!")
            return
        print("\n================ DANH SÁCH SẢN PHẨM ================")
        print(
            f"{'Mã SP':<10}|"
            f"{'Tên sản phẩm':<25}|"
            f"{'Giá bán':<15}|"
            f"{'SL bán':<10}|"
            f"{'Giảm giá':<15}|"
            f"{'Doanh thu':<15}|"
            f"{'Loại DT':<15}|"
        )
        for product in self.products:
            print(
                f"{product.id:<10}|"
                f"{product.name:<25}|"
                f"{product.price:<15,.0f}|"
                f"{product.quantity_sold:<10}|"
                f"{product.discount:<15,.0f}|"
                f"{product.total_revenue:<15,.0f}|"
                f"{product.revenue_type:<15}|"
            )
    def add_product(self):
        print("\n===== THÊM SẢN PHẨM =====")
        while True:
            product_id = input("Nhập mã sản phẩm: ").strip()
            if not product_id:
                print("Mã sản phẩm không được rỗng!")
                continue
            if self.find_by_id(product_id):
                print("Mã sản phẩm đã tồn tại!")
                continue
            break
        while True:
            name = input("Nhập tên sản phẩm: ").strip()
            if not name:
                print("Tên sản phẩm không được rỗng!")
                continue
            break
        price = self.input_positive_number("Nhập giá bán: ")
        quantity_sold = self.input_quantity()
        discount = self.input_positive_number("Nhập giảm giá: ")
        product = Product(
            product_id,
            name,
            price,
            quantity_sold,
            discount
        )
        self.products.append(product)
        print("Thêm sản phẩm thành công.")
    def update_product(self):
        if not self.products:
            print("Danh sách sản phẩm đang rỗng!")
            return
        product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip()
        product = self.find_by_id(product_id)
        if not product:
            print("Không tìm thấy sản phẩm cần cập nhật!")
            return
        product.price = self.input_positive_number("Nhập giá bán mới: ")
        product.quantity_sold = self.input_quantity()
        product.discount = self.input_positive_number("Nhập giảm giá mới: ")
        product.calculate_revenue()
        product.classify_revenue()
        print("Cập nhật sản phẩm thành công!")

def display_menu():
    print("""
================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thoát
======================================
""")

def main():
    manager = ProductManager()

    while True:
        display_menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_product()
            case "3":
                manager.update_product()
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()