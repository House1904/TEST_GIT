def optimize_string(s):
    # Bỏ các khoảng trắng thừa ở đầu và cuối chuỗi, sau đó chia chuỗi thành danh sách từ
    words = s.strip().split()
    
    # Nối lại các từ với một khoảng trắng giữa
    optimized = ' '.join(words)
    return optimized

def main():
    # Nhập chuỗi từ người dùng
    input_string = input("Nhập chuỗi cần tối ưu: ")
    
    # Tối ưu chuỗi
    optimized_string = optimize_string(input_string)
    
    # In kết quả
    print("Chuỗi tối ưu:", optimized_string)

if __name__ == "__main__":
    main()
