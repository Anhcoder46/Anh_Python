class Student:
    def __init__(self, MaSV, Ten, Diem):
        self.MaSV = MaSV
        self.Ten = Ten
        self.Diem = Diem

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f'Mã sinh viên: {student.MaSV}, Tên: {student.Ten}, Điểm: {student.Diem}')

    def find_student(self, MaSV):
        for student in self.students:
            if student.MaSV == MaSV:
                return student
        return None

    def sort_students(self):
        self.students.sort(key=lambda student: student.Diem)

    def remove_student(self, MaSV):
        self.students = [student for student in self.students if student.MaSV != MaSV]

if __name__ == "__main__":

    sv = StudentManagement()

    sv.add_student(Student("SV001", "Trần Đức Anh", 8.5))
    sv.add_student(Student("SV002", "Le Thi B", 7.0))
    sv.add_student(Student("SV003", "Tran Van C", 9.0))

    print("Danh sách sinh viên:")
    sv.display_students()

    print("\nTìm sinh viên SV002:")
    student = sv.find_student("SV002")
    if student:
        print(f'Đã tìm thấy: Mã sinh viên: {student.MaSV}, Tên: {student.Ten}, Điểm: {student.Diem}')
    else:
        print("Không tìm thấy sinh viên")

    print("\nDanh sách sinh viên sau khi sắp xếp theo điểm:")
    sv.sort_students()
    sv.display_students()


    sv.remove_student("SV002")
    print("\nDanh sách sinh viên sau khi xóa SV002:")
    sv.display_students()
