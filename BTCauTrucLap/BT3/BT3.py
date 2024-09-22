while True:
    try:
        n = int(input("Nhap so nguyen duong n: "))
        if (n <= 0):
            print("Nhap lai! n la so nguyen duong")
            continue
        else:
            print(n)
        break
    except ValueError: 
        print("Loi, Vui long nhap n dung dinh dang so nguyen!")
