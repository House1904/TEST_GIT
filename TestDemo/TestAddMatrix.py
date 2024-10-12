import numpy as np # khởi tạo thư viện numpy sử dụng np.[hàm] để dễ dàng tính toán

def nhapMaTran(hang, cot):
    maTran = [] # tạo ma trận ban đầu để người dùng nhập vào
    for i in range(hang):
        while True:
            try:
                hang_i = list(map(int,input(f"Hang {i+1}: ").split()))
                if (len(hang_i) == cot):
                    maTran.append(hang_i) # kiểm tra hợp lệ rồi thêm hàng vào ma trận
                    break
                else:
                    print("Nhap lai!")
            except ValueError:
                print("Nhap lai!")
    return np.array(maTran) # trả về ma trận sau khi nhập hợp lệ

def nhapHangCot():
    while True:
        try:
            hang, cot = map(int,input("Nhap hang va cot tuong ung cho ma tran: ").split())
            if (hang > 0 and cot > 0):
                return hang,cot # trả về hàng và cột tương ứng cho ma trận
            else:
                print("Nhap lai!")
        except ValueError:
            print("Nhap lai!")

while True:
    print("Nhap hang va cot ma tran A: ")
    hangA, cotA = nhapHangCot()
    print("Nhap ma tran A: ")
    A = nhapMaTran(hangA, cotA)

    print("Nhap hang va cot ma tran B: ")
    hangB,cotB = nhapHangCot()
    print("Nhap ma tran B: ")
    B = nhapMaTran(hangB,cotB)

    if (A.shape == B.shape):
        C = A + B
        print("Ket qua cong hai ma tran A va B: \n", C)
        break
    else:
        print("Nhap lai kich co A va B cho phu hop!")


