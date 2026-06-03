raw_input = "   nGuyen vaN aN  ;  2004   "
while True: 
    print("""
                ===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
                1. Hiển thị chuỗi dữ liệu gốc
                2. Chuẩn hóa Họ tên và tính Tuổi
                3. Tạo Mã ID và Email tự động
                4. Thoát chương trình
                =====================================
                                                        """)
    choice = input("Nhập lựa chọn của bạn (1-4): ")
    if choice == "1":
        print(raw_input)
    elif choice == "2":
        user = raw_input.strip().split(";")
        name = user[0].strip().lower().title()
        year = int(user[1].strip())
        print(f"""
                Họ Và Tên:{name}
                Tuổi: {2026 - year} tuổi
        """)
    elif choice == "3":
        user = raw_input.strip().split(";")
        name = user[0].strip().lower().title()
        print(f"Họ Và Tên:{name}")
        year = user[1].strip()
        name_array = name.upper().split(" ")
        user_id = name_array[-1] + year[2:]
        print(f"mã id: {user_id}")

        name_array = name.lower().split(" ")
        ho = name_array[0]          
        ten_dem = name_array[1]     
        ten_chinh = name_array[2]
        email = ho[:1] + ten_dem[:1] + ten_chinh + "@company.com"
        print(f"Email: {email}")
    elif choice == "4":
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")