"""
Sau khi chạy:express_orders.insert(0, "GE100-FAST") ==> ['GE100-FAST', 'GE101', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']
Sau khi chèn "GE100-FAST" vào đầu "GE101" nằm ở index 1, nên dòng lệnh này đã sửa nhầm "GE101"
GE102-WRONG" nằm ở index :2
Nếu muốn xóa đúng đơn hàng "GE103-CANCEL" => express_orders.remove("GE103-CANCEL")
pop() không truyền index sẽ lấy và xóa phần tử cuối cùng trong danh sách
lý do lấy sai đơn hàng đang giao la : Vì pop() lấy phần tử cuối cùng (GE104) thay vì phần tử đầu tiên (GE100-FAST)
Muốn lấy đơn hàng đầu tiên để giao => current_order = express_orders.pop(0)
muốn chương trình chạy cần sửa :
    express_orders[2] = "GE102-UPDATED" thay vì express_orders[1] = "GE102-UPDATED"
    express_orders.remove("GE103-CANCEL") thay vì express_orders.pop(3)
    current_order = express_orders.pop(0) tahy vì current_order = express_orders.pop()
"""

express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]
express_orders.append("GE104")
express_orders.insert(0, "GE100-FAST")
express_orders[2] = "GE102-UPDATED"
express_orders.remove("GE103-CANCEL")
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)