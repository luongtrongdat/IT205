"""
Input:Mã đơn hàng (str)
    Trạng thái đơn hàng (str)
    Vị trí cần sửa/xóa (str)
Output:Danh sách đơn hàng
    Thông báo thêm, sửa, xóa thành công
    Kết quả thống kê theo trạng thái
Giải pháp:Sử dụng:
    append() để thêm đơn hàng
    Gán qua index để sửa đơn hàng
    pop(index) để xóa theo vị trí
    strip() để xóa khoảng trắng
    upper() để chuẩn hóa dữ liệu
    isdigit() để kiểm tra vị trí nhập vào có phải số hay không

 Nếu chọn 1:
        Hiển thị danh sách

    Nếu chọn 2:
        Lặp menu cập nhật

            1. Thêm đơn hàng
                Nhập mã
                Nhập trạng thái
                Chuẩn hóa
                append()

            2. Sửa đơn hàng
                Nhập vị trí
                Kiểm tra hợp lệ
                Nhập dữ liệu mới
                Gán lại phần tử

            3. Xóa đơn hàng
                Nhập vị trí
                Kiểm tra hợp lệ
                pop(vị trí)

            4. Quay lại menu chính
                break

    Nếu chọn 3:
        Thống kê trạng thái

    Nếu chọn 4:
        Thoát chương trình

    Ngược lại:
        Báo lỗi
"""

order_list = ["GE001 - PENDING","GE002 - DELIVERING","GE003 - CANCELLED"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
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
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")

            sub_choice = input("Nhập lựa chọn: ").strip()

            if sub_choice == "1":
                order_code = input("Nhập mã đơn hàng: ").strip().upper()
                status = input("Nhập trạng thái: ").strip().upper()

                order = order_code + " - " + status
                order_list.append(order)

                print("Thêm đơn hàng thành công!")

            elif sub_choice == "2":
                position = input("Nhập vị trí cần sửa: ").strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                if position < 1 or position > len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                order_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                status = input("Nhập trạng thái mới: ").strip().upper()

                order_list[position - 1] = order_code + " - " + status

                print("Cập nhật thành công!")

            elif sub_choice == "3":
                position = input("Nhập vị trí cần xóa: ").strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                if position < 1 or position > len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                deleted_order = order_list.pop(position - 1)

                print("Đã xóa:", deleted_order)

            elif sub_choice == "4":
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    elif choice == "3":
        pending = 0
        delivering = 0
        completed = 0
        cancelled = 0

        for order in order_list:
            status = order.split(" - ")[1]

            if status == "PENDING":
                pending += 1
            elif status == "DELIVERING":
                delivering += 1
            elif status == "COMPLETED":
                completed += 1
            elif status == "CANCELLED":
                cancelled += 1

        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print("PENDING:", pending)
        print("DELIVERING:", delivering)
        print("COMPLETED:", completed)
        print("CANCELLED:", cancelled)
        print("Tổng số đơn hàng:", len(order_list))

    elif choice == "4":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")