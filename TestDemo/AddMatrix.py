import numpy as np

# Hàm nhập ma trận từ bàn phím
def nhap_ma_tran(hang, cot):
    ma_tran = []
    for i in range(hang):
        while True:
            try:
                hang_i = list(map(int, input(f"Hang {i+1}: ").split()))
                if len(hang_i) == cot:
                    ma_tran.append(hang_i)
                    break
                else:
                    print(f"Loi: Vui long nhap chinh xac {cot} so!")
            except ValueError:
                print("Loi: Vui long nhap lai!")
    return np.array(ma_tran)

# Hàm nhập kích thước ma trận (hàng và cột cùng lúc)
def nhap_kich_thuoc_ma_tran():
    while True:
        try:
            hang, cot = map(int, input("Nhap so hang va so cot (cach nhau boi khoang trang): ").split())
            if hang > 0 and cot > 0:
                return hang, cot
            else:
                print("Loi: So hang va so cot phai la so nguyen duong.")
        except ValueError:
            print("Loi: Vui long nhap hai so nguyen.")

while True:
    # Nhập kích thước ma trận A
    print("Nhap kich thuoc ma tran A:")
    hang_A, cot_A = nhap_kich_thuoc_ma_tran()

    # Nhập ma trận A
    print("Nhap ma tran A:")
    A = nhap_ma_tran(hang_A, cot_A)

    # Nhập kích thước ma trận B
    print("Nhap kich thuoc ma tran B:")
    hang_B, cot_B = nhap_kich_thuoc_ma_tran()

    # Nhập ma trận B
    print("Nhap ma tran B:")
    B = nhap_ma_tran(hang_B, cot_B)

    # Kiểm tra kích thước của hai ma trận
    if A.shape != B.shape:
        print("Hai ma tran phai co cung kich thuoc de thuc hien phep cong.")
        print("Vui long nhap lai cac ma tran.")
    else:
        # Cộng hai ma trận
        C = A + 2 * B # tương đương C = np.add(A, B)
        print("Phep cong hai ma tran la:\n", C)
        break  # Thoát khỏi vòng lặp khi đã cộng thành công
