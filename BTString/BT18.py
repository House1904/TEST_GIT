def repeated_substrings(s):
    substrings_count = {}  # Dictionary để lưu số lần xuất hiện của mỗi xâu con
    n = len(s)
    substring = [] # List để lưu chuỗi con

    # Duyệt qua từng vị trí bắt đầu i của xâu
    for i in range(n):
        # Duyệt qua từng vị trí kết thúc j từ i+1 đến hết xâu
        for j in range(i + 1, n + 1):
            # Lấy xâu con từ vị trí i đến j
            substring = s[i:j]
            # Kiểm tra và đếm số lần xuất hiện của xâu con
            if substring in substrings_count:
                substrings_count[substring] += 1
            else:
                substrings_count[substring] = 1

    # Tạo danh sách chứa các xâu con xuất hiện nhiều hơn 1 lần
    repeated_substrings = [sub for sub, count in substrings_count.items() if count > 1]

    return repeated_substrings

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    substrings = repeated_substrings(input_string)
    if substrings:
        print(f"Tất cả các xâu con lặp lại là:")
        for substring in substrings:
            print(substring)
    else:
        print("Không có xâu con lặp lại.")

if __name__ == "__main__":
    main()
