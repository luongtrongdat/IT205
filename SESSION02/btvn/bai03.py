user_name = input("Nhập tên bệnh nhân: ")
age = int(input("Nhập tuổi bệnh nhân: "))

print(f"Tên bệnh nhân: {user_name}")
print(f"Nhập tuổi bệnh nhân: {age}")

if age < 6:
    print("ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.")
elif age > 80:
    print("ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.")
else:
    print("KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.")