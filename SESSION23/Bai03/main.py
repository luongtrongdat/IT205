# import các module tùy chỉnh
from core.logistics import display_flights
from core.manager import add_flight, check_duplicate_id, is_valid_date
from utils.time_helper import calculate_arrive_predict_time
from utils.file_helper import create_path_file


# mock data
flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00",
        "duration_min": 120},  # Hà Nội - TP.HCM
    {"flight_id": "RA002", "passengers": 85,
        "depart_time": "2026-06-15 13:30:00", "duration_min": 45}   # Hà Nội - Vinh
]


def main():
    """Luồng điều hướng chính và hiển thị Menu Terminal liên tục."""
    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần")
        print("2. Tiếp nhận chuyến bay mới")
        print("3. Tính thời gian hạ cánh dự kiến (ETA)")
        print("4. Khởi tạo thư mục lưu trữ log hệ thống")
        print("5. Thoát chương trình")
        print("==================================================")

        choice_str = input("Nhập lựa chọn của bạn: ").strip()

        # --- 1. GUARD CLAUSE: Chặn trường hợp để trống lựa chọn ---
        if not choice_str:
            print("[Lỗi]: Vui lòng không được để trống lựa chọn!")
            continue

        # --- 2. KHỐI TRY-EXCEPT THU HẸP TỐI ĐA ---
        # Chỉ bọc đúng dòng ép kiểu có nguy cơ gây lỗi ValueError
        try:
            user_choice = int(choice_str)
            is_valid_format = True
        except ValueError:
            is_valid_format = False

        # --- 3. GUARD CLAUSE: Chặn trường hợp nhập chữ hoặc ký tự lạ ---
        if not is_valid_format:
            print(
                "[Lỗi]: Định dạng không hợp lệ! Vui lòng chỉ nhập số nguyên từ 1 đến 5.")
            continue

        # --- 4. CẤU TRÚC ĐIỀU HƯỚNG CHỨC NĂNG (Xóa bỏ else/elif cồng kềnh) ---
        if user_choice == 1:
            # Chức năng 1: Hiển thị lịch trình và Thống kê hậu cần
            display_flights(flights)
            continue

        if user_choice == 2:
            # Chức năng 2: Tiếp nhận chuyến bay mới
            add_flight(flights)
            continue

        if user_choice == 3:
            # Chức năng 3: Tính thời gian hạ cánh dự kiến (ETA)
            calculate_arrive_predict_time(flights)
            continue

        if user_choice == 4:
            # Chức năng 4: Khởi tạo thư mục lưu trữ log hệ thống
            path_name = create_path_file("aviation_logs")
            print(path_name)
            continue

        if user_choice == 5:
            print("\nCảm ơn bạn đã sử dụng hệ thống Rikkei Aviation. Tạm biệt!")
            break

        # Nếu chạy xuống tới đây nghĩa là số nằm ngoài khoảng 1-5 (Guard Clause cuối)
        print(
            "[Lỗi]: Lựa chọn không hợp lệ! Vui lòng nhập đúng số trong khoảng từ 1 đến 5.")


if __name__ == "__main__":
    main()


# câu 1 thầy tự xem file nha
# câu 2 việc sử dụng from math import * nó sẽ import tất cả các hàm của thằng math có vào, khiến bị dư thừa hàm và gây ô nhiễm không gian, và có thẻ dẫn đến xung đột tên gọi tên hàm