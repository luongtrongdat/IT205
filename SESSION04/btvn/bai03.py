quantity_order = int(input("nhập số lượng hóa đơn trong ca :"))
max_value =0
min_value =0
for i in range(0,quantity_order):
    invoice_value = int (input(f"nhập giá trj hóa đơn thứ {i+1}"))
    if i ==0 :
        min_value = invoice_value
    print(f"{min_value}")
    
    if invoice_value > max_value :
        max_value = invoice_value
    elif invoice_value <min_value:
        min_value = invoice_value

        
print(f"hóa đơn có giá trị cao nhất là :{max_value}")
print(f"hóa đơn có giá trị thấp nhất là : {min_value}")