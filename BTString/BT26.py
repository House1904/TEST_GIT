import random
import string

def generate_password(length = 8): #nếu người dùng không nhập gì thì cũng mặc định bằng 8
    if (length < 8):
        length = 8  # Đảm bảo mật khẩu có độ dài tối thiểu là 8
    
    # Khởi tạo các danh sách chứa các loại ký tự khác nhau
    letters = string.ascii_letters  # Chữ cái (a-z, A-Z)
    digits = string.digits          # Chữ số (0-9)
    special_characters = string.punctuation  # Ký tự đặc biệt (!@#$%^&*...)

    # Đảm bảo mật khẩu có ít nhất 1 chữ cái, 1 chữ số, và 1 ký tự đặc biệt
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Điền thêm các ký tự ngẫu nhiên để đạt đủ độ dài
    all_characters = letters + digits + special_characters
    password += [random.choice(all_characters) for tmp in range(length - 3)]

    # Xáo trộn các ký tự trong mật khẩu để chúng không theo thứ tự nhất định
    random.shuffle(password)

    # Ghép lại các ký tự thành một chuỗi
    return ''.join(password)

def main():
    length = int(input("Nhập độ dài mật khẩu mong muốn (tối thiểu 8): "))
    password = generate_password(length)
    print(f"Mật khẩu ngẫu nhiên mạnh: {password}")

if __name__ == "__main__":
    main()
