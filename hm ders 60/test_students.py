import unittest
from studentgrades import studentgrades

class TestStudentGrades(unittest.TestCase):
    def setUp(self):
        self.grades = studentgrades()
        self.grades.add_student("S001")
        self.grades.add_student("S002")

    def test_add_grade(self):
        self.grades.add_grade("S001", "Math", 85)
        self.grades.add_grade("S001", "Physics", 90)
        self.assertEqual(len(self.grades.students["S001"]), 2)
        with self.assertRaises(ValueError):
            self.grades.add_grade("S001", "Chemistry", 150)

    def test_gpa_calculation(self):
        self.grades.add_grade("S001", "Math", 80)
        self.grades.add_grade("S001", "Physics", 90)
        self.assertEqual(self.grades.get_gpa("S002"), 0)

    def test_best_student(self):
        self.grades.add_grade("S001", "Math", 70)
        self.grades.add_grade("S002", "Math", 90)
        self.assertEqual(self.grades.get_best_student(), "S002")
        empty_system = studentgrades()
        self.assertIsNone(empty_system.get_best_student())

if __name__ == "__main__":
    unittest.main()