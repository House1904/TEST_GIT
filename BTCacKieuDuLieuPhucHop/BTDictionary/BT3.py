while True:
    try:
        n = int(input("Nhập n (n > 0): "))
        if (n > 0):
            break
        else:
            print("Nhập lại n nguyên dương")
    except ValueError:
        print("Nhập lại số nguyên hợp lệ.")

dic = {}
for i in range(1,n+1):
    dic.update({i:i**2})

print(dic)

