def string_to_ascii(s):
    # Chuyển đổi từng ký tự thành mã ASCII
    ascii_values = [ord(char) for char in s]
    return ascii_values

def ascii_to_string(ascii_values):
    # Chuyển đổi từng mã ASCII thành ký tự
    characters = [chr(value) for value in ascii_values]
    return ''.join(characters)

def main():
    # Chọn chế độ chuyển đổi
    print("Chế độ chuyển đổi giữa ASCII và String:")
    print("1: Xâu ký tự sang mã ASCII")
    print("2: Mã ASCII sang xâu ký tự")
    choice = input("Chọn chế độ chuyển đổi: ")

    if choice == '1':
        input_string = input("Nhập xâu ký tự: ")
        ascii_values = string_to_ascii(input_string)
        print(f"Mã ASCII tương ứng: {ascii_values}")

    elif choice == '2':
        ascii_input = input("Nhập mã ASCII (cách nhau bởi dấu phẩy): ")
        ascii_values = list(map(int, ascii_input.split(',')))
        result_string = ascii_to_string(ascii_values)
        print(f"âu ký tự tương ứng: '{result_string}'")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

if __name__ == "__main__":
    main()
