class Student:
    studentCounter = 0
    def __init__(self, name, progress, db, school = "NVK 10"):
        self.name = name
        self.progress = progress
        self.dateoFBirthday = db
        self.school = school
        Student.studentCounter += 1
        print(f"Student{self.studentCounter}: HI! My name {self.name}!")
        print(f"System:  Now {self.studentCounter} Student!")
    def __str__(self):
        return f"System: Name - {self.name} \n, progress - {self.progress}, date of birthday - {self.dateoFBirthday}!"
    #def method(self):
        #print("Object")
    def addprogress(self, upens_progress):
        self.progress += upens_progress
        print(f"System:  Now medium progress {self.name} {self.progress} marks!")
Student1 = Student("Illa",10, "26.12.2002")
#print(Student1.progress)
#print(Student1.dateoFBirthday)
Student2 = Student("James", 8, "07.08.2022")
Student3 = Student("Robert", 9, "06.09.2008")

Student1.addprogress(6)


class Human:
    def __init__(self, name = "Human"):
        self.name = name
class Auto():
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []
    def add_passenger(self, human):
        self.passenger.append(human)
    def passengers_names(self):
        if self.passenger != []
            print(f"Names of {self.brand} passengers:")
            for pasengers in self.passenger:
                print(pasengers.name)
        else:
            print(f"There are not passers in {self.brand} now!")
p1 = Human("p1")
p2 = Human("p2")
p3 = Human("p3")
car  = Auto("Mercedes")





















