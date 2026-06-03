transaction =" nguyEN van a | PYTHON-01 | 15000000 | paid "
# do chưa gán dữ liệu cho transaction nên in ra dữ liệu cũ
transaction = transaction.strip()
# tách chuỗi sai khi sd "-"
parts = transaction.split("|")
student_name = parts[0].title()
course_code = parts[1]
amount = parts[2]
amount = int(amount)
status = parts[3].upper()
print("Học viên:", student_name)
print("Khóa học:", course_code)
print(f"Sô tiền: {amount:,} VND")
print("Trạng thái:", status)