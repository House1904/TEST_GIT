# Nhập số lượng phần tử n
while True:
    try:
        n = int(input("Nhập số lượng phần tử n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập n lớn hơn 0.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

# Nhập danh sách a
a = []
print("Nhập các phần tử cho danh sách a:")
for i in range(n):
    element = input(f"Nhập phần tử a[{i}]: ")
    a.append(element)

# Nhập danh sách b
b = []
print("Nhập các phần tử cho danh sách b:")
for i in range(n):
    element = input(f"Nhập phần tử b[{i}]: ")
    b.append(element)

# Tạo dictionary mydict
mydict = {a[i]: b[i] for i in range(n)}

# In ra dictionary
print("Dictionary mydict:", mydict)
