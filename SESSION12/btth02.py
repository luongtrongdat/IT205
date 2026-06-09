saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("\nDanh sách sổ tiết kiệm:")
            count = 1
            for account in saving_accounts:
                print(
                    f"{count}. Mã sổ: {account['account_id']} | "
                    f"Khách hàng: {account['customer_name']} | "
                    f"Số tiền gửi: {account['balance']} | "
                    f"Kỳ hạn: {account['term_months']} tháng | "
                    f"Lãi suất: {account['interest_rate']}%/năm | "
                    f"Trạng thái: {account['status']}"
                )
                count += 1

    elif choice == "2":
        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        customer_name = input("Nhập tên khách hàng: ").strip()

        if customer_name == "":
            print("Tên khách hàng không được để trống")
            continue

        duplicate_id = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                duplicate_id = True
                break

        if duplicate_id:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue

        balance = input("Nhập số tiền gửi: ")
        term_months = input("Nhập kỳ hạn gửi theo tháng: ")

        if balance.isdigit() and term_months.isdigit():
            balance = int(balance)
            term_months = int(term_months)

            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
        else:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue

        interest_rate = input("Nhập lãi suất năm: ")

        if interest_rate.replace(".", "").isdigit() and float(interest_rate) > 0:
            interest_rate = float(interest_rate)
        else:
            print("Lãi suất không hợp lệ!")
            continue

        new_account = {
            "account_id": account_id,
            "customer_name": customer_name,
            "balance": balance,
            "term_months": term_months,
            "interest_rate": interest_rate,
            "status": "active"
        }

        saving_accounts.append(new_account)
        print("Mở sổ tiết kiệm thành công!")

    # Chức năng 3
    elif choice == "3":
        account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                    break

                customer_name = input("Nhập tên khách hàng mới: ").strip()

                if customer_name == "":
                    print("Tên khách hàng không được để trống")
                    break

                balance = input("Nhập số tiền gửi mới: ")
                term_months = input("Nhập kỳ hạn mới theo tháng: ")

                if balance.isdigit() and term_months.isdigit():
                    balance = int(balance)
                    term_months = int(term_months)

                    if balance <= 0 or term_months <= 0:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        break
                else:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    break

                interest_rate = input("Nhập lãi suất năm mới: ")

                if interest_rate.replace(".", "").isdigit() and float(interest_rate) > 0:
                    interest_rate = float(interest_rate)
                else:
                    print("Lãi suất không hợp lệ!")
                    break

                account["customer_name"] = customer_name
                account["balance"] = balance
                account["term_months"] = term_months
                account["interest_rate"] = interest_rate

                print("Cập nhật thành công!")
                break

        if found == False:
            print("Không tìm thấy mã sổ tiết kiệm!")

    # Chức năng 4
    elif choice == "4":
        account_id = input("Nhập mã sổ tiết kiệm cần tất toán: ").strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True
                account["status"] = "closed"
                print("Tất toán thành công!")
                break

        if found == False:
            print("Không tìm thấy mã sổ tiết kiệm")

    # Chức năng 5
    elif choice == "5":
        account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    break

                interest = (
                    account["balance"]
                    * account["interest_rate"]
                    / 100
                    * account["term_months"]
                    / 12
                )

                total_amount = account["balance"] + interest

                print("Tiền lãi dự kiến:", interest)
                print("Tổng tiền nhận khi đến hạn:", total_amount)
                break

        if found == False:
            print("Không tìm thấy mã sổ tiết kiệm")

    # Chức năng 6
    elif choice == "6":
        account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    break

                actual_months = input("Nhập số tháng thực gửi: ")

                if actual_months.isdigit():
                    actual_months = int(actual_months)

                    if actual_months <= 0:
                        print("Số tháng thực gửi không hợp lệ!")
                        break
                else:
                    print("Số tháng thực gửi không hợp lệ!")
                    break

                if actual_months < account["term_months"]:
                    applied_rate = 0.5
                    print("Khách hàng rút trước hạn.")
                else:
                    applied_rate = account["interest_rate"]
                    print("Khách hàng đủ điều kiện hưởng lãi đúng hạn.")

                interest = (
                    account["balance"]
                    * applied_rate
                    / 100
                    * actual_months
                    / 12
                )

                total_amount = account["balance"] + interest

                print("Tiền lãi thực nhận:", interest)
                print("Tổng tiền thực nhận:", total_amount)
                break

        if found == False:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == "7":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")