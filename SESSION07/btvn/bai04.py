count = int(
    input("Nhập số lượng phiếu đăng ký: ")
)

# Bẫy 1
if count <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:
    for index in range(count):

        print(f"\n--- Phiếu đăng ký {index + 1} ---")
        raw_data = input("Nhập thông tin đăng ký: ")
        parts = raw_data.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        full_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        course_code = course_name.upper().replace( " ","-")

        confirm_code = (student_code + "_" + course_code)
        
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {full_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_code}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirm_code}")