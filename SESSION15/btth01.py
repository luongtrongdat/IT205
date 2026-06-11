inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    global inventory_stock
    inventory_stock += amount

def process_sale(quantity):
    if quantity > inventory_stock:
        print(f"Không đủ hàng trong kho.Tồn kho hiện tại chỉ còn {inventory_stock}")
        return False
    return True

# Tính tổng tiền cuối cùng của hóa đơn
def calculate_final_price(quantity, price):
    subtotal = quantity * price
    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.1
    after_discount = subtotal - discount
    vat = after_discount * 0.08
    print(f"Tạm tính: ${subtotal}")
    print(f"Giảm giá (10%): ${discount}")
    print(f"Thuế VAT (8%): ${vat}")
    return after_discount + vat

# Hiển thị báo cáo tồn kho và doanh thu
def print_report():
    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")


def main():
    global inventory_stock
    global total_revenue

    while True:
        print("""
                ========== TECHSTORE MANAGEMENT SYSTEM ==========
                1. Nhập thêm hàng vào kho
                2. Bán hàng (Tính toán hóa đơn)
                3. Xem báo cáo tổng quan
                4. Thoát chương trình
                =================================================   
""")
        choice = input("Chọn chức năng (1-4): ")
        if choice == "1":
            print("\n--- NHẬP HÀNG ---")
            amount = input("Nhập số lượng sản phẩm muốn thêm: ")
            if not amount.isdigit():
                print("Dữ liệu phải là số.")
                continue
            amount = int(amount)
            if amount <= 0:
                print("Dữ liệu nhập vào phải lớn hơn 0.")
                continue
            add_stock(amount)
            print(f"Đã nhập thành công {amount} sản phẩm.")
            print(f"Tồn kho hiện tại: {inventory_stock}")
        elif choice == "2":
            print("\n--- BÁN HÀNG ---")
            quantity = input("Nhập số lượng mua: ")
            price = input("Nhập đơn giá ($): ")
            if not quantity.isdigit():
                print("Số lượng phải là số.")
                continue
            # Cho phép nhập số thực cho đơn giá
            if not price.replace(".", "", 1).isdigit():
                print("Đơn giá phải là số.")
                continue
            quantity = int(quantity)
            price = float(price)
            if quantity <= 0 or price <= 0:
                print("Dữ liệu nhập vào phải lớn hơn 0.")
                continue
            if process_sale(quantity):
                final_total = calculate_final_price(quantity, price)
                inventory_stock -= quantity
                total_revenue += final_total
                print(f"Tổng thanh toán: ${final_total}")
                print("Đã bán thành công!")
        elif choice == "3":
            print_report()
        elif choice == "4":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ.")
main()