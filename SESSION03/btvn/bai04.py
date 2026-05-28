# input : Số lượng nhân sự mới nhập là kiểu str cần ép kiểu sang kiêu int 
# Trường hợp không hợp lệ nếu nhập: 0 hoặc -1 => lỗi nhân sự phải lớn hơn 0
# trường hợp hợp lê nếu nhập 10 => có thêm 10 nhân sự mới 
# Giải pháp 1 — Dùng while True sẽ lặp vô hạn nếu nhập đúng thì break ra 
# Giải pháp 2 — Dùng điều kiện trực tiếp là yêu cầu người dùng nhập đến khi nào số nhập vào thỏa mãn điều kiện thì dừng

# Bảng so sánh
#   Tiêu chí	    while True	    while condition
#   Độ ngắn gọn	    Ngắn	        Hơi dài hơn
#   Dễ hiểu	        Trung bình	    Dễ hiểu hơn
# Chọn giải pháp 2 do cách này dễ hiểu hơn 
 

number_of_new_employees = 0
while number_of_new_employees <= 0:
    number_of_new_employees = int(input("Vui long nhap so luong nhan su moi trong thang nay: "))
    if number_of_new_employees <= 0:
        print("LOI: So luong nhan su phai lon hon 0!")
        print("Vui long nhap lai.\n")
print("\nGhi nhan thanh cong",
      number_of_new_employees,
      "nhan su moi!") 