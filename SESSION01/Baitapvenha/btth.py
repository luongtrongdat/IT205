user_name = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính (Nam/Nữ): ")
date_birth = int(input("Nhập năm sinh: "))
phone_number = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symtom = input("Nhập triệu chứng: ")
cost = float(input("Nhập chi phí khám bệnh: "))

# Tạo mã bệnh nhân ngẫu nhiên
code = f"NV{date_birth}001"

# In ra màn hình
print("--- THẺ BÊNH NHÂN ---")
# infomation = f"Mã BN: {code}\nHọ tên: {user_name}\nGiới tính: {gender}\nNăm sinh: {date_birth}\nSố điện thoại: {phone_number}\nEmail: {email}\nTriệu chứng: {symtom}\nChi phí khám bệnh: {cost}"
infomation = f"""
    Mã BN: {code}
    Họ tên: {user_name}
    Giới tính: {gender}
    Năm sinh: {date_birth}
    Số điện thoại: {phone_number}
    Email: {email}
    Triệu chứng: {symtom}
    Chi phí khám bệnh: {cost}
"""
print(infomation)
