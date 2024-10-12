while True:
    try:
        n = int(input("Nhap so nguyen duong n: "))
        if (n > 0):
            break
        else:
            print("Nhap lai n > 0")
    except ValueError: 
        print("Loi, Vui long nhap n dung dinh dang so nguyen!")

print("So vua nhap la:",n)