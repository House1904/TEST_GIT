def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if(x % i) == 0:
            return False
    return True

def get_input(prompt):
    while True:
        try:
            n = int(input(prompt))  # Sử dụng input() của Python
            if n > 0:
                return n
            else:
                print("Nhập lại số dương.")
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng.")

def main():
    n = get_input("Nhập n: ")

    if (is_prime(n)):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không là số nguyên tố")

if __name__ == "__main__":
    main()