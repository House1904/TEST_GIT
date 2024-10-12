it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Yêu cầu 1
print("Chiều dài của tập hợp it_companies là:", len(it_companies))

# Yêu cầu 2
it_companies.add("Twitter")

# Yêu cầu 3
it_companies.update(A)

# Yêu cầu 4
ele_removed = it_companies.pop()
print("Phần tử đã bị xóa:", ele_removed)

# Yêu cầu 5
'''
Sự khác nhau của .remove(<value>) và .discard(<value>) là 
nếu giá trị không tồn tại trong set, phương thức .remove sẽ báo lỗi KeyError 
còn .discard thì không
'''

# Yêu cầu 6
result0 = A.union(B)
print("Tập hợp A hợp với B:", result0)

# Yêu cầu 7
result1 = A.intersection(B)  # Hoặc A & B
print("Phần tử chung giữa A và B:", result1)

# Yêu cầu 8
is_subset = A <= B  # Hoặc A.issubset(B)
print("A có phải là tập hợp con của B không?", is_subset)

# Yêu cầu 9
are_disjoint = len(result1) == 0
print("A và B có phải 2 tập hợp rời rạc không?", are_disjoint)

# Yêu cầu 10
result0_A_B = A.union(B)
result0_B_A = B.union(A)
print("A hợp với B:", result0_A_B)
print("B hợp với A:", result0_B_A)

# Yêu cầu 11
symmetric_difference = A ^ B
print("Các phần tử khác biệt đối xứng của A và B:", symmetric_difference)

# Yêu cầu 12
del A, B

# Yêu cầu 13
print("Độ dài ban đầu của age:", len(age))
age_new = set(age)
print("Độ dài sau khi chuyển thành set của danh sách age:", len(age_new))

if len(age) > len(age_new):
    print("Độ dài sau khi chuyển đổi thành set bị thu hẹp do xóa bớt các phần tử trùng lặp.")
