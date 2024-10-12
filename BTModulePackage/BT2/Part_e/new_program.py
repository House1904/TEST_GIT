from my_package.quadratic_solver import solve_quadratic
from my_package.sort_ascending import sort_ascending
from my_package.sort_descending import sort_descending

# Sử dụng package như bình thường
a = 1
b = -3
c = 2
print(solve_quadratic(a, b, c))

arr = [3, 1, 4, 1, 5, 9]
print("Mảng tăng dần:", sort_ascending(arr))
print("Mảng giảm dần:", sort_descending(arr))
