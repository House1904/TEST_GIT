# Hàm kiểm tra tính bảo mật của mật khẩu
def is_secure_password(password):
    # Kiểm tra độ dài ít nhất 8 ký tự
    if len(password) < 8:
        return False
    
    # Các biến đánh dấu để kiểm tra các điều kiện
    has_lower = False  # Có chứa ký tự viết thường
    has_upper = False  # Có chứa ký tự viết hoa
    has_digit = False  # Có chứa số

    # Duyệt qua từng ký tự trong mật khẩu
    for char in password:
        if char.islower():  # Kiểm tra ký tự viết thường
            has_lower = True
        elif char.isupper():  # Kiểm tra ký tự viết hoa
            has_upper = True
        elif char.isdigit():  # Kiểm tra ký tự số
            has_digit = True

        if (has_lower and has_upper and has_digit):
            return True

    # Kiểm tra tất cả các điều kiện
    return False

# Chương trình chính
def main():
    password = input("Nhập mật khẩu: ")
    if is_secure_password(password):
        print("Mật khẩu có tính bảo mật cao.")
    else:
        print("Mật khẩu không có tính bảo mật cao.")

if __name__ == "__main__":
    main()
