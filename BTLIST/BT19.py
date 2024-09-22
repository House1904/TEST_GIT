while True:
    try:
        N = int(input("Nhap gia tri N (N > 0): "))
        if N > 0:
            break
        else:
            print("Loi: Vui long nhap N > 0.")
    except ValueError:
        print("Loi: Vui long nhap N la so nguyen hop le.")

# Kiểm tra và nhập danh sách các đồng xu
while True:
    S_input = input("Nhap cac gia tri xu (cach nhau boi dau phay): ")
    try:
        S = [int(value.strip()) for value in S_input.split(',') if int(value.strip()) > 0]  # Chuyển đổi và kiểm tra giá trị dương
        if len(S) > 0:
            break
        else:
            print("Loi: Vui long nhap cac gia tri xu dương.")
    except ValueError:
        print("Loi: Vui long nhap cac gia tri xu hop le.")

# Khởi tạo danh sách để lưu số cách đổi cho từng giá trị từ 0 đến N
ways = [0] * (N + 1) # Ban đầu số cách để đổi ra số tiền từ 0 đến N là 0 khi chưa dùng đồng xu nào
ways[0] = 1  # Mặc định: Chỉ có một cách để đổi 0 xu (1 cách duy nhất)

# Sử dụng vòng lặp để tìm số cách đổi
for coin in S:  # Duyệt qua từng đồng xu
    for amount in range(coin, N + 1):  # Duyệt từ giá trị đồng xu hiện đang xét đến N
        ways[amount] += ways[amount - coin]  # Cập nhật số cách đổi sau khi trừ số tiền 
        # định đổi cho xu hiện có, xu còn lại tương ứng số cách đổi được tính trước đó

# In kết quả
print(f"So cach de doi {N} xu voi danh sach xu {S} la: {ways[N]}")
