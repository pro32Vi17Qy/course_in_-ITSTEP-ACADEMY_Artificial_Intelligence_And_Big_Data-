from colorama import Fore
import requests

response = requests.get("https://httpbin.org/get")
print(f"{Fore.LIGHTWHITE_EX}\n\t{response.content}")
