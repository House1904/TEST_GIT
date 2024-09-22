while True:
    try:
        n = int(input("Nhap so phan tu n (n > 0): "))
        if (n > 0):
            break
        else:
            print("Loi: Vui long nhap lai n nguyen duong.")
    except ValueError:
        print("Loi: Vui long nhap lại so hop le.")

lst = []

for i in range(n):
    while True:
        try:
            num = float(input(f"Nhap phan tu thu {i+1}: "))
            lst.append(num)
            break
        except ValueError:
            print("Loi: Vui long nhap lại so nguyen hop le.")

total = sum(lst)

print("Tong cac phan tu trong mang la: ", total)