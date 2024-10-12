def is_symmetrical(s):
    # Xác định độ dài của chuỗi
    length = len(s)
    
    # Chia chuỗi thành hai nửa
    first_half = s[:length // 2]  # Nửa đầu tiên
    if length % 2 == 0:
        second_half = s[length // 2:]  # Nửa thứ hai nếu độ dài là số chẵn
    else:
        second_half = s[length // 2 + 1:]  # Bỏ qua ký tự giữa nếu độ dài là số lẻ
    
    # So sánh hai nửa
    return first_half == second_half

def main():
    # Nhập chuỗi từ người dùng
    input_string = input("Nhập chuỗi cần kiểm tra: ")
    
    # Kiểm tra chuỗi có đối xứng không
    if is_symmetrical(input_string):
        print("Chuỗi là symmetrical.")
    else:
        print("Chuỗi không phải là symmetrical.")

if __name__ == "__main__":
    main()
