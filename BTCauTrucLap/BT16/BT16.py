while True:
    try:
        # Nhap so nguyen N
        N = int(input("Nhap so nguyen N: "))
        if N <= 0:
            print("N phai la so nguyen duong. Vui long nhap lai.")
            continue
        
        # Tim cac uoc so cua N
        print(f"Cac uoc so cua {N} la: ", end="")
        for i in range(1, N + 1):
            if N % i == 0:
                print(i, end=" ")
        print()  # Xuong dong sau khi in het cac uoc so

        break

    except ValueError:
        print("Loi: Vui long nhap mot so nguyen hop le.")

