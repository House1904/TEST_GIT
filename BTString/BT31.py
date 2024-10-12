def optimize_string(input_string):
    # Bước 1: Xóa khoảng trắng ở đầu và cuối chuỗi
    trimmed_string = input_string.strip()

    # Bước 2: Chia chuỗi thành các từ
    words = trimmed_string.split()

    # Bước 3: Chuyển đổi ký tự đầu tiên của mỗi từ thành chữ hoa
    optimized_words = [word.capitalize() for word in words]

    # Bước 4: Ghép các từ lại với nhau bằng một khoảng trắng
    optimized_string = ' '.join(optimized_words)

    return optimized_string

def main():
    # Nhập chuỗi từ người dùng
    input_string = input("Nhập chuỗi danh từ: ")
    optimized_result = optimize_string(input_string)
    print("Chuỗi tối ưu:", optimized_result)

if __name__ == "__main__":
    main() 
