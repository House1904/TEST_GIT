while True:
    try:
        n = int(input("Nhap so phan tu cua danh sach (n > 0): "))
        if (n > 0):
            break
        else:
            print("Vui long nhap mot so nguyen khong am.")
    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

lst = []

for i in range(n):
    while True:
        try:
            num = float(input(f"Nhap phan tu thu {i + 1}: "))
            lst.append(num)
            break
        except ValueError:
            print("Loi: Vui long nhap mot so thuc hop le.")

while True:
    try:
        k = int(input("Nhap gia tri k (tim phan tu am thu k): "))
        if (k > 0):
            break
        else:
            print("Vui long nhap k nguyen duong.")
    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

# Bien dem so phan tu am da tim thay
index = 0

# Duyet qua danh sach va tim phan tu am thu k
for i in range(n):
    if (lst[i] < 0):  # Kiem tra neu phan tu am
        index += 1
        if (index == k):  # Neu tim thay phan tu am thu k
            print(f"Vi tri phan tu am thu {k} la: {i + 1}")
            break
else:
    if index < k:
        print(f"Khong tim thay phan tu am thu {k} trong danh sach.")
