lst = []
tup = ()

tup = tuple(input("Nhập chuỗi số tuỳ ý (cách nhau bằng dấu phẩy): ").strip().split(","))

lst = list(tup)

print(tup)
print(lst)