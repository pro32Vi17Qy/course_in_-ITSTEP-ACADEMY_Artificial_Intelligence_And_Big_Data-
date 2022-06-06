from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style
import re

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"data-label": "Офіційний курс"})

list_currency = []
for i in soup_list:
    list_currency.append(i.text)

find_SYMBOL = re.compile(",")

el1_l_s = list_currency[0]
el2_l_s = list_currency[1]
el3_l_s = list_currency[2]
el4_l_s = list_currency[3]
el5_l_s = list_currency[4]
el6_l_s = list_currency[5]
el7_l_s = list_currency[6]
el8_l_s = list_currency[7]
el9_l_s = list_currency[8]
el10_l_s = list_currency[9]
el11_l_s = list_currency[10]
el12_l_s = list_currency[11]
el13_l_s = list_currency[12]
el14_l_s = list_currency[13]
el15_l_s = list_currency[14]
el16_l_s = list_currency[15]
el17_l_s = list_currency[16]
el18_l_s = list_currency[17]
el19_l_s = list_currency[18]
el20_l_s = list_currency[19]
el21_l_s = list_currency[20]
el22_l_s = list_currency[21]
el23_l_s = list_currency[22]
el24_l_s = list_currency[23]
el25_l_s = list_currency[24]
el26_l_s = list_currency[25]
el27_l_s = list_currency[26]
el28_l_s = list_currency[27]
el29_l_s = list_currency[28]
el30_l_s = list_currency[29]
el31_l_s = list_currency[30]
el32_l_s = list_currency[31]
el33_l_s = list_currency[32]
el34_l_s = list_currency[33]

sub_elem_1 = find_SYMBOL.sub(".", el1_l_s)
sub_elem_2 = find_SYMBOL.sub(".", el2_l_s)
sub_elem_3 = find_SYMBOL.sub(".", el3_l_s)
sub_elem_4 = find_SYMBOL.sub(".", el4_l_s)
sub_elem_5 = find_SYMBOL.sub(".", el5_l_s)
sub_elem_6 = find_SYMBOL.sub(".", el6_l_s)
sub_elem_7 = find_SYMBOL.sub(".", el7_l_s)
sub_elem_8 = find_SYMBOL.sub(".", el8_l_s)
sub_elem_9 = find_SYMBOL.sub(".", el9_l_s)
sub_elem_10 = find_SYMBOL.sub(".", el10_l_s)
sub_elem_11 = find_SYMBOL.sub(".", el11_l_s)
sub_elem_12 = find_SYMBOL.sub(".", el12_l_s)
sub_elem_13 = find_SYMBOL.sub(".", el13_l_s)
sub_elem_14 = find_SYMBOL.sub(".", el14_l_s)
sub_elem_15 = find_SYMBOL.sub(".", el15_l_s)
sub_elem_16 = find_SYMBOL.sub(".", el16_l_s)
sub_elem_17 = find_SYMBOL.sub(".", el17_l_s)
sub_elem_18 = find_SYMBOL.sub(".", el18_l_s)
sub_elem_19 = find_SYMBOL.sub(".", el19_l_s)
sub_elem_20 = find_SYMBOL.sub(".", el20_l_s)
sub_elem_21 = find_SYMBOL.sub(".", el21_l_s)
sub_elem_22 = find_SYMBOL.sub(".", el22_l_s)
sub_elem_23 = find_SYMBOL.sub(".", el23_l_s)
sub_elem_24 = find_SYMBOL.sub(".", el24_l_s)
sub_elem_25 = find_SYMBOL.sub(".", el25_l_s)
sub_elem_26 = find_SYMBOL.sub(".", el26_l_s)
sub_elem_27 = find_SYMBOL.sub(".", el27_l_s)
sub_elem_28 = find_SYMBOL.sub(".", el28_l_s)
sub_elem_29 = find_SYMBOL.sub(".", el29_l_s)
sub_elem_30 = find_SYMBOL.sub(".", el30_l_s)
sub_elem_31 = find_SYMBOL.sub(".", el31_l_s)
sub_elem_32 = find_SYMBOL.sub(".", el32_l_s)
sub_elem_33 = find_SYMBOL.sub(".", el33_l_s)
sub_elem_34 = find_SYMBOL.sub(".", el34_l_s)

list_currency_2 = []
list_currency_2.append(sub_elem_1)
list_currency_2.append(sub_elem_2)
list_currency_2.append(sub_elem_3)
list_currency_2.append(sub_elem_4)
list_currency_2.append(sub_elem_5)
list_currency_2.append(sub_elem_6)
list_currency_2.append(sub_elem_7)
list_currency_2.append(sub_elem_8)
list_currency_2.append(sub_elem_9)
list_currency_2.append(sub_elem_10)
list_currency_2.append(sub_elem_11)
list_currency_2.append(sub_elem_12)
list_currency_2.append(sub_elem_13)
list_currency_2.append(sub_elem_14)
list_currency_2.append(sub_elem_15)
list_currency_2.append(sub_elem_16)
list_currency_2.append(sub_elem_17)
list_currency_2.append(sub_elem_18)
list_currency_2.append(sub_elem_19)
list_currency_2.append(sub_elem_20)
list_currency_2.append(sub_elem_21)
list_currency_2.append(sub_elem_22)
list_currency_2.append(sub_elem_23)
list_currency_2.append(sub_elem_24)
list_currency_2.append(sub_elem_25)
list_currency_2.append(sub_elem_26)
list_currency_2.append(sub_elem_27)
list_currency_2.append(sub_elem_28)
list_currency_2.append(sub_elem_29)
list_currency_2.append(sub_elem_30)
list_currency_2.append(sub_elem_31)
list_currency_2.append(sub_elem_32)
list_currency_2.append(sub_elem_33)
list_currency_2.append(sub_elem_34)

