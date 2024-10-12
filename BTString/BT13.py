def is_reverse(s1, s2):
    # Kiểm tra xem chiều dài của hai xâu có bằng nhau không
    if (len(s1) != len(s2)):
        return False
    # So sánh s1 với đảo ngược của s2
    return s1 == s2[::-1]

def main():
    string1 = input("Nhập xâu ký tự thứ nhất: ")
    string2 = input("Nhập xâu ký tự thứ hai: ")
    if is_reverse(string1, string2):
        print(f"'{string1}' là đảo ngược của '{string2}'")
    else:
        print(f"'{string1}' không phải là đảo ngược của '{string2}'")

if __name__ == "__main__":
    main()
