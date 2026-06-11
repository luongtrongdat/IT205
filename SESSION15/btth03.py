available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0

# Tính tổng chi phí đặt vé.
# Args:
#     ticket_quantity (int): Số lượng vé.
#     ticket_class (int): 1 = Economy, 2 = Business.
# Returns:
#     float: Tổng tiền phải thanh toán.
def calculate_ticket_price(ticket_quantity, ticket_class):
    if ticket_class == 1:
        ticket_price = BASE_PRICE
    else:
        ticket_price = BASE_PRICE * 1.5
    subtotal = ticket_quantity * ticket_price
    service_fee = subtotal * 0.05
    return subtotal + service_fee

def book_tickets(ticket_quantity, total_price):
    global available_seats
    global flight_revenue
    if ticket_quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống." )
        return False
    available_seats -= ticket_quantity
    flight_revenue += total_price
    return True

def cancel_tickets(ticket_quantity):
    global available_seats
    global flight_revenue
    if available_seats + ticket_quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra." )
        return 0
    refund_money = ticket_quantity * BASE_PRICE * 0.8
    available_seats += ticket_quantity
    flight_revenue -= refund_money
    return refund_money

# Hiển thị báo cáo tình trạng chuyến bay.
# Nội dung báo cáo:
# - Sức chứa tối đa.
# - Ghế đã đặt.
# - Ghế trống.
# - Tổng doanh thu hiện tại.
def display_flight_status():
    booked_seats = 50 - available_seats
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print("Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")

def main():
    while True:
        print("""
                ============= SKYBOOKING SYSTEM =============
                Chuyến bay: VN2026 | Khởi hành: Hà Nội
                1. Đặt vé máy bay
                2. Hủy vé & Hoàn tiền
                3. Xem tình trạng chuyến bay
                4. Đóng hệ thống
                =============================================
""")

        choice = input("Chọn chức năng (1-4): ")
        if choice == "1":
            print("--- ĐẶT VÉ MÁY BAY ---")
            quantity = input("Nhập số lượng vé: ")
            if not quantity.isdigit():
                print("Số lượng vé không hợp lệ.")
                continue
            quantity = int(quantity)
            if quantity <= 0:
                print("Số lượng vé phải lớn hơn 0.")
                continue
            ticket_class = input("Chọn hạng vé (1: Economy, 2: Business): ")
            if ticket_class not in ["1", "2"]:
                print("Hạng vé không hợp lệ.")
                continue
            ticket_class = int(ticket_class)
            if ticket_class == 1:
                ticket_price = BASE_PRICE
                class_name = "Economy"
            else:
                ticket_price = BASE_PRICE * 1.5
                class_name = "Business"
            subtotal = quantity * ticket_price
            service_fee = subtotal * 0.05
            total_price = calculate_ticket_price(
                quantity,
                ticket_class
            )

            if book_tickets(quantity, total_price):
                print("-> Xác nhận đặt chỗ:")
                print(f"Số lượng: {quantity} | Hạng: {class_name}")
                print(f"Tạm tính: ${subtotal}")
                print(f"Phí dịch vụ (5%): ${service_fee}")
                print(f"Tổng thanh toán: ${total_price}")
                print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}" )

        elif choice == "2":
            print("\n--- HỦY VÉ & HOÀN TIỀN ---")

            quantity = input("Nhập số lượng vé muốn hủy: ")

            if not quantity.isdigit():
                print("Số lượng vé không hợp lệ.")
                continue

            quantity = int(quantity)

            if quantity <= 0:
                print("Số lượng vé phải lớn hơn 0.")
                continue

            refund_money = cancel_tickets(quantity)

            if refund_money > 0:
                print(
                    f"Hủy vé thành công. "
                    f"Hệ thống đã hoàn lại: "
                    f"${refund_money} (80% giá cơ bản)."
                )
                print(
                    f"Ghế trống hiện tại: "
                    f"{available_seats}"
                )
        elif choice == "3":
            display_flight_status()
        elif choice == "4":
            print("Đóng hệ thống thành công!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

main()