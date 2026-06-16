products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

# Xem danh sách sản phẩm
def show_products(products_list):
    """Hiển thị danh sách sản phẩm"""
    print("\n----- DANH SÁCH SẢN PHẨM -----")
    if len(products_list) == 0:
        print("\n😌 Cửa hàng hiện chưa có sản phẩm nào!")
        return

    print("\n{:<10}| {:<25}| {:>15}|".format("ID", "Tên sản phẩm", "Giá bán"))
    print("-" * 55)

    for product in products_list:
        print(
            "{:<10}| {:<25}| {:>15,}|".format(
                product["id"],
                product["name"],
                product["price"]
            )
        )

# Thêm sản phẩm
def add_product(products_list):
    """Thêm sản phẩm mới"""

    print("\n----- THÊM SẢN PHẨM -----")

    while True:
        product_id = input("Nhập ID sản phẩm: ").strip().upper()

        if not product_id:
            print("💢 ID không được để trống!")
        elif not product_id.startswith("P"):
            print("😡 ID sản phẩm phải bắt đầu bằng chữ 'P'!")
        elif not product_id[1:].isdigit():
            print("🤬 Sau chữ 'P' phải là các chữ số!")
        else:
            break
    while True:
        product_name = input("Nhập tên sản phẩm: ").strip()
        if product_name:
            break
        print("💥 Tên sản phẩm không được để trống!")

    while True:
        try:
            product_price = int(input("Nhập giá bán: "))
            if product_price > 0:
                break
            print("🙄 Giá bán phải lớn hơn 0!")
        except ValueError:
            print("😑 Giá bán phải là số nguyên!")
    new_product = {
        "id": product_id,
        "name": product_name,
        "price": product_price
    }

    products_list.append(new_product)

    print("\n🤗 Thêm sản phẩm thành công!")

# Cập nhật giá sản phẩm theo id
def update_price(products_list):
    """Cập nhật giá sản phẩm"""

    print("\n----- CẬP NHẬT GIÁ SẢN PHẨM -----")

    product_id = input("Nhập ID sản phẩm cần cập nhật: ").strip()

    for product in products_list:

        if product["id"].lower() == product_id.lower():

            while True:
                try:
                    new_price = int(input("Nhập giá mới: "))
                    if new_price > 0:
                        break
                    print("🙂 Giá phải lớn hơn 0!")
                except ValueError:
                    print("🤨 Giá phải là số nguyên!")

            product["price"] = new_price

            print("\n😍 Cập nhật giá thành công!")
            return
    print(f"\n😥 Không tìm thấy sản phẩm có mã {product_id}!")

# Menu
while True:
    print("""
        =================================
          Quản lý cửa hàng - Mini Store
        =================================
        1. Xem danh sách sản phẩm
        2. Thêm sản phẩm mới
        3. Cập nhật giá sản phẩm theo id
        4. Thoát chương trình
        =================================
    """)
    choice = input("✨ Chọn chức năng (1-4): ").strip()
    if choice == '1':
        show_products(products)
    elif choice == "2":
        add_product(products)
    elif choice == "3":
        update_price(products)
    elif choice == "4":
        print("\n💞 Cảm ơn bạn đã sử dụng chương trình!💕")
        break
    else:
        print("\n🥱 Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 4.")