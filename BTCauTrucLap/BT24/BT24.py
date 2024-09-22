import math

points = []

print("Nhap toa do cac diem cua da giac (x y). Nhap khoang trang de ket thuc.")

while True:
    x_input = input("Nhap x: ").strip()
    if x_input == "":
        break
    y_input = input("Nhap y: ").strip()
    
    try:
        x = float(x_input)
        y = float(y_input)
        points.append((x, y))
    except ValueError:
        print("Vui long nhap toa do hop le.")

if len(points) < 3:
    print("Can it nhat 3 diem de tao mot da giac.")
else:
    perimeter = 0
    num_points = len(points)
    
    for i in range(num_points):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % num_points]  # Ket noi diem cuoi voi diem dau
        
        # Tinh khoang cach giua (x1, y1) va (x2, y2)
        dx = x2 - x1
        dy = y2 - y1
        dist = math.sqrt(dx * dx + dy * dy)
        
        perimeter += dist
        
        print(f"Diem {i+1}: ({x1}, {y1}), Khoang cach toi diem {((i + 1) % num_points) + 1}: {dist:.2f}")

    print(f"Chu vi cua da giac la: {perimeter:.2f}")
