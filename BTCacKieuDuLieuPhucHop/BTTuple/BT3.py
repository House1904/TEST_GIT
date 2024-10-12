# Nhập danh sách và tuple
inputList = list(map(int, input("Nhập danh sách các số cho list (cách nhau bởi dấu phẩy): ").split(",")))
inputTuple = tuple(map(int, input("Nhập danh sách các số cho tuple (cách nhau bởi dấu phẩy): ").split(",")))

# Gộp các phần tử của tuple vào list
outputList = inputList + list(inputTuple)

# Chuyển list mới thành tuple
outputTuple = tuple(outputList)

# In kết quả
print("outputList =", outputList)
print("outputTuple =", outputTuple)
