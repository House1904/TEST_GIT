while True:
    try:
        # Nhap 5 so tu nguoi dung
        numbers = []
        for i in range(5):
            num = float(input(f"Nhap so thu {i+1}: "))
            numbers.append(num)
        
        # Khoi tao bien dem
        count_negative = 0
        count_positive = 0
        count_zero = 0
        
        # Dem so luong so am, so duong, va so bang 0
        for number in numbers:
            if number < 0:
                count_negative += 1
            elif number > 0:
                count_positive += 1
            else:
                count_zero += 1
        
        # In ket qua
        print(f"So am: {count_negative}")
        print(f"So duong: {count_positive}")
        print(f"So 0: {count_zero}")
        
        break

    except ValueError:
        print("Loi: Vui long nhap mot so thuc hop le.")
