# module liên quan đến chức năng về chuỗi
from data.students import student_records  # import dữ liệu

# ==== FUNCTION THỰC HIỆN CÁC CHỨC NĂNG
# Xóa khoảng trắng thừa ở đầu và cuối.
# Chuyển nhiều khoảng trắng giữa các từ thành một khoảng trắng.
# Viết hoa chữ cái đầu mỗi từ.


def normalize_student_names(students: list):

    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for position, student in enumerate(students, start=1):
        # # Ghi đè tên đã chuẩn hóa trực tiếp vào key 'name' của từng học sinh
        student['name'] = " ".join(student['name'].split()).title()

        print(f"{position}: {student['name']}")
        
