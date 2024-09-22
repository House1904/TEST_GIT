import xlsxwriter

# Dữ liệu mẫu
data = [
    ['Name', 'Age', 'Department'],
    ['Alice', 30, 'HR'],
    ['Bob', 25, 'IT'],
    ['Charlie', 35, 'Finance']
]

# Tạo tệp Excel mới
workbook = xlsxwriter.Workbook('employees.xlsx')
worksheet = workbook.add_worksheet()

# Ghi dữ liệu vào tệp Excel
for row_num, row_data in enumerate(data):
    worksheet.write_row(row_num, 0, row_data)

# Đóng tệp Excel
workbook.close()

print("Dữ liệu đã được ghi vào tệp 'employees.xlsx'.")

