class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def get_details(self):
        print("Name:", self.name, "¦", "Age:", self.age,"¦", "Gender:", self.gender)

class Student(Person):
    def __init__(self, student_id, course):
        self.student_id = student_id
        self.course = course
        self.grades = []

    def set_student_details(self, student_id, course, grades):
        self.student_id = student_id
        self.course = course
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calcuate_avg_grade(self):
        if self.grades != []:
            total = sum(self.grades)
            num_of_grades = len(self.grades)
            average = total / num_of_grades
            return average
        else:
            return 0
    
    def get_student_summary(self):
        print("Student ID:", self.student_id, "¦", "Course:", self.course,"¦", "Grades:", self.calcuate_avg_grade())
    
#Kryssi = Person("Krysia", 16, "Male")
#Kryssi.set_details("Krysiah", 17, "Female")
#Kryssi.get_details()
   
Kryssi = Student(9482, "Computing")
Kryssi.set_student_details(9482, "Computing", 0)

Kryssi.add_grade(87)
Kryssi.add_grade(94)
Kryssi.add_grade(92)
Kryssi.add_grade(100)
Kryssi.add_grade(97)

Kryssi.get_student_summary()





