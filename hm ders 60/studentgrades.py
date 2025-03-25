import studentgrades

def __init__(self):
    self.students = {}

def add_student(self, student_id):
    if student_id in self.students:
        raise ValueError("Bu öğrenci zaten kayıtlı!")
    self.students[student_id] = []

def add_grade(self, student_id, course, grade):
    if student_id not in self.students:
        raise ValueError("Öğrenci bulunamadı")
    if not (0 <= grade <= 100):
        raise ValueError("Not 0-100 arasında olmalıdır")
    self.students[student_id].append((course, grade))

def get_gpa(self, student_id):
    if student_id not in self.students:
        raise ValueError("Öğrenci bulunamadı")
    grades = self.students[student_id]
    if not grades:
        return 0
    total = sum(grade for _, grade in grades)
    return round(total / len(grades), 2)

def get_best_student(self):
    if not self.students:
        return None
    best_student = None
    best_gpa = -1
    for student_id in self.students:
        current_gpa = self.get_gpa(student_id)
        if current_gpa > best_gpa:
            best_gpa = current_gpa
            best_student = student_id
    return best_student 