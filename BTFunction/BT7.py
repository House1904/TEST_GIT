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

def check_energy_saving(kWh_number):
    if kWh_number < 10:
        print("Tiết kiệm điện")
    else: 
        print("Không tiết kiệm điện")

def main():
    P = get_input("Nhập số kWh điện cần kiểm tra: ")
    check_energy_saving(P)

if __name__ == "__main__":
    main()