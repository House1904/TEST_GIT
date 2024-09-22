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
            lst.append(int(input(f"Nhap phan tu thu {i + 1}: ")))
            break
        except ValueError:
            print("Loi: Vui long nhap mot so nguyen hop le.")

# Danh sach so nguyen to
prime_lst = []

# Duyet qua danh sach de tim so nguyen to
for num in lst:
    if (num < 2):
        continue  # Bo qua cac so nho hon 2 vi khong phai so nguyen to
    is_prime = True  # Mac dinh so do la nguyen to
    for i in range(2, int(num ** 0.5) + 1):  # Kiem tra cac uoc tu 2 den can bac 2 cua num
        if num % i == 0:
            is_prime = False  # Neu chia het thi khong phai la nguyen to
            break
    if (is_prime):
        prime_lst.append(num)  # Neu la nguyen to thi them vao danh sach

# In ra danh sach cac so nguyen to
print("Danh sach cac so nguyen to:", prime_lst)