print(f"\n\t{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Hello dear user of my program"
      f"! This is a program in which you can enter the currency of your country,"
      f" keep the number\n\tof currency units and get the number of currency units in UAH!")
Currency = ""
while True:
    Currency += input(f"\n\tCurrency:\t")
    if Currency == "AUD":
        break
    if Currency == "AZN":
        break
    if Currency == "BYN":
        break
    if Currency == "BGN":
        break
    if Currency == "KRW":
        break
    if Currency == "HRD":
        break
    if Currency == "DKK":
        break
    if Currency == "USD":
        break
    if Currency == "EUR":
        break
    if Currency == "EGP":
        break
    if Currency == "JPY":
        break
    if Currency == "PLN":
        break
    if Currency == "INR":
        break
    if Currency == "CAD":
        break
    if Currency == "HRK":
        break
    if Currency == "MXN":
        break
    if Currency == "MDL":
        break
    if Currency == "ILS":
        break
    if Currency == "NZD":
        break
    if Currency == "NOK":
        break
    if Currency == "ZAR":
        break
    if Currency == "RUB":
        break
    if Currency == "RON":
        break
    if Currency == "IDR":
        break
    if Currency == "SGD":
        break
    if Currency == "XDR":
        break
    if Currency == "KZT":
        break
    if Currency == "TRY":
        break
    if Currency == "HUF":
        break
    if Currency == "GBP":
        break
    if Currency == "CZK":
        break
    if Currency == "SEK":
        break
    if Currency == "CHF":
        break
    if Currency == "CNY":
        break
    else:
        Currency = ""
        print("\n\tWrong choice of currency! Enter the currency again!")


Number_of_currency_units = 0
Number_of_currency_units += int(input("\n\tNumber of currency units:\t"))

UAH = 0
if Currency == "AUD":
    UAH += Number_of_currency_units * float(list_currency_2[0])
if Currency == "AZN":
    UAH += Number_of_currency_units * float(list_currency_2[1])
if Currency == "BYN":
    UAH += Number_of_currency_units * float(list_currency_2[2])
if Currency == "BGN":
    UAH += Number_of_currency_units * float(list_currency_2[3])
if Currency == "KRW":
    UAH += (Number_of_currency_units * float(list_currency_2[4])) / 100
if Currency == "HRD":
    UAH += Number_of_currency_units * float(list_currency_2[5])
if Currency == "DKK":
    UAH += Number_of_currency_units * float(list_currency_2[6])
if Currency == "USD":
    UAH += Number_of_currency_units * float(list_currency_2[7])
if Currency == "EUR":
    UAH += Number_of_currency_units * float(list_currency_2[8])
if Currency == "EGP":
    UAH += Number_of_currency_units * float(list_currency_2[9])
if Currency == "JPY":
    UAH += (Number_of_currency_units * float(list_currency_2[10])) / 10
if Currency == "PLN":
    UAH += Number_of_currency_units * float(list_currency_2[11])
if Currency == "INR":
    UAH += (Number_of_currency_units * float(list_currency_2[12])) / 10
if Currency == "CAD":
    UAH += Number_of_currency_units * float(list_currency_2[13])
if Currency == "HRK":
    UAH += Number_of_currency_units * float(list_currency_2[14])
if Currency == "MXN":
    UAH += Number_of_currency_units * float(list_currency_2[15])
if Currency == "MDL":
    UAH += Number_of_currency_units * float(list_currency_2[16])
if Currency == "ILS":
    UAH += Number_of_currency_units * float(list_currency_2[17])
if Currency == "NZD":
    UAH += Number_of_currency_units * float(list_currency_2[18])
if Currency == "NOK":
    UAH += Number_of_currency_units * float(list_currency_2[19])
if Currency == "ZAR":
    UAH += Number_of_currency_units * float(list_currency_2[20])
if Currency == "RUB":
    UAH += (Number_of_currency_units * float(list_currency_2[21])) / 10
if Currency == "RON":
    UAH += Number_of_currency_units * float(list_currency_2[22])
if Currency == "IDR":
    UAH += (Number_of_currency_units * float(list_currency_2[23])) / 1000
if Currency == "SGD":
    UAH += Number_of_currency_units * float(list_currency_2[24])
if Currency == "XDR":
    UAH += Number_of_currency_units * float(list_currency_2[25])
if Currency == "KZT":
    UAH += (Number_of_currency_units * float(list_currency_2[26])) / 100
if Currency == "TRY":
    UAH += Number_of_currency_units * float(list_currency_2[27])
if Currency == "HUF":
    UAH += (Number_of_currency_units * float(list_currency_2[28])) / 100
if Currency == "GBP":
    UAH += Number_of_currency_units * float(list_currency_2[29])
if Currency == "CZK":
    UAH += Number_of_currency_units * float(list_currency_2[30])
if Currency == "SEK":
    UAH += Number_of_currency_units * float(list_currency_2[31])
if Currency == "CHF":
    UAH += Number_of_currency_units * float(list_currency_2[32])
if Currency == "CNY":
    UAH += Number_of_currency_units * float(list_currency_2[33])

print(f"\n\t{Number_of_currency_units} {Currency} in UAH will be {UAH} UAH!")
