def get_input(prompt):
    while True:
        try:
            n = int(input(prompt)) 
            if n > 0:
                return n
            else:
                print("Nhập lại số dương.")
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng.")

# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if(x % i) == 0:
            return False
    return True

# Hàm tìm số nguyên tố lớn hơn n
def nextPrime(n):
    if n < 2:
        return 2  # Trường hợp n < 2, số nguyên tố nhỏ nhất là 2
    n += 1 if n % 2 == 0 else 2  # Bỏ qua số chẵn, tăng n lên số lẻ kế tiếp
    while not is_prime(n):
        n += 2  # Chỉ kiểm tra các số lẻ
    return n

# Chương trình chính
def main():
    n = get_input("Nhập n để tìm số nguyên tố lớn hơn n đầu tiên: ")
    result = nextPrime(n)
    print(f"Số nguyên tố đầu tiên lớn hơn {n} là {result}")

if __name__ == "__main__":
    main()
