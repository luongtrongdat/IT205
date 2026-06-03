raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
while True:
    print("""
                ===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
                1. Hiển thị chuỗi dữ liệu gốc
                2. Chuẩn hóa dữ liệu và in báo cáo
                3. Tìm kiếm nhân viên theo mã ID
                4. Thoát chương trình
                                                        """)
    choice = input("Mời bạn lựa chọn(1-4): ")
    if choice == "1":
        print (raw_data)
    elif choice == "2":
        employees  = raw_data.strip().split("|")
        for i in range(len(employees)):
            staff = employees[i].split(";")
            staff[0] = staff[0].upper()
            staff[1] = staff[1].title()
            staff[2] = staff[2].strip()
            staff[3] = staff[3].upper()
            phone_check = staff[2].replace("-", "")  
            if phone_check.isdigit() and len(phone_check) == 10:
                staff[2] = "*" * 6 + phone_check[6:]
            else:
                staff[2] = "Invalid Format"
            print(f"nhân viên: {i+1}")
            print(f"id: {staff[0]}, name: {staff[1]},phone: {staff[2]},department: {staff[3]}")
    elif choice == "3":
        employees  = raw_data.strip().split("|")
        check_id = input("nhập ID cần tìm: ").strip().upper()
        check = False
        for i in range(len(employees)):
            staff = employees[i].split(";")
            staff[0] = staff[0].upper().strip()
            staff[1] = staff[1].title()
            staff[2] = staff[2].strip()
            staff[3] = staff[3].upper()
            phone_check = staff[2].replace("-", "")  
            if phone_check.isdigit() and len(phone_check) == 10:
                staff[2] = "*" * 6 + phone_check[6:]
            else:
                staff[2] = "Invalid Format"
            if check_id == staff[0]:
                print(f"nhân viên: {i+1}")
                print(f"id: {staff[0]}, name: {staff[1]},phone: {staff[2]},department: {staff[3]}")
                check = True
        if check == False:
            print("Không tìm thấy nhân viên")
    elif choice == "4":
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")