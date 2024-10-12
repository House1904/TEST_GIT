from my_package.quadratic_solver import solve_quadratic, get_input
from my_package.sort_ascending import sort_ascending
from my_package.sort_descending import sort_descending

def main():
    # Giải phương trình bậc 2
    a = get_input("Nhập a: ")
    b = get_input("Nhập b: ")
    c = get_input("Nhập c: ")
    print(solve_quadratic(a, b, c))

    # Sắp xếp mảng
    arr = list(map(int, input("Nhập mảng các số nguyên cách nhau bởi dấu cách: ").split()))
    print("Mảng tăng dần:", sort_ascending(arr))
    print("Mảng giảm dần:", sort_descending(arr))

if __name__ == "__main__":
    main()