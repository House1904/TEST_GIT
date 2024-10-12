# Danh sách đã sắp xếp
sorted_list = [1.0, 2.5, 3.7, 5.1, 6.8]

while True:
    try:
        # Nhập số thực B từ bàn phím
        B = float(input("Nhap so thuc B: "))
        break

    except ValueError:
        print("Loi: Vui long nhap mot so thuc hop le.")

index = len(sorted_list)  # Mặc định là chèn vào cuối nếu B lớn hơn tất cả các phần tử

for i in range(len(sorted_list)):
    if (B <= sorted_list[i]):
        index = i
        break

# Chèn B vào danh sách
sorted_list.insert(index, B)

print("Danh sach sau khi chen:", sorted_list)