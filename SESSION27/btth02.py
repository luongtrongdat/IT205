from abc import ABC, abstractmethod

class BaseProduct(ABC):
    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000  

    def __init__(self, product_code, product_name, initial_stock=0):
        self.product_code = product_code
        # Goi setter cua property product_name de chuan hoa ngay tu dau
        self.product_name = product_name
        # Private attribute (encapsulation): chi truy cap qua property stock_quantity
        self.__stock_quantity = initial_stock if initial_stock and initial_stock > 0 else 0

    # ---------- Property: dong goi so luong ton kho ----------
    @property
    def stock_quantity(self):
        """
        @property bien stock_quantity thanh thuoc tinh chi-doc tu ben ngoai.
        Khong co setter truc tiep -> moi thay doi so luong ton kho phai di
        qua cac phuong thuc nghiep vu (import_stock, export_stock...),
        tranh thao tung bua bai gay sai lech kiem ke (vi du: prod.stock = 999999).
        """
        return self.__stock_quantity

    def _set_stock_quantity(self, new_quantity):
        """
        Phuong thuc noi bo (protected-by-convention) de cac lop con tu thay
        doi so luong ton kho mot cach co kiem soat, thay vi truy cap truc
        tiep vao bien private __stock_quantity.
        """
        self.__stock_quantity = new_quantity

    # ---------- Property: chuan hoa ten san pham ----------
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        # Tu dong chuan hoa: in hoa toan bo + xoa khoang trang du thua
        self._product_name = value.strip().upper()

    # ---------- Abstract Methods ----------
    @abstractmethod
    def import_stock(self, quantity):
        """Nhap kho - moi loai san pham co logic rieng."""
        pass

    @abstractmethod
    def export_stock(self, quantity):
        """Xuat kho - moi loai san pham co logic rieng."""
        pass

    # ---------- Operator Overloading ----------
    def __add__(self, other):
        """
        Cong so luong ton kho cua 2 doi tuong san pham bat ky.
        Tra ve tong so luong dang so nguyen, khong tra ve doi tuong moi.
        """
        # Bay 3: kiem tra kieu du lieu hop le truoc khi xu ly.
        # Tra ve None (khong dung NotImplemented) de tranh Python tu dong
        # raise TypeError khi other khong co __radd__ tuong ung - dam bao
        # chuong trinh khong bi crash.
        if not isinstance(other, BaseProduct):
            print("Loi: Chi co the cong gop ton kho giua cac doi tuong san pham hop le!")
            return None
        return int(self.stock_quantity + other.stock_quantity)

    def __lt__(self, other):
        """So sanh so luong ton kho cua san pham nay co nho hon san pham kia."""
        # Bay 3: kiem tra kieu du lieu hop le truoc khi xu ly (tuong tu __add__)
        if not isinstance(other, BaseProduct):
            print("Loi: Chi co the so sanh ton kho giua cac doi tuong san pham hop le!")
            return None
        return self.stock_quantity < other.stock_quantity

    # ---------- Static Method & Class Method ----------
    @staticmethod
    def validate_product_code(product_code):
        """
        @staticmethod: khong can truy cap self/cls, vi day chi la ham
        kiem tra dinh dang chuoi don thuan, khong lien quan den trang thai
        cua bat ky instance hay class cu the nao.
        Kiem tra ma san pham phai bat dau bang chu va co dung 10 ky tu.
        """
        if not isinstance(product_code, str) or len(product_code) != 10:
            return False
        return product_code[0].isalpha()

    @classmethod
    def update_warehouse_name(cls, new_name):
        """
        @classmethod: nhan cls (chinh la BaseProduct hoac lop con goi no)
        de cap nhat CLASS ATTRIBUTE warehouse_name, anh huong dong loat den
        toan bo instance hien co va tuong lai - the hien dung tinh chat
        "cau hinh toan he thong" thay vi chi mot doi tuong don le.
        """
        cls.warehouse_name = new_name

    def get_product_type(self):
        """Tra ve ten lop hien tai (Polymorphism ho tro hien thi)."""
        return self.__class__.__name__


