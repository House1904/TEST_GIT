import student_manager

def main_menu():
    while True:
        print("[CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN]")
        print("[1]. Thêm sinh viên")
        print("[2]. Xóa sinh viên")
        print("[3]. Sửa sinh viên")
        print("[4]. Xem danh sách sinh viên")
        print("[5]. Thoát")
        
        choice = input("Chọn chức năng (1 - 5): ")
        
        if choice == '1':
            student_id = input("Nhập mã sinh viên: ")
            student_name = input("Nhập tên sinh viên: ")
            student_manager.add_student(student_id, student_name)
        
        elif choice == '2':
            student_id = input("Nhập mã sinh viên cần xóa: ")
            student_manager.delete_student(student_id)
        
        elif choice == '3':
            student_id = input("Nhập mã sinh viên cần sửa: ")
            new_name = input("Nhập tên mới của sinh viên: ")
            student_manager.edit_student(student_id, new_name)
        
        elif choice == '4':
            student_manager.view_students()
        
        elif choice == '5':
            print("Thoát chương trình...")
            break
        
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main_menu()
