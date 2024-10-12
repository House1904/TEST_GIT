so_am = 0  # Khoi tao bien de dem so am

while True:
    try:
        # Nhap so nguyen tu nguoi dung
        number = int(input("Nhap so (nhap 0 de ket thuc): "))

        # Neu nhap 0 thi ket thuc vong lap
        if (number == 0):
            break

        # Neu la so am thi tang bien dem
        if (number < 0):
            so_am += 1

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

# Xuat ra so luong cac so am
print(f"Co {so_am} so am")

