def main():
    # Nhận chuỗi từ người dùng
    input_string = " ".join(input("Nhập xâu (cách nhau bởi dấu cách): ").strip().split())

    # Đảo ngược toàn bộ chuỗi
    reverse_string = input_string[::-1]

    print("Chuỗi đảo ngược:", reverse_string)

if __name__ == "__main__":
    main()
