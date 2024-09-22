# Nhập số lượng tuple
n = int(input("Nhập số lượng tuple: "))

# Danh sách để chứa các tuple
data_list = []

# Nhập từng tuple
for i in range(n):
    # input_data = input(f"Nhập thông tin cho tuple {i + 1} (name, age, score): ")
    input_data = input()
    name, age, score = input_data.split(',')
    data_tuple = (name, age, score)
    data_list.append(data_tuple)

# Sắp xếp theo name, age, score
data_list.sort(key = lambda x: (x[0], x[1], x[2]))

# In ra kết quả
print(data_list)

