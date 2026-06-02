# ==============================
# HỆ THỐNG QUẢN LÝ KHO ĐƠN GIẢN
# ==============================

qty_laptop = 0
qty_phone = 0
qty_tablet = 0


# Hàm chọn sản phẩm
def chon_san_pham():
    print("\nChọn mặt hàng:")
    print("1. Laptop")
    print("2. Phone")
    print("3. Tablet")

    while True:
        choice = input("Lựa chọn: ")

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại!")


# Hàm nhập số lượng hợp lệ
def nhap_so_luong():
    while True:
        qty = input("Nhập số lượng: ")

        if not qty.isdigit():
            print("Vui lòng nhập số nguyên không âm!")
            continue

        qty = int(qty)

        if qty < 0:
            print("Số lượng không được âm!")
            continue

        return qty


while True:
    print("\n========== QUẢN LÝ KHO ==========")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo tồn kho thấp")
    print("5. Thoát")
    print("=================================")

    menu = input("Chọn chức năng: ")

    # 1. Báo cáo tồn kho
    if menu == "1":
        print("\n===== BÁO CÁO TỒN KHO =====")

        print(f"Laptop ({qty_laptop}): ", end="")
        for i in range(qty_laptop):
            print("*", end="")
        print()

        print(f"Phone ({qty_phone}): ", end="")
        for i in range(qty_phone):
            print("*", end="")
        print()

        print(f"Tablet ({qty_tablet}): ", end="")
        for i in range(qty_tablet):
            print("*", end="")
        print()

    # 2. Nhập kho
    elif menu == "2":
        product = chon_san_pham()
        quantity = nhap_so_luong()

        if product == "1":
            qty_laptop += quantity
            print("Nhập Laptop thành công!")

        elif product == "2":
            qty_phone += quantity
            print("Nhập Phone thành công!")

        else:
            qty_tablet += quantity
            print("Nhập Tablet thành công!")

    # 3. Xuất kho
    elif menu == "3":
        product = chon_san_pham()
        quantity = nhap_so_luong()

        if product == "1":
            if quantity > qty_laptop:
                print("Không đủ hàng trong kho!")
            else:
                qty_laptop -= quantity
                print("Xuất Laptop thành công!")

        elif product == "2":
            if quantity > qty_phone:
                print("Không đủ hàng trong kho!")
            else:
                qty_phone -= quantity
                print("Xuất Phone thành công!")

        else:
            if quantity > qty_tablet:
                print("Không đủ hàng trong kho!")
            else:
                qty_tablet -= quantity
                print("Xuất Tablet thành công!")

    # 4. Cảnh báo tồn kho thấp
    elif menu == "4":
        print("\n===== CẢNH BÁO TỒN KHO =====")

        low_stock = False

        if qty_laptop < 5:
            print(f"Laptop chỉ còn {qty_laptop} sản phẩm.")
            low_stock = True

        if qty_phone < 5:
            print(f"Phone chỉ còn {qty_phone} sản phẩm.")
            low_stock = True

        if qty_tablet < 5:
            print(f"Tablet chỉ còn {qty_tablet} sản phẩm.")
            low_stock = True

        if not low_stock:
            print("Tất cả mặt hàng đều đủ tồn kho.")

    elif menu == "5":
        print("Thoát chương trình. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5!")