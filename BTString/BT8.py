def sort_string(s):
    # Sử dụng sorted để sắp xếp các ký tự trong chuỗi
    sorted_characters = sorted(s)  # hàm sorted trả về danh sách các kí tự 
    return ''.join(sorted_characters)  # Chuyển danh sách ký tự đã sắp xếp thành chuỗi

def main():
    # Nhập chuỗi từ người dùng
    input_string = input("Nhập chuỗi cần sắp xếp: ")

    # Gọi hàm sắp xếp và in kết quả
    sorted_string = sort_string(input_string)
    print("Chuỗi sau khi sắp xếp:", sorted_string)

if __name__ == "__main__":
    main()
