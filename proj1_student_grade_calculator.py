class Student:
    def __init__(self, name):
        self.name = name
        self.grade_dict = {}

    def add_grades(self, subject, grade):
        self.grade_dict[subject] = grade

    def average_grade(self):
        total = sum(self.grade_dict.values())
        count = len(self.grade_dict)
        average = (total / count)
        return average
    
class GradeTracker:
    def __init__(self):
        self.students = {}
        
    def add_students(self, name):
        new_student = Student(name)
        self.students[name] = new_student
        return new_student
    
    def add_grades(self, name, subject, grade):
        student = self.students[name]
        student.add_grades(subject, grade)

    def get_average_grade(self, name):
        student = self.students[name]
        average = student.average_grade()
        return average

    def display_student_info(self, name):
            student = self.students[name]
            print("Student Name:", student.name)
            print("Grades:")
            for subject, grade in student.grade_dict.items():
                print(subject, ":", grade)
            print("Average Grade:", student.average_grade())

tracker = GradeTracker()

# tracker.add_students('Ahana')
# tracker.add_grades('Ahana', 'Math', 100)
# tracker.add_grades('Ahana', 'Organic Chemistry', 90)
# tracker.display_student_info('Ahana')