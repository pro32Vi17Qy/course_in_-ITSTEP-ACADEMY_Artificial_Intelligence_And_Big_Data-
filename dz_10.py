from colorama import Fore, Style
import re

# part_1

print(f"\n\t\t{Style.BRIGHT}{Fore.CYAN}part 1 of my program:")
string_1 = "123"
search_str = re.compile("2")
find_str_1 = search_str.search(string_1)
if len(search_str.findall(string_1)) == 1:
    print(f"\n\t{Fore.LIGHTWHITE_EX}Yes!")
else:
    print(f"\n\t{Fore.LIGHTWHITE_EX}No!")

# part_2

print(f"\n\t\t{Fore.CYAN}part 2 of my program:")
print(f"\n\t{Fore.LIGHTWHITE_EX}Hello dear user of my program! Now you see the second part of my program,"
      " namely the function that allows you to find certain text in a certain string!")
string2 = input("\n\tEnter your string! - ")
find_text_input = input("\n\tEnter the text you want to find in the string! - ")
find_text = re.compile(find_text_input)
find_str2 = find_text.search(string2)
if find_str2 is not None:
    print(f"\n\tYour string \"{string2}\" really has a text"
          f" \"{find_text_input}\" and in your string he comes across {len(find_text.findall(string2))} times!")
else:
    print(f"Sorry, but your string \"{string2}does not have"
          f" the text \"{find_text_input}\"you want to find")
