# *** Chức năng 4: Khởi tạo thư mục lưu trữ log hệ thống
import os


def create_path_file(path_name: str) -> str:
    print("----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    if not os.path.exists(path_name):
        print(
            f"[SYSTEM] Thư mục {path_name} chưa tồn tại. Đang tiến hành khởi tạo...")
        os.makedirs(path_name, exist_ok=True)
        print("[SYSTEM] Tạo thư mục thành công!")

        return path_name

    return "Thư mục đã tồn tại, bỏ qua bước khởi tạo"
