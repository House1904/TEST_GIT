while True:
    while True:
        try:
            # Nhap so nguyen duong N
            N = int(input("Nhap so nguyen duong N: "))
            if (N > 0):
                break
            else:
                print("N phai la so nguyen duong. Vui long nhap lai.")
        except ValueError:
            print("Loi: Vui long nhap mot so nguyen hop le.")

    # Nhap N so nguyen va tim so le lon nhat
    so_le_lon_nhat = None
    for i in range(N):
        num = int(input(f"Nhap so thu {i+1}: "))
        if (num % 2 != 0):  # Kiem tra so le
            if (so_le_lon_nhat is None or num > so_le_lon_nhat):
                so_le_lon_nhat = num

    # In ra so le lon nhat neu co
    if so_le_lon_nhat is not None:
       print(f"So le lon nhat la: {so_le_lon_nhat}")
    else:
       print("Khong co so le nao duoc nhap.")

    # Hoi nguoi dung co muon tiep tuc khong
    tiep_tuc = input("Ban co muon tiep tuc khong? Nhan 'c' de tiep tuc, phim khac de thoat: ")
    if (tiep_tuc.lower() != 'c'):
       print("Chuong trinh da thoat.")
       break
