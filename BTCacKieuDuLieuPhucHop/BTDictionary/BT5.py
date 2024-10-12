# Tạo dictionary để lưu thông tin học sinh
mydict = {}

while True:
    try:
        name = input("Nhập tên học sinh (hoặc để trống để dừng): ")
        if name == "":
            break
        
        # Nhập điểm và kiểm tra
        score = float(input(f"Nhập điểm của {name} (0-10): "))
        if score < 0 or score > 10:
            print("Điểm phải nằm trong khoảng [0, 10]. Vui lòng nhập lại.")
            continue
        
        mydict[name] = score  # Lưu tên và điểm vào dictionary
    except ValueError:
        print("Vui lòng nhập điểm hợp lệ.")

# Thống kê số lượng học sinh đạt được các mốc điểm
score_counts = {10: 0, 8: 0, 6: 0, 4: 0, 2: 0, 0: 0}

for score in mydict.values():
    if score == 10:
        score_counts[10] += 1
    elif score >= 8:
        score_counts[8] += 1
    elif score >= 6:
        score_counts[6] += 1
    elif score >= 4:
        score_counts[4] += 1
    elif score >= 2:
        score_counts[2] += 1
    else:
        score_counts[0] += 1

# In ra kết quả thống kê
print("Thống kê số lượng học sinh đạt được các mốc điểm:")
for key in score_counts:
    print(f"Điểm {key}: {score_counts[key]} học sinh")
