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

# Lọc các phần tử âm
phan_tu_am = [x for x in lst if x < 0]

# Sắp xếp các phần tử âm theo thứ tự giảm dần
phan_tu_am.sort(reverse=True)

# Tạo danh sách kết quả với các số dương giữ nguyên vị trí
result = []
j = 0  # Biến chỉ mục để duyệt qua các phần tử âm đã sắp xếp
for x in lst:
    if x < 0:
        result.append(phan_tu_am[j])
        j += 1
    else:
        result.append(x)

# In ra danh sách đã được sắp xếp
print("Danh sach sau khi sap xep phan tu am giam dan va giu nguyen vi tri cac so duong:", result)
