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
        pct = self.salary + (self.salary/10)
        return pct

    def get_professor_summary(self):
        print("Name:", self.name, "¦", "Age:", self.age,"¦", "Gender:", self.gender)
        print("Staff ID:", self.staff_id, "¦", "Department:", self.department,"¦", "Salary:", self.increase_salary())

class Administrator(Person):
    def __init__(self, admin_id, office, yrs_of_service):
        self.admin_id = admin_id
        self.office = office
        self.yrs_of_service = yrs_of_service

    def set_admin_details(self, admin_id, office, yrs_of_service):
        self.admin_id = admin_id
        self.office = office
        self.yrs_of_service = 2
    
    def increment_service_yrs(self):
        self.yrs_of_service = self.yrs_of_service + 1
        return self.yrs_of_service
    
    def get_admin_summary(self):
        print("Name:", self.name, "¦", "Age:", self.age,"¦", "Gender:", self.gender)
        print("Admin ID:", self.admin_id, "¦", "Office:", self.office,"¦", "Years of work:", self.increment_service_yrs())
       

#------------------------------------------------------------------------------------------

#Students
Kryssi = Person("Kryssia", 16, "Male")
Kryssi.set_details("Krysiah", 17, "Female") 
Kryssi = Student(9482, "Computing")
Kryssi.set_student_details(9482, "Computing", 0)

Kryssi.add_grade(87)
Kryssi.add_grade(94)
Kryssi.add_grade(92)
Kryssi.add_grade(100)
Kryssi.add_grade(97)

Kryssi.get_student_summary()
print("----------------------------------")

Kris = Person("Chris", 16, "Female")
Kris.set_details("Kris",17,"Male")
Kris = Student(9483, "Computing")
Kris.set_student_details(9483, "Computing", 0)

Kris.add_grade(12)
Kris.add_grade(4)
Kris.add_grade(34)
Kris.add_grade(42)
Kris.add_grade(27)

Kris.get_student_summary()
print("----------------------------------")

Miss_T = Professor("Mis Traviss",31,"Female")
Miss_T.set_details("Miss Travis",21,"Female")
Miss_T.set_professor_details(1045,"Computing",100000)

Miss_T.give_feedback("Krysiah","Splendid coding work!")
Miss_T.give_feedback("Kris","Please work harder in class.")

print("----------------------------------")

Miss_T.get_professor_summary()
print("[Your salary has increased by 10%]")

print("----------------------------------")

Miss_A = Administrator("Miss Angle",20,"Female")
Miss_A.set_details("Miss Angel",30,"Female")
Miss_A.set_admin_details("A120","Room 10, 3rd floor",0)

Miss_A.get_admin_summary()
print("[Years of experience has updated from 2 --> 3]")




