from BT8 import check_star_saving 

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

def get_energy_saving_message(star_number):
    if star_number < 3:
        return "Không tiết kiệm điện."
    else:
        return "Tiết kiệm điện."

def main():
    P = get_input("Nhập số kWh điện cần kiểm tra: ")
    star_rating = check_star_saving(P)
    message = get_energy_saving_message(star_rating)

    # In ra kết quả
    print(f"Số sao tiết kiệm điện của thiết bị: {star_rating} sao")
    print(message)

if __name__ == "__main__":
    main()
