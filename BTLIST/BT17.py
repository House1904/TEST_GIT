while True:
    try:
        n = int(input("Nhap so gia tri n (n > 0): "))
        if n > 0:
            break
        else:
            print("Loi: Vui long nhap lai n > 0")
    except ValueError:
        print("Loi: Vui long nhap lai so nguyen hop le.")

lst = []

for i in range(n):
    while True:
        try:
            lst.append(int(input(f"Nhap gia tri thu {i+1}: ")))
            break
        except ValueError:
            print("Loi: Vui long nhap lai so nguyen hop le.")

# Khởi tạo max và min với giá trị đầu tiên trong danh sách
max_value = lst[0]
min_value = lst[0]

# Tìm giá trị lớn nhất và nhỏ nhất
for value in lst:
    if (value > max_value):
        max_value = value
    if (value < min_value):
        min_value = value

# In kết quả
print(f"Gia tri max cua mang la: {max_value}")
print(f"Gia tri min cua mang la: {min_value}")