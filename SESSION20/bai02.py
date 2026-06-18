# # Dữ liệu từ API: (Tên, Số trận, MMR)
# data = [
#     ("Levi", 120, 2500),      # Dữ liệu chuẩn
#     ("SofM", 150),            # Lỗi API: Bị thiếu mất trường MMR (Tuple chỉ có 2 phần tử)
#     ("Optimus", 100, "N/A")   # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
# ]

# # Hàm xử lý dồn cục, không có cơ chế bẫy lỗi
# def process(ds):
#     print("--- BẢNG TÍNH THƯỞNG RP ---")
#     for p in ds:
#         t = p[0]
#         m = p[1]
#         r = p[2]  # Lấy điểm MMR
        
#         # Tính toán tiền thưởng
#         b = (m * 10) + (int(r) * 0.5)
#         print("Tuyển thủ", t, "nhận được", b, "RP")

# # Chạy hệ thống
# process(data)

# (1) Phân tích lỗi (Code Review) Hãy trả lời các câu hỏi sau:

# Giải thích chi tiết lỗi IndexError: tuple index out of range ở dòng r = p[2]. Tại sao đối với "Levi" thì dòng code này chạy được, nhưng đến "SofM" thì lại sập?
#  bị sập do chưa có dữ liệu 
# Giả sử ban tổ chức sửa lại dữ liệu của "SofM" thành ("SofM", 150, 2800) để chương trình chạy tiếp. Khi vòng lặp chạy đến "Optimus", chương trình sẽ sập ở dòng nào? Tên của lỗi (Exception) in ra trên Console lúc này sẽ là gì? (Gợi ý: chú ý hàm int()).
#  bị lỗi do sai kiểu dữ liệu kia là string là chưz cái nên k ép dc sang float 
# Kỹ năng Debug: Nếu bạn chèn thêm lệnh print("Đang xử lý:", p) vào ngay dưới dòng for p in ds:, nó sẽ giúp ích gì cho bạn trong việc tìm ra nguyên nhân gây lỗi trước khi chương trình sập? 
#  giúp cho nguoiiwf đọc biết mình sai ở đâu dểd còn sửa  
# Đánh giá về cách đặt tên biến ds, p, t, m, r, b. Theo chuẩn Clean Code, bạn nên đổi tên các biến này thành gì? 
#  các tên biến chưa đúng yêu cầu đặt tên biến và làm cho người khác k hiểu cide mình hơn
# (2) Sửa lỗi (Refactoring) và Bẫy lỗi (Exception Handling) Viết lại source code chuẩn chỉnh theo các yêu cầu sau:
# Clean Code: Đổi tên biến cho rõ nghĩa (Ví dụ: player_records, record, name, matches, mmr, bonus).
# Modular (Tách hàm): Tạo hàm calculate_bonus(matches, mmr) chuyên để tính và trả về tiền thưởng.
# Exception Handling: Trong hàm duyệt danh sách, dùng try...except để bẫy 2 loại lỗi:
# Nếu gặp IndexError (Thiếu dữ liệu), in ra: [Tên tuyển thủ]: Lỗi - Hồ sơ bị thiếu thông tin!
# Nếu gặp ValueError (Dữ liệu không thể ép sang số), in ra: [Tên tuyển thủ]: Lỗi - Dữ liệu MMR không hợp lệ!
# (Lưu ý: Dù báo lỗi, vòng lặp vẫn phải dùng continue để chạy tiếp cho các tuyển thủ phía sau).
# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]
# Hàm tính thưởng
def calculate_bonus(matches, mmr):
    return (matches * 10) + (int(mmr) * 0.5)
# Hàm xử lý danh sách tuyển thủ
def process_players(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for record in player_records:
        player_name = record[0]
        try:
            matches = record[1]
            mmr = record[2]
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {player_name} nhận được {bonus} RP")
        except IndexError:
            print(f"{player_name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
        except ValueError:
            print(f"{player_name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue
# Chạy chương trình
process_players(data)