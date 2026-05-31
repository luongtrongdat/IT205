count =0
quantity=0
choice = True
total_value =0
while choice != "k" :
    invoice_value = int(input(f"khách hàng thứ {count+1} nhập giá trị hóa đơn :"))
    total_value =total_value + invoice_value
    if invoice_value >=1000000 :
        quantity +=1 
    
    choice = input("có muốn nhập tiếp ko(c/k) ")
    count += 1

print("=====báo cáo doanh thu cuối ngày =====")
print(f"tổng số hóa đơn đã xử lý {count} hóa đơn ")
print(f"tổng doanh thu ngày hôm nay là : {total_value}VND")
print(f"số hóa đơn lớn (>1000000VND) là : {quantity}")
print(f"tỉ lệ hóa đơn lớn hiện tại {quantity / count * 100}%")