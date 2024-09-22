while True:
    try:
        # Nhập 3 số nguyên
        a = int(input("Nhap so nguyen a: "))
        b = int(input("Nhap so nguyen b: "))
        c = int(input("Nhap so nguyen c: "))

        # Khởi tạo biến max_even với giá trị None
        max_even = None

        # Kiểm tra từng số để tìm số chẵn lớn nhất
        if a % 2 == 0:
            max_even = a
        if b % 2 == 0 and (max_even is None or b > max_even):
            max_even = b
        if c % 2 == 0 and (max_even is None or c > max_even):
            max_even = c

        # In ra kết quả
        if max_even is not None:
            print(f"So chan lon nhat la: {max_even}")
        else:
            print("Khong co so chan nao.")

        break

    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le!")


