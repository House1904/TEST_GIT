import numpy as np

def nhap_ma_tran(hang, cot):
	ma_tran = []
	for i in range(hang):
		while True:
			try:
				hang_i = list(map(int,input(f"Hang {i+1}: ").split()))
				if (len(hang_i) == cot):
					ma_tran.append(hang_i)
					break
				else:
					print("Nhap lai cac phan tu cua hang.")
			except ValueError:
				print("Loi: Vui long nhap so nguyen.")
	return np.array(ma_tran)

def kiem_tra_kich_thuoc():
	while True:
		try:
			hang,cot = map(int,input("Nhap hang va cot tuong ung: ").split())
			if hang > 0 and cot > 0:
				return hang,cot
			else:
				print("Nhap lai!")
		except ValueError:
			print("Loi: Vui long nhap so nguyen.")

while True:
	print("Nhap ma tran A: ")
	hang_A, cot_A = kiem_tra_kich_thuoc()

	print("Nhap cac phan tu cua ma tran A: ")
	A = nhap_ma_tran(hang_A, cot_A)

	print("Nhap ma tran B: ")
	hang_B, cot_B = kiem_tra_kich_thuoc()

	print("Nhap cac phan tu cua ma tran B: ")
	B = nhap_ma_tran(hang_B, cot_B)

	if (cot_A == hang_B):
		C = A @ B
		print("Tich ma tran A va B la: \n" , C)
		break
	else:
		print("So cot A phai bang so hang B, yeu cau nhap lai 2 MT.")
		

