while True:
    try:
        n = int(input("Nhap so phan tu cua danh sach (n > 0): "))
        if (n > 0):
            break
        else:
            print("Vui long nhap mot so nguyen khong am.")
    except ValueError:
        print("Vui long nhap mot so nguyen hop le.")

# Nhap cac phan tu vao danh sach
lst = []

for i in range(n):
    while True:
        try:
            num = float(input(f"Nhap phan tu thu {i + 1}: "))
            lst.append(num)
            break
        except ValueError:
            print("Vui long nhap mot so thuc hop le.")

for i in range(n-1):
    for j in range (i+1,n):
        if (lst[i] < 0 and lst[j] < 0 and lst[i] < lst[j] ):
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

# In ra danh sách đã được sắp xếp
print("Danh sach sau khi sap xep phan tu am giam dan va giu nguyen vi tri cac so duong:", lst)
