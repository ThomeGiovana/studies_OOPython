class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 a 100

    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []

    # como adicionar estudantes dentro do curso?
    def addStudent(self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return True
        else:
            return False
    
    def getAverageGrade(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value/len(self.students)

s1 = Student("Laura", 18, 90)
s2 = Student("Joana", 18, 85)
s3 = Student("Mariana", 18, 72)

course = Course("Science", 2)

course.addStudent(s1)
course.addStudent(s2)
course.addStudent(s3)

for studentId in course.students:
    print(studentId.name)
print(course.getAverageGrade())