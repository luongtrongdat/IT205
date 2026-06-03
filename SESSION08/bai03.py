sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
order_code = ""
order_note = ""

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa trong ghi chú")
    print("5. Thoát chương trình")
    print("==================================================")
    
    choice = input("Vui lòng chọn chức năng (1-5): ").strip()
    
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")
        continue
        
    if choice == "1":
        s_name = input("Nhập tên người gửi: ")
        if not s_name.strip():
            print("Tên người gửi không được bỏ trống")
            continue
            
        s_phone = input("Nhập số điện thoại người gửi: ")
        if not s_phone.strip():
            print("Số điện thoại người gửi không được bỏ trống")
            continue
            
        p_address = input("Nhập địa chỉ lấy hàng: ")
        if not p_address.strip():
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue
            
        r_name = input("Nhập tên người nhận: ")
        if not r_name.strip():
            print("Tên người nhận không được bỏ trống")
            continue
            
        r_phone = input("Nhập số điện thoại người nhận: ")
        if not r_phone.strip():
            print("Số điện thoại người nhận không được bỏ trống")
            continue
            
        d_address = input("Nhập địa chỉ giao hàng: ")
        if not d_address.strip():
            print("Địa chỉ giao hàng không được bỏ trống")
            continue
            
        o_note = input("Nhập ghi chú giao hàng: ")
        if not o_note.strip():
            print("Ghi chú giao hàng không được bỏ trống")
            continue
            
        sender_name = s_name.strip().title()
        receiver_name = r_name.strip().title()
        sender_phone = s_phone.strip()
        receiver_phone = r_phone.strip()
        
        pickup_address = " ".join(p_address.strip().split())
        delivery_address = " ".join(d_address.strip().split())
        order_note = o_note.strip()
        
        print("\n--- BÁO CÁO THỐNG KÊ ĐƠN HÀNG ---")
        print(f"Tên người gửi: {sender_name}")
        print(f"Tên người nhận: {receiver_name}")
        print(f"Địa chỉ lấy hàng: {pickup_address}")
        print(f"Địa chỉ giao hàng: {delivery_address}")
        print(f"Ghi chú giao hàng: {order_note}")
        print(f"Độ dài ghi chú giao hàng: {len(order_note)} ký tự")
        print(f"Số lượng từ trong ghi chú: {len(order_note.split())} từ")
        print(f"Ghi chú dạng chữ thường: {order_note.lower()}")
        print(f"Ghi chú dạng chữ hoa: {order_note.upper()}")
        
    elif choice == "2":
        raw_order_code = input("Nhập mã đơn hàng cần chuẩn hóa: ")
        if not raw_order_code.strip():
            print("Mã đơn hàng không được bỏ trống")
            continue
            
        clean_code = raw_order_code.strip().upper()
        clean_code = "-".join(clean_code.split())
        
        if not clean_code.startswith("GRAB-"):
            order_code = "GRAB-" + clean_code
        else:
            order_code = clean_code
            
        print("\n--- CHUẨN HÓA MÃ ĐƠN HÀNG ---")
        print(f"Mã đơn hàng ban đầu: {raw_order_code}")
        print(f"Mã đơn hàng sau chuẩn hóa: {order_code}")
        
    elif choice == "3":
        if not sender_phone or not receiver_phone:
            print("Vui lòng chạy Chức năng 1 để nhập thông tin đơn hàng trước!")
            continue
            
        print("\n--- ẨN SỐ ĐIỆN THOẠI KHÁCH HÀNG ---")
        
        if not sender_phone.isdigit() or not receiver_phone.isdigit():
            print("Số điện thoại không hợp lệ")
            continue
            
        if len(sender_phone) != 10 or len(receiver_phone) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            continue
            
        hidden_sender = sender_phone[:3] + "*****" + sender_phone[-2:]
        hidden_receiver = receiver_phone[:3] + "*****" + receiver_phone[-2:]
        
        print(f"SĐT người gửi: {hidden_sender}")
        print(f"SĐT người nhận: {hidden_receiver}")
        
    elif choice == "4":
        if not order_note:
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue
            
        print("\n--- TÌM KIẾM VÀ THAY THẾ TỪ KHÓA ---")
        search_key = input("Nhập từ khóa cần tìm: ")
        replace_key = input("Nhập từ khóa thay thế: ")
        
        if search_key in order_note:
            occurrences = order_note.count(search_key)
            order_note = order_note.replace(search_key, replace_key)
            print(f"Số lần xuất hiện của từ khóa: {occurrences}")
            print(f"Ghi chú đơn hàng sau khi thay thế: {order_note}")
        else:
            print(f"Không tìm thấy từ khóa '{search_key}' trong ghi chú giao hàng")
            
    elif choice == "5":
        print("Thoát chương trình")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")