while True:
    try:
        x = float(input("Nhap so thuc: "))

        if (x > 0):
            result = x**2 + 3*x + 5
        else:
            result = -x**2 - 3*x - 5

        print(f"Gia tri bieu thuc la: {result:.2f}")

        break
    except ValueError:
        print("Nhap so thuc hop le!")
