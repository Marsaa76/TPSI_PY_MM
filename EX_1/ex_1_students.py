class Student:
    student_count = 0

    def __init__(self, name, age, n_matricola):
        self.name = name
        self.age = age
        self.n_matricola = n_matricola
        Student.student_count += 1  # add the total of the students

    def __str__(self) -> str:
        return f"{self.name}, {self.age} anni, {self.n_matricola}"

    @staticmethod
    def count():
        return Student.student_count  # give back the total number of created students 
    
s1 = Student("Marco", 20, "123456")
s2 = Student("Laura", 22, "654321")

print(s1)  
print(s2)  

print(f"the total of the students is "+{Student.count()})  