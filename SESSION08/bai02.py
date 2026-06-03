shop_name = ""
product_name = ""
product_description = ""
product_category = ""
keywords_list = []

while True:
    print("\n===== HỆ THỐNG KIỂM DUYỆT SẢN PHẨM SHOPEE =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")
    print("===============================================")
    
    choice = input("Vui lòng chọn chức năng (1-5): ").strip()
    
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")
        continue
        
    if choice == "1":
        raw_shop = input("Nhập tên shop: ")
        if not raw_shop.strip():
            print("Tên shop không được bỏ trống")
            continue
            
        raw_product = input("Nhập tên sản phẩm: ")
        
        raw_description = input("Nhập mô tả sản phẩm: ")
        if not raw_description.strip():
            print("Mô tả sản phẩm không được rỗng")
            continue
            
        raw_category = input("Nhập danh mục sản phẩm: ")
        raw_keywords = input("Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): ")
        
        shop_name = raw_shop.strip()
        product_name = raw_product.strip().title()
        product_description = raw_description.strip()
        product_category = raw_category.strip().lower()
        keywords_list = [key.strip() for key in raw_keywords.split(",") if key.strip()]
        
        print("\n--- BÁO CÁO THỐNG KÊ SẢN PHẨM ---")
        print(f"+ Tên shop (Làm sạch): {shop_name}")
        print(f"+ Tên sản phẩm (Chuẩn hóa): {product_name}")
        print(f"+ Mô tả sản phẩm (Làm sạch): {product_description}")
        print(f"+ Độ dài mô tả sản phẩm: {len(product_description)} ký tự")
        print(f"+ Danh mục sản phẩm (Chuẩn hóa): {product_category}")
        print(f"+ Danh sách từ khóa sau chuẩn hóa: {keywords_list}")
        print(f"+ Số lượng từ khóa tìm kiếm: {len(keywords_list)}")
        print(f"+ Mô tả sản phẩm (Chữ thường): {product_description.lower()}")
        print(f"+ Mô tả sản phẩm (Chữ hoa): {product_description.upper()}")
        
    elif choice == "2":
        if not shop_name:
            print("Vui lòng chạy Chức năng 1 để nhập tên shop trước!")
            continue
            
        shop_lower_hyphen = shop_name.lower().replace(" ", "-")
        
        if not shop_lower_hyphen.startswith("shop-"):
            normalized_shop = "shop-" + shop_lower_hyphen
        else:
            normalized_shop = shop_lower_hyphen
            
        print("\n--- CHUẨN HÓA TÊN SHOP ---")
        print(f"Tên shop ban đầu     : \"{shop_name}\"")
        print(f"Tên shop sau chuẩn hóa: \"{normalized_shop}\"")
        
    elif choice == "3":
        print("\n--- KIỂM TRA MÃ GIẢM GIÁ ---")
        coupon = input("Nhập mã giảm giá cần kiểm tra: ")
        
        if not coupon.strip():
            print("Không hợp lệ. Lý do: Mã giảm giá không được rỗng")
        elif " " in coupon:
            print("Không hợp lệ. Lý do: Mã giảm giá không được chứa khoảng trắng")
        elif not (6 <= len(coupon) <= 12):
            print("Không hợp lệ. Lý do: Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
        elif coupon != coupon.upper():
            print("Không hợp lệ. Lý do: Mã giảm giá phải được viết hoa toàn bộ")
        elif not coupon.startswith("SALE"):
            print("Không hợp lệ. Lý do: Mã giảm giá phải bắt đầu bằng chuỗi SALE")
        elif not coupon.isalnum():
            print("Không hợp lệ. Lý do: Mã giảm giá chỉ được chứa chữ cái và chữ số")
        else:
            print("Mã giảm giá hợp lệ")
            
    elif choice == "4":
        if not product_description:
            print("Vui lòng chạy Chức năng 1 để nhập mô tả sản phẩm trước!")
            continue
            
        print("\n--- TÌM KIẾM & THAY THẾ TRONG MÔ TẢ ---")
        search_key = input("Nhập từ khóa cần tìm: ")
        replace_key = input("Nhập từ khóa thay thế: ")
        
        if search_key in product_description:
            occurrences = product_description.count(search_key)
            product_description = product_description.replace(search_key, replace_key)
            
            print("\nKết quả xử lý thành công:")
            print(f"- Số lần xuất hiện của từ khóa: {occurrences}")
            print(f"- Mô tả sau khi thay thế:\n{product_description}")
        else:
            print(f"Không tìm thấy từ khóa '{search_key}' trong mô tả sản phẩm.")
            
    elif choice == "5":
        print("\nThoát chương trình")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")