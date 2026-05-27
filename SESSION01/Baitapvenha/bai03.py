#input
user_name = input("nhập tên bệnh nhân: ")
Id = input("nhập mã BN: ")
Department = input("nhập tên khoa: ")
#Output
infomaton = f"""
        Mã BN: {Id}
        tên BN:{user_name}
        Chuyển tới: {Department}    
"""
print(infomaton)