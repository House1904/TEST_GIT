def get_input(prompt):
    while True:
        try:
            n = float(input(prompt))  
            if n > 0:
                return n
            else:
                print("Nhập lại số dương.")
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng.")

def filter_speeds(speed_lst, min_speed):
    filtered_speeds = []  # Danh sách để lưu các tốc độ nhỏ hơn min
    indices_lst = []          # Danh sách để lưu chỉ số của các tốc độ nhỏ hơn min
    
    # Duyệt qua từng tốc độ trong danh sách bằng vòng lặp bình thường
    for i in range(len(speed_lst)):
        speed = speed_lst[i]  # Lấy tốc độ tại chỉ số i
        if (speed < min_speed):
            filtered_speeds.append(speed)  # Thêm tốc độ vào danh sách lọc
            indices_lst.append(i)          # Thêm chỉ số vào danh sách chỉ số

    return filtered_speeds, indices_lst

def main():
    speed_lst = list(map(int,input("Nhập danh sách các tốc độ quay của động cơ: ").strip().split()))

    min_speed = get_input("Nhập tốc độ nhỏ nhất: ")

    result_speeds, result_indices = filter_speeds(speed_lst, min_speed)

    print("Tốc độ quay nhỏ hơn min:", result_speeds)
    print("Chỉ số của các tốc độ này:", result_indices)

if __name__ == "__main__":
    main()
