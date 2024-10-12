import math as m

def get_input(prompt):
    while True:
        try:
            n = float(input(prompt))  
            return n
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng.")

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Vô số nghiệm"
            else:
                return []
        else:
            x = round((-c / b),2)
            return [x]
    else:
        delta = b**2 - 4 * a * c
        if (delta > 0):
            x1 = round(((-b + m.sqrt(delta)) / (2*a)),2)
            x2 = round(((-b - m.sqrt(delta)) / (2*a)),2)
            return [x1,x2]
        elif (delta  == 0):
            x = round((-b / (2*a)),2)
            return [x]
        else:
            return []
def main(): 
    a = get_input("Nhập hệ số a: ")
    b = get_input("Nhập hệ số b: ")
    c = get_input("Nhập hệ số c: ")

    print("Danh sách các nghiệm của phương trình ax^2 + bx + c = 0 là:")
    print(solve_quadratic(a, b, c))

if __name__ == "__main__":
    main()