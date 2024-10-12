def validate_email(email):
    # Kiểm tra nếu email chứa đúng 1 ký tự '@'
    if email.count('@') != 1:
        return False
    
    # Phân tách chuỗi email thành phần trước và sau '@'
    local_part, domain_part = email.split('@')

    # Kiểm tra chuỗi trước và sau '@' không được rỗng
    if not local_part or not domain_part:
        return False

    # Phân tách phần domain với dấu '.'
    domain_parts = domain_part.split('.')

    # Kiểm tra xem domain phải có ít nhất 2 phần và không có phần nào rỗng
    if len(domain_parts) < 2 or any(part == '' for part in domain_parts):
        return False

    return True

def main():
    # Yêu cầu người dùng nhập địa chỉ email
    email = input("Nhập địa chỉ email: ")
    
    # Kiểm tra tính hợp lệ của email
    if validate_email(email):
        print("Địa chỉ email hợp lệ.")
    else:
        print("Địa chỉ email không hợp lệ.")

if __name__ == "__main__":
    main()