class ColdStorageProduct(BaseProduct):
    """Hang dong lanh - can kiem soat nhiet do, hao hut khi xuat kho."""

    EXPORT_LOSS_RATE = 0.05       # Hao hut bao quan 5% khi xuat kho
    COOLING_COST_RATE = 3000      # Chi phi lam lanh VND/don vi/ngay

    def __init__(self, product_code, product_name, initial_stock=0, required_temperature=0):
        # super().__init__() de tai su dung logic khoi tao tu lop cha BaseProduct
        super().__init__(product_code, product_name, initial_stock)
        self.required_temperature = required_temperature

    def import_stock(self, quantity):
        """Nhap kho binh thuong (override)."""
        if quantity is None or quantity <= 0:
            print("Loi: So luong nhap phai lon hon 0!")
            return False
        self._set_stock_quantity(self.stock_quantity + quantity)
        return True

    def export_stock(self, quantity):
        """
        Xuat kho - chiu them 5% phi hao hut bao quan phu troi tinh tren
        so luong xuat (Hanh vi dac thu) (override).
        """
        if quantity is None or quantity <= 0:
            print("Loi: So luong xuat phai lon hon 0!")
            return False

        loss = quantity * self.EXPORT_LOSS_RATE
        total_deduct = quantity + loss

        if total_deduct > self.stock_quantity:
            print("Loi: Ton kho khong du de thuc hien xuat kho (da bao gom hao hut)!")
            return False

        self._set_stock_quantity(self.stock_quantity - total_deduct)
        return {"quantity": quantity, "loss": loss, "total_deduct": total_deduct,
                "new_stock": self.stock_quantity}

    def apply_cooling_cost(self):
        """Tinh chi phi van hanh may lanh phat sinh dua tren ton kho hien tai."""
        cost = self.stock_quantity * self.COOLING_COST_RATE
        return cost


class HazardousProduct(BaseProduct):
    """Hang hoa nguy hiem - khong duoc vuot qua han muc luu tru an toan."""

    def __init__(self, product_code, product_name, initial_stock=0, max_safety_limit=0):
        super().__init__(product_code, product_name, initial_stock)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        """
        Kiem tra logic: neu stock_quantity + quantity > max_safety_limit
        thi phai tu choi nhap kho de dam bao an toan (override) (Bay 2).
        """
        if quantity is None or quantity <= 0:
            print("Loi: So luong nhap phai lon hon 0!")
            return False

        if self.stock_quantity + quantity > self.max_safety_limit:
            print(f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá "
                  f"hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit:.0f}).")
            return False

        self._set_stock_quantity(self.stock_quantity + quantity)
        return {"quantity": quantity, "new_stock": self.stock_quantity}

    def export_stock(self, quantity):
        """Xuat kho binh thuong theo quy trinh an toan (override)."""
        if quantity is None or quantity <= 0:
            print("Loi: So luong xuat phai lon hon 0!")
            return False

        if quantity > self.stock_quantity:
            print("Loi: Ton kho khong du de thuc hien xuat kho!")
            return False

        self._set_stock_quantity(self.stock_quantity - quantity)
        return {"quantity": quantity, "loss": 0, "total_deduct": quantity,
                "new_stock": self.stock_quantity}


class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):
    """
    San pham lai cao cap - vua mang dac tinh nhiet do nghiem ngat cua
    hang dong lanh, vua phai tuan thu han muc an toan cua hang nguy hiem.

    MRO thuc te: HybridPremiumProduct -> ColdStorageProduct ->
                 HazardousProduct -> BaseProduct -> ABC -> object

    QUAN TRONG: Vi ca ColdStorageProduct va HazardousProduct deu override
    import_stock/export_stock (xung dot phuong thuc), lop nay BAT BUOC
    phai tu override lai ca hai ham, goi truc tiep dich danh logic can
    thiet tu tung lop cha - khong the dua vao MRO tu nhien (vi MRO se
    chi chay logic cua ColdStorageProduct, bo qua hoan toan kiem tra an
    toan cua HazardousProduct). Xem giai thich chi tiet trong DESIGN_AMAZON.md.
    """

    def __init__(self, product_code, product_name, initial_stock=0,
                 required_temperature=0, max_safety_limit=0):
        # Goi ro rang tung lop cha de dam bao ca 2 nhanh thuoc tinh
        # (required_temperature va max_safety_limit) deu duoc khoi tao day du
        ColdStorageProduct.__init__(self, product_code, product_name,
                                     initial_stock, required_temperature)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        """
        Tich hop kiem tra han muc an toan (logic HazardousProduct) TRUOC,
        vi day la dieu kien chan cung (an toan > hieu qua) (override) (Bay 2).
        """
        if quantity is None or quantity <= 0:
            print("Loi: So luong nhap phai lon hon 0!")
            return False

        if self.stock_quantity + quantity > self.max_safety_limit:
            print(f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá "
                  f"hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit:.0f}).")
            return False

        self._set_stock_quantity(self.stock_quantity + quantity)
        return {"quantity": quantity, "new_stock": self.stock_quantity}

    def export_stock(self, quantity):
        """
        Ap dung logic hao hut 5% cua ColdStorageProduct khi xuat kho
        (override) - tai su dung lai code thay vi viet lai tu dau.
        """
        return ColdStorageProduct.export_stock(self, quantity)


