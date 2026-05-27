user_name = input("nhập tên bệnh nhân: ")
Id = input("nhập id bệnh nhân: ")
temperature = float(input("nhập nhiệt độ cơ thể: "))
heart_rate = int(input("nhập nhịp tim BN: "))
weight = int(input("nhập cân nặng bệnh nhân: "))
examination_form = f"""
    ---  Phiếu Khám Bệnh Điện Tử ---
    Tên BN: {user_name}
    Mã BN: {Id}
    Nhiệt độ cơ thể: {temperature}
    Nhịp tim: {heart_rate}
    Cân nặng: {weight}
"""

system_log = f"""
    --- Log hệ thống ---
    Biến: 'user_name' | Giá trị: {user_name} | Kiểu dữ liệu: {type(user_name)}
    Biến: 'Id' | Giá trị: {Id} | Kiểu dữ liệu: {type(Id)}
    Biến: 'temperature' | Giá trị: {temperature} | Kiểu dữ liệu: {type(temperature)}
    Biến: 'heart_rate' | Giá trị: {heart_rate} | Kiểu dữ liệu: {type(heart_rate)}
    Biến: 'weight' | Giá trị: {weight} | Kiểu dữ liệu: {type(weight)}
"""

print(examination_form)
print(system_log)