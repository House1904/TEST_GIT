def main():
    input_string = input("Nhập chuỗi kí tự: ")
    char = input("Nhập kí tự muốn thay thế: ")
    char_replace = input("Nhập kí tự thay thế: ")

    # Thực hiện thay thế ký tự
    if char in input_string:
        new_string = input_string.replace(char, char_replace)
        print(f"Chuỗi sau khi thay thế: {new_string}")
    else:
        print(f"Ký tự '{char}' không có trong chuỗi.")

if __name__ == "__main__":
    main()
