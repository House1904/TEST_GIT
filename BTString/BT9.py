def longest_unique_substring(s):
    max_length = 0  # Độ dài tối đa của chuỗi con không trùng lặp
    longest_substring = ""  # Chuỗi con dài nhất
    n = len(s)

    # Duyệt qua từng ký tự để tìm chuỗi con không trùng lặp
    for i in range(n):
        current_substring = ""  # Chuỗi con hiện tại
        for j in range(i, n):
            if s[j] in current_substring:
                break  # Nếu ký tự trùng lặp, dừng vòng lặp
            current_substring += s[j]  # Thêm ký tự vào chuỗi con hiện tại
            
            # Cập nhật chuỗi con dài nhất nếu cần
            if len(current_substring) > max_length:
                max_length = len(current_substring)
                longest_substring = current_substring  # Lưu chuỗi con dài nhất

    return longest_substring

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    substring = longest_unique_substring(input_string)
    print(f"Chuỗi con dài nhất không chứa ký tự trùng lặp là: '{substring}'")

if __name__ == "__main__":
    main()