class FedExCarrier:
    """Doi tac van chuyen FedEx - khong ke thua tu bat ky lop san pham nao."""

    def ship_package(self, product, quantity):
        print(f"[Hệ thống FedEx]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        # Van chuyen qua doi tac ngoai: tru kho truc tiep theo dung so luong
        # ban giao, KHONG tinh phi hao hut bao quan (khac voi export_stock noi
        # bo o Chuc nang 3) - dung theo so lieu demo trong de (100-20=80)
        product._set_stock_quantity(product.stock_quantity - quantity)


class DHLCarrier:
    """Doi tac van chuyen DHL - doc lap hoan toan voi FedExCarrier."""

    def ship_package(self, product, quantity):
        print(f"[Hệ thống DHL]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        # Tuong tu FedExCarrier: tru kho truc tiep, khong hao hut
        product._set_stock_quantity(product.stock_quantity - quantity)


def dispatch_to_carrier(carrier_agent, product, quantity):
    """
    Ham toan cuc doc lap minh hoa Duck Typing: khong quan tam carrier_agent
    thuoc class nao, mien la co phuong thuc ship_package.
    """
    try:
        carrier_agent.ship_package(product, quantity)
        return True
    except AttributeError:
        # Bay 4: doi tac van chuyen khong co ship_package
        print("Đơn vị vận chuyển không hợp lệ hoặc chưa ký kết hợp đồng kỹ thuật")
        return False


def read_quantity(prompt):
    """Doc so luong tu input, cho phep nhap co dau phay phan cach hang nghin."""
    raw = input(prompt).strip().replace(",", "")
    try:
        return float(raw)
    except ValueError:
        print("Giá trị không hợp lệ, vui lòng nhập một số!")
        return None


def print_product_summary(product):
    print(f"Loại sản phẩm: {product.get_product_type()}")
    print(f"Chuỗi kho: {product.warehouse_name}")
    print(f"Mã sản phẩm: {product.product_code}")
    print(f"Tên sản phẩm: {product.product_name}")
    print(f"Số lượng tồn kho: {product.stock_quantity:.0f} đơn vị")
    if isinstance(product, ColdStorageProduct):
        print(f"Nhiệt độ yêu cầu: {product.required_temperature:.0f} độ C")
    if isinstance(product, HazardousProduct):
        print(f"Hạn mức an toàn tối đa: {product.max_safety_limit:.0f} đơn vị")

def register_new_product(products):
    print("\n--- CHỌN LOẠI SẢN PHẨM KHỞI TẠO ---")
    print("1. Cold Storage Product (Hàng Đông Lạnh)")
    print("2. Hazardous Product (Hàng Nguy Hiểm)")
    print("3. Hybrid Premium Product (Hàng Lai Cao Cấp)")
    choice = input("Chọn loại sản phẩm (1-3): ").strip()

    if choice not in ("1", "2", "3"):
        print("Lựa chọn không hợp lệ! Hủy đăng ký.")
        return None

    product_code = input("Nhập mã sản phẩm 10 ký tự: ").strip()

    # Bay quan trong: validate ma san pham bang @staticmethod
    if not BaseProduct.validate_product_code(product_code):
        print("Mã sản phẩm không hợp lệ! Phải gồm đúng 10 ký tự, bắt đầu bằng chữ.")
        return None

    # Kiem tra trung ma san pham voi cac san pham da dang ky trong he thong
    if any(p.product_code == product_code for p in products):
        print(f"Lỗi: Mã sản phẩm {product_code} đã tồn tại trong hệ thống! Vui lòng dùng mã khác.")
        return None

    product_name = input("Nhập tên sản phẩm: ")

    raw_stock = input("Nhập số lượng tồn kho ban đầu (Enter để bỏ qua = 0): ").strip().replace(",", "")
    if raw_stock == "":
        initial_stock = 0
    else:
        try:
            initial_stock = float(raw_stock)
        except ValueError:
            print("Giá trị không hợp lệ, số lượng tồn kho ban đầu được đặt về 0.")
            initial_stock = 0

    if choice == "1":
        temperature = read_quantity("Nhập nhiệt độ bảo quản yêu cầu (độ C): ")
        if temperature is None:
            return None
        new_product = ColdStorageProduct(product_code, product_name, initial_stock, temperature)
        print("Đăng ký sản phẩm Đông Lạnh thành công!")
    elif choice == "2":
        safety_limit = read_quantity("Nhập hạn mức an toàn tối đa (đơn vị): ")
        if safety_limit is None:
            return None
        new_product = HazardousProduct(product_code, product_name, initial_stock, safety_limit)
        print("Đăng ký sản phẩm Nguy Hiểm thành công!")
    else:
        temperature = read_quantity("Nhập nhiệt độ bảo quản yêu cầu (độ C): ")
        if temperature is None:
            return None
        safety_limit = read_quantity("Nhập hạn mức an toàn tối đa (đơn vị): ")
        if safety_limit is None:
            return None
        new_product = HybridPremiumProduct(product_code, product_name, initial_stock,
                                            temperature, safety_limit)
        print("Đăng ký sản phẩm Lai Cao Cấp (Hybrid) thành công!")

    print(f"Tên sản phẩm: {new_product.product_name}")
    products.append(new_product)
    return new_product


def view_product_info(current_product):
    if current_product is None:
        print("\nHệ thống chưa có thông tin sản phẩm. Vui lòng đăng ký ở Chức năng 1 trước.")
        return

    print("\n--- THÔNG TIN SẢN PHẨM HIỆN TẠI ---")
    print_product_summary(current_product)

    # In ra danh sach MRO de kiem tra ky thuat da ke thua
    mro_names = " -> ".join(cls.__name__ for cls in type(current_product).__mro__)
    print(f"\nMRO (Method Resolution Order): {mro_names}")


def transaction_menu(current_product):
    if current_product is None:
        print("\nHệ thống chưa có thông tin sản phẩm. Vui lòng đăng ký ở Chức năng 1 trước.")
        return

    print("\n--- GIAO DỊCH NHẬP / XUẤT KHO ---")
    print("1. Nhập kho")
    print("2. Xuất kho")
    choice = input("Chọn giao dịch (1-2): ").strip()

    if choice == "1":
        quantity = read_quantity("Nhập số lượng nhập kho: ")
        if quantity is None:
            return
        # Tinh da hinh: cung mot loi goi import_stock() nhung hanh vi khac
        # nhau tuy theo loai san pham dang active
        result = current_product.import_stock(quantity)

        if result:
            print("Nhập kho thành công!")
            print(f"Số lượng nhập: {result['quantity']:.0f} đơn vị")
            print(f"Tồn kho cập nhật: {result['new_stock']:.0f} đơn vị")

    elif choice == "2":
        quantity = read_quantity("Nhập số lượng cần xuất: ")
        if quantity is None:
            return
        # Tinh da hinh: cung mot loi goi export_stock() nhung hanh vi khac
        # nhau tuy theo loai san pham dang active
        result = current_product.export_stock(quantity)

        if result:
            print("Xuất kho thành công!")
            print(f"Số lượng yêu cầu: {result['quantity']:.0f} đơn vị")
            if result.get("loss", 0) > 0:
                print(f"Số lượng hao hụt bảo quản (5%): {result['loss']:.1f} đơn vị")
                print(f"Tổng số lượng khấu trừ trong kho: {result['total_deduct']:.1f} đơn vị")
            print(f"Tồn kho còn lại: {result['new_stock']:.1f} đơn vị")
    else:
        print("Lựa chọn không hợp lệ!")


def check_storage_condition(current_product):
    if current_product is None:
        print("\nHệ thống chưa có thông tin sản phẩm. Vui lòng đăng ký ở Chức năng 1 trước.")
        return

    print("\n--- TÍNH PHÍ BẢO QUẢN ĐÔNG LẠNH ---")

    # Chi ColdStorageProduct va HybridPremiumProduct (vi HybridPremiumProduct
    # ke thua tu ColdStorageProduct) moi co kha nang tinh chi phi lam lanh
    if not isinstance(current_product, ColdStorageProduct):
        print("Sản phẩm Nguy Hiểm (HazardousProduct) không hỗ trợ tính năng này.")
        return

    print(f"Số lượng tồn kho hiện tại: {current_product.stock_quantity:.0f} đơn vị")
    print(f"Nhiệt độ yêu cầu: {current_product.required_temperature:.0f} độ C")

    cost = current_product.apply_cooling_cost()
    print(f"Chi phí làm lạnh phát sinh trong ngày: +{cost:,.0f} VND")


def merge_and_compare_products(products, current_product):
    print("\n--- ĐỒNG BỘ & SO SÁNH TỒN KHO (OPERATOR OVERLOADING) ---")
    if current_product is None:
        print("Hệ thống chưa có thông tin sản phẩm. Vui lòng đăng ký ở Chức năng 1 trước.")
        return

    other_products = [p for p in products if p is not current_product]
    if not other_products:
        print("Chưa có sản phẩm đối ứng nào khác trong hệ thống để so sánh!")
        return

    print(f"Sản phẩm hiện tại (A): {current_product.product_name} "
          f"(Tồn kho: {current_product.stock_quantity:.0f} đơn vị)")

    print("Danh sách sản phẩm khác trong hệ thống:")
    for idx, p in enumerate(other_products, start=1):
        print(f"{idx}. {p.product_code} ({p.product_name} - "
              f"Tồn kho: {p.stock_quantity:.0f} đơn vị)")

    selected = input("Chọn số thứ tự sản phẩm đối ứng (B): ").strip()
    try:
        target = other_products[int(selected) - 1]
    except (ValueError, IndexError):
        print("Lựa chọn không hợp lệ!")
        return

    # Su dung toan tu nap chong __lt__
    print()
    comparison = current_product < target
    if comparison is None:
        return
    elif comparison:
        print("[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A ÍT HƠN tồn kho sản phẩm B.")
    elif current_product.stock_quantity == target.stock_quantity:
        print("[Kết quả So sánh]: Hai sản phẩm có tồn kho bằng nhau.")
    else:
        print("[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A NHIỀU HƠN tồn kho sản phẩm B.")

    # Su dung toan tu nap chong __add__
    total = current_product + target
    if total is not None:
        print(f"[Kết quả Tổng hợp (__add__)]: Tổng số lượng tồn kho của cả 2 mã sản phẩm là: "
              f"{total} đơn vị.")


def dispatch_shipment(current_product):
    print("\n--- ĐIỀU PHỐI ĐƠN VỊ VẬN CHUYỂN NGOÀI ---")
    if current_product is None:
        print("Hệ thống chưa có thông tin sản phẩm. Vui lòng đăng ký ở Chức năng 1 trước.")
        return

    print("1. Vận chuyển qua đối tác FedEx")
    print("2. Vận chuyển qua đối tác DHL")
    choice = input("Chọn đối tác vận chuyển (1-2): ").strip()

    quantity = read_quantity("Nhập số lượng hàng hóa bàn giao: ")
    if quantity is None:
        return

    if choice == "1":
        carrier = FedExCarrier()
    elif choice == "2":
        carrier = DHLCarrier()
    else:
        print("Lựa chọn không hợp lệ!")
        return

    success = dispatch_to_carrier(carrier, current_product, quantity)
    if success:
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Đơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {quantity:.0f} đơn vị.")
        print(f"Số lượng tồn kho cập nhật: {current_product.stock_quantity:.1f} đơn vị.")


def main():
    products = []
    current_product = None

    while True:
        print("\n===== AMAZON INVENTORY SIMULATOR PRO =====")
        print("1. Đăng ký mã hàng hóa mới (Chọn loại sản phẩm)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nhập / Xuất kho (Đa hình)")
        print("4. Kiểm tra điều kiện bảo quản / Tính chi phí phụ trội")
        print("5. Kiểm tra tính năng gộp lô hàng & So sánh tồn kho (Overloading)")
        print("6. Điều phối vận chuyển qua Đối tác thứ ba (Duck Typing)")
        print("7. Thoát chương trình")
        print("==========================================")
        choice = input("Chọn chức năng (1-7): ").strip()

        if choice == "1":
            new_product = register_new_product(products)
            if new_product is not None:
                current_product = new_product
        elif choice == "2":
            view_product_info(current_product)
        elif choice == "3":
            transaction_menu(current_product)
        elif choice == "4":
            check_storage_condition(current_product)
        elif choice == "5":
            merge_and_compare_products(products, current_product)
        elif choice == "6":
            dispatch_shipment(current_product)
        elif choice == "7":
            print("Cảm ơn đã sử dụng hệ thống Amazon Inventory Simulator Pro!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1-7.")


if __name__ == "__main__":
    main()