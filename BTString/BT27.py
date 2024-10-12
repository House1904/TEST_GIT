def format_and_translate(sentence):
    # Viết hoa chữ cái đầu của mỗi từ
    titled_sentence = sentence.title()
    print(f"Câu sau khi dùng title(): {titled_sentence}")

    # Tạo bản dịch từ nguyên âm sang số
    translation_table = str.maketrans('abcdefghi', '123456789')

    # Thay thế các nguyên âm trong câu đã định dạng bằng số
    translated_sentence = titled_sentence.translate(translation_table)
    
    return translated_sentence

def main():
    # Nhập câu từ người dùng
    sentence = input("Nhập một câu: ")
    
    # Gọi hàm xử lý và hiển thị kết quả
    result = format_and_translate(sentence)
    print(f"Câu sau khi dùng translate(): {result}")

if __name__ == "__main__":
    main()
