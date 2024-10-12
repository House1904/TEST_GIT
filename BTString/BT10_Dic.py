def most_frequent_characters(s):
    s = ''.join(s.strip().split())
    char_count = {}
    
    # Đếm số lần xuất hiện của từng ký tự
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Tìm số lần xuất hiện lớn nhất
    max_count = max(char_count.values())
    
    # Lưu tất cả ký tự có số lần xuất hiện lớn nhất
    max_chars = [char for char, count in char_count.items() if count == max_count]

    return max_chars, max_count

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    chars, count = most_frequent_characters(input_string)
    print(f"Ký tự xuất hiện nhiều lần nhất là: {', '.join(chars)} với số lần xuất hiện: {count}")

if __name__ == "__main__":
    main()
