while True:
    try:
        n = int(input("Nhap so tu nhien n (n > 0): "))
        if (n > 0):
            break
        else:
            print("Loi: Vui long nhap lai n > 0")
    except ValueError:
        print("Loi: Vui long nhap lai n hop le.")

lst_natural = []
lst_squares = [] 

for i in range(n + 1):
    lst_natural.append(i)

for i in range(n):
    if (i**2 < n):
        lst_squares.append(i)

print(f"Danh sach so tu nhien tu 0 den {n} la:",lst_natural)
print(f"Danh sach binh phuong so tu nhien nho hon {n} la:", lst_squares)