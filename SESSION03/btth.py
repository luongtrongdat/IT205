# Lựa chọn từ người dùng
choice = True

while choice:
    # Nhập số lượng nhân viên
    employee_quantity = int(input("Nhập số lượng nhân viên: "))
    # Nhập thông tin cho từng nhân viên
    for employee_id in range(0, employee_quantity):
        print(f"Nhập thông tin cho nhân viên thứ {employee_id + 1}: ")
        full_name = input("Họ và tên: ")
        working_days = int(input("Số ngày đi làm: "))

        print("---- Thông tin nhân viên ----")
        print(f"Họ và tên: {full_name}")
        print(f"Số ngày đi làm: {working_days}")

        # Kiểm tra để đánh giá nhân viên
        if working_days >= 20:
            print("Đánh giá: Nhân viên chuyên cần")
        else:
            print("Đánh giá: Nhân viên cần cải thiện")
