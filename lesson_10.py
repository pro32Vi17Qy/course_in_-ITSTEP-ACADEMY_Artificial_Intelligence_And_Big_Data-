from colorama import Fore, Style
import requests

response = requests.get("https://coinmarketcap.com")
response_text = response.text
response_parse = response_text.split("<span>")
for i in response_parse:
    if i.startswith("$"):
        print(f"\n\t{Fore.LIGHTWHITE_EX}{Style.BRIGHT}{i}")
