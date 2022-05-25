from colorama import Fore, Style

d = range(0, 10)
dd = iter(d)
a1 = [(1+next(dd)*5) for i1 in range(10)]
print(f"\t{Fore.BLUE}part_1:\n\t{a1}")

print(f"\n\t{Fore.LIGHTYELLOW_EX}part_2:")
print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}\n\tHi User! This is an arithmetic progression calculator, keep:")
number_members_in_progression = int(input("\n\tThe number of members in progression is - "))
start_num = int(input("\n\tStart number is - "))
progression_difference = int(input("\n\tProgression difference is - "))

d = range(0, number_members_in_progression)
dd = iter(d)
a = [(start_num+next(dd)*progression_difference) for i in range(number_members_in_progression)]
sum_all_members_progression = ((min(a)+max(a))*number_members_in_progression) / 2


print(f"\n\tResult arithmetic progression is - {a}, the last member of the arithmetic progression is - {max(a)},\n\t"
      f"the sum of all members of the progression is {sum_all_members_progression}")
