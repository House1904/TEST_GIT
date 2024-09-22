while True:
    try:
        # Nhap ba so thuc
        a = float(input("Nhap a: "))
        b = float(input("Nhap b: "))
        c = float(input("Nhap c: "))

        # Kiem tra va in cac so co tri tuyet doi nho hon 10
        found = False  # Bien de kiem tra xem co so nao thoa man khong

        if abs(a) < 10:
            print(a)
            found = True
        if abs(b) < 10:
            print(b)
            found = True
        if abs(c) < 10:
            print(c)
            found = True
        
        # Neu khong co gia tri nao thoa man
        if not found:
            print("Khong co gia tri nao thoa man.")
        
        break

    except ValueError:
        print("Loi: Vui long nhap mot so thuc hop le.")
          