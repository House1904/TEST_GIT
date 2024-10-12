while True:
    try:
        a = int(input("Nhap so a: "))
        b = int(input("Nhap so b: "))
        c = int(input("Nhap so c: "))
        break  
    except ValueError:
        print("Vui long nhap so nguyen hop le!")

trung_binh = (a + b + c) / 3.0

print(f"Gia tri trung binh cua 3 so la: {trung_binh:.1f}")

