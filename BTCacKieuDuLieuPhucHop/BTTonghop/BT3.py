# Khởi tạo dictionary để lưu trữ thời gian hoạt động
activities = {
    'Học': 0,
    'Ngủ': 0,
    'Thể dục': 0,
    'Chơi game': 0,
    'Làm BT': 0
}

while True:
    print("[Chọn một hành động]")
    print("[1]. Nhập thêm thời gian")
    print("[2]. Thống kê thời gian các hoạt động")
    print("[3]. Xem hoạt động nhiều nhất và ít nhất")
    print("[4]. Thoát")
    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if (choice == '1'):
        activity = input("Nhập loại hoạt động (Học, Ngủ, Thể dục, Chơi game, Làm BT): ")
        if activity in activities.key():
            try:
                minutes = int(input(f"Nếu bạn đã làm hoạt động {activity}, nhập số phút thêm vào: "))
                if (minutes > 0):
                    activities[activity] += minutes
                    print(f"Thời gian cho hoạt động '{activity}' đã được cập nhật.")
                else:
                    print("Số phút phải là số nguyên dương!")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")
        else:
            print("Hoạt động không hợp lệ. Vui lòng thử lại.")

    elif (choice == '2'):
        print("\nThống kê thời gian các hoạt động (tính theo giờ):")
        for activity, minutes in activities.items():
            hours = minutes / 60  # Chuyển đổi phút sang giờ
            print(f"{activity}: {hours:.2f} giờ")

    elif (choice == '3'):
        sorted_activities = sorted(activities.items(), key=lambda item: item[1], reverse=True)
        print("\n2 hoạt động nhiều nhất:")
        for activity, minutes in sorted_activities[:2]:
            print(f"{activity}: {minutes} phút")

        print("\n2 hoạt động ít nhất:")
        for activity, minutes in sorted_activities[-2:]:
            print(f"{activity}: {minutes} phút")

    elif (choice == '4'):
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
