while True:
    try:
        # Nhập và kiểm tra điểm lý thuyết
        while True:
            theory_score = float(input("Nhap diem ly thuyet (0 - 10): "))
            if 0 <= theory_score <= 10:
                break
            else:
                print("Diem ly thuyet phai trong khoang [0, 10]. Vui long nhap lai.")
        
        # Nhập và kiểm tra điểm thực hành
        while True:
            practical_score = float(input("Nhap diem thuc hanh (0 - 10): "))
            if 0 <= practical_score <= 10:
                break
            else:
                print("Diem thuc hanh phai trong khoang [0, 10]. Vui long nhap lai.")
        
        # Tính điểm trung bình cộng
        average_score = (theory_score + practical_score) / 2
        print(f"Diem trung binh cong la: {average_score:.2f}")
        break

    except ValueError:
        print("Loi: Vui long nhap diem hop le (so thuc)!")
