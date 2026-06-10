danh_sach_nhan_vien = []

while True:
    print("\n" + "="*35)
    print("🧠 QUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("="*35)
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên")
    print("3. Xóa nhân viên khỏi hệ thống")
    print("4. Thoát chương trình")
    print("="*35)
    
    choice = input("Nhập lựa chọn của bạn: ").strip()
# Chức năng 1:
    if choice == "1":
        print("\n--- 👨🏼‍💻 THÊM NHÂN VIÊN MỚI ---")
        
        while True:
            ma_nv = input("Nhập mã nhân viên: ").strip()
            if not ma_nv:
                print("💢 Mã nhân viên không được để trống!")
                continue
            trung = False
            for i in danh_sach_nhan_vien:
                if i['id'] == ma_nv:
                    trung = True
                    break
            if trung:
                print(f"💥 Mã ID '{ma_nv}' đã tồn tại! Vui lòng nhập mã khác.")
            else:
                break
        while True:
            ten_nv = input("Nhập họ và tên nhân viên: ").strip()
            if ten_nv:
                break
            print("💥 Họ tên không được để trống!")
        while True:
            luong_input = input("Nhập mức lương của nhân viên: ").strip()
            luong = int(luong_input)
            if luong > 0:
                break
            else:
                print("💢 Lương phải là số lớn hơn 0!")
        nhan_vien_moi = {
            "id": ma_nv,
            "name": ten_nv,
            "luong": luong
        }
        danh_sach_nhan_vien.append(nhan_vien_moi)
        print(f"🎉 Thêm thành công nhân viên: {ten_nv} (ID: {ma_nv})")
# Chức năng 2:
    elif choice == "2":
        print("\n--- DANH SÁCH NHÂN VIÊN HIỆN TẠI ---")
        if len(danh_sach_nhan_vien) == 0:
            print("⚡ Hệ thống hiện tại chưa có nhân viên nào.")
        else:
            print(f"{'ID':<5} | {'Tên NV (ID)':<12} | {'Mức lương':<10}")
            stt = 1
            for nv in danh_sach_nhan_vien:
                print(f"{stt:<5} | {nv['id']:<12} | {nv['name']:<25} | {nv['luong']:<6}")
                stt += 1
            print(f"\nTổng số nhân viên: {len(danh_sach_nhan_vien)}")

# Chức năng 3:
    elif choice == "3":
        print("\n--- XÓA NHÂN VIÊN ---")
        if len(danh_sach_nhan_vien) == 0:
            print("💥 Hệ thống trống, không có dữ liệu để xóa.")
            continue
            
        ma_xoa = input("Nhập mã nhân viên (ID) cần xóa: ").strip()
# Chức năng 4:
    elif choice == "4":
        print("Thoát chương trình!")
        break
    else:
        print("💥 Lựa chọn không hợp lệ! Vui lòng chỉ nhập số từ 1 đến 4.")
        continue