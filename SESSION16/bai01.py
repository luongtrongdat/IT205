"""
raw_diagnosis.strip() và raw_diagnosis.title() trong hàm không hề làm thay đổi giá trị là vì :
    string là bất biến nên ko thể thay đổi giá trị trực tiếp mà cần tạo biến mới lưu giá trị 
cú pháp đúng là : raw_diagnosis = raw_diagnosis.strip()
    raw_diagnosis = raw_diagnosis.title()
extend() thêm từng phần tử của một iterable vào list nên kết quả in ra các ký tự 'v', 'i', 'E', 'm' 
Thay extend() bằng phương thức append(): Vì append() thêm nguyên vẹn một phần tử vào cuối list

"""

patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)

    return current_list

new_diagnosis = "  viEm phE QUan  "
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)