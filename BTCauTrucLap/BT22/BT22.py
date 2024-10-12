import math

while True:
    try:
        x = float(input("Nhap so x de tinh can bac hai: "))
        if (x > 0):
            break
        else:
            print("So phai khong am.")
    except ValueError:
        print("Loi: Vui long nhap mot so thuc hop le.")

# Khoi tao gia tri guess
guess = x / 2.0

# Tieu chuan de kiem tra dieu kien dung
tolerance = 1e-12

# Phuong phap Newton de tinh can bac hai
while abs(guess * guess - x) > tolerance:
    guess = (guess + x / guess) / 2.0

# In ket qua
print(f"Can bac hai cua {x} xap xi la: {guess:.12f}")
