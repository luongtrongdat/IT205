
class NetflixAccount:
  
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"

        self.profiles = []

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

   
    @property
    def plan(self):
        return self.__plan

   
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

  
    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit

  
    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return

        self.profiles.append(profile_name)

        print("Thêm Profile thành công")

    def upgrade_plan(self, new_plan):
        plans = ["Basic", "Standard", "Premium"]

        if new_plan not in plans:
            print("Gói cước không hợp lệ")
            return

        self.__plan = new_plan

        print("Nâng cấp gói cước thành công")

    def display_info(self):

        print("\n----- ACCOUNT INFORMATION -----")
        print("Platform:", NetflixAccount.platform_name)
        print("Email:", self.email)
        print("Password:", self.password)
        print("Current Plan:", self.plan)

        if len(self.profiles) == 0:
            print("Profiles: []")
        else:
            print("Profiles:", self.profiles)


current_account = None


def show_menu():
    print("\n===== NETFLIX ACCOUNT MANAGER =====")
    print("1. Đăng ký tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Thêm người xem")
    print("4. Nâng cấp gói cước")
    print("5. Cập nhật chính sách Netflix")
    print("6. Thoát chương trình")
    print("===================================")


def register_account():
    global current_account

    print("\n--- REGISTER ACCOUNT ---")
    while True:
        email = input("Nhập email: ")
        if NetflixAccount.validate_email(email):
            break
        print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")

    current_account = NetflixAccount(email)

    while True:
        try:
            password = input("Nhập mật khẩu: ")
            current_account.password = password
            break
        except ValueError as e:
            print(e)

    print("Đăng ký tài khoản thành công")


def view_account():
    if current_account is None:
        print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
        return

    current_account.display_info()


def add_profile():
    if current_account is None:
        print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
        return

    profile_name = input("Nhập tên profile mới: ")

    current_account.add_profile(profile_name)


def upgrade_plan():
    if current_account is None:
        print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
        return

    print("\nCác gói cước hiện có:")
    print("Basic")
    print("Standard")
    print("Premium")

    new_plan = input("Nhập gói cước mới: ")

    current_account.upgrade_plan(new_plan)


def update_policy():
    try:
        new_limit = int(input("Nhập số lượng profile tối đa mới: "))
        if new_limit <= 0:
            print("Giới hạn phải lớn hơn 0")
        else:
            NetflixAccount.update_max_profiles(new_limit)
            print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {NetflixAccount.max_profiles}")

    except ValueError:

        print("Vui lòng nhập số nguyên")

while True:
    show_menu()

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        register_account()

    elif choice == "2":
        view_account()

    elif choice == "3":
        add_profile()

    elif choice == "4":
        upgrade_plan()

    elif choice == "5":
        update_policy()

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ")
