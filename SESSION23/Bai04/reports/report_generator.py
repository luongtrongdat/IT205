from datetime import datetime

# module báo cáo về danh sách học sinh
from data.students import student_records
from utils.score_utils import calculate_average

from colorama import Fore, Style, init

# xem danh sachs sinh viên và tính điểm trung bình


def display_student_scores(students: list):

    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")

    for position, student in enumerate(students):

        student_id = student.get('student_id', 'ERR00')
        student_name = student.get('name', 'Ẩn danh')
        scores = student.get('scores', [])

        # tính điểm trung bình
        avg_score, rank = calculate_average(scores)

        print(
            f"{position}. [{student_id}] {student_name:<16} | Điểm: {scores} | ĐTB: {avg_score:,.2f} - {rank}")


# hàm xuất báo cáo học tập
def export_learning_report(students: list):

    negative_students = 0
    positive_students = 0

    # lấy ra thời gian hiện tại
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")
    # lọc ra học sinh
    for student in students:
        if calculate_average(student['scores']) >= 5:
            positive_students += 1
        elif calculate_average(student['scores']) < 5:
            negative_students += 1

    # nội dung báo cáo
    content_report = f"""--- BAO CAO KET QUA HOC TAP ---
Tổng số sinh viên: {len(student)}
Số sinh viên đạt yêu cầu: {positive_students}
Số sinh viên cần cải thiện: {negative_students}
Thời gian ghi log: {formatted_now}
----------------------------------"""

    # ghi báo cáo ra file log
    file_name = "learning_report.txt"
    with open(file_name, "w", encoding= "utf-8") as file:
        file.write(content_report)

    print(Fore.GREEN + f"✔ Đã ghi báo cáo thành công vào file '{content_report}'!")
    print(Fore.YELLOW + f"  Thời gian tạo: {formatted_now}")