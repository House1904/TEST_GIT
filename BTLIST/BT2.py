while True:
    try:
        n = int(input("Nhap so phan tu n (n > 0): "))
        if n > 0:
            break
        else:
            print("Loi: Vui long nhap n la so nguyen duong.")
    except ValueError:
        print("Loi: Vui long nhap lai so hop le.")

lst = []

for i in range (n):
    while True:
        try:
            num = float(input(f"Nhap phan tu thu {i+1}: "))
            lst.append(num)
            break
        except ValueError:
            print("Loi: Vui long nhap lai so hop le.")

sum = 0

for x in lst:
    sum += x

avarage = sum/n

print("Trung binh cac phan tu trong mang la: ",avarage)