def main():
    input_string = input("Nhập chuỗi đầu vào: ")
    substring = input("Nhập chuỗi con cần tìm: ")

    count = input_string.count(substring)
    print(f"Số lần xuất hiện của chuỗi con {substring} là: {count}")

if __name__ == "__main__":
    main()
