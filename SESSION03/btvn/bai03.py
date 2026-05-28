# input : Mã nhân viên	string	
#         Họ và tên	    string	
#         Phòng ban	    string
# output : Trường hợp hợp lệ: in Phiếu Hồ sơ Nhân sự
#          Trường hợp không hợp lệ:thì hiển thị: tên hoặc mã ko hợp lệ hủy bỏ tạo hồ sơ cho nhân viên này 
# giải pháp :Sử dụng vòng lặp ,kiểm tra dữ liệu bằng cách xem dữ liệu có bằng 1 chuỗi rỗng ko nếu bằng thì in lỗi ,nếu khác thì in phiếu 

# thuật toán :

# Lap tu 1 den 3:
#   Nhap ma nhan vien
#   Nhap ho ten
#   Nhap phong ban
#   Neu ma nhan vien rong
#   HOAC ho ten rong:
#       In thong bao loi
#   Nguoc lai:
#       In phieu ho so nhan su



for employee_number in range(1, 4):

    print(f"\n--- Nhap thong tin nhan vien thu {employee_number} ---")

    employee_id = input("Nhap ma nhan vien: ")
    full_name = input("Nhap ho va ten: ")
    department = input("Nhap phong ban: ")

    if employee_id == "" or full_name == "":
        print("\nLOI: Ma nhan vien va Ho ten khong duoc de trong!")
    else:
        print("\n===== HO SO NHAN SU =====")
        print("Ma nhan vien :", employee_id)
        print("Ho ten       :", full_name)
        print("Phong ban    :", department)
        print("=========================")

print("\nDa hoan tat khoi tao ho so cho 3 nhan vien!")