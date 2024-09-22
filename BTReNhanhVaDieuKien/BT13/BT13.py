import math

while True:
    try:
        # Nhập 3 số nguyên a, b, c
        a = int(input("Nhap so nguyen a: "))
        b = int(input("Nhap so nguyen b: "))
        c = int(input("Nhap so nguyen c: "))

        # Kiểm tra nếu tất cả các số đều âm
        if a <= 0 and b <= 0 and c <= 0:
            print("Khong co so nguyen duong nho nhat!")
        else:
            # Khởi tạo giá trị min_positive với giá trị vô cùng dương (math.inf)
            min_positive = math.inf

            # So sánh từng số và tìm số dương nhỏ nhất
            if a > 0:
                min_positive = a
            if b > 0 and b < min_positive:
                min_positive = b
            if c > 0 and c < min_positive:
                min_positive = c

            # In ra kết quả
            print(f"So nguyen duong nho nhat la: {min_positive}")
        
        break

    except ValueError:
        print("Loi: Nhap lai 3 so nguyen!")
