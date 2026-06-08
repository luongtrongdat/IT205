# Khởi tạo tuple
my_tuple = (1, 2, 3, 4, )
my_tuple2 = ("Đạt", "Hoàng", "Hiệp")
my_tuple3 = 1, 2, 3, 4

# Cách lấy giá trị trong tuple
print(my_tuple[1])

# Cách kết hợp tuple
tuple_a = ("Đạt", "Hoàng", "Hiệp")
tuple_b = ("chó", "mèo", "chuột")
new_tuple = tuple_a + tuple_b
print(new_tuple)
# => dùng vòng for để duyệt các phân tử

# Tính chất nhân trong tuple
"""
new_tuple = old_tuple * number
"""
my_tuple = (1, 2, 3, 4, )
print(my_tuple * 2) 


#### DICTIONARY
information_dict = {
    "id": 1,
    "name": "Đạt",
    "age": 20,
    "school": "PTIT"
}
# Cách 1: dict[key]
print(information_dict["name"])
    # Trường hợp lấy key không trong dict:
    # print(information_dict["address"]) => gây lỗi
# Cách 2: dict.get(key, default)