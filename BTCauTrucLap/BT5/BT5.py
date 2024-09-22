while True:
    try:
        n = int(input("Nhap so nguyen duong n: "))
        if n <= 0:
            print("Nhap lai. n phai la so nguyen duong (lớn hơn 0)!")
            continue
        else:
            for i in range(1, n + 1):
                print(f"{i} ", end='')  # In số trên cùng một dòng
            print()  # Xuống dòng sau khi in xong
        break
    except ValueError:
        print("Loi. Vui long nhap dung dinh dang so nguyen!")
