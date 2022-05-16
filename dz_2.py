import random

class Student:
    studentCounter = 0
    def __init__(self, name, progress, db, money):
        self.name = name
        self.progress = progress
        self.dateOFbirthday = db
        self.money = money
        Student.studentCounter += 1
        print(f"\nStudent{self.studentCounter}({self.name}): HI! My name {self.name}!")
        print(f"\nSystem: Now {self.studentCounter} Student!")
    def __str__(self):
        return f"System: Name - {self.name} , progress - {self.progress}, date of birthday - {self.dateOFbirthday}!\n"
    def addprogress(self, upens_progress):
        self.progress += upens_progress
        if self.progress + upens_progress > 12:
            self.progress = 12
        elif self.progress + upens_progress < 1:
            self.progress = 1
        if self.progress < 4:
            random_add_progress = random.randint(1, 5)
            print(f"System: Now {self.name} began to learn better now his average progress {self.progress} marks!\n")
            self.progress +=random_add_progress
            print(f"System: Now {self.name} began to learn better now his average progress {self.progress} marks!\n")
        if upens_progress > 0:
            print(f"System: Now {self.name} began to learn better now his average progress {self.progress} marks!\n")
        elif upens_progress < 0:
            print(f"System: Now {self.name } began to learn worse now his average progress {self.progress} marks\n")
    def work(self, upens_money):
        self.money += upens_money
        if self.money < 50:
            random_add_money = random.randint(100, 500)
            self.money += random_add_money
            print(f"System:  Now {self.name} has worked and collect {random_add_money}$! Now the budget {self.name}'s is {self.money}$!\n")
        if upens_money > 0:
            print(f"System:  Now {self.name} has worked and collect {upens_money}$!  Now the budget {self.name}'s is {self.money}$!\n")
        elif upens_money < 0:
            print(f"System:  Now {self.name} spent on vacation {-upens_money}$! Now the budget {self.name}'s is {self.money}$!\n")

    def action(self, action):
        if action == 1:
            random_add_money = random.randint(-100, 500)
            Student.work(self, random_add_money)
        if action == 2:
            random_add_progress = random.randint(-5, 5)
            Student.addprogress(self, random_add_progress)

Student1 = Student("Illa",10, "26.12.2002", 100)
Student2 = Student("James", 8, "07.08.2022", 100)
Student3 = Student("Robert", 9, "06.09.2008", 100)

random_returns = random.randint(50, 100)
for i in range(random_returns):
    random_student = random.randint(1, 3)
    random_action = random.randint(1, 2)
    if random_student == 1:
        Student1.action(random_action)
    elif random_student == 2:
        Student2.action(random_action)
    elif random_student == 3:
        Student3.action(random_action)