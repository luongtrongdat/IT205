total_amount=int(input("nhap so tien ban dau "))

if total_amount >500000:
    total_amount_1=total_amount *0.1
    total_amount = total_amount - total_amount_1
    print(f"số tiền đc giảm giá là{total_amount_1} ")

print(f"tổng số tiền khách phải trả là {total_amount}")