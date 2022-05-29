# class Hello:
#     def __init__(self):
#         print("Hello")
#
#
# class HelloWord(Hello):
#     def __init__(self):
#         super().__init__()
#         print("Word")
#
#
# helW = HelloWord()

#
# class Class1:
#     var = 20
#
#     def __init__(self):
#         self.var = 10
#
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
#
# ob = Class2()


class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

    def calculate(self):
        print("Calculating...")


class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"

    def display(self):
        print("I display the image on the screen...")


class Phone:
    def call(self):
        print("calling...")


class SmartPhone(Display, Computer, Phone):
    def printInfo(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)


iphone = SmartPhone(model="New")
iphone.printInfo()
