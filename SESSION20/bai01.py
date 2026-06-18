# # Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
# data = [
#     ("Faker", "10", "2", "8"),      # Tuyển thủ 1: Dữ liệu bình thường
#     ("ShowMaker", "15", "0", "10"), # Tuyển thủ 2: Không chết mạng nào (Deaths = 0)
#     ("Chovy", "12", "ba", "5")      # Tuyển thủ 3: Lỗi API trả về chữ 'ba' thay vì số 3
# ]

# # Hàm xử lý dồn cục, đặt tên biến kém
# def tinh_toan(ds):
#     print("--- BẢNG XẾP HẠNG KDA ---")
#     for x in ds:
#         n = x[0]
#         k = x[1]
#         d = x[2]
#         a = x[3]
        
#         # Ép kiểu và tính toán trực tiếp
#         kda = (int(k) + int(a)) / int(d)
#         print("Tuyển thủ", n, "có chỉ số KDA là:", kda)

# # Chạy hệ thống
# tinh_toan(data)

# # Giải thích chi tiết tại sao chương trình lại in ra dòng chữ ZeroDivisionError: division by zero
# vì đang bị lỗi chi cho 0 
# Nếu chúng ta tạm xóa ShowMaker khỏi danh sách, thì khi xử lý đến Chovy, màn hình Console sẽ in ra thông báo lỗi (Exception) tên là gì? Vì sao?
# nếu tạm xoá showmaker thì nó sẽ boá  lỗi invalid literal for int() with base 10: 'ba' lỗi chi cho string
# Đánh giá về cách đặt tên biến ds, x, n, k, d, a. Theo chuẩn Clean Code, bạn nên đổi tên các biến này thành gì để code tự giải thích được ý nghĩa của nó (Self-documenting code)?
# chưa tối ưu kiến những người dùng , người code sau khó hiểu khó tiếp cận với code này
# Việc tách công thức tính KDA ra thành một hàm riêng biệt (ví dụ: calculate_kda(kills, deaths, assists)) mang lại lợi ích gì theo nguyên tắc DRY (Don't Repeat Yourself)?
#  mang lại lời ích kiến code lập trình viên dễ đọc dex hiểu và cho phé sử dụng lại nhiều lần về sau 
# sửa code 
# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
data = [
    ("Faker", "10", "2", "8"),      # Tuyển thủ 1: Dữ liệu bình thường
    ("ShowMaker", "15", "0", "10"), # Tuyển thủ 2: Không chết mạng nào (Deaths = 0)
    ("Chovy", "12", "ba", "5")      # Tuyển thủ 3: Lỗi API trả về chữ 'ba' thay vì số 3
]
def tinh_toan(ds):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for x in ds:
        try:
            n, k, d, a = x[0], int(x[1]), int(x[2]), int(x[3])    
            # Kiểm tra tránh chia cho 0
            if d == 0:
                kda = float(k + a) # Hoặc quy ước KDA khi d=0
            else:
                kda = (k + a) / d
            print(f"Tuyển thủ {n} có chỉ số KDA là: {kda}")
        except ValueError:
            print(f"Lỗi: Dữ liệu của {x[0]} không hợp lệ (phải là số).")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")