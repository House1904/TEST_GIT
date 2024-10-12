def validate_cccd(id_number):
    if len(id_number) != 12 or not id_number.isdigit():
        return False
    return True

def get_info_from_id(id_number):
    province_code = id_number[:3]  # 03 chữ số đầu là mã tỉnh
    gender_code = id_number[3]      # 01 chữ số tiếp theo là giới tính
    birth_year_code = id_number[4:6]  # 02 chữ số tiếp theo là năm sinh
    random_number = id_number[6:]    # 06 chữ số cuối là khoảng số ngẫu nhiên định danh

    gender = "Nam" if gender_code in "02468" else "Nữ"
    
    year = int(birth_year_code)
    if (year < 50):
        year += 2000  
    else:
        year += 1900 
    
    return province_code, gender, year

def main():
    while True:
        id_number = input("Nhập số Căn Cước (12 ký tự số): ")
        
        # Kiểm tra tính hợp lệ của số Căn Cước
        if validate_cccd(id_number):
            print("Số Căn Cước hợp lệ.")
            break  # Thoát vòng lặp nếu nhập đúng
        else:
            print("Số Căn Cước không hợp lệ. Vui lòng nhập lại.")

    province_code, gender, year = get_info_from_id(id_number)
    print(f"Căn Cước hợp lệ.")
    print(f"Mã tỉnh: {province_code}")
    print(f"Giới tính: {gender}")
    print(f"Năm sinh: {year}")

if __name__ == "__main__":
    main()
