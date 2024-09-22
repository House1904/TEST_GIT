while True:
    try:
        n = int(input("Nhap so phan tu n (n > 0): "))
        if n > 0:
            break
        else: 
            print("Loi: Nhap lai n > 0")
    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le.")

lst = []

for i in range(n):
    while True:
        try: 
            num = int(input(f"Nhap phan tu thu {i+1}: "))
            lst.append(num)
            break
        except ValueError: 
            print("Loi: Vui long nhap so nguyen hop le.")

# Tạo danh sách mới chứa các phần tử không trùng lặp
unique_lst = []
for x in lst:
    if lst.count(x) == 1:  # Kiểm tra phần tử xuất hiện một lần
        unique_lst.append(x)

print("Danh sach phan biet chua cac phan tu:", unique_lst)
