while True:
    try:
        # Nhap so nguyen duong n
        n = int(input("Nhap so nguyen duong n: "))
        if n <= 0:
            print("Vui long nhap so nguyen duong!")
            continue

        # Tinh tong S1
        S1 = 0
        for i in range(1, n + 1):
            S1 += 1 / (i * (i + 1))

        # Tinh tong S2
        S2 = 0
        for i in range(0, n + 1):
            S2 += (2 * i + 1) / (2 * i + 2)

        # Xuat ket qua tong S1 va S2
        print(f"Tong S1 la: {S1:.2f}")
        print(f"Tong S2 la: {S2:.2f}")
        break

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")
