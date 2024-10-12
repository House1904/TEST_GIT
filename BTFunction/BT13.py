def capitalize_words(s):
    # Tách chuỗi thành các từ bằng cách sử dụng split()
    words = s.lower().strip().split()
    
    # Viết hoa chữ cái đầu của mỗi từ, phần còn lại chuyển thành chữ thường
    capitalized_words = [word.capitalize() for word in words]
    
    # Ghép lại các từ thành chuỗi, cách nhau bằng dấu cách
    return ' '.join(capitalized_words)

def main():
    input_str = input("Nhập chuỗi: ")
    result_str = capitalize_words(input_str)
    print("Chuỗi sau khi viết hoa các chữ cái đầu:", result_str)

if __name__ == "__main__":
    main()
