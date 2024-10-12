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