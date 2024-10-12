def remove_duplicate(s):
    result_string = ""  # Chuỗi kết quả sau khi loại bỏ ký tự trùng lặp

    for char in s:
        if (char not in result_string):
            result_string += char  # Thêm ký tự vào kết quả nếu chưa có

    return result_string

def main():
    input_string = input("Nhập chuỗi cần xoá trùng lặp: ")
    print("Chuỗi sau khi xoá kí tự trùng lặp: " + remove_duplicate(input_string))

if __name__ == "__main__":
    main()
