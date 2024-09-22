while True:
    try:
        n = int(input("Nhap so phan tu n (n > 0): "))
        if n > 0:
            break
        else:
            print("Loi: Vui long nhap lai n > 0")
    except ValueError:
        print("Loi: Vui long nhap lai so nguyen hop le")

lst = []

for i in range(n):
    while True:
        try:
            lst.append(int(input(f"Nhap phan tu thu {i + 1}: ")))
            break
        except ValueError:
            print("Loi: Vui long nhap lai so nguyen hop le")

while True:
    try:
        k = int(input("Nhap so nguyen k (k >= 0): "))
        if k >= 0:
            break
        else:
            print("Loi: Vui long nhap lai k >= 0")
    except ValueError:
        print("Loi: Vui long nhap lai so nguyen hop le")

boi_k = []
uoc_k = []

for x in lst:
    if (k == 0):
        for item in lst:
            if item not in uoc_k:
                uoc_k.append(item)  # Chỉ thêm khi chưa có trong uoc_k
        break
    if (k % x == 0 and x not in uoc_k):
        uoc_k.append(x)
    if (x % k == 0 and x not in boi_k):
        boi_k.append(x)

if boi_k:
    print(f"Cac boi cua {k} co trong mang la:", sorted(boi_k))
else:
    print(f"Khong co boi nao cua {k} trong mang")

if uoc_k:
    print(f"Cac uoc cua {k} co trong mang la:", sorted(uoc_k))
else:
    print(f"Khong co uoc nao cua {k} trong mang")
