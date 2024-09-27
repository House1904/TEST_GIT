while True:
    try:
        n = int(input("Nhap so nguyen duong n: "))

        if (n > 10000 and n < 99999):
            break
        else:
            print("Nhap lai.")
    except ValueError:
        print("Loi. Vui long nhap dung dinh dang so nguyen!")

count_even = 0
count_odd = 0
original_n = n  # Lưu lại giá trị ban đầu của n để in ra sau
while n != 0:
    chu_so = n % 10  # Lấy chữ số cuối của n
    if chu_so % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    n = n // 10  # Loại bỏ chữ số cuối của n bằng phép chia nguyên

# In ra kết quả
print(f"Co {count_even} chu so CHAN trong {original_n}")
print(f"Co {count_odd} chu so LE trong {original_n}")