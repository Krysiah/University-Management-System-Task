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

class Professor(Person):
    def __init__(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def set_professor_details(self,staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self, student, feedback):
        print("Feedback for", student,":",feedback)

    def increase_salary(self):
        twenty_pct = self.salary + ((self.salary/10)*2)
        return twenty_pct

    def get_professor_summary(self):
        print("Name:", self.name, "¦", "Age:", self.age,"¦", "Gender:", self.gender)
        print("Staff ID:", self.staff_id, "¦", "Department:", self.department,"¦", "Salary:", self.increase_salary())


#------------------------------------------------------------------------------------------

Kryssi = Person("Krysia", 16, "Male")
Kryssi.set_details("Krysiah", 17, "Female")
Kryssi.get_details()
   
Kryssi = Student(9482, "Computing")
Kryssi.set_student_details(9482, "Computing", 0)

Kryssi.add_grade(87)
Kryssi.add_grade(94)
Kryssi.add_grade(92)
Kryssi.add_grade(100)
Kryssi.add_grade(97)

Kryssi.get_student_summary()

Miss_T = Professor("Miss Travis",21,"Female")
Miss_T.set_details("Miss Travis",21,"Female")
Miss_T.set_professor_details(1045,"Computing",100000)
#Miss_T.give_feedback("Kryssi","Splendid coding work!")

Miss_T.get_professor_summary()



