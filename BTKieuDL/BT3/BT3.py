n = input("Nhap so nguyen 3 chu so: ")

tong = 0
for i in range(3):
    tong += int(n[i])

ketQua = tong / 3.0
print(f"Trung binh cong 3 chu so cua {n} la: {ketQua:.1f}")

