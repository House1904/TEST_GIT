# Nhập nội dung chuỗi ký tự từ người dùng
input_string = input("Nhập vào một nội dung chuỗi ký tự: ")

# Khởi tạo biến đếm
letter_count = 0
digit_count = 0

# Duyệt qua từng ký tự trong chuỗi
for char in input_string:
    if (char.isalpha()):  # Kiểm tra xem ký tự có phải là chữ cái không
        letter_count += 1
    if (char.isdigit()):  # Kiểm tra xem ký tự có phải là chữ số không
        digit_count += 1

# In ra kết quả
print(f"Số ký tự chữ: {letter_count}, số ký tự là số: {digit_count}")
