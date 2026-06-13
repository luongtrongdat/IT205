"""
Hàm: find_patient_index(records, patient_id)
Input:records: List chứa các hồ sơ bệnh án.
    patient_id: Mã bệnh nhân cần tìm.
Output:int: Vị trí bệnh nhân trong danh sách
    -1 nếu không tìm thấy.
Pseudocode:
    Duyệt từng hồ sơ trong records
    Nếu hồ sơ bắt đầu bằng patient_id
        Trả về vị trí
    Kết thúc vòng lặp
    Trả về -1
Hàm: display_records(records)
Input:records: List hồ sơ bệnh án.
Output:None
Pseudocode:
    Nếu danh sách rỗng
        In thông báo
    Ngược lại
        Duyệt từng hồ sơ
        Dùng split("-")
        In thông tin bệnh nhân
Hàm: add_patient(records)
Input:records: List hồ sơ bệnh án.
Output:None
Pseudocode:
    Nhập mã BN
    Chuẩn hóa mã
    Kiểm tra trùng mã
    Nếu trùng -> báo lỗi
    Nhập tên
    Thay "-" bằng khoảng trắng
    Title()
    Nhập năm sinh
    Kiểm tra là số
    Kiểm tra từ 1900 đến năm hiện tại
    Nhập chẩn đoán
    Thay "-" bằng khoảng trắng
    Capitalize()
    Ghép dữ liệu bằng join()
    Append vào records
Hàm: update_diagnosis(records)
Input:records: List hồ sơ bệnh án.
Output:None
Pseudocode:
    Nhập mã BN
    Tìm vị trí bệnh nhân
    Nếu không thấy
        Báo lỗi
    Tách chuỗi bằng split("-")
    Nhập chẩn đoán mới
    Chuẩn hóa dữ liệu
    Gán lại phần tử cuối
    Dùng join()
    Tạo chuỗi mới
    Gán đè vào records[index]
Hàm: generate_age_report(records)
Input:records: List hồ sơ bệnh án.
Output:None
Pseudocode:
    Khởi tạo 3 biến đếm
    Duyệt danh sách
    Lấy năm sinh
    Tính tuổi
    Nếu tuổi < 16
        tăng trẻ em
    Nếu 16 <= tuổi <= 60
        tăng trưởng thành
    Nếu tuổi > 60
        tăng cao tuổi

    In kết quả
"""

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

current_year = 2026


def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()

    for i in range(len(records)):
        if records[i].startswith(patient_id + "-"):
            return i

    return -1


def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN ---")

    for i in range(len(records)):
        info = records[i].split("-")

        print(
            f"{i+1}. [{info[0]}] {info[1]} | "
            f"Năm sinh: {info[2]} | "
            f"Chẩn đoán: {info[3]}"
        )


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ")
    patient_name = patient_name.strip().replace("-", " ").title()

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if not birth_year.isdigit():
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        birth_year = int(birth_year)

        if birth_year < 1900 or birth_year > current_year:
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        break

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.strip().replace("-", " ").capitalize()

    record = "-".join([
        patient_id,
        patient_name,
        str(birth_year),
        diagnosis
    ])

    records.append(record)

    print("Thêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu đã lưu:")
    print(record)


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    info = records[index].split("-")

    print(f"Tìm thấy bệnh nhân: {info[1]}")
    print(f"Chẩn đoán hiện tại: {info[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ")

    new_diagnosis = (
        new_diagnosis.strip()
        .replace("-", " ")
        .capitalize()
    )

    info[3] = new_diagnosis

    records[index] = "-".join(info)

    print("Cập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[index])


def generate_age_report(records):
    child = 0
    adult = 0
    elderly = 0

    for record in records:
        info = record.split("-")

        age = current_year - int(info[2])

        if age < 16:
            child += 1
        elif age <= 60:
            adult += 1
        else:
            elderly += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {child} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")

    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        display_records(patient_records)

    elif choice == "2":
        add_patient(patient_records)

    elif choice == "3":
        update_diagnosis(patient_records)

    elif choice == "4":
        generate_age_report(patient_records)

    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 1-5!")