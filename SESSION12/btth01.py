cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]
while True:
    print("""
            SHOP CART MANAGEMENT SYSYTEM
            1. Xem chi tiết giỏ hàng và tính tổng tiền
            2. Thêm sản phẩm mới / Cộng dồ số lượng
            3. Cập nhật số lượng của một sản phẩm 
            4. Xóa sản phẩm khỏi giỏ hàng
            5.Thoát chương trình 
""")
    
    choice = input("Mời bạn chọn chức năng (1-5): ")
    if choice == "1":
        print("--- CHI TIẾT GIỎ HÀNG ---")
        print("STT | Mã SP | Tên sản phẩm | SL | Đơn giá | Thành Tiền")
        total_number = 0
        total_pice = 0
        for i , cart in enumerate(cart_items, start=1):
            total_number += cart["number"]
            total_pice += cart["price"] * cart["number"]
            print(f" {i} | {cart['id']} | {cart['name']} | {cart['number']} | {cart['price']} | {cart['number']*cart['price']}")
        print(f"tổng sl sản phẩm trong giỏ: {total_number}")
        print(f"Tổng tiền thanh toán: {total_pice}đ")
    elif choice == "2":

        cart_id = input("Nhập mã sản phẩm: ").strip().upper()
        duplicate = False

        for cart in cart_items:
            if cart["id"] == cart_id:
                duplicate = True
                cart_number_str = input("Nhập số lượng muốn cộng dồn thêm: ").strip()
                if not cart_number_str.isdigit():
                    print("Số lượng phải là ký tự số hợp lệ")
                    continue
                added_number = int(cart_number_str)
                if added_number <= 0:
                    print("Số lượng cộng thêm phải lớn hơn 0")
                    continue
                cart["number"] += added_number
                break

        if duplicate == True:
             continue
        
        cart_name = input("Nhập tên sản phẩm: ").strip()
        cart_number = input("Nhập số lượng sản phẩm: ").strip()
        cart_price = input("Nhập đơn giá sản phẩm: ").strip()
        
        if not cart_number.isdigit() or not cart_price.isdigit():
            print("Hệ thống phải báo lỗi và không thực hiện thao tác")
            continue

        number = int(cart_number)
        price = int(cart_price)

        if number <= 0 or price < 0:
            print("Hệ thống phải báo lỗi và không thực hiện thao tác")

    elif choice == "3":
        cart_id = input("Nhập mã sản phẩm: ").strip().upper()
        duplicate = False

        for cart in cart_items:
            if cart["id"] == cart_id:
                duplicate = True
                break
        if duplicate == True:
            cart_number = input("nhập số lượng mới cần thay đổi: ")
            if not cart_number.isdigit() :
                print("Hệ thống phải báo lỗi và không thực hiện thao tác")
                continue
            number = int(cart_number)
            if number <= 0 :
                print("Hệ thống phải báo lỗi và không thực hiện thao tác")
            for cart in cart_items:
                if cart["id"] == cart_id:
                    cart["number"] = number
                    break
        else:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "4":
        cart_id = input("Nhập mã sản phẩm: ").strip().upper()
        duplicate = False
        for cart in cart_items:
            if cart["id"] == cart_id:
                duplicate = True
                cart_items.remove(cart)
                print("Xóa sản phẩm thành công.")
                print
                break
        if duplicate == False:
             print("Mã sản phẩm không tồn tại trong giỏ hàng.")
             continue
    elif choice == "5":
        print("bạn đã thoát chương trình")
        break
    else:
        print("dữ liệu nhập không hợp lệ")
