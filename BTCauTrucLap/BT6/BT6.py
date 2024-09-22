while True:
    try:
        # Nhập tháng từ người dùng
        month = int(input("Nhap thang (1 - 12): "))

        # Kiểm tra xem tháng nhập có hợp lệ không
        if 1 <= month <= 12:
            # Xác định mùa dựa trên tháng nhập
            if month in [12, 1, 2]:
                season = "Mua dong"
            elif month in [3, 4, 5]:
                season = "Ma xuan"
            elif month in [6, 7, 8]:
                season = "Mua ha"
            else:  # month in [9, 10, 11]
                season = "Mua thu"

            # In ra mùa của tháng đã nhập
            print(f"Thang {month} thuoc {season}.")
            break
        else:
            print("Thang khong hop le. Vui long nhap thang tu 1 den 12!")

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le!")
