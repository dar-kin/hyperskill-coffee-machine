class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year


n = input()
l_n = input()
b_d = input()
student = Student(n, l_n, b_d)
print(student.id)
