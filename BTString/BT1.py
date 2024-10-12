def main():
    input_string = input("Nhập chuỗi cần in từng kí tự: ")

    print("Tất cả các kí tự của chuỗi đầu vào là: ")
    for i in range(len(input_string)):
        print(input_string[i])

if __name__ == "__main__":
    main()