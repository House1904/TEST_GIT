while True:
    try:
        # Nhap hai so nguyen duong
        a = int(input("Nhap so nguyen duong a: "))
        b = int(input("Nhap so nguyen duong b: "))

        # Kiem tra xem a va b co phai la so nguyen duong khong
        if a <= 0 or b <= 0:
            print("Loi: Vui long nhap 2 so nguyen duong.")
            continue
        
        # Kiem tra xem a va b co phai la so chan khong
        if a % 2 == 0 and b % 2 == 0:
            print(f"{a} va {b} la 2 so chan")
        elif a % 2 == 0 or b % 2 == 0:
            print("Chi co mot so chan")
        else:
            print(f"{a} va {b} la hai so le")
        
        break

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen.")
