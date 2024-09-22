while True:
    try:
        # Nhập 3 số nguyên
        a = int(input("Nhap so nguyen a: "))
        b = int(input("Nhap so nguyen b: "))
        c = int(input("Nhap so nguyen c: "))

        # Tìm số lớn nhì
        if (a >= b and a <= c) or (a >= c and a <= b):
            second_largest = a
        elif (b >= a and b <= c) or (b >= c and b <= a):
            second_largest = b
        else:
            second_largest = c

        # In ra kết quả
        print(f"So lon nhi la: {second_largest}")

        break

    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le!")

