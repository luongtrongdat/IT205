# Vòng lặp for
# for index in list/string/range()/tuple/dict:
#     # code block

# range(): tạo ra một dãy số nguyên. lưu ý: range(1,5) => 1,2,3,4
# In ra dãy số từ 1 đến 10
for value in range(1, 11):
    print(value)

# Dùng range() chỉ cho tham số là stop: nếu không có start thì mặc định sẽ là 0
for value in range(11):
    print(value)

# In ra dãy số chẵn từ 0 đến 10
for value in range(0, 11, 2):
    print(value)

# Tính tổng các số từ 1 đến 10
    # Khởi tạo biến tổng
total = 0
    # Tạo 1 dãy số từ 1 đến 10
for value in range(1, 11):
    # Cộng dần các số vào biến tổng
    total += value

print(f"Tổng các số từ 1 đến 10 là: {total}")

print("----- Vòng lặp while -----")
# while condition:
#     # code block
#     # Tăng giá trị của biến khởi tạo làm điều kiện

# In ra các số từ 1 đến 10 bằng vòng lặp while
initial_value = 1
while initial_value <= 10:
    print(initial_value)
    # Tăng giá trị của biến khởi tạo lên 1 đơn vị để tránh vòng lặp vô hạn
    initial_value += 1

# Xây dựng ứng dụng đăng nhập cho phép người dùng nhập mật khẩu tối đa 3 lần,
# nếu nhập đúng thì in ra "Thành công", nếu nhập sai quá 3 lần thì in ra "Khóa tài khoản"
    # Mật khẩu đúng
password = "123456"
    # Biến phát hiện khi nào đăng nhập thanh công
is_success = False
    # Biến đếm số lần đăng nhập thất bại
counter_failed_login = 0
    # Điều kiện dừng
while not is_success and counter_failed_login < 3:
    password_input = input("Nhập mật khẩu: ")
    # Logic xử lý
    if password_input == password:
        print("Thành công")
        is_success = True
    else:
        print("Thất bại")
        # Tăng biến đếm số lần đăng nhập thất bại lên 1 đơn vị
        counter_failed_login += 1

# Tạo ứng dụng in ra bảng cửu chương từ 2 đến 9
for first_value in range(2, 10):
    print(f"Bảng cửu chương {first_value}")
    # Tạo ra dãy số từ 1 đến 10
    for second_value in range(1, 11):
        print(f"{first_value} x {second_value} = {first_value*second_value}")

