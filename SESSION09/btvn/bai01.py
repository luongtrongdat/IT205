# Sau khi chạy dòng lệnh delivery_orders.insert(0, "GE000") => ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"]
# lý do sửa sai đơn hàng cần cập nhập là vì sau khi thêm thì "GE002" index là 2 ko phải 1
# lý do lỗi là vì remove là xóa theo giá trị ko phải theo vị trí 
# muốn xóa đơn hàng "GE003-CANCEL" thì câu lệnh là : delivery_orders.remove("GE003-CANCEL")
# pop() có tác dụng là : Xóa và trả về phần tử cuối danh sách
# lý do gây lỗi transferred_order là vì chưa tạo biến
# Lưu giá trị từ pop(): transferred_order = delivery_orders.pop()

delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
delivery_orders.append("GE004")
delivery_orders.insert(0, "GE000")
delivery_orders[2] = "GE002-UPDATED"
delivery_orders.remove("GE003-CANCEL")
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)