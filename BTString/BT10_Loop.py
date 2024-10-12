def most_frequent_characters(s):
    s = ''.join(s.strip().split())
    max_count = 0  # Đếm số lần xuất hiện lớn nhất
    max_chars = []  # Danh sách lưu ký tự xuất hiện nhiều lần nhất
    n = len(s)

    # Duyệt qua từng ký tự trong chuỗi
    for char in s:
        count = s.count(char)  # Đếm số lần xuất hiện của ký tự

        # Nếu số lần xuất hiện lớn hơn max_count
        if (count > max_count):
            max_count = count  # Cập nhật số lần xuất hiện lớn nhất
            max_chars = [char]  # Bắt đầu một danh sách mới với ký tự hiện tại
        elif (count == max_count and char not in max_chars):
            max_chars.append(char)  # Thêm ký tự vào danh sách nếu nó đã có số lần xuất hiện bằng nhau

    return max_chars, max_count

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    chars, count = most_frequent_characters(input_string)
    print(f"Ký tự xuất hiện nhiều lần nhất là: {', '.join(chars)} với số lần xuất hiện: {count}")

if __name__ == "__main__":
    main()
