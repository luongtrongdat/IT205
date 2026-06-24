orders = [
    {"id": "HD01", "name": "Dai ly Hoang Long", "price": 45000000, "status": "Paid"},
    {"id": "HD02", "name": "Tap hoa Minh Thu", "price": 15000000, "status": "Unpaid"}
]

def display_orders(order_list):
    if len(order_list) == 0:
        print("Danh sách đơn hàng trống!")
        return
    print("DANH SÁCH ĐƠN HÀNG")
    print("-" * 60)
    for order in order_list:
        print(
            f"Mã: {order['id']} | "
            f"Tên: {order['name']} | "
            f"Giá trị: {order['price']:,} VND | "
            f"Trạng thái: {order['status']}"
        )
def add_order(order_list):
    print("THÊM ĐƠN HÀNG")
    order_id = input("Nhập mã đơn hàng: ").strip().upper()
    if order_id == "":
        print("Mã đơn hàng không được để trống!")
        return
    for order in order_list:
        if order["id"] == order_id:
            print("Mã đơn hàng đã tồn tại!")
            return
    name = input("Nhập tên đại lý: ").strip()
    if name == "":
        print("Tên đại lý không được để trống!")
        return
    try:
        price = int(input("Nhập giá trị đơn hàng: "))
        if price <= 0:
            print("Giá trị đơn hàng phải lớn hơn 0!")
            return
    except ValueError:
        print("Giá trị đơn hàng không hợp lệ!")
        return
    new_order = {
        "id": order_id,
        "name": name,
        "price": price,
        "status": "Unpaid"
    }
    order_list.append(new_order)
    print("Thêm đơn hàng thành công!")

def update_order_status(order_list):
    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip().upper()
    for order in order_list:
        if order["id"] == order_id:
            if order["status"] == "Paid":
                print("Đơn hàng đã được thanh toán trước đó!")
                return
            order["status"] = "Paid"
            print("Cập nhật trạng thái thành công!")
            return
    print("Không tìm thấy đơn hàng!")

def calculate_revenue(order_list):
    total_revenue = 0
    for order in order_list:
        if order["status"] == "Paid":
            total_revenue += order["price"]
    discount_percent = 0
    if total_revenue >= 100000000:
        discount_percent = 5
    discount_amount = total_revenue * discount_percent // 100
    return total_revenue, discount_percent, discount_amount

while True:
    print("===== QUẢN LÝ ĐƠN HÀNG =====")
    print("1. Xem danh sách đơn hàng")
    print("2. Thêm đơn hàng")
    print("3. Cập nhật trạng thái thanh toán")
    print("4. Tính doanh thu")
    print("5. Thoát")

    choice = int(input("Nhập lựa chọn: "))

    if choice == "1":
        display_orders(orders)
    elif choice == "2":
        add_order(orders)
    elif choice == "3":
        update_order_status(orders)
    elif choice == "4":
        revenue, percent, discount = calculate_revenue(orders)
        print("\nBÁO CÁO DOANH THU")
        print(f"Doanh thu: {revenue:,} VND")
        print(f"Chiết khấu: {percent}%")
        print(f"Số tiền chiết khấu: {discount:,} VND")
    elif choice == "5":
        print("Thoát chương trình!")
        break
    else:
        print("Vui lòng chọn từ 1 đến 5!")
