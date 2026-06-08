inventory_data = {
    "Táo": 50,
    "Chuối": 100,
    "Cam": 75
}


apple_qty = inventory_data["Táo"]

grape_qty = inventory_data.get("Nho", 0)

inventory_data["Chuối"] += 20

inventory_data["Lê"] = 30


inventory_data.pop("Cam", None)

print("Số lượng Táo:", apple_qty)
print("Số lượng Nho (kiểm tra an toàn):", grape_qty)
print("Dữ liệu kho hàng sau khi cập nhật:")
print(inventory_data)