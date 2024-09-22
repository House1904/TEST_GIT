import xlsxwriter

# Tạo tệp Excel mới
workbook = xlsxwriter.Workbook('products.xlsx')
worksheet = workbook.add_worksheet()

# Thêm tiêu đề cho các cột
worksheet.write('A1', 'ID')
worksheet.write('B1', 'Code')
worksheet.write('C1', 'Name')
worksheet.write('D1', 'Quantity')
worksheet.write('E1', 'Price')

# Thêm một dòng dữ liệu
worksheet.write('A2', 1)
worksheet.write('B2', 'SP1')
worksheet.write('C2', 'Coca')
worksheet.write('D2', 15)
worksheet.write('E2', 15000)

# Thêm một dòng dữ liệu
worksheet.write('A3', 2)
worksheet.write('B3', 'SP2')
worksheet.write('C3', 'Pepsi')
worksheet.write('D3', 20)
worksheet.write('E3', 18000)

# Chèn logo vào
worksheet.insert_image('B5', 'logo_UTE.png')

# Đóng tệp Excel
workbook.close()

print("Dữ liệu và logo đã được ghi vào tệp 'products.xlsx'.")
