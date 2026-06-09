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
    print("\n" + "="*40)
    print("🛍  AMAZON CART MANAGEMENT SYSTEM CLI  🛍")
    print("="*40)
    print("1. Xem chi tiết giỏ hàng và Tổng tiền")
    print("2. Thêm sản phẩm mới hoặc Tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("="*40)
    choice_str = input("Vui lòng chọn chức năng (1-5): ").strip()

    if choice_str not in ["1", "2", "3", "4", "5"]:
        print("💥Lỗi: Chức năng không hợp lệ! Vui lòng nhập số từ 1 đến 5.")
        continue
    choice = int(choice_str)
    if choice == 1:
        print("Chi tiết giỏ hàng:")
        print("-"*40)
        total = 0
        for item in cart_items: 
            print(f"ID: {item['id']}, Tên: {item['name']}, Số lượng: {item['number']}, Giá: {item['price']}")
            total += item['number'] * item['price']
        print("-"*40)
        print(f"🧧 Tổng tiền: {total}")
    elif choice == 2:
        new_item = {}
        new_item['id'] = input("Nhập ID sản phẩm: ")
        new_item['name'] = input("Nhập tên sản phẩm: ")
        new_item['number'] = int(input("Nhập số lượng sản phẩm: "))
        new_item['price'] = int(input("Nhập giá sản phẩm: "))
        cart_items.append(new_item)
        print("🤗 Thêm sản phẩm thành công!")
    elif choice == 3:
        item_id = input("Nhập ID sản phẩm cần cập nhật: ")
        for item in cart_items:
            if item['id'] == item_id:
                item['number'] = int(input("Nhập số lượng mới: "))
                item['price'] = int(input("Nhập giá mới: "))
                print("✨ Cập nhật sản phẩm thành công!")
                break
        else:
            print("🎃 Không tìm thấy sản phẩm với ID này.")
    elif choice == 4:
        item_id = input("Nhập ID sản phẩm cần xóa: ")
        for item in cart_items:
            if item['id'] == item_id:
                cart_items.remove(item)
                print("🎉 Xóa sản phẩm thành công!")
        else:
            print("🎃 Không tìm thấy sản phẩm với ID này.")
    elif choice == 5:
        print("🤢 Cảm ơn bạn đã sử dụng chương trình!🤮")
        break