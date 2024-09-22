BangAnhXa = {
    "A+" : 4.0,
    "A" : 4.0,
    "A-" : 3.7,
    "B+" : 3.3,
    "B" : 3.0,
    "B-" : 2.7,
    "C+" : 2.3,
    "C" : 2.0,
    "C-" : 1.7,
    "D+" : 1.3,
    "D" : 1.0,
    "F" : 0
    }
while True:
    # Đọc ký tự từ người dùng
    kyTu = input("Nhap 1 ki tu: ").upper()  # Chuyển ký tự về chữ in hoa

    # Kiểm tra ký tự trong bảng ánh xạ
    if kyTu in BangAnhXa:
        print(f"Diem so cua ki tu '{kyTu}' la: {BangAnhXa[kyTu]}")
        break  # Thoát khỏi vòng lặp khi nhập đúng ký tự
    else:
        print("Yeu cau nhap lai ki tu hop le!")
