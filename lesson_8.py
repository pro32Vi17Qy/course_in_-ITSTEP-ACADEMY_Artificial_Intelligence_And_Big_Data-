from colorama import Fore


# import random
# a = random.randint(0, 100)
# b = random.randint(100, 200)
# c = random.randint(200, 300)
# my_list = [a, b, c]
# print(my_list)
# i = iter(my_list)
# for _ in my_list:
#     print(next(i))

class Counter:
    def __init__(self, maxNum):
        self.i = 0
        self.maxNumber = maxNum

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.maxNumber:
            raise StopIteration
        return self.i


count = Counter(int(input("Enter max number! - ")))
for element in count:
    print(F"\n{Fore.RESET}{element}")
