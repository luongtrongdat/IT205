Id = input("Nhập id BN: ")
body_temperature = float(input("Nhập nhiệt độ cơ thể: "))
type_body_temperature = type(body_temperature)
heart_rate = int(input("nhập nhịp tim: "))
type_heart_rate = type(heart_rate)
infomaton = f"""
            --- Kết quả chuẩn hóa dữ liệu ---
            Mã BN:{Id}
            Nhiệt độ cơ thể: {body_temperature}
            Kiểu dữ liệu ghi nhận <class '{type_body_temperature}'>
            Nhịp tim: {heart_rate}
            Kiểu dữ liệu ghi nhận <class '{type_heart_rate}'>
"""
print(infomaton)