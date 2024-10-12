def count_words(s):
    # Phân tách chuỗi thành danh sách các từ
    words = s.split()
    # Trả về số lượng từ
    return len(words)

def main():
    input_string = input("Nhập xâu (cách nhau bởi dấu cách): ")
    word_count = count_words(input_string)
    print(f"Số lượng từ trong xâu là: {word_count}")

if __name__ == "__main__":
    main()
