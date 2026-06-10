danh_sach_nhan_vien = []
id_tu_dong = 101

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
        
        ma_nv = id_tu_dong
        while True:
            ten_nv = input("Nhập họ và tên nhân viên: ").strip()
            if ten_nv:
                break
            print("💥 Họ tên không được để trống!")
        while True:
            luong_input = input("Nhập mức lương: ").strip()
            if not luong_input:
                print("💢 Mức lương không được để trống. Vui lòng nhập lại.")
                continue
            luong_nv = float(luong_input)
            if luong_nv > 0:
                break
            else:
                print("💢 Mức lương phải là số dương (> 0). Vui lòng nhập lại.")
        nhan_vien_moi = {
            "id": ma_nv,
            "name": ten_nv,
            "luong": luong_nv
        }
        danh_sach_nhan_vien.append(nhan_vien_moi)
        print(f"🎉 Thêm nhân viên thành công! ID: {ma_nv}")
        id_tu_dong += 1
# Chức năng 2:
    elif choice == "2":
        print("\n--- 🎃 DANH SÁCH NHÂN VIÊN HIỆN TẠI ---")
        if len(danh_sach_nhan_vien) == 0:
            print("⚡ Hệ thống hiện tại chưa có nhân viên nào.")
        else:
            print(f"{'ID':<5} | {'Tên NV':<12} | {'Mức lương':<10}")
            stt = 1
            for nv in danh_sach_nhan_vien:
                print(f"{nv['id']:<5} | {nv['name']:<12} | {nv['luong']:<10}")
                stt += 1
            print(f"\n👍 Tổng số nhân viên: {len(danh_sach_nhan_vien)}")

# Chức năng 3:
    elif choice == "3":
        print("\n--- 🍔 XÓA NHÂN VIÊN ---")
        if len(danh_sach_nhan_vien) == 0:
            print("💥 Hệ thống trống, không có dữ liệu để xóa.")
            continue
            
        ma_xoa = input("Nhập mã nhân viên (ID) cần xóa: ").strip()
# Chức năng 4:
    elif choice == "4":
        print("🤢 Thoát chương trình! 🤮")
        break
    else:
        print("💥 Lựa chọn không hợp lệ! Vui lòng chỉ nhập số từ 1 đến 4.")
        continue
