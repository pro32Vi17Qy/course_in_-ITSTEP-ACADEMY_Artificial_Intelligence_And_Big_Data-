from colorama import Fore, Back

print(f"\n{Fore.BLUE} This text has blue color,{Fore.GREEN} but this text has green color!")
print(
    f"\n{Fore.LIGHTWHITE_EX} In order for your text to have color, you need to {Fore.LIGHTRED_EX}"
    f"import{Fore.LIGHTWHITE_EX} the {Fore.LIGHTRED_EX}\"colorama\" library{Fore.LIGHTWHITE_EX}"
    f" and enter in the command {Fore.MAGENTA}\"print{Fore.LIGHTWHITE_EX}{Fore.RESET}(){Fore.MAGENTA}\""
    f"{Fore.LIGHTWHITE_EX} command {Fore.LIGHTYELLOW_EX}[Fore.Color]{Fore.LIGHTWHITE_EX}"
    f" (only with the command {Fore.MAGENTA}\"print {Fore.RESET}(){Fore.MAGENTA}\"{Fore.LIGHTWHITE_EX}"
    f", which can use functions and only in curly braces{Fore.LIGHTWHITE_EX} ),\n "
    f"where {Fore.LIGHTYELLOW_EX}\"Color\"{Fore.LIGHTWHITE_EX} is the color you want to assign"
    f" for your text,which will be highlighted when you enter the {Fore.LIGHTYELLOW_EX}\"Fore\"{Fore.LIGHTWHITE_EX} "
    f"function, namely when you write {Fore.LIGHTYELLOW_EX}\"Fore\"{Fore.LIGHTWHITE_EX} and put a dot after "
    f"that will be displayed\n choice of colors!")
print(
    f"\n In addition to the {Fore.LIGHTYELLOW_EX}\"Fore\"{Fore.LIGHTWHITE_EX} function, "
    f"the {Fore.LIGHTRED_EX}\"colorama\" library{Fore.LIGHTWHITE_EX} has 3 other functions, the next of which is"
    f" {Fore.LIGHTYELLOW_EX}\"Back\"{Fore.LIGHTWHITE_EX}. It is a selection of the text on the outside."
    f" For example, note the following sentence in "
    f"quotation marks:\n {Back.BLACK}\"This sentence is outlined in black color.\"{Back.RESET} "
    f"To outline text you need to enter in the command"
    f" {Fore.MAGENTA}\"print{Fore.RESET}(){Fore.MAGENTA}\"{Fore.LIGHTWHITE_EX} command "
    f"{Fore.LIGHTYELLOW_EX}[Back.Color]{Fore.LIGHTWHITE_EX} (only with the command {Fore.MAGENTA}\""
    f"print{Fore.RESET}(){Fore.MAGENTA}\"{Fore.LIGHTWHITE_EX}, which can use functions "
    f"and only in curly braces ), \n where {Fore.LIGHTYELLOW_EX}\"Color\"{Fore.LIGHTWHITE_EX} "
    f"- color which you want to circle the text on the outside")
