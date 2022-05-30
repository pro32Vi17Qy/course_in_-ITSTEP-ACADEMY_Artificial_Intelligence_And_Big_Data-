import logging
from colorama import Fore, Style
import random

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w+",
                    format="\n\tWe have next logging massage: %(asctime) s%(levelname)s - %(message)s")

try:
    print(
        f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}\n\tHello user of my program! A list of 10 "
        f"arithmetic values is generated here "
        f"progression. First "
        f"element of progressions 3, and the difference 8.\n\tAlso here the same list is generated "
        f"arithmetic progression, only "
        f"divide each element of this progression by a random number "
        f"from (-5 to 5).\n\tIf the first list of arithmetic progression is a list in which each"
        f" element of this progression is divided by a random number"
        f" from (-5 to 5) - no,\n\tdo not be surprised, this is probably because when generating divisors "
        f" one of them was assigned a value of 0, and as you know zero can not be divided,\n\tso the list in which each"
        f" element of this progression is divided by a random number "
        f"from (-5 to 5) was not generated. happened, I welcome you to a list\n\t"
        f"in which each element of this progression"
        f" is divided by a random number from (-5 to 5) a little lower!")
    d = range(0, 10)
    it_d = iter(d)

    a1 = [(1 + next(it_d) * 5) for i1 in range(10)]
    print(f"\t\n\t{Fore.LIGHTCYAN_EX}List of arithmetic progression - {Fore.LIGHTWHITE_EX}{a1}")
    for i in d:
        a1[i] /= random.randint(-5, 5)
    print(f"\t\n\t{Fore.LIGHTCYAN_EX}A list in which each element of this progression is divided "
          f"by a random number from (-5 to 5) - {Fore.LIGHTWHITE_EX}{a1}")
except ZeroDivisionError:
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
