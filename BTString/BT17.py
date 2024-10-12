def unique_substrings(s):
    # Tập hợp để lưu các xâu con khác nhau
    substrings = set()
    n = len(s)

    # Duyệt qua từng vị trí bắt đầu i của xâu
    for i in range(n):
        # Duyệt qua từng vị trí kết thúc j từ i đến hết xâu
        for j in range(i + 1, n + 1):
            # Thêm xâu con từ vị trí i đến j vào tập hợp
            substrings.add(s[i:j])

    return substrings

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    substrings = unique_substrings(input_string)
    print(f"Tất cả các xâu con khác nhau là:")
    for substring in substrings:
        print(substring)

if __name__ == "__main__":
    main()
