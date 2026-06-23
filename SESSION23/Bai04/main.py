"""Module quản lý giao diện điều hướng chính của Hệ thống tiện ích học tập Rikkei Academy."""
from data.students import student_records  # dữ liệu gốc
from reports.report_generator import display_student_scores, export_learning_report
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code


def main():
    """Luồng điều hướng chính và hiển thị Menu Terminal liên tục."""
    while True:
        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")

        choice_str = input("Chọn chức năng (1-5): ").strip()

        # --- 1. GUARD CLAUSE: Chặn trường hợp bấm Enter để trống ---
        if not choice_str:
            print("[Lỗi]: Vui lòng không được để trống lựa chọn!")
            continue

        # --- 2. KHỐI TRY-EXCEPT THU HẸP TỐI ĐA ---
        # Chỉ bọc đúng duy nhất dòng ép kiểu dữ liệu để phòng thủ lỗi nhập chữ
        try:
            user_choice = int(choice_str)
            is_valid_format = True
        except ValueError:
            is_valid_format = False

        # --- 3. GUARD CLAUSE: Chặn trường hợp nhập ký tự hoặc chữ cái ---
        if not is_valid_format:
            print(
                "[Lỗi]: Định dạng không hợp lệ! Vui lòng chỉ nhập số nguyên từ 1 đến 5.")
            continue

        # --- 4. ĐIỀU HƯỚNG CHỨC NĂNG BẰNG MATCH-CASE (Xóa bỏ hoàn toàn else/elif) ---
        match user_choice:
            case 1:
                # Chức năng 1: Xem danh sách sinh viên và điểm trung bình
                # chuẩn hóa trước khi in điểm
                normalize_student_names(student_records)
                display_student_scores(student_records)
            case 2:
                # Chức năng 2: Chuẩn hóa tên sinh viên
                normalize_student_names(student_records)
            case 3:
                # Chức năng 3: Sinh mã bài tập ngẫu nhiên
                generate_assignment_code()
            case 4:
                # Chức năng 4: Xuất báo cáo học tập
                export_learning_report(student_records)
            case 5:
                print("\nCảm ơn bạn đã sử dụng hệ thống Rikkei Academy. Tạm biệt!")
                break  # Bẻ gãy vòng lặp while True để thoát chương trình an toàn

            case _:
                # Tấm lưới bảo vệ tóm toàn bộ các số nguyên nằm ngoài khoảng 1-5
                print(
                    "[Lỗi]: Lựa chọn không hợp lệ! Vui lòng nhập đúng số trong khoảng từ 1 đến 5.")


if __name__ == "__main__":
    main()
