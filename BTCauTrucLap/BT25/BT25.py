while True:
    binary_str = input("Nhap chuoi nhi phan gom 8 bit (hoac khoang trang de ket thuc): ")
    
    # Ket thuc chuong trinh khi nhap khoang trang
    if binary_str.strip() == "":
        break
    
    # Kiem tra do dai chuoi nhap vao
    if len(binary_str) != 8 or not all(bit in '01' for bit in binary_str):
        print("Loi: Vui long nhap mot chuoi nhi phan chinh xac gom 8 bit.")
        continue

    # Hien thi thong diep cho bit parity
    parity_choice = input("Nhap 'c' cho parity chan hoac 'l' cho parity le: ").strip().lower()
    
    # Tinh tong so bit 1
    ones_count = binary_str.count('1')
    
    if parity_choice == 'c':
        # Tinh bit parity cho parity chan
        parity_bit = '0' if ones_count % 2 == 0 else '1'
        print(f"Chuoi nhi phan nhap vao: {binary_str}")
        print(f"Bit parity chan: {parity_bit}")

    elif parity_choice == 'l':
        # Tinh bit parity cho parity le
        parity_bit = '1' if ones_count % 2 == 0 else '0'
        print(f"Chuoi nhi phan nhap vao: {binary_str}")
        print(f"Bit parity le: {parity_bit}")
    
    else:
        print("Loi: Vui long nhap 'c' cho parity chan hoac 'l' cho parity le.")
        continue
