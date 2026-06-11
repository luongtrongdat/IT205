atm_vault_balance = 50000000
user_account_balance = 10000000

# Hiển thị số dư tài khoản và tiền mặt trong ATM.
# Returns:
#     None
def display_balances():
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")

# Nạp tiền vào tài khoản.
# Args:
#     amount (int): Số tiền muốn nạp.
# Returns:
#     bool: True nếu nạp thành công.
def deposit_money(amount):
    global user_account_balance
    global atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount
    return True

# Kiểm tra điều kiện rút tiền.
# Args:
#   amount (int): Số tiền cần rút.
# Returns:
#   tuple: (status, fee, total_deduction)
def check_withdrawal_rules(amount):
    fee = 1100
    total_deduction = amount + fee
    if amount % 50000 != 0:
        return "INVALID_AMOUNT", fee, total_deduction
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS", fee, total_deduction
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH", fee, total_deduction
    return "OK", fee, total_deduction

# Thực hiện giao dịch rút tiền.
# Args:
#   total_deduction (int): Tổng tiền bị trừ.
#   amount_to_dispense (int): Tiền khách nhận.
# Returns:
#   None
def execute_withdrawal(total_deduction, amount_to_dispense):
    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense

def main():
    while True:
        print("""
                ============= SMART ATM =============
                1. Xem số dư
                2. Nạp tiền
                3. Rút tiền
                4. Kết thúc giao dịch
                =====================================
""")
        choice = input("Vui lòng chọn giao dịch (1-4): ")
        if choice == "1":
            display_balances()
        elif choice == "2":
            print("--- NẠP TIỀN ---")
            amount = input("Nhập số tiền muốn nạp: ")
            if not amount.isdigit():
                print("Số tiền không hợp lệ")
                continue
            amount = int(amount)
            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue
            if deposit_money(amount):
                print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND")
        elif choice == "3":
            print("--- RÚT TIỀN ---")
            amount = input("Nhập số tiền cần rút: ")
            if not amount.isdigit():
                print("Số tiền không hợp lệ")
                continue
            amount = int(amount)
            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue
            status, fee, total_deduction = check_withdrawal_rules(amount)
            if status == "INVALID_AMOUNT":
                print("Số tiền rút phải là bội số của 50,000")
            elif status == "INSUFFICIENT_FUNDS":
                print("Giao dịch thất bại: Số dư tài khoản không đủ.")
            elif status == "ATM_OUT_OF_CASH":
                print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ")
            else:
                execute_withdrawal(total_deduction,amount)
                print(f"""Giao dịch đang xử lý...
                          Phí giao dịch: {fee:,} VND
                          Bạn đã rút thành công {amount:,} VND
                          Số dư tài khoản còn lại: {user_account_balance:,} VND
                      """)
        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
        else:
            print("Lựa chọn không hợp lệ.")
main()