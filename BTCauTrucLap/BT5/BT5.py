while True:
    try:
        n = int(input("Nhap so nguyen duong n: "))
        if (n > 0):
            break
        else:
            print("Nhap lai. n phai la so nguyen duong (lon hon 0)!")
    except ValueError:
        print("Loi. Vui long nhap dung dinh dang so nguyen!")

for i in range(1, n + 1):
    print(f"{i} ", end='')  # In số trên cùng một dòng
    print()  # Xuống dòng sau khi in xong
