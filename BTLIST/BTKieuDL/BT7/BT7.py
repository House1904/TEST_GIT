import math

while True:
    try: 
        a = float(input("Nhap he so a: "))
        b = float(input("Nhap he so b: "))
        c = float(input("Nhap he so c: "))

        if a == 0:
            print("He so a phai khac 0, Vui long nhap lai.")
            continue

        delta = b**2 - 4*a*c

        if delta < 0:
            print("Delta nho hon 0, Vui long nhap lai.")
            continue

        KQ = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Bieu thuc co ket qua la: {KQ}")
        break
        
    except ValueError:
        print("Vui long nhap gia tri so hop le.")

