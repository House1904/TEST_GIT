import math

while True:
    try:
        # Nhập số nguyên dương
        n = int(input("Nhap so nguyen duong n: "))
        if n > 0:
            break
        else:
            print("Nhap lai n > 0")
    except ValueError:
        print("Loi. Vui long nhap so nguyen hop le!")

# Kiểm tra số chính phương
sqrt_n = int(math.sqrt(n))
if (sqrt_n * sqrt_n == n):
   print(f"{n} la so chinh phuong")
else:
# Tìm số chính phương gần nhất
    lower_square = sqrt_n * sqrt_n
    upper_square = (sqrt_n + 1) * (sqrt_n + 1)

    # So sánh khoảng cách để tìm số chính phương gần nhất
    if (n - lower_square) < (upper_square - n):
       print(f"{n} KHONG phai la so chinh phuong. So chinh phuong gan nhat la {lower_square}.")
    else:
       print(f"{n} KHONG phai la so chinh phuong. So chinh phuong gan nhat la {upper_square}.")
