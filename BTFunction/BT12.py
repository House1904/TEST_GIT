import math 

def get_input(prompt):
    while True:
        try:
            n = float(input(prompt))  
            return n
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng.")

def cos_taylor(x, epsilon=1e-15): #epsilon càng nhỏ thì độ chính xác càng cao
    # Khởi tạo các giá trị ban đầu cho chuỗi Taylor
    term = 1  # Số hạng đầu tiên là 1 ứng với n = 0 
    cos_x = term  # Bắt đầu với giá trị cos(x) = 1 ứng với n = 0
    n = 1  # Bắt đầu từ số hạng thứ 1 trong chuỗi Taylor
    
    while abs(term) > epsilon:  # Tiếp tục nếu số hạng đủ lớn
        term = (-1) ** n * (x ** (2 * n)) / math.factorial(2 * n)  # Tính số hạng thứ n
        cos_x += term  # Cộng số hạng vào kết quả
        n += 1  # Tăng n để chuyển sang số hạng tiếp theo
    
    return cos_x

# Ví dụ sử dụng
if __name__ == "__main__":
    x = get_input("Nhập giá trị x (radian): ")
    print("cos(x) được tính bằng chuỗi Taylor:", cos_taylor(x))
    print("cos(x) thực tế:", math.cos(x))  # Đối chiếu với hàm cos của thư viện math
