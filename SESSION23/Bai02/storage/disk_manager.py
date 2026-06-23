# Module disk_manager.py: Sử dụng thư viện math viết hàm calculate_disk_blocks(size_bytes, block_size=4096) để tính chính xác số block bộ nhớ tiêu tốn bằng hàm làm tròn lên (math.ceil).
import math


def calculate_disk_blocks(size_bytes: float, block_size=4096) -> float:

    # trả về và làm tròn tổng số block tiêu tốn
    blocks = math.ceil(size_bytes / block_size)

    return blocks
