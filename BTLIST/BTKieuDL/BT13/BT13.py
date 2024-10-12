import math

x = [math.pi, math.pi / 2, (4 * math.pi) / 3]

for i in range(3):
    ketQua = bool((math.sin(x[i])**2 + math.cos(x[i])**2) == 1)
    print(ketQua)

