student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

# Tính điểm trung bình của sinh viên
def calculate_average(student):
    return (student["math"]+ student["physics"]+ student["chemistry"]) / 3

# Xếp loại học lực
def get_rank(average):
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    else:
        return "Yếu"

#Tìm sinh viên theo mã
def find_student_by_id(records, student_id):
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None

# Nhập điểm hợp lệ từ 0 đến 10
def input_score():
    while True:
        score_input = input("Nhập điểm mới: ").strip()
        # Kiểm tra có phải số hay không
        if score_input.replace(".", "", 1).isdigit():
            score = float(score_input)
            if 0 <= score <= 10:
                return score
        print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
# Hiển thị bảng điểm
def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")
    for index, student in enumerate(records, start=1):
        average = calculate_average(student)
        rank = get_rank(average)
        print(f"{index}.  [{student['student_id']}] {student['name']} | Toán: {student['math']} | Lý: {student['physics']} | Hóa: {student['chemistry']} | ĐTB: {average:.2f} - {rank}")
    print("---------------------------")

# Cập nhật điểm sinh viên
def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(records,student_id)
    if student is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return
    subject = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa):: ").strip()
    score = input_score()
    if subject == "1":
        student["math"] = score
        subject_name = "Toán"
    elif subject == "2":
        student["physics"] = score
        subject_name = "Lý"
    elif subject == "3":
        student["chemistry"] = score
        subject_name = "Hóa"
    else:
        print("Lựa chọn môn học không hợp lệ!")
        return
    print(f">> Đã cập nhật điểm {subject_name} của sinh viên '{student['name']} thành {score}")

# Báo cáo thống kê
def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total = len(records)
    passed = 0
    failed = 0
    for student in records:
        average = calculate_average(student)
        if average >= 5:
            passed += 1
        else:
            failed += 1
    passed_percent = passed / total * 100
    failed_percent = failed / total * 100
    print(f"""
    --- BÁO CÁO HỌC VỤ ---
        Tổng số sinh viên: {total}
        Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên(Chiếm {passed_percent:.2f}%)
        Số lượng trượt (ĐTB < 5.0): {failed} sinh viên(Chiếm {failed_percent:.2f}%)
    ----------------------
    """)

# Tìm thủ khoa
def find_valedictorian(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    top_student = records[0]
    top_average = calculate_average(top_student)
    for student in records[1:]:
        average = calculate_average(student)
        if average > top_average:
            top_average = average
            top_student = student
    print(f"""
        --- VINH DANH THỦ KHOA ---
            Sinh viên: {top_student['name']}(Mã: {top_student['student_id']})
            Điểm Trung Bình: {top_average:.2f}
        Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!
        --------------------------
    """)

def main():
    while True:
        print("""
            ===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====
                        1. Xem bảng điểm và học lực
                        2. Cập nhật điểm thi sinh viên
                        3. Báo cáo thống kê (Đỗ/Trượt)
                        4. Tìm sinh viên Thủ khoa
                        5. Thoát chương trình
            ======================================================
            Chọn chức năng (1-5):            
""")
        choice = input("Chọn chức năng (1-5): ").strip()
        if choice == "1":
            display_grades(student_records)
        elif choice == "2":
            update_student_score(student_records)
        elif choice == "3":
            generate_report(student_records)
        elif choice == "4":
            find_valedictorian(student_records)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
main()