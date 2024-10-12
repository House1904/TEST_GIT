# Danh sách sinh viên khởi tạo rỗng
students = []

def add_student(student_id, student_name):
    students.append({"id": student_id, "name": student_name})
    print(f"Đã thêm sinh viên: {student_name}")

def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print(f"Đã xóa sinh viên có mã: {student_id}")
            return
    print(f"Không tìm thấy sinh viên có mã: {student_id}")

def edit_student(student_id, new_name):
    for student in students:
        if student["id"] == student_id:
            student["name"] = new_name
            print(f"Đã sửa sinh viên có mã: {student_id}")
            return
    print(f"Không tìm thấy sinh viên có mã: {student_id}")

def view_students():
    if not students:
        print("Danh sách sinh viên rỗng.")
    else:
        print("Danh sách sinh viên:")
        for student in students:
            print(f"Mã sinh viên: {student['id']}, Tên sinh viên: {student['name']}")

