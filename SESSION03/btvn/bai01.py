print(" --- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG --- ")
#nên khai báo biên bên ngoài for
total_budget = 0
# Vòng lặp chạy 3 lần dể nhập lương cho 3 nhân viên 
for employee_number in range(1, 4):
    # Khởi tạo chiếc hộp dựng tổng tiền 
    #do tạo biến trong vòng lặp nên khi bắt đầu vòng lặp sẽ reset lại biến
    #total_budget = 0
    print("Đang xử lý nhân viên số", employee_number)
    # Nhập mức lương
    salary = int(input("Nhập mức lương (VNĐ): "))
    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp 
    total_budget = total_budget + salary
# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print(" KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")