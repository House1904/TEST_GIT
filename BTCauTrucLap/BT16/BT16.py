while True:
    try:
        # Nhap so nguyen N
        N = int(input("Nhap so nguyen N: "))
        if (N > 0):
            break
        else:
            print("N phai la so nguyen duong. Vui long nhap lai.")

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

# Tim cac uoc so cua N
print(f"Cac uoc so cua {N} la: ")
for i in range(1, N + 1):
     if (N % i == 0):
        print(i)

