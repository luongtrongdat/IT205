"""
Module score_utils.py
Vai trò:Xử lý tính toán điểm
Hàm chính:
    calculate_average()
    classify_student()
Kiểu import:
    from utils.score_utils import calculate_average

Module string_utils.py
Vai trò:Chuẩn hóa tên sinh viên
Hàm chính:
    normalize_student_names()
Kiểu import:
    from utils.string_utils import normalize_student_names
Module random_utils.py
Vai trò:
    Sinh mã bài tập ngẫu nhiên
Hàm chính:
    generate_assignment_code()
Module chuẩn sử dụng:
    random
    string
Kiểu import:
    import random
    import string as st
Module report_generator.py
Vai trò:Hiển thị danh sách sinh viên và xuất báo cáo
Hàm chính:
    display_student_scores()
    export_learning_report()
Module chuẩn sử dụng:
    datetime
Third-party:
    colorama

    
Hàm calculate_average(scores)
Input:list
Output:float
Module:utils.score_utils
Pseudocode:
    Nếu scores rỗng:
        trả về 0
    Lọc ra các phần tử kiểu int hoặc float
    Nếu không còn phần tử hợp lệ:
        trả về 0
    average = tổng / số lượng
    return average

Hàm classify_student(average)
Input:float
Output:str
Module:utils.score_utils
Pseudocode:
    Nếu average >= 8:
        Giỏi
    Nếu average >= 6.5:
        Khá
    Nếu average >= 5:
        Trung bình
    Ngược lại:
        Yếu

Hàm display_student_scores(records)
Input:list
Output:Không có
Module:reports.report_generator
Pseudocode:
    Nếu danh sách rỗng:
        thông báo
    Duyệt từng sinh viên
    Tính ĐTB
    Xếp loại
    In ra màn hình

Hàm normalize_student_names(records)
Input:list
Output:Không có
Module:utils.string_utils
Pseudocode:
    Nếu danh sách rỗng:
        thông báo
    Duyệt từng sinh viên
    Cập nhật lại tên

Hàm generate_assignment_code()
Input:Không có
Output:str
Module:utils.random_utils
Pseudocode:
    Tạo tập ký tự chữ hoa + số
    Sinh ngẫu nhiên 4 ký tự
    Ghép thêm "PY-"
    Trả về kết quả

Hàm export_learning_report(records)
Input:list
Output:File learning_report.txt
Module:reports.report_generator
Pseudocode:
    Nếu danh sách rỗng:
        thông báo
    Tính tổng sinh viên
    Tính số đạt
    Tính số chưa đạt
    Lấy thời gian hiện tại
    Ghi ra learning_report.txt
    Hiển thị thông báo màu xanh bằng colorama

"""

from data.students import student_records

from reports.report_generator import (
    display_student_scores,
    export_learning_report
)

from utils.string_utils import (
    normalize_student_names
)

from utils.random_utils import (
    generate_assignment_code
)


def main():

    while True:

        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")

        try:

            choice = int(
                input("Chọn chức năng (1-5): ")
            )

            if choice == 1:

                display_student_scores(
                    student_records
                )

            elif choice == 2:

                normalize_student_names(
                    student_records
                )

            elif choice == 3:

                print("\n--- SINH MÃ BÀI TẬP ---")

                assignment_code = (
                    generate_assignment_code()
                )

                print(
                    f"Mã bài tập của bạn là: "
                    f"{assignment_code}"
                )

            elif choice == 4:

                export_learning_report(
                    student_records
                )

            elif choice == 5:

                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )

                break

            else:

                print(
                    "Chức năng không hợp lệ. "
                    "Vui lòng chọn từ 1 đến 5."
                )

        except ValueError:

            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 5."
            )


main()