import logging

user_balance = 0

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def user_deposit(user_balance):
    print("--- NẠP TIỀN VÀO VÍ ---")

    while True:
        try:
            deposit = int(input("Nhập số tiền cần nạp: "))
        except ValueError:
            print("Chỉ được nhập giá trị!!")
            logging.error(f"ValueError: Invalid numeric input for deposit.")
        else:
            if deposit > 0:
                break
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0")
            logging.error(f"InvalidAmountError: Attempted to process {deposit} VND.")



    user_balance += deposit

    logging.info(f"Deposit successful: +{deposit:,} VND. Current Balance: {user_balance:,}")
    print("Nạp số tiền thành công: +",f"{deposit:,} VND" )
    print(f"Số dư hiện tại: {user_balance:,} VND") 

    return user_balance

def transfer_user(cur_user_balance):
    print("--- CHUYỂN TIỀN ---")
    while True:
        phone_number = input("Nhập số điện thoại: ")
        if not phone_number.isdigit():
            print("SĐT chỉ được chứa chữ số!")
            continue
        if len(phone_number) != 10:
            print("SĐT phải có đúng 10 số!")
            continue
        break

    while True:
        try:
            transfer_amount = int(input("Số tiền cần chuyển: "))
        except ValueError:
            print("Tiền tệ là phải số !!")
        else:
            if transfer_amount > 0:
                break
            print("Chuyển tiền phải lớn hơn 0 !!!")
            logging.error(f"InvalidAmountError: Attempted to process {transfer_amount} VND.")

    if transfer_amount > cur_user_balance:
        print("Giao dịch thất bại: Số dư của bạn không đủ.")
        print(f"Số dư hiện tại: {cur_user_balance:,} VND")
        logging.error(f"InsufficientBalanceError: Attempted to transfer {transfer_amount:,} VND with balance {cur_user_balance:,} VND.")
        return cur_user_balance

    cur_user_balance -= transfer_amount
    print(f"Số tiền đã chuyển {transfer_amount}")
    print(f"Số dư còn lại: {cur_user_balance}")


    if transfer_amount >= 10000000:
        logging.warning(f"High value transaction detected: {transfer_amount} VND to {phone_number}")

    logging.info(f"Transfer successful: -{transfer_amount} VND to {phone_number}. Current Balance: {cur_user_balance}")

    return cur_user_balance

def check_balance(cur_balance):
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {cur_balance:,} VND")

    logging.info(
        f"Balance checked. Current Balance: {cur_balance}"
    )

while True:
    print(" VÍ MOMO GIẢ LẬP".center(50, "="))
    print("1. Nạp tiền vào ví")
    print("2. CHuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("=" * 50)

    user_choice = input("Chọn chức năng (1-4): ")

    match user_choice:
        case "1":
            user_balance =  user_deposit(user_balance) 
        case "2":
            user_balance = transfer_user(user_balance)
        case "3":
            check_balance(user_balance)
        case "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ")
            logging.info("System shutdown")
            break
        case _:
            print("Nhập sai yêu cầu nhập lại!!")
    