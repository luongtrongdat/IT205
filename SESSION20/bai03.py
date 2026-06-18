import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    filename='tournament_app.log'
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]

def display_matches(match_list):
    """
    Hiển thị lịch thi đấu và kết quả dưới dạng cột rõ ràng.

    Args:
        match_list (list): Danh sách các trận đấu.
    """
    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    logging.info("User viewed the match list.")
    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10} | {'Đội A':<15} | {'Đội B':<15} | {'Tỷ số':<10} | {'Trạng thái'}")
    print("-" * 70)

    for match in match_list:
        try:
            score_str = f"{match['score_a']}-{match['score_b']}"
            print(
                f"{match['match_id']:<10} | {match['team_a']:<15} | {match['team_b']:<15} | {score_str:<10} | {match['status']}")
        except KeyError as e:
            logging.error(f"Dữ liệu trận đấu thiếu key: {e}")


def add_match(match_list):
    """
    Thêm một trận đấu mới vào hệ thống với trạng thái mặc định là Pending.

    Args:
        match_list (list): Danh sách các trận đấu.
    """
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    match_id = input("Nhập mã trận đấu: ").strip()

    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    if any(match['match_id'].upper() == match_id.upper() for match in match_list):
        print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
        logging.warning(f"Match ID {match_id} already exists.")
        return

    team_a = input("Nhập tên Đội A: ").strip()
    if not team_a:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    team_b = input("Nhập tên Đội B: ").strip()
    if not team_b:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    match_list.append(new_match)
    print(f"Thành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully")


def update_score(match_list):
    """
    Cập nhật tỷ số trận đấu, bẫy lỗi nhập liệu bằng try...except ValueError.

    Args:
        match_list (list): Danh sách các trận đấu.
    """
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()

    target_match = None
    for match in match_list:
        if match['match_id'].upper() == match_id.upper():
            target_match = match
            break

    if not target_match:
        print(f"Không tìm thấy trận đấu mang mã {match_id}.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return

    print(
        f"Trận đấu: {target_match['team_a']} vs {target_match['team_b']} ({target_match['status']})")

    while True:
        try:
            score_a_input = input("Nhập điểm Đội A: ").strip()
            score_a = int(score_a_input)
            if score_a < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_a}")
                continue
            break
        except ValueError as e:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: {e}")

    while True:
        try:
            score_b_input = input("Nhập điểm Đội B: ").strip()
            score_b = int(score_b_input)
            if score_b < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_b}")
                continue
            break
        except ValueError as e:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: {e}")

    status = "Completed"
    if score_a == 0 and score_b == 0:
        confirm = input(
            "Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").strip().lower()
        if confirm != 'y':
            status = "Pending"

    target_match['score_a'] = score_a
    target_match['score_b'] = score_b
    target_match['status'] = status

    print(
        f"Thành công: Đã cập nhật tỷ số trận đấu {target_match['match_id']}.")
    logging.info(
        f"Match {target_match['match_id']} score updated successfully")


def determine_winner(match):
    """
    Hàm phụ trợ xác định đội chiến thắng dựa trên thông tin trận đấu.

    Args:
        match (dict): Chi tiết một trận đấu.
    Returns:
        str: Tên đội thắng, 'Draw' nếu hòa, hoặc 'Not Started' nếu chưa đá xong.
    """
    try:
        if match['status'] == "Pending":
            return "Not Started"
        if match['score_a'] > match['score_b']:
            return match['team_a']
        elif match['score_b'] > match['score_a']:
            return match['team_b']
        else:
            return "Draw"
    except KeyError as e:
        logging.error(f"Lỗi cấu trúc dữ liệu trận đấu khi tìm đội thắng: {e}")
        return "Error"


def generate_report(match_list):
    """
    In báo cáo thống kê các trận đấu đã hoàn thành và tổng số lượng.

    Args:
        match_list (list): Danh sách các trận đấu.
    """
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    completed_count = 0

    for match in match_list:
        if match.get('status') == "Completed":
            winner = determine_winner(match)
            print(
                f"{match['match_id']}: {match['team_a']} {match['score_a']}-{match['score_b']} {match['team_b']} | Kết quả: {winner}")
            completed_count += 1

    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")

    print(f"Tổng số trận đã hoàn thành: {completed_count}")
    logging.info("User generated tournament report.")



while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
    print("1. Hiển thị lịch thi đấu & Kết quả")
    print("2. Thêm trận đấu mới")
    print("3. Cập nhật tỷ số trận đấu")
    print("4. Báo cáo thống kê")
    print("5. Thoát chương trình")
    print("==================================================")

    choice = input("Chọn chức năng (1-5): ").strip()

    if choice == "1":
        display_matches(matches)
    elif choice == "2":
        add_match(matches)
    elif choice == "3":
        update_score(matches)
    elif choice == "4":
        generate_report(matches)
    elif choice == "5":
        print("Hệ thống đang đóng. Tạm biệt!")
        logging.info("System shutdown code 5.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")
        logging.warning("Invalid menu choice selected")