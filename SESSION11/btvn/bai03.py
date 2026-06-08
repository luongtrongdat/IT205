product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 250000, "quantity": 30},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 350000, "quantity": 15},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 450000, "quantity": 50}
]

while True:
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    print("==========================================")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()
    print("-" * 50)
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("[LỖI] Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
        continue

    
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.\n")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for p in product_list:
                print(f"- Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']:,} | Số lượng: {p['quantity']}")
            print("")

  
    elif choice == "2":
        new_id = input("Nhập mã sản phẩm mới: ").strip().upper()
        
        is_duplicate = False
        for p in product_list:
            if p["product_id"] == new_id:
                is_duplicate = True
                break
        
        if is_duplicate:
            print(f"[LỖI] Mã sản phẩm '{new_id}' đã tồn tại trên hệ thống!\n")
            continue
            
        new_name = input("Nhập tên sản phẩm: ").strip()
        new_price = int(input("Nhập giá bán: "))
        new_qty = int(input("Nhập số lượng tồn kho: "))
        
        if new_price <= 0 or new_qty <= 0:
            print("[LỖI] Giá bán và số lượng tồn kho phải lớn hơn 0!\n")
            continue
            
        new_product = {
            "product_id": new_id,
            "product_name": new_name,
            "price": new_price,
            "quantity": new_qty
        }
        product_list.append(new_product)
        print("-> Thêm sản phẩm mới thành công!\n")

  
    elif choice == "3":
        search_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        
        found_product = None
        for p in product_list:
            if p["product_id"] == search_id:
                found_product = p
                break
                
        if found_product is None:
            print("[LỖI] Không tìm thấy mã sản phẩm cần cập nhật!\n")
            continue
            
        print(f"Đang sửa sản phẩm: {found_product['product_name']}")
        update_name = input("Nhập tên mới (Bấm Enter để bỏ qua): ").strip()
        update_price_str = input("Nhập giá mới (Bấm Enter để bỏ qua): ").strip()
        update_qty_str = input("Nhập số lượng mới (Bấm Enter để bỏ qua): ").strip()
        
        if update_name != "":
            found_product["product_name"] = update_name
            
        if update_price_str != "":
            up_price = int(update_price_str)
            if up_price <= 0:
                print("[LỖI] Giá mới không hợp lệ! Không cập nhật giá.")
            else:
                found_product["price"] = up_price
                
        if update_qty_str != "":
            up_qty = int(update_qty_str)
            if up_qty <= 0:
                print("[LỖI] Số lượng mới không hợp lệ! Không cập nhật số lượng.")
            else:
                found_product["quantity"] = up_qty
                
        print("-> Cập nhật thông tin sản phẩm thành công!\n")

   
    elif choice == "4":
        delete_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        
        found_index = -1
        for i in range(len(product_list)):
            if product_list[i]["product_id"] == delete_id:
                found_index = i
                break
                
        if found_index == -1:
            print("[LỖI] Không tìm thấy mã sản phẩm cần xóa!\n")
        else:
            removed_p = product_list.pop(found_index)
            print(f"-> Đã xóa thành công sản phẩm: {removed_p['product_name']}\n")

    
    elif choice == "5":
        print("Thoát chương trình.")
        print("Hệ thống quản lý sản phẩm Yody đã đóng an toàn.")
        break