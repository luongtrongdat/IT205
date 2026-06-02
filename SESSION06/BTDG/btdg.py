# Câu 1
don_gia = float(input("Nhập đơn giá của sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong_tien = don_gia * so_luong
if tong_tien >= 1000000:
    giam_gia = tong_tien * 0.10
    thanh_toan = tong_tien - giam_gia
else:
    thanh_toan = tong_tien

print(f"Số tiền thanh toán: {thanh_toan}")

# Câu 2
mat_khau_dung = "123456"
so_lan_nhap_sai = 0

while so_lan_nhap_sai < 3:
    mat_khau = input("Nhập mật khẩu: ")
    if mat_khau == mat_khau_dung:
        print("Đăng nhập thành công!")
        break
    else:
        so_lan_nhap_sai += 1
        print("Mật khẩu sai, vui lòng nhập lại!")

if so_lan_nhap_sai == 3:
    print("Tài khoản đã bị khóa!")

# Câu 3
tong_so_luong_san_pham = 0
so_thung_hang_hop_le = 0

while True:
    so_luong_san_pham = int(input("Nhập số lượng sản phẩm: "))
    if so_luong_san_pham < 0:
        print("Số lượng sản phẩm không hợp lệ, vui lòng nhập lại!")
        continue
    if so_luong_san_pham == 0:
        break
    tong_so_luong_san_pham += so_luong_san_pham
    so_thung_hang_hop_le += 1

print(f"Tổng số thùng hàng hợp lệ: {so_thung_hang_hop_le}")
print(f"Tổng số lượng sản phẩm thu được: {tong_so_luong_san_pham}")
