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
            print("Loi: Vui long nhap gia tri hop le.")

while True:
    try:
        k = int(input("Nhap gia tri k (tim va xoa tat ca cac phan tu co gia tri k): "))
        break
    except ValueError:
        print("Loi: Vui long nhap gia tri hop le.")

# Kiểm tra và xóa tất cả các phần tử bằng k
if k in lst:
    while k in lst:
        lst.remove(k)  # Xoá từng lần xuất hiện của k
    print("Danh sach sau khi xoa toan bo so k:", lst)
else:
    print("Gia tri k khong ton tai trong danh sach.")
