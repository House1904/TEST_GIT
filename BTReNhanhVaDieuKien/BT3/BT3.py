while True:
    try:
        year = int(input("Nhap nam: "))  
    except ValueError: 
        print("Vui long nhap lai!")
        continue    

    if (year % 400 == 0):
        print(f"{year} la nam nhuan")
        break
    elif (year % 4 == 0 and year % 100 != 0):
        print(f"{year} la nam nhuan")
        break
    else:
        print(f"{year} la nam khong nhuan")
        break
