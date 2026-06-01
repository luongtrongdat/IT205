#Input:
# num_branches (Số lượng chi nhánh): Kiểu số nguyên (int)
# student_count (Số học viên đi học của từng lớp): Kiểu số nguyên (int)
# Quy định cố định: Mỗi chi nhánh luôn có 2 lớp học

# Output:
# Trạng thái đánh giá của từng lớp ngay sau khi nhập dữ liệu hợp lệ:
# Từ 20 học viên trở lên "Lớp học ổn định"
# Dưới 20 học viên "Lớp cần được nhắc nhở theo dõi"

num_branches = int(input("Nhập số lượng chi nhánh: "))

for branch_idx in range(1, num_branches + 1):
    print(f"\nChi nhánh {branch_idx}:")
    
    for class_idx in range(1, 3):
        while True:
            student_count = int(input(f"  Nhập số học viên đi học của lớp {class_idx}: "))
            if student_count < 0:
                print("  Số học viên không hợp lệ. Vui lòng nhập lại.")
            if student_count == 0:
                print("  Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
                break  
            if student_count >= 20:
                print(f"  -> Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp học ổn định")
            else:
                print(f"  -> Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp cần được nhắc nhở theo dõi")
            break  