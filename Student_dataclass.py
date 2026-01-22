from dataclasses import dataclass
@dataclass
class Student:
    name:str
    school_id:str
    gpa: float

    def __str__(self):
        return f'Name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'


Amir = Student('Amir','112233',2.9)
print(Amir)
bob = Student('bob','223344',3.5)
print(bob)
kevin = Student('kevin','334455',3.1)
print(kevin)
# in a dataclass it automatically creates the special methods like __init__ and __str__ for you which is a shortcut
# but in the "traditional" way  you manually have to add the special methods which can take some time

