# Input:
# num_rooms (Số lượng phòng học cần kiểm tra): Kiểu số nguyên (int).
# num_rows (Số hàng ghế của từng phòng): Kiểu số nguyên (int).
# num_cols (Số ghế trên mỗi hàng): Kiểu số nguyên (int).

# Output:
# Các thông báo lỗi tương ứng nếu dính bẫy dữ liệu.
# Sơ đồ chỗ ngồi dạng hình chữ nhật cấu thành từ các ký tự * cho từng phòng hợp lệ.

num_rooms = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if num_rooms <= 0:
    print("Số lượng phòng học không hợp lệ")
    print("Chương trình kết thúc")
else:
    for room_idx in range(1, num_rooms + 1):
        print(f"\n--- Nhập dữ liệu cho phòng học thứ {room_idx} ---")
        
        num_rows = int(input(f"Nhập số hàng ghế của phòng {room_idx}: "))
        num_cols = int(input(f"Nhập số ghế trên mỗi hàng của phòng {room_idx}: "))
        
        if num_rows > 10 or num_cols > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break 

        if num_rows <= 0 or num_cols <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue  
            
        print(f"\nSơ đồ chỗ ngồi phòng học thứ {room_idx}:")
        for _ in range(num_rows):
            print("*" * num_cols)