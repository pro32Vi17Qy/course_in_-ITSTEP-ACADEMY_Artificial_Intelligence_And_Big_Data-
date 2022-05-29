class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


class Hi(Hello_world):

    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self._Hi__hello)
        print(self.__world)
        hello = Hello_world()
        hello.printer()


hi = Hi()
hi.hi_print()

# class Human:
#     weight = 70
#     old = 80
#     endurance = 100
#     def __init__(self):
#         print("Human")
#         print(f"weight {self.weight}")
#         print(f"old {self.old}")
#         print(f"endurance {self.endurance}")
# class elves(Human):
#     weight = 20
#     old = 500
#     manna = 45
#     def __init__(self):
#         print("Human")
#         print(f"weight {self.weight}")
#         print(f"old {self.old}")
#         print(f"endurance {self.endurance}")
#         print(f"manna {self.manna}")
# class hobbyt(Human):
#     endurance = 50
#     def __init__(self):
#         print("Human")
#         print(f"weight {self.weight}")
#         print(f"old {self.old}")
#         print(f"endurance {self.endurance}")
#
# a = Human()
# b = elves
# c = hobbyt


# class Human:
#     height = 170
# class Stusent(Human):
#     pass
# class worker(Human):
#     pass
# Nick = Stusent
# Ann = worker
#
# print(Nick.height)
# print(Ann.height)
