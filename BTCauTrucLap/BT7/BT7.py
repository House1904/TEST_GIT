while True:
    try:
        # Nhập thứ trong tuần từ người dùng
        day = int(input("Nhap thu trong tuan (1-7): "))

        # Kiểm tra xem giá trị nhập có hợp lệ không
        if (1 <= day <= 7):
            # Xác định tên của thứ trong tuần dựa trên số nhập
            days_of_week = {
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
            }
            print(f"Ngay {day} la {days_of_week[day]}.")
            break
        else:
            print("Gia tri khong hop le. Vui long nhap thu tu 1 den 7.")

    except ValueError:
        print("Loi: Vui long nhap so nguyen hop le.")

