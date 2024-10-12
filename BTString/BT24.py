def count_word_frequency(input_string):
    # Chuyển chuỗi về dạng chữ thường để không phân biệt hoa thường
    input_string = input_string.lower().strip()

    # Tách chuỗi thành danh sách các từ (xóa các dấu câu trước khi đếm)
    words = input_string.split()

    # Sử dụng dictionary để đếm số lần xuất hiện của các từ
    word_count = {}

    for word in words:
        # Loại bỏ dấu câu khỏi từ
        word = word.strip(".,!?-")
        # Nếu từ đã tồn tại trong dictionary, tăng giá trị lên 1
        if word in word_count:
            word_count[word] += 1
        # Nếu từ chưa tồn tại, thêm từ vào dictionary và gán giá trị ban đầu là 1
        else:
            word_count[word] = 1

    return word_count

def main():
    input_string = input("Nhập chuỗi: ")
    word_count = count_word_frequency(input_string)

    print("Số lần xuất hiện của các từ:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
