student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

# do chưa gán lại các dữ liệu nên khi print ra sẽ giữ nguyên dữ liệu đầu
student_name = student_name.strip()
student_name = student_name.title()

student_code = student_code.strip()
student_code = student_code.upper()

email = email.strip()
email = email.lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)