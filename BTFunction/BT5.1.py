import re  # Sử dụng regex để kiểm tra điều kiện

# Hàm kiểm tra tính bảo mật của mật khẩu
def is_secure_password(password):
    # Kiểm tra độ dài ít nhất 8 ký tự
    if len(password) < 8:
        return False
    
    # Kiểm tra có ít nhất 1 ký tự viết thường
    if not re.search("[a-z]", password):
        return False
    
    # Kiểm tra có ít nhất 1 ký tự viết hoa
    if not re.search("[A-Z]", password):
        return False
    
    # Kiểm tra có ít nhất 1 chữ số
    if not re.search("[0-9]", password):
        return False
    
    return True

# Chương trình chính
def main():
    password = input("Nhập mật khẩu: ")

    if is_secure_password(password):
        print("Mật khẩu có tính bảo mật cao.")
    else:
        print("Mật khẩu không có tính bảo mật cao.")

if __name__ == "__main__":
    main()
