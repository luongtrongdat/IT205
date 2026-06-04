# Cách khởi tạo

## C1: list rỗng[], list()
array_list = []
array_list2 = list()

print(array_list)
print(array_list2)

# a = {1, 2, 3} -> set
a = [1, 2, 3]
print(a)
print(list(a))

## C2: Khai báo cùng kiểu dữ liệu
name_list = ["Alice", "Bob", "Charlie"]
score_list = [8, 9, 10, 7]
students = ["Alice", 10, "Hà Nội", 8.5]
print(name_list)
print(score_list)
print(students)

# Cơ chế index
name_list = ["Alice", "Bob", "Charlie"]
print(name_list[0])  # Alice
print(name_list[2])  # Charlie

# list[-1]
print(name_list[-1])  # Charlie

## Các thao tác với list
# Thêm: append(), insert(), extend()
"""
- list.append(value): thêm value vào cuối list
- list.insert(index, value): thêm value vào vị trí index
- listA.extend(listB): thêm tất cả phần tử của listB vào cuối listA
"""
score_list = [8, 9, 10, 7, 6, 5]
print(f"score_list = {score_list}")

    # Thêm 1 phần tử vào cuối list
score_list.append(0)
print(score_list)

    # Thêm 1 phần tử vào vị trí index
score_list.insert(2, "CỨT")
print(score_list)

    # Thêm tất cả phần tử của listB vào cuối listA
listA = [1, 2, 3]
listB = ["a", "b", "c"]
listA.extend(listB)
print(listA)

# Sửa: list[index] = value
name_list = ["Alice", "Bob", "Charlie"]
name_list[1] = "David"
print(name_list)

# Xóa: pop(), remove(), clear(), del
"""
- remove(value): xóa phần tử đầu tiên có giá trị value trong list, nếu không tìm thấy thì báo lỗi
- pop(index): xóa và trả về phần tử tại vị trí index, nếu không có index thì xóa phần tử cuối
- del list[index]: xóa phần tử tại vị trí index
- clear(): xóa tất cả phần tử trong list
"""
# remove(value) method
name_array = ["Alex", "Bitch", "Anger", "David"]
name_array.remove("Bitch")
print(name_array)
# -> xoá phần tử có giá trị "Bitch" trong list name_array, nếu không tìm thấy thì sẽ báo lỗi 

# pop(index) method
name_array.pop(1)
print(name_array)

# del list[index] statement
del name_array[1]

# clear() method
name_array.clear()
print(name_array)

# khác nhau giữ del và pop
"""
- pop() sẽ trả về giá trị của phần tử bị xóa, còn del thì không
- del() có thể xóa phần tử theo chỉ số, còn pop() thì phải biết chỉ số của phần tử cần xóa
- del() có thể xóa nhiều phần tử cùng lúc, còn pop() thì chỉ xóa một phần tử tại một thời điểm
"""

# 
name_array = ["Bitch", "Huy", "Hùng"]

#Duyệt phần tử trong list
length_name_array = len(name_array)
print(name_array[0]) #Bitch
print(name_array[1]) #Huy
print(name_array[2]) #Hùng


# for i in range( start , stop , step ):
# -> Thực hiện câu lệnh

#Cách 1: Duyệt theo index
for idx in range(len(name_array)):
    print(name_array[idx])
print()
#Cách 2: Duyệt theo value
for name in name_array:
    print(name)
print()
for value in name_array:
    print(value)
print()
# Duyệt danh sách những  sinh viên bắt đầu bằng chữ "T"
for name in name_array:
    if name.startswith("T"):
        print(name)
# Duyệt phần tử trong mảng bằng while
print("Duyệt phần tử trong mảng bằng while")
i = 0
while i < len(name_array):
    print(name_array[i])
    i += 1

# ENUMERATE
for idx, name in enumerate(name_array):
    print(f"{idx} - {name}")
print()
for value in enumerate(name_array):
    print(f"{value}")