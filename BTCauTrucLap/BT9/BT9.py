while True:
    try:
        # Nhap tu so va mau so
        tu_so = int(input("Nhap tu so: "))
        mau_so = int(input("Nhap mau so: "))

        # Kiem tra neu tu so hoac mau so bang 0 thi ket thuc vong lap
        if (tu_so == 0 or mau_so == 0):
            print("Ket thuc chuong trinh.")
            break

        # Tinh gia tri thap phan cua phan so
        gia_tri_thap_phan = tu_so / mau_so
        print(f"Gia tri thap phan cua phan so {tu_so}/{mau_so} la: {gia_tri_thap_phan:.3f}")

    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le.")


