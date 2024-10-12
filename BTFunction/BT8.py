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

def check_star_saving(kWh_number):
    if kWh_number < 2:
        return 5
    elif kWh_number >= 2 and kWh_number < 4:
        return 4
    elif kWh_number >= 4 and kWh_number < 6:
        return 3
    elif kWh_number >= 6 and kWh_number < 10:
        return 2
    else: 
        return 1

def main():
    P = get_input("Nhập số kWh điện cần kiểm tra: ")
    print("Số sao tiết kiệm điện của thiết bị:", check_star_saving(P))

if __name__ == "__main__":
    main()
