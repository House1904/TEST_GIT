while True:
    try:
        n = int(input("Nhap so phan tu n (n > 0): "))
        if n > 0:
            break
        else:
            print("Loi: Vui long nhap n > 0")
    except ValueError:
        print("Loi: Vui long nhap lai so nguyen hop le.")

lst = []

for i in range(n):
    while True:
        try:
            num = float(input(f"Nhap phan tu thu {i+1}: "))
            lst.append(num)
            break
        except ValueError:
            print("Loi: Vui long nhap so nguyen hop le.")

for i in range(n-1):
    for j in range (i+1,n):
        if(lst[i] < 0 and lst[j] < 0 and lst[i] > lst[j]):
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
        if(lst[i] > 0 and lst[j] > 0 and lst[i] < lst[j]):
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

print("Danh sach sau khi sap xep phan tu am tang dan va duong giam dan la:", lst)
