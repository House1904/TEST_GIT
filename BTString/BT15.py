def find_substrings(s, min_length):
    substrings = []  # Danh sách để lưu các xâu con

    n = len(s)
    
    # Duyệt qua từng vị trí bắt đầu của xâu ký tự
    for i in range(n):
        # Tạo xâu con từ độ dài min_length trở lên
        for j in range(i + min_length, n + 1):
            substrings.append(s[i:j])  # Thêm xâu con vào danh sách

    return substrings

def main():
    input_string = input("Nhập xâu ký tự: ")
    min_length = int(input("Nhập độ dài tối thiểu của xâu con: ")) 
    
    # Gọi hàm để tìm tất cả các xâu con thỏa mãn độ dài tối thiểu
    substrings = find_substrings(input_string, min_length)
    
    # In các xâu con tìm được
    print(f"Tất cả các xâu con có độ dài >= {min_length}:")
    for substring in substrings:
        print(substring)

if __name__ == "__main__":
    main()
