# Định nghĩa các hằng số
BASE_FARE = 4.0  # Giá cơ sở (USD)
COST_PER_140M = 0.25  # Giá mỗi 140m (USD)
METERS_PER_KM = 1000  # Số mét trong 1 km
DISTANCE_UNIT = 140  # Đơn vị khoảng cách tính giá (140m)

def get_input(prompt):
    while True:
        try:
            n = float(input(prompt))  # Sử dụng input() của Python
            if n > 0:
                return n
            else:
                print("Nhập lại số dương.")
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng.")

# Hàm tính giá dịch vụ taxi
def calculate_taxi_fare(distance_km):
    # Chuyển đổi quãng đường từ km sang mét
    distance_m = distance_km * METERS_PER_KM
    
    # Tính số lần của 140m trong quãng đường
    units_of_140m = distance_m / DISTANCE_UNIT
    
    # Tính giá thành dựa trên quãng đường
    total_fare = BASE_FARE + units_of_140m * COST_PER_140M
    
    return total_fare

# Nhập quãng đường di chuyển từ người dùng
distance_km = get_input("Nhập giá trị km để tính tiền: ")

# Tính giá dịch vụ taxi
fare = calculate_taxi_fare(distance_km)

# In ra giá dịch vụ 
print(f"Giá dịch vụ cho quãng đường {distance_km} km là: {fare:.2f} USD")
