def NegativeNumberInStrings(s):
    negative_numbers = []  # Danh sách để lưu trữ các số âm
    current_number = ""     # Biến để xây dựng số hiện tại
    found_negative = False  # Biến cờ để kiểm tra nếu đã tìm thấy số âm

    for char in s:
        if char.isdigit() or char == '-':
            if char == '-':
                # Nếu đã tìm thấy dấu âm trước đó mà không có số sau,
                # reset current_number
                if current_number:
                    if current_number.startswith('-') and current_number[1:].isdigit():
                        negative_numbers.append(int(current_number))
                    current_number = char  # Khởi tạo current_number mới với dấu '-'
                    found_negative = True  # Đánh dấu đã tìm thấy dấu âm
                else:
                    current_number += char  # Bắt đầu số mới
            else:
                current_number += char  # Xây dựng số hiện tại
        else:
            # Nếu gặp ký tự không phải số, kiểm tra current_number
            if current_number.startswith('-') and current_number[1:].isdigit():
                negative_numbers.append(int(current_number))  # Thêm số âm vào danh sách
            current_number = ""  # Reset current_number

    # Kiểm tra số cuối cùng trong chuỗi
    if current_number.startswith('-') and current_number[1:].isdigit():
        negative_numbers.append(int(current_number))

    return negative_numbers


def main():
    string_input = input("Nhập chuỗi đầu vào: ")
    print("Các số nguyên âm trong chuỗi là:", NegativeNumberInStrings(string_input))

if __name__ == "__main__":
    main()
