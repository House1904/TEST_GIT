while True:
    try:
        a = int(input("Nhap so nguyen a: "))
        b = int(input("Nhap so nguyen b: "))

        # Xem xét trường hợp số b = 0
        if b == 0:
            print(f"{a} KHONG la boi so cua {b}")
            continue
        
        # Xem xét trường hợp số a = 0
        if a == 0:
            print(f"{a} la boi so cua {b}")
            continue
        
        # Xem xét trường hợp b != 0 và a != 0
        if a % b == 0:
            print(f"{a} la boi so cua {b}")
        else:
            print(f"{a} KHONG la boi so cua {b}")

        break

    except ValueError:
        print("Loi: Nhap lai so nguyen!")
