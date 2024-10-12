def unique_substrings(s):
    # Dùng list để lưu trữ các xâu con và bảo toàn thứ tự
    substrings = []
    n = len(s)

    # Duyệt qua từng vị trí bắt đầu i của xâu
    for i in range(n):
        # Duyệt qua từng vị trí kết thúc j từ i đến hết xâu
        for j in range(i + 1, n + 1):
            # Lấy xâu con từ vị trí i đến j
            substring = s[i:j]
            # Chỉ thêm xâu con vào nếu chưa có trong list
            if substring not in substrings:
                substrings.append(substring)

    return substrings

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    substrings = unique_substrings(input_string)
    print(f"Tất cả các xâu con khác nhau là:")
    for substring in substrings:
        print(substring)

if __name__ == "__main__":
    main()
