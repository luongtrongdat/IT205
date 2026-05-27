# Tên biến (snake_case) 	Nội dung nhập liệu	    	Kiểu dữ liệu
# patient_name	            Họ và tên bệnh nhân		    str
# patient_age	            Tuổi bệnh nhân		        int
# spo2_level	            Nồng độ oxy trong máu (%)	int
# heart_rate	            Nhịp tim (bpm)		        int
# has_insurance	            Có BHYT không		        str

# Nhập:
#    - Họ tên bệnh nhân
#    - Tuổi
#    - SpO2
#    - Nhịp tim
#    - BHYT (yes/no)

#Kiểm tra phân luồng y khoa:
#    Nếu SpO2 < 90 hoặc nhịp tim > 120
#        => Báo động ĐỎ

#    Ngược lại nếu:
#        SpO2 từ 90-95
#        hoặc nhịp tim từ 100-120
#        => Báo động VÀNG

#    Ngược lại
#        => XANH

#Tính viện phí:
#    Nếu tuổi < 6 hoặc tuổi >= 80
#        => 0 VNĐ

#    Ngược lại nếu có BHYT
#        => 250000 VNĐ

#    Ngược lại
#        => 500000 VNĐ

#In Phiếu Khám Bệnh Điện Tử
#In Log hệ thống:
#    - tên biến
#    - kiểu dữ liệu

# code :

patient_name = input(
    "Nhập họ và tên bệnh nhân "
    "(Ví dụ: Nguyễn Văn A): ")

patient_age = int(
    input(
        "Nhập tuổi bệnh nhân "
        "(Ví dụ: 25): "))

spo2_level = int(
    input(
        "Nhập nồng độ oxy trong máu SpO2 (%) "
        "(Ví dụ: 97): "))

heart_rate = int(
    input(
        "Nhập nhịp tim (nhịp/phút) "
        "(Ví dụ: 85): "))

has_insurance = input(
    "Bạn có thẻ BHYT không? "
    "(Vui lòng chỉ nhập 'yes' hoặc 'no'): ")

if spo2_level < 90 or heart_rate > 120:
    triage_result = (
        "BÁO ĐỘNG ĐỎ"
        "CẤP CỨU KHẨN")
elif (
    90 <= spo2_level <= 95
    or 100 <= heart_rate <= 120
):
    triage_result = (
        "BÁO ĐỘNG VÀNG"
        "THEO DÕI SÁT")
else:
    triage_result = (
        "XANH - KHÁM THƯỜNG"
    )

base_fee = 500000

# Miễn phí cho trẻ em hoặc người cao tuổi
if patient_age < 6 or patient_age >= 80:

    medical_fee = 0

# Giảm 50% nếu có BHYT
elif has_insurance == "yes":

    medical_fee = base_fee * 0.5
else:
    medical_fee = base_fee

print("PHIẾU KHÁM BỆNH ĐIỆN TỬ")

print("Họ tên bệnh nhân :", patient_name)
print("Tuổi             :", patient_age)
print("SpO2             :", spo2_level, "%")
print("Nhịp tim         :", heart_rate, "bpm")
print("Có BHYT          :", has_insurance)

print("KẾT QUẢ PHÂN LUỒNG:")
print(triage_result)

print(
    "Tạm ứng viện phí :",
    format(int(medical_fee), ","),
    "VNĐ")

print("patient_name   :", type(patient_name))
print("patient_age    :", type(patient_age))
print("spo2_level     :", type(spo2_level))
print("heart_rate     :", type(heart_rate))
print("has_insurance  :", type(has_insurance))
print("medical_fee    :", type(medical_fee))