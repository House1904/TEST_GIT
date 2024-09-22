while True:
    try:
        # Nhập số thực B từ bàn phím
        B = float(input("Nhap so thuc B: "))

        # Danh sách đã sắp xếp
        sorted_list = [1.0, 2.5, 3.7, 5.1, 6.8]

        # Tìm vị trí thích hợp để chèn B
        index = 0
        for i in range(len(sorted_list)):
            if B <= sorted_list[i]:
                index = i
                break
        else:
            # Nếu B lớn hơn tất cả các phần tử trong danh sách, chèn vào cuối
            index = len(sorted_list)

        # Chèn B vào danh sách
        sorted_list.insert(index, B)

        print("Danh sach sau khi chen:", sorted_list)
        break

    except ValueError:
        print("Loi: Vui long nhap mot so thuc hop le.")
