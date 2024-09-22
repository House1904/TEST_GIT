import pandas as pd

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel('productsss.xlsx')

# In nội dung của DataFrame
print(df)

# Lấy dữ liệu cụ thể (ví dụ: cột "Name")
product_names = df['Name']
print("\nDanh sách sản phẩm: \n",product_names)

# Đọc một hàng cụ thể
row_data = df.loc[1]  # Hàng đầu tiên (index 1)
for key, value in row_data.items():
    print(f"{key}: {value}")

# Trong pandas, hàng đầu tiên có chỉ số index là 0 và hàng thứ hai có chỉ số index là 1. 
# Đây là cách chỉ mục (index) được đánh số mặc định trong pandas.

# Hàng đầu tiên 1 SP1 Coca 15 15000 có index là 0.
# Hàng thứ hai 2 SP2 Pepsi 20 18000 có index là 1.






