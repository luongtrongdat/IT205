# 1.Nhập thông tin bệnh nhân
user_name = input("Nhập tên bệnh nhân: ")
birth_year = int(input("Nhập năm sinh: "))
total_date = int(input("Nhập tổng số ngày bị bệnh: "))
body_temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
cost = float(input("Nhập chi phí điều trị (VNĐ): "))

# 2. Kiểm tra dữ liệu đầu vào
    # Tên không được để trống
if user_name == "":
    print("Tên bệnh nhân không được để trống.")
    # Năm sinh phải nằm trong khoảng hợp lệ (1900 → năm hiện tại)
if birth_year < 1900 or birth_year > 2026:
    print("Năm sinh không hợp lệ.")
    # Số ngày bị bệnh ≥ 0
if total_date < 0:
    print("Số ngày bị bệnh không hợp lệ.")
    # Nhiệt độ nằm trong khoảng 30 → 45°C
if body_temperature < 30 or body_temperature > 45:
    print("Nhiệt độ không hợp lệ.")
    # Chi phí khám > 0
if cost <= 0:
    print("Chi phí khám không hợp lệ.")
# 3. Tính toán thông tin
    # Tính tuổi bệnh nhân
my_age = 2026 - birth_year
    # Tính phụ phí = 10% chi phí khám
surcharge = cost * 0.1
    # Tính tổng chi phí = chi phí khám + phụ phí
total_cost = cost + surcharge
# 4. Phân loại tình trạng sức khỏe
    # Nếu nhiệt độ > 38°C và số ngày bệnh > 3 → "Nguy hiểm"
if body_temperature > 38 and total_date > 3:
    print("Nguy hiểm")
    # Nếu nhiệt độ > 38°C → "Sốt cao"
elif body_temperature > 38:
    print("Sốt cao")
    # Nếu nhiệt độ > 37.5°C → "Sốt nhẹ"
elif body_temperature > 37.5:
    print("Sốt nhẹ")
    # Ngược lại → "Bình thường"
else:
    print("Bình thường")
# 5. Đánh giá mức độ ưu tiên
    # Nếu tình trạng là "Nguy hiểm":
        # Nếu tuổi > 60 → "Cấp cứu"
if body_temperature > 38 and total_date > 3:
    if my_age > 60:
        print("Cấp cứu")
        # Ngược lại → "Ưu tiên cao"
    else:
        print("Ưu tiên cao")   
    # Các trường hợp khác:
        # → "Bình thường"
else:
    print("Bình thường")
# 6. Đánh giá mức chi phí (Toán tử 3 ngôi)
    # Nếu tổng chi phí > 500000 → "Cao"
    # Ngược lại → "Thấp"
evaluation = "Cao" if total_cost > 500000 else "Thấp"
print(f"Đánh giá mức chi phí: {evaluation}")