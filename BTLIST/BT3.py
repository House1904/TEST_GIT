while True:
    try:
        n = int(input("Nhap so phan tu n (n > 0): "))
        if (n > 0):
            break
        else: 
            print("Loi: Vui long nhap lai n > 0")
    except ValueError:
        print("Loi: Vui long nhap lai so hop le.")

lst = []

for i in range(n):
    while True:
        try:
            num = float(input(f"Nhap phan tu thu {i+1}: "))
            lst.append(num)
            break
        except ValueError:
            print("Loi: Vui long nhap lai so hop le.")

found = False
for x in lst:
    if x < 0:
        print("Vi tri phan tu am dau tien cua mang la:",lst.index(x)+1)
        found = True
        break

if not found:
    print("Mang khong co phan tu am.")