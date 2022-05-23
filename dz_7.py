from colorama import Fore, Back, Style
import random

a = random.randint(2, 8)
c = random.randint(1, a)
if a == c:
    a += 1
b = random.randint(c, a)
if b == c:
    b += 1
elif b == a:
    a += 1
data = {1: c, 2: b, 3: a}
result = []


def division(af, bf):
    if af == 1 and bf == 3:
        raise ValueError
    elif af == 2 and bf == 3:
        raise ValueError
    # part 2\ :(
    elif af == 3 and bf == 4:
        raise ValueError
    # part 3\ :(
    elif af == 1 and bf == 6:
        raise ValueError
    elif af == 2 and bf == 6:
        raise ValueError
    elif af == 4 and bf == 6:
        raise ValueError
    elif af == 5 and bf == 6:
        raise ValueError
    # part 4\ :(
    elif af == 1 and bf == 7:
        raise ValueError
    elif af == 2 and bf == 7:
        raise ValueError
    elif af == 3 and bf == 7:
        raise ValueError
    elif af == 4 and bf == 7:
        raise ValueError
    elif af == 5 and bf == 7:
        raise ValueError
    elif af == 6 and bf == 7:
        raise ValueError
    elif af == 1 and bf == 7:
        raise ValueError
    # part 5\ :(
    elif af == 1 and bf == 9:
        raise ValueError
    elif af == 2 and bf == 9:
        raise ValueError
    elif af == 3 and bf == 9:
        raise ValueError
    elif af == 4 and bf == 9:
        raise ValueError
    elif af == 5 and bf == 9:
        raise ValueError
    elif af == 6 and bf == 9:
        raise ValueError
    elif af == 7 and bf == 9:
        raise ValueError
    elif af == 8 and bf == 9:
        raise ValueError
    return af / bf


print(
    f"\n{Fore.LIGHTYELLOW_EX}\tInfo:\n\t\t{Fore.BLUE}Hi, dear user of my program, "
    f"a random list of numbers is generated here,"
    f" which will then be divided by the numbering of repetitions of their creation,\n\t\tin a word"
    f" should be the result of the calculation three numbers not greater than one and only correct numbers, two numbers"
    f" or one may be displayed, or\n\t\tnumbers may not be displayed but they must not be greater than one."
    f" If you see problems or the number in the results list is more than one, contact\n\t\twith me and email me,"
    f" my email is {Fore.LIGHTWHITE_EX}{Back.BLACK}kriskovroman16072008@gmail.com{Back.RESET}{Fore.BLUE}!\n")
for i in data:
    try:
        res = division(i, data[i])
        result.append(res)
    except ValueError:
        pass
print(f"\t\t{Fore.LIGHTWHITE_EX}List - {Fore.CYAN}{data}")
print(f"\t{Fore.LIGHTWHITE_EX}result is - {Fore.LIGHTGREEN_EX}{result}\n")
print(f"\t {Fore.LIGHTYELLOW_EX}More info above {Style.BRIGHT}↑ !")
