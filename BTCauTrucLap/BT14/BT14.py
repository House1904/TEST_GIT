while True:
    try:
        n = int(input("Nhap n (n > 0): "))
        if (n > 0):
            break
        else:
            print("Nhap lai n nguyen duong.")
    except ValueError:
        print("Nhap lai gia tri hop le.")

# Tính tổng của biểu thức S = 1 + 1/2 + 1/3 + ... + 1/n
S = 0
P = 0
i = 1
while (i <= n):
    P += i
    S += 1 / P
    i += 1

# Tính tổng dãy 1/2 + 3/4 + ... + n/(n+1)
D = 0
for j in range(1, n + 1):
    D += j / (j + 1)

# In kết quả
print(f"Gia tri bieu thuc S = {S:.2f}")
print(f"Gia tri bieu thuc D = {D:.2f}")
