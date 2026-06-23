
# import cái function tự làm
from analytics.time_validator import parse_and_inspect_date
from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir


# Danh sách tệp tin truyền về từ phòng hậu kỳ
raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500,
        "duration_sec": 180, "upload_at": "2026-06-10"},  # Hợp lệ
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145,
        # Sai ngày (Tháng 6 chỉ có 30 ngày -> ValueError)
        "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200,
        "duration_sec": 15, "upload_at": "2026-05-15"}  # Hợp lệ
]


print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
base_vault_path = "media_vault"
safe_create_dir(base_vault_path)
print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
print("-" * 75)

success_count = 0

# Code xử lý dồn cục, đặt tên biến tối nghĩa
for f in raw_files:

    # lấy ra hết thông tin bằng get
    filename = f.get('filename', 'unknown_file')
    size_bytes = f.get('size_bytes', 0)
    upload_at = f.get("upload_at", "")

    # bắt lỗi ngày tháng không hợp lệ
    try:
        up_date = parse_and_inspect_date(upload_at)
        is_valid_date = True
    except ValueError:
        is_valid_date = False

    # guard Clause

    if not is_valid_date:
        print(
            f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at}' không tồn tại)\n")
        continue

    # luồng xử lí hợp lệ
    allocated_blocks = calculate_disk_blocks(size_bytes)

    # xử lí loại file
    if filename.lower().endswith(".mp3"):
        file_type = "audio"
    
    if filename.lower().endswith(".mp4"):
        file_type = "video"
    
    # Xuất kết quả nghiệm thu thành công ra console
    print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
    print(f" + Số khối phân vùng (4KB Block): {allocated_blocks} Blocks")
    print(
        f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{file_type}')\n")

    success_count += 1

    # 3. In báo cáo tiến độ tổng kết toàn hệ thống
print("========================================================")
print(
    f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{len(raw_files)} tệp tin thành công. Hệ thống ổn định.")


# 1. khiến usingNameSpace trở nên quá chung chung và gây trùng các hàm khác, phá vỡ các quy tắc thiết kế của Python, dẫn đến những rủi ro nghiêm trọng về không gian tên.,
# khi import hết tất cả từ dateTime python sẽ quét qua toàn bộ thư viện của dateTime và trong đó có thuộc tính tên Time, và nó sẽ ghi đè hoàn tên lên biến time = 120

# 2. ta sử dụng os.makedirs() với 2 tham số ("Tên file cần tạo", exists_ok = True) Tham số thứ 2 sẽ bỏ qua và tiếp tục thực thi code nếu đã trùng lặp tên file
