def sisyphus_sequence(num):
    seen_123 = 0  # Biến đếm số lần xuất hiện của 123

    while seen_123 < 2:
        # Chuyển số thành chuỗi để xử lý
        str_num = str(num)

        # Đếm số chữ số chẵn, lẻ và tổng
        even_count = sum(1 for digit in str_num if int(digit) % 2 == 0)
        odd_count = sum(1 for digit in str_num if int(digit) % 2 != 0)
        total_count = len(str_num)

        # Tạo số mới từ đếm chữ số
        new_num = int(f"{even_count}{odd_count}{total_count}")

        # In ra kết quả từng bước
        print(f"{even_count} chữ số chẵn – {odd_count} chữ số lẻ - tổng {total_count} chữ số, ta được số: {new_num}")

        # Kiểm tra xem số mới có phải là 123 không
        if new_num == 123:
            seen_123 += 1
        else:
            seen_123 = 0  # Reset nếu không phải 123

        # Cập nhật số cho vòng lặp tiếp theo
        num = new_num

# Nhập vào một số bất kỳ
input_number = int(input("Nhập vào một số tự nhiên: "))
sisyphus_sequence(input_number)
