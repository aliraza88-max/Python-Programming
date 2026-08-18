# OOPS in Python

# class:Template

class Student:
    def __init__(self,name,grade,team,percentage): # method
        self.name=name # attributes
        self.grade=grade # attributes
        self.team=team # attributes
        self.percentage=percentage # attributes

    def student(self):
        print(f"{self.name} is a good student and he got {self.percentage}%")

team1="A"
team2="B"

# Object : instance of class
student_1=Student("Ali",12,team1)
print(f"{student_1.name} is in grade {student_1.grade}")

student_2=Student("Ahmed",9,team2)
print(f"{student_2.name} is in grade {student_2.grade}")

student_1.student()

print(student_1.name)

del student_1.name
print(student_1.name)

print(student_1.team)

# 4 Features in OOPS
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

### ABSTRACTION

class Student:
    def __init__(self,name,grade,team,percentage): # method
        self.name=name # attributes
        self.grade=grade # attributes
        self.team=team # attributes
        self.percentage=percentage # attributes

    def student(self):
        print(f"{self.name} is a good student and he got {self.percentage + 2}%")

team1="A"
team2="B"

student_3=Student("Ali",10,team1,89)
print(student_3.percentage)
student_3.student()

### ENCAPSULATION

class Student:
    def __init__(self,name,grade,team,percentage): # method
        self.name=name # attributes
        self.grade=grade # attributes
        self.team=team # attributes
        self.__percentage=percentage # attributes

    def percentage(self):
        return self.__percentage

    def student(self):
        print(f"{self.name} is a good student and he got {self.percentage}%")

team1="A"
team2="B"

student_3=Student("Ali",10,team1,89)
print(student_3.percentage())

### INHERITANCE

# allows one class(child) to reuse the properties and methods of another child(parent).

class Student:
    def __init__(self,name,grade,team,percentage): # method
        self.name=name # attributes
        self.grade=grade # attributes
        self.team=team # attributes
        self.__percentage=percentage # attributes

    def percentage(self):
        return self.__percentage

    def student(self):
        print(f"{self.name} is a good student and he got {self.percentage}%")

team1="A"
team2="B"



class GraduateStudent(Student):
    def __init__(self, name, grade, team, percentage,stream):
        super().__init__(name, grade, team, percentage) 
        self.stream=stream

Grad_Student01=GraduateStudent("Ali",9,team1,89,"DS")
print(Grad_Student01.stream)


### POLYMORPHISM

class Student:
    def __init__(self,name,grade,team,percentage): # method
        self.name=name # attributes
        self.grade=grade # attributes
        self.team=team # attributes
        self.__percentage=percentage # attributes

    def percentage(self):
        return self.__percentage

    def student(self):
        print(f"{self.name} is a good student and he got {self.percentage}%")

team1="A"
team2="B"



class GraduateStudent(Student):
    def __init__(self, name, grade, team, percentage,stream):
        super().__init__(name, grade, team, percentage) 
        self.stream=stream

    def student(self):
        print(f"{self.name} is in {self.stream} stream")


student_4=GraduateStudent("Ali",12,team1,89,"DS")
print(student_4.student())