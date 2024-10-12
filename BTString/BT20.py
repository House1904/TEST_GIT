def count_characters(s):
    digits = 0  # Biến đếm số lượng ký tự số
    uppercase = 0  # Biến đếm số lượng chữ cái in hoa
    lowercase = 0  # Biến đếm số lượng chữ cái thường
    special = 0  # Biến đếm số lượng ký tự đặc biệt

    # Duyệt qua từng ký tự trong chuỗi
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif not char.isalnum():  # Ký tự không phải là chữ hoặc số
            special += 1

    return digits, uppercase, lowercase, special

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    digits, uppercase, lowercase, special = count_characters(input_string)

    print(f"Số lượng ký tự số: {digits}")
    print(f"Số lượng ký tự in hoa: {uppercase}")
    print(f"Số lượng ký tự thường: {lowercase}")
    print(f"Số lượng ký tự đặc biệt: {special}")

if __name__ == "__main__":
    main()
