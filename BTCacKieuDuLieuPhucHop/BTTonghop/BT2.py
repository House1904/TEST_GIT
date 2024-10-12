import string

# Nhập câu từ người dùng
input_sentence = input("Nhập câu của bạn: ")

# Khởi tạo dictionary để lưu số lần xuất hiện của mỗi chữ cái
letter_count = {}

# Loại bỏ dấu câu
input_sentence = input_sentence.translate(str.maketrans("", "", string.punctuation))

# Duyệt qua từng ký tự trong câu
for char in input_sentence:
    if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
        if char in letter_count:  # Nếu ký tự đã có trong dictionary
            letter_count[char] += 1  # Tăng số lần xuất hiện
        else:
            letter_count[char] = 1  # Khởi tạo số lần xuất hiện là 1

# In ra kết quả
for letter, count in letter_count.items():
    print(f"Số lần xuất hiện của '{letter}': {count} lần")
