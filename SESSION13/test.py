# ==========================================
# PHẦN I - KHỞI TẠO HỆ THỐNG
# ==========================================
# Khởi tạo danh sách nhân viên trống ban đầu
# Dữ liệu tổ chức dạng List của Dictionary: [{"id": ..., "name": ..., "age": ..., "position": ...}]
danh_sach_nhan_vien = []

# ==========================================
# PHẦN II & III - MENU ĐIỀU HƯỚNG & XỬ LÝ NGHIỆP VỤ
# ==========================================
while True:
    print("\n" + "="*35)
    print("      QUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("="*35)
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên")
    print("3. Xóa nhân viên khỏi hệ thống")
    print("4. Thoát chương trình")
    print("="*35)
    
    lua_chon = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    # --------------------------------------
    # LỰA CHỌN 1: THÊM NHÂN VIÊN MỚI
    # --------------------------------------
    if lua_chon == "1":
        print("\n--- THÊM NHÂN VIÊN MỚI ---")
        
        # 1. Nhập và validate Mã nhân viên (ID) - Chống trùng lặp
        while True:
            ma_nv = input("Nhập mã nhân viên (ID): ").strip()
            if not ma_nv:
                print("❌ Mã nhân viên không được để trống!")
                continue
                
            # Duyệt danh sách để kiểm tra trùng ID
            trung_lap = False
            for nv in danh_sach_nhan_vien:
                if nv['id'] == ma_nv:
                    trung_lap = True
                    break
            
            if trung_lap:
                print(f"❌ Mã ID '{ma_nv}' đã tồn tại! Vui lòng nhập mã khác.")
            else:
                break
        
        # 2. Nhập và validate Họ tên
        while True:
            ten_nv = input("Nhập họ và tên nhân viên: ").strip()
            if ten_nv:
                break
            print("❌ Họ tên không được để trống!")
            
        # 3. Nhập và validate Tuổi (Xử lý trực tiếp không dùng def)
        while True:
            tuoi_input = input("Nhập tuổi nhân viên: ").strip()
            try:
                tuoi_nv = int(tuoi_input)
                if tuoi_nv > 0:
                    break  # Hợp lệ thì thoát vòng lặp nhập tuổi
                else:
                    print("❌ Tuổi phải là số nguyên dương lớn hơn 0!")
            except ValueError:
                print("❌ Định dạng không hợp lệ! Vui lòng nhập một số nguyên.")
        
        # 4. Nhập và validate Chức vụ
        while True:
            chuc_vu = input("Nhập chức vụ: ").strip()
            if chuc_vu:
                break
            print("❌ Chức vụ không được để trống!")
            
        # Lưu thông tin nhân viên vào Dictionary và thêm vào List tổng
        nhan_vien_moi = {
            "id": ma_nv,
            "name": ten_nv,
            "age": tuoi_nv,
            "position": chuc_vu
        }
        danh_sach_nhan_vien.append(nhan_vien_moi)
        print(f"🎉 Thêm thành công nhân viên: {ten_nv} (ID: {ma_nv})")

    # --------------------------------------
    # LỰA CHỌN 2: DANH SÁCH NHÂN VIÊN
    # --------------------------------------
    elif lua_chon == "2":
        print("\n--- DANH SÁCH NHÂN VIÊN HIỆN TẠI ---")
        if len(danh_sach_nhan_vien) == 0:
            print("❌ Hệ thống hiện tại chưa có nhân viên nào.")
        else:
            # In tiêu đề bảng hiển thị gọn gàng
            print(f"{'STT':<5} | {'Mã NV (ID)':<12} | {'Họ và Tên':<25} | {'Tuổi':<6} | {'Chức vụ':<15}")
            print("-" * 72)
            
            # Duyệt index thủ công thay thế cho việc in thông thường để định dạng STT
            stt = 1
            for nv in danh_sach_nhan_vien:
                print(f"{stt:<5} | {nv['id']:<12} | {nv['name']:<25} | {nv['age']:<6} | {nv['position']:<15}")
                stt += 1
            print(f"\nTổng số nhân viên: {len(danh_sach_nhan_vien)}")

    # --------------------------------------
    # LỰA CHỌN 3: XÓA NHÂN VIÊN KHỎI HỆ THỐNG
    # --------------------------------------
    elif lua_chon == "3":
        print("\n--- XÓA NHÂN VIÊN ---")
        if len(danh_sach_nhan_vien) == 0:
            print("❌ Hệ thống trống, không có dữ liệu để xóa.")
            continue
            
        ma_xoa = input("Nhập mã nhân viên (ID) cần xóa: ").strip()
        
        # Tìm kiếm vị trí (index) nhân viên dựa trên ID nhập vào
        vi_tri_xoa = -1
        for i in range(len(danh_sach_nhan_vien)):
            if danh_sach_nhan_vien[i]['id'] == ma_xoa:
                vi_tri_xoa = i
                break
                
        # Thực hiện xóa bằng hàm pop() của list nếu tìm thấy
        if vi_tri_xoa != -1:
            nv_bi_xoa = danh_sach_nhan_vien.pop(vi_tri_xoa)
            print(f"🗑️ Đã xóa thành công nhân viên {nv_bi_xoa['name']} (ID: {ma_xoa}) khỏi hệ thống.")
        else:
            print(f"❌ Không tìm thấy nhân viên nào có mã ID là '{ma_xoa}'!")

    # --------------------------------------
    # LỰA CHỌN 4: THOÁT CHƯƠNG TRÌNH
    # --------------------------------------
    elif lua_chon == "4":
        print("\nCảm ơn bạn đã sử dụng hệ thống Staff Manager. Tạm biệt!")
        break

    # --------------------------------------
    # XỬ LÝ LỖI NHẬP SAI MENU LỰA CHỌN
    # --------------------------------------
    else:
        print("⚠️ Lựa chọn không hợp lệ! Vui lòng chỉ nhập số từ 1 đến 4.")