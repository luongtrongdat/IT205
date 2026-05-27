# 1.Toán tử số học
first_num = 20
second_num = 30

print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
print(f"{first_num} * {second_num} = {first_num * second_num}") 
print(f"{first_num} / {second_num} = {first_num / second_num}")
# Toán tử chia lấy phần nguyên
print(f"{first_num} // {second_num} = {first_num // second_num}") 
# Toán tử chia lấy phần dư
print(f"{first_num} % {second_num} = {first_num % second_num}")

# 2. Toán tử so sánh
print(f"{first_num} > {second_num} = {first_num > second_num}") # False
print(f"{first_num} < {second_num} = {first_num < second_num}") # True
print(f"{first_num} >= {second_num} = {first_num >= second_num}") # False
print(f"{first_num} <= {second_num} = {first_num <= second_num}") # True
print(f"{first_num} == {second_num} = {first_num == second_num}") # False
print(f"{first_num} != {second_num} = {first_num != second_num}") # True

# 3. Toán tử logic: and, or, not
# Trong python sẽ có 1 số giá trị là False: 0, False, "", (), [], {}
first_result = 20 > 10 and 30 > 20 and 100
second_result = 0 or 30 > 20 or 100
print(f"first_result = {first_result}")
print(f"second_result = {second_result}")
print(f"not second_result = {not second_result}")

# 4. Cấu trúc điều kiện
# Lưu ý: Trong python để thể hiện 1 block code thì dùng tab thay cho {}
# - Trường hợp bài toán chỉ có 1 điều kiện duy nhất
age = 18
if age >= 18:
    print("Bạn đã đủ tuổi thi bằng lái xe.")
# - Trường hợp bài toán có 2 điều kiện
gender = "male"
if gender == "male":
    print("Bạn là nam.")
else:
    print("Bạn là nữ.")
# - Trường hợp bài toán có nhiều hơn 2 điều kiện trở lên và điều kiện phải nằm trong khoảng nào đó
avg_point = 8.5
if avg_point >= 9 and avg_point <= 10:
    print("Bạn đạt loại xuất sắc.")
elif avg_point >= 8 and avg_point < 9:
    print("Bạn đạt loại giỏi.")
elif avg_point >= 6.5 and avg_point < 8:
    print("Bạn đạt loại khá.")
elif avg_point >= 5 and avg_point < 6.5:
    print("Bạn đạt loại trung bình.")
else:
    print("Bạn đạt loại yếu.")

# Math case
status = "ACTIVE" # ACTIVE, INACTIVE, PAUSE_ACTIVE
match status:
    case "ACTIVE":
        print("Đang hoạt động.")
    case "INACTIVE":
        print("Ngừng hoạt động.")
    case "PAUSE_ACTIVE":
        print("Tạm dừng hoạt động.")
    case _:
        print("Trạng thái không xác định.")

# Điều kiện lồng nhau
# Kiểm tra điều kiện thi bằng lái: tuổi > 18, độ cận < 3
my_age = 18
my_cant = 5
if my_age >= 18:
    # Tiếp tục kiểm tra độ cận
    if my_cant < 3:
        print("Bạn đủ tuổi thi bằng lái xe. Kết luận không đạt")
    else:
        print("Bạn không đủ tuổi thi bằng lái xe.")
else:
    print("Chưa đủ tuổi thi bằng lái xe.")

# 5. Toán tử 3 ngôi
print(f"{"NAM" if gender == "MALE" else  "NỮ"}")
print(True and False)