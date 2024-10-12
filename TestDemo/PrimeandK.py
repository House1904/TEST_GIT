# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True

# Hàm nhập vào mảng các số nguyên tố
def nhap_mang_nguyen_to():
    mang = list(map(int, input("Nhap cac so nguyen to cach nhau boi khoang trang: ").split()))
    mang_nguyen_to = [x for x in mang if is_prime(x)]
    return mang_nguyen_to

# Hàm tìm và in các cặp (a, b) sao cho a + b = k
def tim_cap_so_voi_k(mang, k):
    found = False
    for i in range(len(mang)):
        for j in range(i+1, len(mang)):  # Để không chọn cùng một số hai lần
            if (mang[i] + mang[j] == k):
                print(f"Cặp ({mang[i]}, {mang[j]}) có tổng bằng {k}")
                found = True
    if not found:
        print(f"Không có cặp nào trong mảng có tổng bằng {k}.")

# Chương trình chính
mang_nguyen_to = nhap_mang_nguyen_to()
print(mang_nguyen_to)

while True:
    try:
        k = int(input("Nhap so k: "))
        break
    except ValueError:
        print("Nhap lai k dung dinh dang!")

# Tìm và in các cặp số sao cho a + b = k
tim_cap_so_voi_k(mang_nguyen_to, k)
