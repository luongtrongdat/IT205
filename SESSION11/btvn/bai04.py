product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 250000, "quantity": 30, "sold": 5},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 350000, "quantity": 15, "sold": 2},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 450000, "quantity": 3, "sold": 10}
]

while True:
    print("===== HỆ THỐNG VẬN HÀNH BÁN HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu ngày")
    print("5. Thoát chương trình")
    print("===========================================")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()
    print("-" * 60)
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("[LỖI] Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
        continue

    
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.\n")
        else:
            print("DANH SÁCH SẢN PHẨM HIỆN TẠI:")
            for i in range(len(product_list)):
                p = product_list[i]
                qty = p["quantity"]
                
                if qty >= 10:
                    status = "Còn hàng"
                elif 0 < qty < 10:
                    status = "Sắp hết hàng"
                else:
                    status = "Hết hàng"
                    
                print(f"{i+1}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']:,} | Tồn kho: {qty} | Đã bán: {p['sold']} | Trạng thái: {status}")
            print("")

   
    elif choice == "2":
        sell_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
        
        found_product = None
        for p in product_list:
            if p["product_id"] == sell_id:
                found_product = p
                break
                
        if found_product is None:
            print("[LỖI] Không tìm thấy mã sản phẩm cần bán/cập nhật!\n")
            continue
            
        qty_input = input("Nhập số lượng khách mua: ").strip()
        
        # --- BẪY 3: Kiểm tra số lượng mua không phải số nguyên dương (nhỏ hơn hoặc bằng 0) ---
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("[LỖI] Số lượng mua/Nhập kho không hợp lệ!\n")
            continue
            
        sell_qty = int(qty_input)
        
        if sell_qty > found_product["quantity"]:
            print("[LỖI] Số lượng trong kho không đủ để bán!\n")
            continue
            
        found_product["quantity"] -= sell_qty  # Trừ số lượng tồn kho
        found_product["sold"] += sell_qty      # Cộng dồn số lượng đã bán
        
        total_payment = sell_qty * found_product["price"]
        print(f"-> Bán hàng thành công! Sản phẩm: {found_product['product_name']} | Số lượng: {sell_qty}")
        print(f"-> Tổng tiền khách cần thanh toán: {total_payment:,} VNĐ\n")

    
    elif choice == "3":
        import_id = input("Nhập mã sản phẩm cần nhập thêm kho: ").strip().upper()
        
        found_product = None
        for p in product_list:
            if p["product_id"] == import_id:
                found_product = p
                break
                
        if found_product is None:
            print("[LỖI] Không tìm thấy mã sản phẩm cần bán/cập nhật!\n")
            continue
            
        import_input = input("Nhập số lượng hàng nạp thêm vào kho: ").strip()
        
        if not import_input.isdigit() or int(import_input) <= 0:
            print("[LỖI] Số lượng mua/Nhập kho không hợp lệ!\n")
            continue
            
        import_qty = int(import_input)
        
        found_product["quantity"] += import_qty
        print(f"-> Nhập hàng thành công! Số lượng {found_product['product_name']} trong kho hiện tại: {found_product['quantity']} chiếc.\n")

    
    elif choice == "4":
        print("===== BÁO CÁO DOANH THU BÁN HÀNG YODY =====")
        
        day_total_revenue = 0
        best_seller_product = product_list[0] 
        
        for p in product_list:
            product_revenue = p["price"] * p["sold"]
            day_total_revenue += product_revenue
            
            print(f"- {p['product_name']} | Đã bán: {p['sold']} | Doanh thu: {product_revenue:,} VNĐ")
            
            if p["sold"] > best_seller_product["sold"]:
                best_seller_product = p
                
        print("-------------------------------------------")
        print(f"TỔNG DOANH THU TOÀN CỬA HÀNG: {day_total_revenue:,} VNĐ")
        
        if day_total_revenue == 0:
            print("Sản phẩm bán chạy nhất: Chưa có doanh thu phát sinh.")
        else:
            print(f"Sản phẩm bán chạy nhất: {best_seller_product['product_name']} ({best_seller_product['sold']} chiếc)")
        print("===========================================\n")

   
    elif choice == "5":
        print("Thoát chương trình.")
        print("Hệ thống quản lý vận hành Yody đã kết thúc ca làm việc an toàn.")
        break