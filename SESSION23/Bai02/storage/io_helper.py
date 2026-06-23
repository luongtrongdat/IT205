import os


# Module io_helper.py: Sử dụng thư viện os viết hàm safe_create_dir(path) giúp khởi tạo thư mục lưu trữ một cách an toàn, tự động kiểm tra nếu thư mục tồn tại thì bỏ qua.

def safe_create_dir(path: str):
    os.makedirs(path, exist_ok=True)
