n = int(input("Nhap so duong n: "))

while n <= 0:
    print("Vui long nhap so duong!")
    n = int(input("Nhap so duong n: "))

count = 0
original_n = n  # Lưu giá trị ban đầu của n để sử dụng sau trong câu lệnh print

while n != 0:
    chuso = n % 10  # Lấy chữ số cuối cùng của n
    if chuso == 7:
        count += 1  # Tăng biến đếm nếu chữ số là 7
    n //= 10  # Loại bỏ chữ số cuối cùng của n

print(f"{original_n} có {count} số 7")
