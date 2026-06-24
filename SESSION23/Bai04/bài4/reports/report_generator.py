from datetime import datetime

from colorama import Fore, Style

from utils.score_utils import (
    calculate_average,
    classify_student
)


def display_student_scores(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        average = calculate_average(
            student["scores"]
        )

        classification = classify_student(
            average
        )

        print(
            f'{index}. '
            f'[{student["student_id"]}] '
            f'{student["name"]} | '
            f'Điểm: {student["scores"]} | '
            f'ĐTB: {average:.2f} - '
            f'{classification}'
        )

    print("---------------------------------")


def export_learning_report(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)

    passed_students = 0

    weak_students = 0

    for student in records:

        average = calculate_average(
            student["scores"]
        )

        if average >= 5:
            passed_students += 1
        else:
            weak_students += 1

    current_time = datetime.now()

    with open(
            "learning_report.txt",
            "w",
            encoding="utf-8"
    ) as file:

        file.write(
            "===== BÁO CÁO HỌC TẬP =====\n"
        )

        file.write(
            f"Thời gian tạo báo cáo: "
            f"{current_time}\n"
        )

        file.write(
            f"Tổng số sinh viên: "
            f"{total_students}\n"
        )

        file.write(
            f"Số sinh viên đạt yêu cầu: "
            f"{passed_students}\n"
        )

        file.write(
            f"Số sinh viên cần cải thiện: "
            f"{weak_students}\n"
        )

    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(
        f"Tổng số sinh viên: "
        f"{total_students}"
    )
    print(
        f"Số sinh viên đạt yêu cầu: "
        f"{passed_students}"
    )
    print(
        f"Số sinh viên cần cải thiện: "
        f"{weak_students}"
    )

    print(
        Fore.GREEN
        + ">> Đã xuất báo cáo ra file learning_report.txt"
        + Style.RESET_ALL
    )