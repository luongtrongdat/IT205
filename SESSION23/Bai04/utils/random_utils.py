# module sinh ngẫu nhiên
from data.students import student_records
import string
import random

# from data.students import student_records


# tạo mã bài tập ngẫu nhiên
def generate_assignment_code():

    # sinh ra 4 kí tự ngẫu nhiên

    print("-- SINH MÃ BÀI TẬP --")
    for i in range(len(student_records)):

        allow_keyword = string.ascii_uppercase + string.digits

        random_id = "".join(random.choices(allow_keyword, k=4))

        rand_ex_id = f"PY-{random_id}"
        print(rand_ex_id)
        i += 1
