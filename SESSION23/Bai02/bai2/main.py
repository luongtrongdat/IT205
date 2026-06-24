"""
Tác hại của from datetime import * là :
    Khi đọc code sẽ khó biết hàm nào đến từ thư viện nào
    sẽ khiến dự án chạy chậm 
Nếu trong mã nguồn có một biến global tên là time = 120 thì khi thực hiện câu lệnh sẽ khiến gây nhầm lẫn 

Hàm tối ưu hơn os.mkdir() là : os.makedirs(path, exist_ok=True)

cây thư mục :
Rikkei_Media/
|
|__ main.py
|
|__ storage/
|   |__ __init__.py
|   |__ disk_manager.py
|   |__ io_helper.py
|
|__ analytics/
|   |__ __init__.py
|   |__ time_validator.py
|
|__ media_vault/
  
"""
from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date


raw_files = [
    {
        "filename": "pod_ep1.mp3",
        "size_bytes": 4500,
        "duration_sec": 180,
        "upload_at": "2026-06-10"
    },
    {
        "filename": "movie_trailer.mp4",
        "size_bytes": 105000,
        "duration_sec": 145,
        "upload_at": "2026-06-31"
    },
    {
        "filename": "clip_short.mp4",
        "size_bytes": 8200,
        "duration_sec": 15,
        "upload_at": "2026-05-15"
    }
]


success_count = 0

print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")

safe_create_dir("media_vault")

print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
print("-" * 75)

for media_file in raw_files:

    print(f"[TỆP TIN: {media_file['filename']}]")

    upload_date = parse_and_inspect_date(
        media_file["upload_at"]
    )

    if upload_date is None:
        print(
            f" + Trạng thái phân loại: 🔴 THẤT BẠI "
            f"(Lỗi: Định dạng ngày upload "
            f"'{media_file['upload_at']}' không tồn tại)"
        )
        print()
        continue

    block_count = calculate_disk_blocks(
        media_file["size_bytes"]
    )

    if media_file["filename"].endswith(".mp3"):
        folder_type = "audio"
    else:
        folder_type = "video"

    print(
        f" + Dung lượng thực tế: "
        f"{media_file['size_bytes']:,} Bytes"
    )

    print(
        f" + Số khối phân vùng (4KB Block): "
        f"{block_count} Blocks"
    )

    print(
        f" + Trạng thái phân loại: 🟢 HỢP LỆ "
        f"(Lưu trữ vào thư mục '{folder_type}')"
    )

    print()

    success_count += 1

print("=" * 56)

print(
    f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý "
    f"{success_count}/{len(raw_files)} tệp tin thành công. "
    f"Hệ thống ổn định."
)