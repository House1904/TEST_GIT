while True:
    try:
        # Nhap so luong phan tu cua danh sach
        n = int(input("Nhap so luong phan tu: "))
        
        if n <= 0:
            print("Vui long nhap so nguyen duong!")
            continue

        # Nhap cac phan tu cua danh sach
        my_list = []
        for i in range(n):
            num = float(input(f"Nhap phan tu thu {i + 1}: "))
            my_list.append(num)

        # Nhap gia tri A
        A = float(input("Nhap gia tri A: "))

        # Tao danh sach moi chi chua cac phan tu khong lon hon A
        filtered_list = [x for x in my_list if x <= A]

        # Xuat danh sach moi
        print("Danh sach sau khi xoa cac phan tu lon hon A:")
        print(filtered_list)
        
        break

    except ValueError:
        print("Loi: Vui long nhap so hop le!")

