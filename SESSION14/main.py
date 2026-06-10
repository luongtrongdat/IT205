"""
Tham số: các biến định nghĩa hàm(dạng tổng quát)
Đối số: giá trị thực tế
"""
def get_information_of_student(name, age, school):
    print(f"{name}, {age}, {school}")


## Các loại tham số:
# Tham số thông thường
"""
Bắt buộc truyền đối số
"""
def get_stu1(name, age, school):
    print(f"{name}, {age}, {school}")

# Tham số mặc định
"""
Nếu mà k có đối số -> truyền mặc định giá trị khởi tạo tham số
Nếu mà có đối số -> lấy giá trị mới
"""
def get_stu2(name = "Dat", age = 18, school = "FPT"):
    print(f"{name}, {age}, {school}")
get_stu2("Datta", 17, "PTIT")

# Tham số từ khóa
def get_stu3(name, age, school):
    print(f"{name}, {age}, {school}")
get_stu3(name = "Hoang", age = 18, school = "NEU")

# Tham số args



