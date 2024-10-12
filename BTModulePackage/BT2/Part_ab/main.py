from random_sequence import generate_random_sequence

def main():
    n = int(input("Nhập số phần tử trong dãy: "))
    min_value = int(input("Nhập giá trị nhỏ nhất: "))
    max_value = int(input("Nhập giá trị lớn nhất: "))
    
    random_sequence = generate_random_sequence(n, min_value, max_value)
    print("Dãy số ngẫu nhiên:", random_sequence)

if __name__ == "__main__":
    main()