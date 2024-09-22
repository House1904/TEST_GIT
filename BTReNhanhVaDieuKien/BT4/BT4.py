import math

while True:
    try:
        # Nhập ba số thực
        a = float(input("Nhap a: "))
        b = float(input("Nhap b: "))
        c = float(input("Nhap c: "))
        
        # Kiểm tra và giải phương trình bậc hai
        if a == 0:
            if b == 0:
                if c == 0:
                    print("Phuong trinh vo so nghiem.")
                else:
                    print("Phuong trinh vo nghiem.")
            else:
                x = -c / b
                print(f"Phuong trinh co mot nghiem: x = {x:.2f}")
        else:
            # Tính delta
            delta = b**2 - 4*a*c
            
            if delta < 0:
                print("Phuong trinh vo nghiem.")
            elif delta == 0:
                x = -b / (2*a)
                print(f"Phuong trinh co nghiem kep: x = {x:.2f}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                print(f"Phuong trinh co hai nghiem phan biet: x1 = {x1:.2f}, x2 = {x2:.2f}")
        
        # Thoát khỏi vòng lặp nếu người dùng đã nhập đúng và chương trình đã giải xong
        break

    except ValueError:
        print("Loi: Vui long nhap mot so thuc hop le.")
