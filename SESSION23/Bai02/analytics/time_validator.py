from datetime import datetime
# Module time_validator.py: Sử dụng thư viện datetime để viết hàm parse_and_inspect_date(date_str). Hàm này phải bẫy lỗi dữ liệu ngày tháng không hợp lệ (như ngày 31/06) bằng try-except, in ra cảnh báo và không làm sập chương trình.


def parse_and_inspect_date(date_str: str):
    return datetime.strptime(date_str, "%Y-%m-%d")
