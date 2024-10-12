def get_file_name(file_path):
    """Lấy tên tệp từ đường dẫn."""
    # Tách chuỗi theo dấu '\\' và lấy phần cuối cùng
    parts = file_path.split('\\')
    return parts[-1]  # Phần cuối cùng là tên tệp

def get_file_name_without_extension(file_path):
    """Lấy tên tệp mà không có phần mở rộng."""
    # Gọi hàm get_file_name để lấy tên tệp
    file_name = get_file_name(file_path)

    # Tách tên tệp theo dấu '.' để lấy phần trước dấu '.'
    name_parts = file_name.split('.')
    return name_parts[0]  # Phần đầu tiên là tên tệp không có phần mở rộng

def main():
    file_path = input("Nhập đường dẫn tệp: ")
    
    # Lấy tên tệp và tên tệp không có phần mở rộng
    file_name = get_file_name(file_path)
    file_name_without_extension = get_file_name_without_extension(file_path)
    
    print("Tên tệp:", file_name)
    print("Tên tệp không có phần mở rộng:", file_name_without_extension)

if __name__ == "__main__":
    main()
