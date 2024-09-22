while True:
    try:
        n = int(input("Nhap so phan tu cua danh sach (n > 0): "))
        if n > 0:
            break
        else:
            print("Vui long nhap mot so nguyen khong am.")
    except ValueError:
        print("Vui long nhap mot so nguyen hop le.")

lst = []
for i in range(n):
    while True:
        try:
            lst.append(float(input(f"Nhap phan tu thu {i + 1}: ")))
            break
        except ValueError:
            print("Vui long nhap gia tri hop le.")

# Sap xep danh sach theo thu tu tang dan
lst.sort()

# In ra danh sach da duoc sap xep
print("Danh sach sau khi sap xep tang dan:", lst)
