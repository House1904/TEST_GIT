THUE = 0.10  #10%

don_gia = float(input("Nhap don gia: "))
so_luong = float(input("Nhap so luong san pham: "))

tong_tien_truoc_thue = don_gia * so_luong
tien_thue = tong_tien_truoc_thue * THUE
tong_tien_sau_thue = tong_tien_truoc_thue + tien_thue

print(f"Tong tien truoc thue: {tong_tien_truoc_thue:.2f} VND")
print(f"Tien thue 10%: {tien_thue:.2f} VND")
print(f"Tong tien sau thue: {tong_tien_sau_thue:.2f} VND")