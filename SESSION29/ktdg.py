from abc import ABC, abstractmethod

class BaseVehicle(ABC):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.__odometer = 0.0

    @property
    def odometer(self):
        """Thuộc tính chỉ đọc qua @property"""
        return self.__odometer

    @abstractmethod
    def calculate_efficiency(self):
        """Phương thức trừu tượng tính hiệu suất"""
        pass

    def drive(self, distance: float):
        """Phương thức thực thể di chuyển"""
        if distance <= 0:
            raise ValueError("Số km di chuyển phải là số dương lớn hơn 0.")
        self.__odometer += distance

    def __lt__(self, other):
        """Nạp chồng toán tử so sánh ít hơn dựa trên odometer"""
        if not isinstance(other, BaseVehicle):
            return NotImplemented
        return self.__odometer < other.__odometer

    @staticmethod
    def validate_license_plate(plate: str) -> bool:
        """Thẩm định dữ liệu đầu vào bằng @staticmethod"""
        return len(plate) == 9 and plate.startswith("29")


class ElectricBus(BaseVehicle):
    def calculate_efficiency(self):
        """Hiệu suất của xe buýt điện tiêu chuẩn"""
        efficiency = 100.0 - (self.odometer * 0.005)
        return max(efficiency, 50.0)


class AutonomousFeature:
    def calculate_efficiency(self):
        """Hệ thống AI tự hành tiêu tốn năng lượng cố định"""
        return 95.0

class RoboBus(ElectricBus, AutonomousFeature):
    def calculate_efficiency(self):
        """Trung bình cộng hiệu suất của cả 2 lớp cha (gọi qua tên lớp cụ thể)"""
        eff_electric = ElectricBus.calculate_efficiency(self)
        eff_autonomous = AutonomousFeature.calculate_efficiency(self)
        return (eff_electric + eff_autonomous) / 2
    
def main():
    current_vehicle = None

    while True:
        print("\nChọn chức năng (1-2): ", end="")
        choice = input().strip()
        if choice == "1":
            print("--- KHỞI TẠO XE LAI ROBOBUS ---")
            while True:
                print("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ", end="")
                plate = input().strip()
                
                if BaseVehicle.validate_license_plate(plate):
                    current_vehicle = RoboBus(plate)
                    print(f"\n[Thành công]: Khởi tạo phương tiện RoboBus thành công!")                    
                    mro_chain = " → ".join([cls.__name__ for cls in RoboBus.__mro__])
                    print(f"[MRO Architecture]: {mro_chain}")
                    break
                else:
                    print("[Lỗi]: Biển số không hợp lệ (Phải đúng 9 ký tự và bắt đầu bằng '29'). Vui lòng nhập lại!")

        elif choice == "2":
            print("--- GIẢ LẬP VẬN HÀNH PHƯƠNG TIỆN ---")
            if current_vehicle is None:
                print("[Lỗi]: Chưa khởi tạo phương tiện. Vui lòng chọn chức năng 1 trước.")
                continue
            
            print("Nhập số km di chuyển mới phát sinh: ", end="")
            try:
                distance_input = input().strip()
                distance = float(distance_input)                
                current_vehicle.drive(distance)
                eff = current_vehicle.calculate_efficiency()
                
                print(f"\n[Thành công]: Cập nhật lộ trình xe chạy thành công.")
                print(f"Tổng quãng đường tích lũy (Odometer): {current_vehicle.odometer} km")
                print(f"Hiệu suất tiêu thụ năng lượng tích hợp: {eff:.1f}%")
                
            except ValueError:
                print("[Lỗi]: Dữ liệu nhập vào phải là số dương và không chứa ký tự chữ.")

        else:
            print("[Lỗi]: Chức năng không hợp lệ, vui lòng chọn lại (1 hoặc 2).")


if __name__ == "__main__":
    main()