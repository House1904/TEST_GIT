while True:
    try:
        # Nhap so luong phan tu cua danh sach
        n = int(input("Nhap so luong phan tu: "))
        
        if (n > 0):
            break
        else:
            print("Vui long nhap so nguyen duong!")

    except ValueError:
        print("Loi: Vui long nhap so hop le!")

while True:
    try:
        lst = list(map(float,input("Nhap cac phan tu (cach nhau bang khoang trang): ").split()))
        if (len(lst) == n):
            break
        else:
            print("Nhap lai cac phan tu!")
    except ValueError:
        print("Nhap lai dung kieu du lieu!")

 # Nhap gia tri A
A = float(input("Nhap gia tri A: "))

# Tao danh sach moi chi chua cac phan tu khong lon hon A
for num in lst:
    if (num > A):
        lst.remove(num)

# Xuat danh sach moi
print("Danh sach sau khi xoa cac phan tu lon hon A:")
print(lst)

