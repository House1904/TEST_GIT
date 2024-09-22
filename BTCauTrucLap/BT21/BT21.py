import math

# Nhap so nguyen duong N
while True:
    try:
        N = int(input("Nhap so nguyen duong N: "))
        if N <= 0:
            print("Nhap lai! N phai la so nguyen duong.")
            continue
        break
    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le.")

# Tim N so nguyen to dau tien
primes = []
num = 2  # Bat dau kiem tra tu so nguyen to nho nhat

while len(primes) < N:
    # Kiem tra so nguyen to
    is_prime = True
    m = int(math.sqrt(num))
    for i in range(2, m + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)
    
    num += 1

# Xuat ket qua
print(f"{N} so nguyen to dau tien la: {primes}")
