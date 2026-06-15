students = []

# Tính điểm trung bình
def calculate_average(math, physics, chemistry):
    return round((math + physics + chemistry) / 3, 2)

# Xếp loại học lực
def classify_student(avg):
    if avg < 5:
        return "Yếu"
    elif avg < 7:
        return "Trung bình"
    elif avg < 8:
        return "Khá"
    else:
        return "Giỏi"

# Nhập điểm hợp lệ
def input_score(subject):
    while True:
        score = float(input(f"Nhập điểm {subject}: "))
        if 0 <= score <= 10:
            return score            
        else:
            print("🙄 Điểm phải nằm trong khoảng từ 0 đến 10!")
# Tìm kiếm sinh viên theo mã
def find_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

# Hiện thị danh sách sinh viên
def display_students(student_list = None):
    if student_list is None:
        student_list = students

    if len(student_list) == 0:
        print("\n🥱 Danh sách sinh viên trống!")
        return
    print("\n" + "=" * 98)
    print(
        f"{'Mã SV':<10}|"
        f"{'Họ tên':<25}|"
        f"{'Toán':<10}|"
        f"{'Lý':<10}|"
        f"{'Hóa':<10}|"
        f"{'Điểm TB':<12}|"
        f"{'Xếp loại':<15}|"
    )
    print("=" * 98)

    for student in student_list:
        print(
            f"{student['id']:<10}|"
            f"{student['name']:<25}|"
            f"{student['math']:<10}|"
            f"{student['physics']:<10}|"
            f"{student['chemistry']:<10}|"
            f"{student['average']:<12}|"
            f"{student['rank']:<15}|"
        )

    print("=" * 98)
# Thêm sinh viên
def add_student():
    print("\n===== THÊM SINH VIÊN =====")
    while True:
        student_id = input("Nhập mã sinh viên: ").strip()
        if student_id == "":
            print("😑 Mã sinh viên không được để trống!")
            continue
        if find_student_by_id(student_id):
            print("😏 Mã sinh viên đã tồn tại!")
            continue
        break
    while True:
        name = input("Nhập họ tên sinh viên: ").strip()
        if name == "":
            print("😡 Tên sinh viên không được để trống!")
        else:
            break
    math = input_score("Toán")
    physics = input_score("Lý")
    chemistry = input_score("Hóa")
    avg = calculate_average(math, physics, chemistry)
    rank = classify_student(avg)
    student = {
        "id": student_id,
        "name": name,
        "math": math,
        "physics": physics,
        "chemistry": chemistry,
        "average": avg,
        "rank": rank
    }
    students.append(student)
    print("😊 Thêm sinh viên thành công!")

# Xóa sinh viên
def delete_student():
    print("\n===== XÓA SINH VIÊN =====")

    student_id = input("Nhập mã sinh viên cần xóa: ").strip()

    student = find_student_by_id(student_id)

    if not student:
        print("🤗 Không tìm thấy sinh viên!")
        return

    confirm = input(
        f"🤔 Bạn có chắc muốn xóa {student['name']}? (y/n): "
    ).lower()

    if confirm == "y":
        students.remove(student)
        print("😌 Đã xóa sinh viên thành công!")
    else:
        print("🙄 Đã hủy thao tác xóa.")
# Thống kê điểm trung bình
def statistics():
    if len(students) == 0:
        print("😪 Danh sách sinh viên trống!")
        return

    gioi = 0
    kha = 0
    trung_binh = 0
    yeu = 0

    for student in students:
        if student["rank"] == "Giỏi":
            gioi += 1
        elif student["rank"] == "Khá":
            kha += 1
        elif student["rank"] == "Trung bình":
            trung_binh += 1
        else:
            yeu += 1

    print("\n===== THỐNG KÊ ĐIỂM TRUNG BÌNH =====")
    print(f"Giỏi       : {gioi}")
    print(f"Khá        : {kha}")
    print(f"Trung bình : {trung_binh}")
    print(f"Yếu        : {yeu}")
# Menu 
while True:
    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm sinh viên")
    print("3. Cập nhật kết quả học tập")
    print("4. Xóa sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Thống kê điểm trung bình")
    print("7. Phân loại học lực")
    print("8. Thoát")
    print("=" * 45)

    choice = input("💢 Chọn chức năng: ")
    if choice == "1":
        display_students()
    elif choice == "2":
        add_student()
    # elif choice == "3":

    elif choice == "4":
        delete_student()
    # elif choice == "5":

    elif choice == "6":
        statistics()
    # elif choice == "7":

    elif choice == "8":
        print("🤢 Thoát chương trình! 🤮")
        break
    else:
        print("🤬 Vui lòng chọn từ 1 đến 8")