import math

# Nhap so nguyen duong N
while True:
    try:
        N = int(input("Nhap so nguyen duong N: "))
        if (N > 0):
            break
        else: 
            print("Nhap lai! N phai la so nguyen duong.")
    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le.")

# Tim N so nguyen to dau tien
primes = []
num = 2  # Bat dau kiem tra tu so nguyen to nho nhat

while (len(primes) < N): # N là số lượng số nguyên tố đầu tiên
    # Kiem tra so nguyen to
    is_prime = True
    m = int(math.sqrt(num))
    for i in range(2, m + 1):
        if (num % i == 0):
            is_prime = False
            break
    
    if (is_prime): # thoả mãn yêu cầu thì thêm vào mảng chứa số nguyên tố
        primes.append(num)
    
    num += 1

# Xuat ket qua
print(f"{N} so nguyen to dau tien la: {primes}")
