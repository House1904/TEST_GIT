class ToanHoc:
    def __init__(self, *nso):
        # Khởi tạo với n số đầu vào
        self.nso = nso

    def TinhTong(self):
        # Hàm tính tổng các số
        return sum(self.nso)

    def TinhTrungBinh(self):
        # Hàm tính trung bình cộng
        return sum(self.nso) / len(self.nso) if self.nso else 0

    def TimMax(self):
        # Hàm tìm số lớn nhất
        return max(self.nso) if self.nso else None

    def TimMin(self):
        # Hàm tìm số nhỏ nhất
        return min(self.nso) if self.nso else None

    def HienThi(self):
        # Hàm hiển thị thông tin các số
        print("Danh sách các số:", self.nso)
        print("Tổng các số:", self.TinhTong())
        print("Trung bình cộng:", self.TinhTrungBinh())
        print("Số lớn nhất:", self.TimMax())
        print("Số nhỏ nhất:", self.TimMin())

# Ví dụ sử dụng lớp ToanHoc
toan_hoc = ToanHoc(5, 10, 15, 20, 25)

# Hiển thị thông tin về các số
toan_hoc.HienThi()
