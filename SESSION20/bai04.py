# I. PHÂN TÍCH THIẾT KẾ
# - Áp dụng PEP 8: snake_case, hàm 1 nhiệm vụ, tên biến rõ nghĩa.
# - Logging: lưu file roster_app.log, format [%(asctime)s] - [%(levelname)s] - %(message)s.
# - update_player_status(roster_list):
#   Input: danh sách tuyển thủ.
#   Output: cập nhật lương hoặc trạng thái.
#   Exceptions: ValueError (lương không hợp lệ), không tìm thấy ID.
#   Pseudocode:
#   1. Nhập ID.
#   2. Tìm tuyển thủ.
#   3. Chọn cập nhật lương hoặc trạng thái.
#   4. Kiểm tra dữ liệu.
#   5. Cập nhật và ghi log.

import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]


def calculate_actual_pay(player):
    match player["status"]:
        case "Benched":
            return player["salary"] * 0.5
        case _:
            return player["salary"]


def find_player(roster_list, player_id):
    return next(
        (
            player
            for player in roster_list
            if player["player_id"] == player_id
        ),
        None
    )


def display_roster(roster_list):
    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")

    for player in roster_list:

        status = player.get("status", "Unknown")
        name = player["name"]

        if status == "Benched":
            name += " [DỰ BỊ]"

        print(
            f"{player['player_id']:<8}"
            f"{name:<25}"
            f"{player['role']:<15}"
            f"{player['salary']:<12,.1f}"
            f"{status}"
        )

    logging.info("Coach viewed the team roster.")


def sign_player(roster_list):

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    if find_player(roster_list, player_id):
        print(f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại.")
        logging.warning(
            f"Failed to sign player - Duplicate player ID {player_id}"
        )
        return

    name = input("Nhập tên tuyển thủ: ").title()
    role = input("Nhập vị trí thi đấu: ").title()

    while True:
        try:
            salary = float(
                input("Nhập mức lương hàng tháng: ")
            )

            if salary <= 0:
                print("Lương phải là số dương.")
                continue

            break

        except ValueError:
            print("Lương phải là số.")
            logging.warning(
                "Failed to sign player - Invalid salary input"
            )

    roster_list.append(
        {
            "player_id": player_id,
            "name": name,
            "role": role,
            "salary": salary,
            "status": "Active"
        }
    )

    logging.info(
        f"Signed new player {name} with salary {salary}"
    )

    print(f"Đã chiêu mộ {name}.")


def update_player_status(roster_list):

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    player = find_player(
        roster_list,
        player_id
    )

    if not player:
        print(f"Không tìm thấy {player_id}.")
        logging.warning(
            f"Failed to update player - Player ID {player_id} not found"
        )
        return

    print(f"\nTuyển thủ: {player['name']}")
    print(f"Lương: {player['salary']}")
    print(f"Trạng thái: {player['status']}")

    choice = input(
        "\n1. Cập nhật lương\n2. Cập nhật trạng thái\nChọn: "
    )

    match choice:

        case "1":

            while True:

                try:

                    new_salary = float(
                        input("Nhập lương mới: ")
                    )

                    if new_salary <= 0:
                        print("Lương phải là số dương.")
                        continue

                    old_salary = player["salary"]
                    player["salary"] = new_salary

                    logging.info(
                        f"Updated player {player_id} salary "
                        f"from {old_salary} to {new_salary}"
                    )

                    print("Cập nhật thành công.")
                    break

                except ValueError:
                    print("Lương không hợp lệ.")

        case "2":

            status_choice = input(
                "1. Active\n2. Benched\nChọn: "
            )

            old_status = player["status"]

            match status_choice:
                case "1":
                    player["status"] = "Active"
                case "2":
                    player["status"] = "Benched"
                case _:
                    print("Lựa chọn không hợp lệ.")
                    return

            logging.info(
                f"Updated player {player_id} status "
                f"from {old_status} to {player['status']}"
            )

            print("Cập nhật thành công.")

        case _:
            print("Lựa chọn không hợp lệ.")


def generate_payroll_report(roster_list):

    print("\n--- BÁO CÁO QUỸ LƯƠNG ---")

    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return

    total_payroll = 0

    try:

        for player in roster_list:

            actual_pay = calculate_actual_pay(player)

            print(
                f"{player['player_id']:<8}"
                f"{player['name']:<15}"
                f"{player['status']:<12}"
                f"{player['salary']:<12,.1f}"
                f"{actual_pay:,.1f}"
            )

            total_payroll += actual_pay

        print("-" * 60)
        print(
            f"Tổng quỹ lương: {total_payroll:,.1f}"
        )

        logging.info(
            f"Generated monthly payroll report. Total: {total_payroll}"
        )

    except KeyError as error:

        print(
            "Lỗi: Một tuyển thủ đang bị thiếu dữ liệu."
        )

        logging.error(
            f"Missing key while generating payroll report: {error}"
        )


def main():

    while True:

        print("\n===== RIKKEI ESPORTS =====")
        print("1. Xem đội hình")
        print("2. Chiêu mộ tuyển thủ")
        print("3. Cập nhật thông tin")
        print("4. Báo cáo quỹ lương")
        print("5. Thoát")

        choice = input("Chọn chức năng: ")

        match choice:

            case "1":
                display_roster(roster)

            case "2":
                sign_player(roster)

            case "3":
                update_player_status(roster)

            case "4":
                generate_payroll_report(roster)

            case "5":
                logging.info("System shutdown.")
                print("Tạm biệt.")
                break

            case _:
                print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()