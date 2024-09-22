while True:
    try:
        # Nhap 5 so thuc
        a = float(input("Nhap a: "))
        b = float(input("Nhap b: "))
        c = float(input("Nhap c: "))
        d = float(input("Nhap d: "))
        e = float(input("Nhap e: "))

        # Tim max
        max_value = a
        if b > max_value:
            max_value = b
        if c > max_value:
            max_value = c
        if d > max_value:
            max_value = d
        if e > max_value:
            max_value = e

        # Tim min
        min_value = a
        if b < min_value:
            min_value = b
        if c < min_value:
            min_value = c
        if d < min_value:
            min_value = d
        if e < min_value:
            min_value = e

        # In ket qua
        print(f"So lon nhat la: {max_value}")
        print(f"So nho nhat la: {min_value}")
        break  # Thoat khoi vong lap neu da nhap thanh cong

    except ValueError:
        print("Loi: Vui long nhap mot so thuc hop le.")
