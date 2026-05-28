# vì khi kiểm tra điều kiện đúng => hiển thị ra cảnh báo và tiếp tục thực hiện tiếp chương trình 
# cách giải quyết là dùng else để khi điều kiện sai thì mới tính thưởng và gửi email 
 
print("=== HE THONG GUI EMAIL THUONG TET ===")
for employee_number in range(1, 4):
    print(f"\n--- Dang xu ly nhan vien so {employee_number} ---")
    working_days = int(input("Nhap so ngay cong trong thang: "))
    if working_days == 0:
        print("CANH BAO: Nhan vien nghi ca thang, khong xet duyet thuong.")
    else:
        bonus_amount = working_days * 200000
        print("-> Da gui Email: Chuc mung nhan duoc",bonus_amount,"VND tien thuong!")

print("\nDa hoan tat qua trinh duyet thuong cho 3 nhan vien!")