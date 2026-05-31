total_revenue=0
total_day= 0
for i in range(1,8):
     total = int(input(f"Nhap doanh thu ngày {i}: "))
     total_revenue = total_revenue + total
     if total > 5000000 :
          total_day += 1 

average_revenue =total_revenue / 7

print(f"tổng doanh thu cả tuần là {total_revenue}")
print(f"tổng doanh thu trung bình mỗi ngày là {average_revenue}")
print(f"số  ngày đạt doanh thu mục tiêu (>= 5000000 VND) :{total_day} ngày ")