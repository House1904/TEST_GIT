def is_palindrome(s):
    # Chuyển đổi chuỗi thành chữ thường và loại bỏ các khoảng trắng
    s = s.lower().replace(" ", "")
    # So sánh chuỗi với chuỗi nghịch đảo của nó
    return s == s[::-1]

def main():
    # Nhập chuỗi từ người dùng
    input_string = input("Nhập chuỗi cần kiểm tra: ")
    # Gọi hàm kiểm tra và in kết quả
    if is_palindrome(input_string):
        print("Chuỗi là chuỗi đối xứng.")
    else:
        print("Chuỗi không phải là chuỗi đối xứng.")

if __name__ == "__main__":
    main()