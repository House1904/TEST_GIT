import math

# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if (x <= 1):
        return False
    for i in range(2, int(x**0.5) + 1):  # Ép kiểu x**0.5 thành số nguyên
        if (x % i == 0):
            return False
    return True

# Nhập danh sách số nguyên từ người dùng
lst = list(map(int, input("Nhập các phần tử cách nhau bằng khoảng trắng: ").split()))

# Lọc ra các số nguyên tố trong danh sách
lst_prime = [x for x in lst if is_prime(x)]

print(lst_prime)
# Nhập giá trị k
while True:
    try:
        k = int(input("Nhập k: "))
        break
    except ValueError:
        print("Nhập k đúng định dạng!")

# Tìm cặp số nguyên tố có tổng bằng k
found = False
for i in range(len(lst_prime)):
    for j in range(i + 1, len(lst_prime)):
        if lst_prime[i] + lst_prime[j] == k:
            print(f"Cặp số {lst_prime[i]} và {lst_prime[j]} có tổng bằng {k}")
            found = True

# Nếu không tìm thấy cặp nào
if not found:
    print("Không có cặp số nào thoả mãn!")
