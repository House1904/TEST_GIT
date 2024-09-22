lst = []
for i in range(7):
    while True:
        try:
            lst.append(float(input(f"Nhap nhiet do ngay Thu {i+1}: ")))
            break
        except ValueError:
            print("Loi: Vui long nhap dung dinh dang nhiet do.")

total = sum(lst)
avarage = total/7 # nhiệt độ trung bình

count = 0
for x in lst:
    if x > avarage:
        count+=1

print(f"Nhiet do trung binh trong tuan la: {avarage:.2f} do C")
print(f"Co {count} ngay nhiet do lon hon nhiet do trung binh {avarage:.2f} do C")

