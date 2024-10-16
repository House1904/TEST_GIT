import json

class Subject:
    def __init__(self, subject_id, subject_name, credits):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.credits = credits

    def __str__(self):
        return f"Subject ID: {self.subject_id}, Subject Name: {self.subject_name}, Credits: {self.credits}"

class Student:
    def __init__(self, id_number, name, birth_year, subjects):
        self.id_number = id_number
        self.name = name
        self.birth_year = birth_year
        self.subjects = subjects  # Danh sách các môn học (list các đối tượng Subject)

    def __str__(self):
        subjects_info = "\n".join([str(subject) for subject in self.subjects])
        return f"ID: {self.id_number}, Name: {self.name}, Birth Year: {self.birth_year}\nSubjects:\n{subjects_info}"

class StudentManagement:
    def __init__(self, filename="dssv.txt"):
        self.students = []
        self.filename = filename

    def add_students(self):
        while True:
            print("\nEnter student information (or type 'done' to finish):")
            id_number = input("Enter ID Number (CMND, CCCD, Birth Certificate): ")
            if id_number.lower() == 'done':
                break

            # Kiểm tra ID sinh viên đã tồn tại
            if any(student.id_number == id_number for student in self.students):
                print(f"Student with ID {id_number} already exists. Please enter a different ID.")
                continue

            name = input("Enter Student Name: ")
            birth_year = input("Enter Birth Year: ")

            subjects = []
            while True:
                subject_id = input("Enter Subject ID (or 'done' to finish): ")
                if subject_id.lower() == 'done':
                    break
                subject_name = input("Enter Subject Name: ")
                credits = int(input("Enter Credits: "))
                subject = Subject(subject_id, subject_name, credits)
                subjects.append(subject)

            student = Student(id_number, name, birth_year, subjects)
            self.students.append(student)

            print(f"Student {name} added successfully!")

        # Save all student information to file after batch input
        self.save_to_file()
        print("All students have been added and saved to file.")

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            student_data = []
            for student in self.students:
                student_dict = {
                    "id_number": student.id_number,
                    "name": student.name,
                    "birth_year": student.birth_year,
                    "subjects": [{"subject_id": subj.subject_id, "subject_name": subj.subject_name, "credits": subj.credits} for subj in student.subjects]
                }
                student_data.append(student_dict)
            json.dump(student_data, file)

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                student_data = json.load(file)
                for data in student_data:
                    subjects = [Subject(sub['subject_id'], sub['subject_name'], sub['credits']) for sub in data['subjects']]
                    student = Student(data['id_number'], data['name'], data['birth_year'], subjects)
                    self.students.append(student)
        except FileNotFoundError:
            print("File not found, starting with an empty list.")

    def display_all_students(self):
        if not self.students:
            print("No students found.")

        print("\nSTUDENTS LIST:")
        for student in self.students:
            print(student)
            print("----------------------------------------------------------")

    def display_students_with_multiple_subjects(self):
        print("\nStudents enrolled in at least 2 subjects:")
        found = False
        for student in self.students:
            if len(student.subjects) >= 2:
                print(student)
                found = True
        if not found:
            print("No students enrolled in multiple subjects.")

    def display_most_popular_subject(self):
        subject_count = self.count_students_per_subject()

        if subject_count:
            max_count = max(subject_count.values())
            # Lấy danh sách tất cả các môn học có số lượng học viên bằng max_count
            most_popular_subjects = [subject for subject, count in subject_count.items() if count == max_count]

            print(f"The most popular subjects are: {', '.join(most_popular_subjects)} with {max_count} students.")
        else:
            print("No subjects found.")

    def count_students_per_subject(self):
        subject_count = {}
        for student in self.students:
            for subject in student.subjects:
                subject_name = subject.subject_name
            
                if subject_name in subject_count:
                    subject_count[subject_name] += 1
                else:
                    subject_count[subject_name] = 1

        return subject_count  # Trả về dictionary chứa số lượng sinh viên theo môn học

def main():
    management = StudentManagement()
    management.load_from_file()

    while True:
        print("\n[Control Panel]:")
        print("[1]. Add Students")
        print("[2]. Display All Students")
        print("[3]. Display Students with at Least 2 Subjects")
        print("[4]. Display Most Popular Subject")
        print("[5]. Count Students Per Subject")
        print("[6]. Exit")

        choice = input("Choose an option (1-6): ")
        if choice == '1':
            management.add_students()
        elif choice == '2':
            management.display_all_students()
        elif choice == '3':
            management.display_students_with_multiple_subjects()
        elif choice == '4':
            management.display_most_popular_subject()
        elif choice == '5':
            subject_count = management.count_students_per_subject()
            if subject_count:
                print("Number of students per subject:")
                for subject, count in subject_count.items():
                    print(f"{subject}: {count} students")
            else:
                print("No subjects found.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
