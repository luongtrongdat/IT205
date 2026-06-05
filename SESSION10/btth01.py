cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n==================================================")
    print("      HỆ THỐNG QUẢN LÝ GIỎ HÀNG SHOPEE")
    print("==================================================")
    print("[1] Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("[2] Thêm sản phẩm mới / Cộng dồn số lượng")
    print("[3] Cập nhật số lượng của một sản phẩm")
    print("[4] Xóa sản phẩm khỏi giỏ hàng")
    print("[5] Thoát chương trình")
    print("==================================================")

    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    if choice == "1":
        if len(cart_items) == 0:
            print("Giỏ hàng của bạn đang trống.")
        else:
            print("\n── CHI TIẾT GIỎ HÀNG ──")
            print(f"{'STT':<4} | {'Mã SP':<6} | {'Tên sản phẩm':<22} | {'SL':<3} | {'Đơn Giá':<10} | {'Thành Tiền'}")
            print("-" * 75)
            
            total_quantity = 0
            total_price = 0
            index = 1
            
            for item in cart_items:
                product_id, product_name, quantity, price = item
                subtotal = quantity * price
                total_quantity += quantity
                total_price += subtotal
                
                print(f"{index:<4} | {product_id:<6} | {product_name:<22} | {quantity:<3} | {price:<10}đ | {subtotal}đ")
                index += 1
                
            print("-" * 75)
            print(f"Tổng số lượng: {total_quantity}")
            print(f"Tổng tiền: {total_price}đ")

    elif choice == "2":
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        if product_id == "":
            print("Lỗi: Mã sản phẩm không được để trống!")
            continue
            
        product_name = input("Nhập tên sản phẩm: ").strip()
        quantity_str = input("Nhập số lượng: ").strip()
        price_str = input("Nhập đơn giá: ").strip()

        if quantity_str.isdigit() and price_str.isdigit():
            quantity = int(quantity_str)
            price = int(price_str)
            
            if quantity > 0 and price >= 0:
                found = False
                for item in cart_items:
                    if item[0] == product_id:
                        item[2] += quantity
                        print("Đã cộng dồn số lượng")
                        found = True
                        break
                        
                if not found:
                    cart_items.append([product_id, product_name, quantity, price])
                    print("Đã thêm sản phẩm mới")
            else:
                print("Số lượng phải > 0 và đơn giá >= 0")
        else:
            print("Số lượng và đơn giá phải là số nguyên")

    elif choice == "3":
        product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        quantity_str = input("Nhập số lượng mới: ").strip()

        if quantity_str.isdigit():
            new_quantity = int(quantity_str)
            
            if new_quantity > 0:
                found = False
                for item in cart_items:
                    if item[0] == product_id:
                        item[2] = new_quantity
                        print("Đã cập nhật số lượng")
                        found = True
                        break
                        
                if not found:
                    print("Mã sản phẩm không tồn tại trong giỏ hàng.")
            else:
                print("Số lượng phải > 0")
        else:
            print("Số lượng phải là số nguyên")

    elif choice == "4":
        product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        found = False
        
        for item in cart_items:
            if item[0] == product_id:
                cart_items.remove(item)
                print(f"Đã xóa hoàn toàn sản phẩm {product_id} khỏi giỏ hàng")
                found = True
                break
                
        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "5":
        print("Thoát chương trình")
        break
        
    else:
        print("Lựa chọn không hợp lệ")