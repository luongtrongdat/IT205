from datetime import datetime


def parse_and_inspect_date(date_str):
    """
    Chuyển chuỗi ngày sang datetime.
    Trả về None nếu dữ liệu không hợp lệ.
    """

    try:
        upload_date = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )
        return upload_date

    except ValueError:
        print(
            f"[WARNING] Định dạng ngày upload '{date_str}' không tồn tại."
        )
        return None