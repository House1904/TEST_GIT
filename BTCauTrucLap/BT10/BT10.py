while True:
    try:
        # Nhap so nguyen duong
        n = int(input("Nhap so nguyen duong: "))

        # Kiem tra xem so nhap vao co phai la so duong hay khong
        if n <= 0:
            print("Loi: Vui long nhap so nguyen duong.")
            continue
        
        # Tinh tong cac chu so trong so nguyen
        tong_chu_so = 0
        while n > 0:
            tong_chu_so += n % 10  # Lay chu so cuoi cung
            n = n // 10  # Loai bo chu so cuoi cung

        print(f"Tong cac chu so trong so vua nhap la: {tong_chu_so}")
        break

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

