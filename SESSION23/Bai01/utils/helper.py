"""Module phụ trách các tác vụ xử lý tệp tin và hệ điều hành."""

import os
# hàm tạo log


def create_log_dir(dir_name: str):

    # Code này sẽ văng lỗi FileExistsError nếu thư mục 'dir_name' đã có sẵn trên máy
    os.mkdir(dir_name)
