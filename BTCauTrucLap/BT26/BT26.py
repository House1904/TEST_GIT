# Nhập số nguyên dương từ người dùng
decimal_number = int(input("Nhap so nguyen duong: "))

# Kiểm tra số âm và số 0
if decimal_number < 0:
    print("Vui long nhap so nguyen duong!")
else:
    result = ""  # Khởi tạo chuỗi rỗng để lưu kết quả

    q = decimal_number  # Số cần chuyển đổi

    # Lặp cho đến khi q bằng 0
    while q > 0:
        r = q % 2  # Phần dư của phép chia q cho 2
        result = str(r) + result  # Chuyển r thành chuỗi và cộng với phần bắt đầu của result
        q = q // 2  # Chia q cho 2 và loại bỏ phần dư, lưu phần nguyên vào q

    # Hiển thị kết quả
    print(f"Chuoi nhi phan tuong ung voi {decimal_number} la: {result}")

