tong_so_duong = 0  # Khoi tao bien tong de luu tong cac so duong

while True:
    try:
        # Nhap so nguyen tu nguoi dung
        number = int(input("Nhap so (nhap 0 de ket thuc): "))

        # Neu nhap 0 thi ket thuc vong lap
        if number == 0:
            break

        # Chi cong vao tong neu la so duong
        if number > 0:
            tong_so_duong += number

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

# Xuat ra tong cac so duong
print(f"Tong cac so duong la: {tong_so_duong}")

