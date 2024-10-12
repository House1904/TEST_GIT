# Chuyển đổi từ hệ nhị phân sang thập phân
def binary_to_decimal(binary):
    try:
        return int(binary, 2)
    except ValueError:
        print("Lỗi: Giá trị không phải là hệ nhị phân hợp lệ.")
        return None

# Chuyển đổi từ hệ thập lục phân sang thập phân
def hex_to_decimal(hexadecimal):
    try:
        return int(hexadecimal, 16)
    except ValueError:
        print("Lỗi: Giá trị không phải là hệ thập lục phân hợp lệ.")
        return None

# Chuyển đổi từ hệ thập phân sang nhị phân
def decimal_to_binary(decimal):
    if decimal < 0:
        return '-' + bin(decimal)[3:] 
    return bin(decimal)[2:]  # Loại bỏ '0b' ở đầu chuỗi nhị phân

# Chuyển đổi từ hệ thập phân sang thập lục phân
def decimal_to_hex(decimal):
    if decimal < 0:
        return '-' + hex(decimal)[3:]
    return hex(decimal)[2:]  # Loại bỏ '0x' ở đầu chuỗi thập lục phân

# Chương trình chính
def main():
    print("Chương trình chuyển đổi giữa các hệ số (nhị phân, thập phân, thập lục phân)")
    while True:
        print("[Lựa chọn]")
        print("1. Nhị phân --> Thập phân")
        print("2. Thập lục phân --> Thập phân")
        print("3. Thập phân --> Nhị phân")
        print("4. Thập phân --> Thập lục phân")
        print("5. Thoát")
        
        # Nhận lựa chọn từ người dùng
        choice = input("Nhập lựa chọn (1-5): ")

        if choice == '1':
            binary = input("Nhập giá trị nhị phân: ")
            decimal = binary_to_decimal(binary)
            if decimal is not None:
                print(f"Giá trị thập phân: {decimal}")
        
        elif choice == '2':
            hexadecimal = input("Nhập giá trị thập lục phân: ")
            decimal = hex_to_decimal(hexadecimal)
            if decimal is not None:
                print(f"Giá trị thập phân: {decimal}")
        
        elif choice == '3':
            try:
                decimal = int(input("Nhập giá trị thập phân: "))
                print(f"Giá trị nhị phân: {decimal_to_binary(decimal)}")
            except ValueError:
                print("Lỗi: Giá trị không phải là số thập phân hợp lệ.")
        
        elif choice == '4':
            try:
                decimal = int(input("Nhập giá trị thập phân: "))
                print(f"Giá trị thập lục phân: {decimal_to_hex(decimal)}")
            except ValueError:
                print("Lỗi: Giá trị không phải là số thập phân hợp lệ.")
        
        elif choice == '5':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
