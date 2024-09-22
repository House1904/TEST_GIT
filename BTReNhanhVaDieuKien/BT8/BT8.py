while True:
    try:
        month = int(input("Nhap thang: "))
        if 1 <= month <= 12:
            print("Thang nhap vao hop le!")
            break
        else:
            print("Nhap lai! Thang phai trong khoang tu 1 den 12.")
    except ValueError:
        print("Loi: Vui long nhap mot so nguyen.")
