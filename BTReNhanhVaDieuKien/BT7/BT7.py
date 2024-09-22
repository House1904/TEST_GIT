import math

# Nhap nam tu nguoi dung
while True:
    try:
        year = int(input("Nhap nam: "))
        if year > 0:
            break
        else:
            print("Loi: Vui long nhap nam lon hon 0.")
    except ValueError:
        print("Loi: Vui long nhap mot nam hop le.")

# Tinh toan thu cua ngay 1 thang 1
day_of_the_week = (year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7

# Su dung if-else de xac dinh thu cua ngay 1 thang 1
if day_of_the_week == 0:
    print(f"Ngay 1 thang 1 nam {year} la Chu Nhat.")
elif day_of_the_week == 1:
    print(f"Ngay 1 thang 1 nam {year} la Thu Hai.")
elif day_of_the_week == 2:
    print(f"Ngay 1 thang 1 nam {year} la Thu Ba.")
elif day_of_the_week == 3:
    print(f"Ngay 1 thang 1 nam {year} la Thu Tu.")
elif day_of_the_week == 4:
    print(f"Ngay 1 thang 1 nam {year} la Thu Nam.")
elif day_of_the_week == 5:
    print(f"Ngay 1 thang 1 nam {year} la Thu Sau.")
else:
    print(f"Ngay 1 thang 1 nam {year} la Thu Bay.")
