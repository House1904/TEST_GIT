n = int(input("Nhập số lượng tuple: "))

# Danh sách để chứa các tuple
data_list = []

# Nhập từng tuple
for i in range(n):
    # Nhập và tạo tuple trong một dòng
    tuple_data = tuple(input(f"Nhập thông tin cho tuple {i + 1} (name, age, score): ").strip().split(','))
    
    # Thêm tuple vào danh sách
    data_list.append(tuple_data)

# Sắp xếp theo name, age, score dưới dạng chuỗi
data_list.sort(key=lambda x: (x[0], x[1], x[2]))

# In ra kết quả
print(data_list)
