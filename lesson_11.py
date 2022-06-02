from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style

response = requests.get("https://coinmarketcap.com")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
    res = soup_list[0].find("span")
    print(f"\n\t{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Price bitcoin - {res.text}")
