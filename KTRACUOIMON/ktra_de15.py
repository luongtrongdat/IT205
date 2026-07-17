class BankAccount:
    def __init__(self, id, owner_name, bank_name, initial_balance, deposit_amount, withdrawal_amount, transaction_fee):
        self.id = id
        self.owner_name = owner_name
        self.bank_name = bank_name
        self.initial_balance = initial_balance
        self.deposit_amount = deposit_amount
        self.withdrawal_amount = withdrawal_amount
        self.transaction_fee = transaction_fee
        self.final_balance = 0
        self.balance_type = ""

    def calculate_final_balance(self):
        self.final_balance = self.initial_balance + self.deposit_amount - self.withdrawal_amount - self.transaction_fee
    
    def classify_balance(self):
        if self.final_balance < 0:
            self.balance_type = "Âm"
        elif self.final_balance < 5000000:
            self.balance_type = "Thấp"
        elif self.final_balance < 50000000:
            self.balance_type = "Trung bình"
        else:
            self.balance_type = "Cao"

class BankAccountManager:
    def __init__(self):
        self.accounts = []
# Hàm check trùng id
    def find_account_by_id(self, id):
        for account in self.accounts:
            if account.id == id:
                return account
        return None
    
# Hàm check để trống
    def input_none_empty(self, prompt):
        while True:
            value = input(prompt).strip()
            if value=="":
                print("Giá trị không được để trống")
            else:
                return value
            
# Hàm hiển thị
    def show_all(self):
        if not self.accounts:
            print("Danh sách tài khoản đang rỗng")
            return
        print(f"|{'Mã tài khoản':<10}| {'Tên chủ tài khoản':<20}| {'Tên ngân hàng':<20}| {'Số dư ban đầu':<15}| {'Số tiền nạp':<15}| {'Số tiền rút':<15}| {'Phí giao dịch':<15}| {'Số dư cuối cùng':<15}| {'Loại số dư':<10}|")
        for account in self.accounts:
            account.calculate_final_balance()
            account.classify_balance()
            print(f"|{account.id:<10}| {account.owner_name:<20}| {account.bank_name:<20}| {account.initial_balance:<15}| {account.deposit_amount:<15}| {account.withdrawal_amount:<15}| {account.transaction_fee:<15}| {account.final_balance:<15}| {account.balance_type:<10}|")

# Hàm thêm
    def add_account(self):
        id = input("Nhập mã tài khoản: ")
        if self.find_account_by_id(id):
            print("Mã tài khoản đã tồn tại. Vui lòng nhập mã khác")
            return
        owner_name = input("Nhập tên chủ tài khoản: ")
        bank_name = input("Nhập tên ngân hàng: ")
        initial_balance = float(input("Nhập số dư ban đầu: "))
        deposit_amount = float(input("Nhập số tiền nạp: "))
        withdrawal_amount = float(input("Nhập số tiền rút: "))
        transaction_fee = float(input("Nhập phí giao dịch: "))
        account = BankAccount(id, owner_name, bank_name, initial_balance, deposit_amount, withdrawal_amount, transaction_fee)
        self.accounts.append(account)
        print("Thêm tài khoản thành công")

# Hàm xóa
    def delete_account(self):
        if not self.accounts:
            print("Danh sách tài khoản trống. Không thể xóa tài khoản")
            return
        id = input("Nhập mã tài khoản cần xóa: ")
        account = self.find_account_by_id(id)
        if not account:
            print("Không tìm thấy tài khoản cần xóa")
            return
        confirm = input(f"Bạn có chắc muốn xóa tài khoản này không? (y/n): ")
        if confirm.lower() == "y":
            self.accounts.remove(account)
            print("Xóa tài khoản thành công")
            return
        elif confirm.lower() == "n":
            print("Hủy thao tác")
        else:
            print("Lựa chọn không hợp lệ")
# Hàm tìm kiếm
    def search_account(self):
        if not self.accounts:
            print("Danh sách tài khoản trống")
            return
        

def show_menu():
    print("""
============== MENU ==============
    1. HIỆN THỊ DANH SÁCH TÀI KHOẢN
    2. THÊM TÀI KHOẢN MỚI
    3. CẬP NHẬT TÀI KHOẢN
    4. XÓA TÀI KHOẢN
    5. TÌM KIẾM TÀI KHOẢN
    6. THOÁT
==================================
""")
    
def main():
    account_manager = BankAccountManager()
    show_menu()
    while True:
        show_menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                account_manager.show_all()
            case "2":
                account_manager.add_account()
            case "3":
                pass
            case "4":
                account_manager.delete_account()
            case "5":
                account_manager.search_account()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý tài khoản ngân hàng.")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại")

if __name__ == "__main__":
    main()
