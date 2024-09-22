while True:
    try:
        # Nhap chuoi so nhi phan
        binary_str = input("Nhap chuoi so nhi phan: ")

        # Kiem tra chuoi co hop le hay khong
        if not all(bit in '01' for bit in binary_str):
            print("Chuoi nhi phan khong hop le. Vui long nhap lai.")
            continue

        # Chuyen doi chuoi nhi phan sang so thap phan
        decimal_value = 0
        power = 0
        for bit in reversed(binary_str):
            decimal_value += int(bit) * (2 ** power)
            power += 1

        # In ket qua
        print(f"So thap phan tuong ung la: {decimal_value}")
        break

    except ValueError:
        print("Loi: Vui long nhap chuoi nhi phan hop le.")
