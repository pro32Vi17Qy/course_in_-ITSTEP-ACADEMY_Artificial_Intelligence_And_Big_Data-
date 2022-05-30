from colorama import Fore
import urllib.request

opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(f"\n\t{Fore.LIGHTWHITE_EX}{response.read()}")
