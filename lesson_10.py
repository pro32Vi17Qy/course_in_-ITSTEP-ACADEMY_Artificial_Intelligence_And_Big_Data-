from colorama import Fore, Back
import requests

# response = requests.get("https://httpbin.org/get")
# print(f"{Fore.LIGHTWHITE_EX}\n\t{response.text}")

response = requests.post("https://httpbin.org/post", data="TEST DATA", headers = {"h1" : "Test title" })
print(response.text)
