import string 

def is_strong_password(password):
    # Kiểm tra độ dài mật khẩu
    if len(password) < 8:
        return False

    # Khởi tạo các biến cờ (flag) để kiểm tra từng loại ký tự
    has_letter = False
    has_digit = False
    has_special = False

    # Kiểm tra từng ký tự trong mật khẩu
    for char in password:
        if char.isalpha():  # Kiểm tra nếu là chữ cái (bất kể hoa hay thường)
            has_letter = True
        elif char.isdigit():  # Kiểm tra nếu là chữ số
            has_digit = True
        elif char in string.punctuation:  # Kiểm tra nếu là ký tự đặc biệt
            has_special = True

    # Mật khẩu mạnh nếu có tất cả các loại ký tự cần thiết
    if has_letter and has_digit and has_special:
        return True
    else:
        return False

def main():
    password = input("Nhập mật khẩu: ")

    if is_strong_password(password):
        print("Mật khẩu mạnh.")
    else:
        print("Mật khẩu không mạnh. Vui lòng nhập mật khẩu mới.")

if __name__ == "__main__":
    main()
