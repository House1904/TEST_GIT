so_xe = input("Nhap so xe gom 5 chu so: ")

tong = 0
for i in range(5):
    tong += int(so_xe[i])
    
print(f"So xe cua ban co {tong%10} nut.")
