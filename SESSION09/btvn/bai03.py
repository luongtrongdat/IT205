"""
Input:Lựa chọn menu của người dùng (str)
    Mã đơn hàng cần thêm (str)
    Mã đơn hàng cần xóa (str)
Output:Danh sách đơn hàng hiện tại
    Thông báo thêm/xóa thành công
    Thông báo lỗi khi nhập sai
Giải pháp:Dùng append() để thêm đơn hàng.
    Dùng remove() để xóa đơn hàng.
    Dùng strip() để xóa khoảng trắng đầu cuối.
    Dùng upper() để chuẩn hóa mã đơn hàng.
    Dùng toán tử in để kiểm tra đơn hàng có tồn tại hay không.

Nếu chọn 1:
    Nếu danh sách rỗng:
        In thông báo danh sách trống
    Ngược lại:
        Hiển thị toàn bộ đơn hàng

Nếu chọn 2:
    Nhập mã đơn hàng
    Chuẩn hóa bằng strip() và upper()
    Thêm vào danh sách

Nếu chọn 3:
    Nhập mã cần xóa
    Chuẩn hóa bằng strip() và upper()

    Nếu tồn tại:
        Xóa khỏi danh sách
    Ngược lại:
        Thông báo không tìm thấy

Nếu chọn 4:
    Thoát chương trình
    break

Ngược lại:
    Thông báo lựa chọn không hợp lệ
"""

order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                print(f"{i + 1}. {order_list[i]}")

    elif choice == "2":
        new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
        if new_order:
            order_list.append(new_order)
            print("Thêm đơn hàng thành công!")
        else:
            print("Mã đơn hàng không hợp lệ!")

    elif choice == "3":
        order_code = input("Nhập mã đơn hàng cần xóa: ").strip().upper()

        if order_code in order_list:
            order_list.remove(order_code)
            print("Xóa đơn hàng thành công!")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")

    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")