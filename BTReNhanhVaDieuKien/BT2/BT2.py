import decimal
from decimal import Decimal

# Đặt độ chính xác cho Decimal tối đa 10 chữ số thập phân
#decimal.getcontext().prec = 10

while True:
    try:
        n = Decimal(input("Nhap n: "))  # Chuyển đổi đầu vào thành Decimal
    except decimal.InvalidOperation:    # Bắt lỗi nhập sai cú pháp
        print("Vui long nhap lai!")
        continue    # Bỏ qua đánh giá n khi chưa nhập đúng cú pháp

    if n >= Decimal('0.6'):
        print("Danh gia: Meritorious")
        break
    elif n == Decimal('0.4'):
        print("Danh gia: Acceptable")
        break
    elif n == Decimal('0'):
        print("Danh gia: Unacceptable")
        break
    else:
        print("Vui long nhap lai!") # Bắt lỗi nhập không đúng giá trị sẵn có 

giaTriThuong = Decimal('2400') * n
print(f"Gia tri thuong la: {giaTriThuong:.2f}$")
