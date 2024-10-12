import pandas as pd

# Đọc file Excel
file_name = 'stock_prices_and_portfolios_vn.xlsx'  # Tên file Excel
stock_df = pd.read_excel(file_name, sheet_name='Stock Prices')
portfolio_df = pd.read_excel(file_name, sheet_name='Portfolio Structure')

# Chuyển đổi cột 'Date' về kiểu datetime
stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')

# Lưu trữ độ lệch chuẩn của các portfolio
std_devs = {}

# Duyệt qua từng portfolio trong Portfolio Structure
for index, row in portfolio_df.iterrows():
    stock = row['Stock']
    percentage = row['Percentage']
    
    # Kiểm tra nếu cổ phiếu có trong dữ liệu
    if stock in stock_df.columns:
        # Lấy giá trị của cổ phiếu từ ngày thứ 10 trở đi
        values = stock_df[stock].iloc[9:]  # Từ dòng thứ 10 trở đi
        # Tính giá trị của portfolio
        portfolio_value = values * percentage
        # Tính độ lệch chuẩn cho giá trị portfolio
        std_dev = portfolio_value.std()
        std_devs[stock] = std_dev

# In kết quả
for stock, std_dev in std_devs.items():
    print(f"{stock}: Độ lệch chuẩn = {std_dev:.2f}")
