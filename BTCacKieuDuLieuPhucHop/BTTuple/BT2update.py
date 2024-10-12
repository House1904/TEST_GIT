# Danh sách để chứa các tuple
data_list = []

# Nhập tuple cho đến khi người dùng không nhập gì và nhấn Enter
i = 0
while True:
    # Nhập và tạo tuple trong một dòng
    tuple_data = tuple(input(f"Nhập thông tin cho tuple {i + 1} (name, age, score): ").strip().split(','))
    
    # Nếu người dùng không nhập gì và nhấn Enter, dừng lại
    if (len(tuple_data) != 3):
        break
     
    # Thêm tuple vào danh sách
    data_list.append(tuple_data)
    
    i += 1

# Sắp xếp theo name, age, score dưới dạng chuỗi
data_list.sort(key=lambda x: (x[0], x[1], x[2]))

# In ra kết quả
print("Danh sách sau khi nhập là:\n",data_list)
