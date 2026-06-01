## Cách duùng break, continue
# state = 1
# cost = 0

# while state > 0:
#     state_name = f"State {state}"
#     print(state_name)

#     if state % 2 == 0:
#         state += 1
#         continue
    
#     cost += 100_000
#     if state == 5:
#         break

#     state += 1

# print(f"Tiền thưởng theo state = {cost}")

# """
# state lẻ: 1, 3, 5
# => cost = 100_000 + 100_000 + 100_000 = 300_000
# """

## In bảng cửu chương từ 2 đến 9
# for i in range(2, 10):
#     print(f"Bảng cửu chương {i}")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()

## Vẽ hình chữ nhật bằng dấu *
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

# for row in range(rows):          # vòng ngoài: 4 hàng
#     for col in range(cols):      # vòng trong: 6 cột mỗi hàng
#         print("*", end="")
#     print()                      # xuống dòng sau mỗi hàng

# Vẽ hình chưa nhật rỗng
for row in range(rows):
    for col in range(cols):
        if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")  # khoảng trống ở giữa
    print()