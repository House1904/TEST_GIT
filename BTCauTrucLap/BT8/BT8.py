max_value = None  # Khoi tao bien de luu gia tri lon nhat

while True:
    try:
        # Nhap so nguyen tu nguoi dung
        number = int(input("Nhap so (nhap 0 de ket thuc): "))

        # Kiem tra neu nhap so 0 thi ket thuc vong lap
        if number == 0:
            break

        # Cap nhat gia tri lon nhat
        if (max_value is None or number > max_value):
            max_value = number

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

# Kiem tra neu khong co so nao duoc nhap (ngoai tru 0)
if max_value is None:
    print("Khong co so nao duoc nhap.")
else:
    print(f"Gia tri lon nhat trong cac so da nhap la: {max_value}")
