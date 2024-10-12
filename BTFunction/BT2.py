# Hàm tính trung vị của 3 số
def median_of_three(a, b, c):
    # Sắp xếp 3 số theo thứ tự và trả về số ở giữa
    return sorted([a, b, c])[1]

def get_input(prompt):
    while True:
        try:
            n = float(input(prompt))  # Sử dụng input() của Python
            if n > 0:
                return n
            else:
                print("Nhập lại số dương.")
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng.")

# Chương trình chính
def main():
    # Đọc 3 giá trị từ người dùng
    x = get_input("Nhập giá trị thứ nhất: ")
    y = get_input("Nhập giá trị thứ hai: ")
    z = get_input("Nhập giá trị thứ ba: ")
        
    # Tính trung vị
    median = median_of_three(x, y, z)
        
    # Hiển thị kết quả
    print(f"Trung vị của ba điểm {x}, {y}, {z} là: {median}")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()
