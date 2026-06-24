import os


def create_log_dir(dir_name):
    """
    Tạo thư mục lưu log nếu chưa tồn tại.
    """

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)