name = ""
title = ""
describe = ""
fist_hashtags = ""
current_hashtags = []

while True:
    print("""
                HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK
                1. Nhập và phân tích thông tin video
                2. Chuẩn hóa tên tài khoản
                3. Kiểm tra tính hợp lệ của hashtag
                4. Tìm kiếm và thay thế từ khóa trong mô tả
                5. Thoát chương trình
    """)

    choice = input("Mời bạn chọn chức năng (1-5): ")

    if choice == "1":
        name = input("Tên tài khoản người đăng video: ").strip()

        if not name:
            print("Tên tài khoản không được rỗng")
            continue

        title = input("Tiêu đề video: ").strip()

        describe = input("Mô tả video: ").strip()

        if not describe:
            print("Mô tả video không được rỗng")
            continue

        fist_hashtags = input(
            "Danh sách hashtag, cách nhau bởi dấu phẩy: "
        ).strip()

        current_hashtags = [
            tag.strip()
            for tag in fist_hashtags.split(",")
            if tag.strip()
        ]

        print(f"""
                Tên tài khoản: {name}
                Tiêu đề: {title.title()}
                Mô tả: {describe}
                Độ dài mô tả video: {len(describe)}
                Số lượng từ trong mô tả video: {len(describe.split())}
                Danh sách hashtag: {fist_hashtags}
                Số lượng hashtag: {len(current_hashtags)}
                Mô tả video được chuyển toàn bộ sang chữ thường: {describe.lower()}
                Mô tả video được chuyển toàn bộ sang chữ hoa: {describe.upper()}
        """)

    elif choice == "2":
        if not name:
            print("Vui lòng chạy Chức năng 1 để nhập tên tài khoản trước!")
            continue

        normalized_username = "@" + name.lower().replace(" ", "")

        print(f"""
                Tên tài khoản ban đầu: {name}
                Tên tài khoản sau khi được chuẩn hóa: {normalized_username}
        """)

    elif choice == "3":
        hashtag_check = input(
            "Nhập một hashtag cần kiểm tra: "
        ).strip()

        if not hashtag_check:
            print("Hashtag không được rỗng")

        elif not hashtag_check.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")

        elif " " in hashtag_check:
            print("Hashtag không được chứa khoảng trắng")

        elif len(hashtag_check) < 2:
            print("Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")

        else:
            body = hashtag_check[1:]

            if body.replace("_", "").isalnum():
                print("Hashtag hợp lệ")

                if hashtag_check not in current_hashtags:
                    current_hashtags.append(hashtag_check)

                print("Danh sách hashtag hiện tại:")
                for tag in current_hashtags:
                    print("-", tag)

            else:
                print(
                    "Hashtag chỉ được chứa chữ cái, chữ số hoặc dấu gạch dưới (_)"
                )

    elif choice == "4":
        if not describe:
            print("Vui lòng chạy Chức năng 1 để nhập mô tả trước!")
            continue

        search_key = input("Nhập từ khóa cần tìm: ").strip()
        replace_key = input("Nhập từ khóa thay thế: ").strip()

        if search_key in describe:
            count_appear = describe.count(search_key)

            describe = describe.replace(
                search_key,
                replace_key
            )

            print("\nThay thế thành công!")
            print(f"Mô tả mới: {describe}")
            print(f"Số lần xuất hiện và thay thế: {count_appear} lần")

        else:
            print(
                f"Không tìm thấy từ khóa '{search_key}' trong mô tả video."
            )

    elif choice == "5":
        print("Thoát chương trình. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")