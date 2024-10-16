from abc import ABC, abstractmethod
from datetime import datetime

class GiaoDich(ABC):
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong):
        self.ma_giao_dich = ma_giao_dich
        self.ngay_giao_dich = datetime.strptime(ngay_giao_dich, "%d/%m/%Y")
        self.don_gia = don_gia
        self.so_luong = so_luong

    @abstractmethod
    def thanh_tien(self):
        pass

    def __str__(self):
        return f"Mã giao dịch: {self.ma_giao_dich}, Ngày giao dịch: {self.ngay_giao_dich.strftime('%d/%m/%Y')}, Đơn giá: {self.don_gia}, Số lượng: {self.so_luong}"

class GiaoDichVang(GiaoDich):
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_vang):
        super().__init__(ma_giao_dich, ngay_giao_dich, don_gia, so_luong)
        self.loai_vang = loai_vang

    def thanh_tien(self):
        return self.so_luong * self.don_gia

    def __str__(self):
        return super().__str__() + f", Loại vàng: {self.loai_vang}, Thành tiền: {self.thanh_tien()}"


class GiaoDichTienTe(GiaoDich):
    def __init__(self, ma_giao_dich, ngay_giao_dich, ty_gia, so_luong, loai_tien_te, loai_giao_dich):
        super().__init__(ma_giao_dich, ngay_giao_dich, ty_gia, so_luong)
        self.loai_tien_te = loai_tien_te
        self.loai_giao_dich = loai_giao_dich

    def thanh_tien(self):
        if self.loai_giao_dich.lower() == "mua":
            return self.so_luong * self.don_gia
        elif self.loai_giao_dich.lower() == "bán":
            return (self.so_luong * self.don_gia) * 1.05
        return 0

    def __str__(self):
        return super().__str__() + f", Loại tiền tệ: {self.loai_tien_te}, Loại giao dịch: {self.loai_giao_dich}, Thành tiền: {self.thanh_tien()}"


class QuanLyGiaoDich:
    def __init__(self):
        self.danh_sach_giao_dich = []

    def nhap_giao_dich(self):
        while True:
            print("\nNhập thông tin giao dịch (hoặc gõ 'done' để kết thúc):")
            loai_giao_dich = input("Nhập loại giao dịch (vàng/tiền tệ): ")
            if loai_giao_dich.lower() == 'done':
                break

            ma_giao_dich = input("Nhập mã giao dịch: ")
            ngay_giao_dich = input("Nhập ngày giao dịch (ngày/tháng/năm): ")
        
            try:
                don_gia = float(input("Nhập đơn giá: "))
                so_luong = float(input("Nhập số lượng: "))
            except ValueError:
                print("Đơn giá và số lượng phải là số hợp lệ. Vui lòng thử lại.")
                continue
        
            try:
                if loai_giao_dich.lower() == 'vàng':
                    loai_vang = input("Nhập loại vàng (18k/24k/9999): ")
                    giao_dich = GiaoDichVang(ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_vang)
                elif loai_giao_dich.lower() == 'tiền tệ':
                    loai_tien_te = input("Nhập loại tiền tệ (USD/EUR/AUD): ")
                    loai_giao_dich_tien_te = input("Nhập loại giao dịch (mua/bán): ")
                    giao_dich = GiaoDichTienTe(ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_tien_te, loai_giao_dich_tien_te)
                else:
                    print("Loại giao dịch không hợp lệ.")
                    continue
            
                self.danh_sach_giao_dich.append(giao_dich)
                print(f"Giao dịch {ma_giao_dich} đã được thêm thành công!")
            except ValueError:
                print("Có lỗi xảy ra khi thêm giao dịch. Vui lòng kiểm tra lại thông tin.")

    def xuat_giao_dich(self):
        if not self.danh_sach_giao_dich:
            print("Chưa có giao dịch nào được nhập.")
            return
        print("\nDanh sách các giao dịch:")
        for giao_dich in self.danh_sach_giao_dich:
            print(giao_dich)

    def tong_so_luong_theo_loai(self):
        tong_so_luong = {}
        for giao_dich in self.danh_sach_giao_dich:
            loai = giao_dich.__class__.__name__
            if loai not in tong_so_luong:
                tong_so_luong[loai] = 0
            tong_so_luong[loai] += giao_dich.so_luong
        print("\nTổng số lượng theo loại giao dịch:")
        for loai, so_luong in tong_so_luong.items():
            print(f"{loai}: {so_luong}")

    def tong_thanh_tien_theo_loai(self):
        tong_thanh_tien = {}
        for giao_dich in self.danh_sach_giao_dich:
            loai = giao_dich.__class__.__name__
            if loai not in tong_thanh_tien:
                tong_thanh_tien[loai] = 0
            tong_thanh_tien[loai] += giao_dich.thanh_tien()
        print("\nTổng thành tiền theo loại giao dịch:")
        for loai, thanh_tien in tong_thanh_tien.items():
            print(f"{loai}: {thanh_tien}")

def main():
    quan_ly = QuanLyGiaoDich()
    while True:
        print("\n[BẢNG ĐIỀU KHIỂN]:")
        print("[1]. Nhập giao dịch")
        print("[2]. Xuất danh sách giao dịch")
        print("[3]. Tính tổng số lượng theo loại")
        print("[4]. Tính tổng thành tiền theo loại")
        print("[5]. Thoát")

        choice = input("Chọn một tùy chọn (1-5): ")
        if choice == '1':
            quan_ly.nhap_giao_dich()
        elif choice == '2':
            quan_ly.xuat_giao_dich()
        elif choice == '3':
            quan_ly.tong_so_luong_theo_loai()
        elif choice == '4':
            quan_ly.tong_thanh_tien_theo_loai()
        elif choice == '5':
            break
        else:
            print("Tùy chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
