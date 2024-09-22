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
            num = int(input(f"Nhap phan tu thu {i + 1}: "))
            lst.append(num)
            break
        except ValueError:
            print("Loi: Vui long nhap mot so nguyen hop le.")

# Danh sach so chan va le
even_lst = []
odd_lst = []

# Duyet danh sach de phan loai so chan va so le
for num in lst:
    if num % 2 == 0:
        even_lst.append(num)
    else:
        odd_lst.append(num)

# In ra danh sach so chan va le
print("Danh sach cac so chan:", even_lst)
print("Danh sach cac so le:", odd_lst)
