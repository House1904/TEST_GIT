while True:
    try:
        # Nhập số lượng phần tử của danh sách
        n = int(input("Nhap so luong phan tu: "))

        if n > 0:
            break
        else:
            print("Vui long nhap so nguyen duong!")

    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le!")

while True:
    try:
        # Nhập tất cả các phần tử cách nhau bởi khoảng trắng trong một dòng
        my_list = list(map(int, input("Nhap cac phan tu cach nhau bang khoang trang: ").split()))
        if (len(my_list) == n):
            break
        else:
            print("Nhap lai!")
    except ValueError:
        print("Nhap lai dung dinh dang!")

# Khởi tạo biến để lưu phần tử chia hết cho 5 lớn nhất
max_div_by_5 = None

# Dùng vòng lặp for để tìm phần tử chia hết cho 5 lớn nhất
for num in my_list:
    if num % 5 == 0:
       if (max_div_by_5 is None or num > max_div_by_5):
          max_div_by_5 = num

# Xuất kết quả
if max_div_by_5 is not None:
    print(f"Phan tu chia het cho 5 lon nhat la: {max_div_by_5}")
else:
    print("Khong co phan tu chia het cho 5 trong danh sach.")
