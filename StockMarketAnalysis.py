import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from termcolor import colored
import re
plt.close('all')
from pytrends.request import TrendReq
go = True
while go:
    pytrends = TrendReq(hl='en-US', tz=360)
    pd.set_option('display.max_rows', 10)
    hund = 100
    nine = 99
    nineeight = 98
    nineseven = 97
    ninesix = 96
    ninefive = 95



    usr_inp = str(input("Which stock do you want to look at?"))
    usr_inp = usr_inp.replace(" ", "")
    cversion = colored(usr_inp, "blue")
    keywords = [usr_inp]
    pytrends.build_payload(keywords, timeframe='now 7-d', geo='US')
    graph = pytrends.interest_over_time()
    print(colored("Search Trends for ", "blue") + str(cversion))
    graph.drop(graph.head(158).index,inplace=True)
    print(graph)

    strgraph = graph.astype("|S")

    usr_choice = yf.Ticker(usr_inp)
    numbers = re.findall('[0-9]+', str(graph))
    hundred = False
    checked = False
    for i in numbers:
        list.append(int(i))

    if hund in list:
        checked = True
        hundred = True
    elif nine in list:
        checked = True
    elif nineeight in list:
        checked = True
    elif nineseven in list:
        checked = True
    elif ninesix in list:
        checked = True
    elif ninefive in list:
        checked = True

    history = usr_choice.history(period='7d')
    print("")
    print(colored("Stock History for ", "blue") + str(cversion))
    print(history.tail(10))



print(list)
inf = usr_choice.info['ask']
high = usr_choice.info['fiftyTwoWeekHigh']
low = usr_choice.info['fiftyTwoWeekLow']
mp = usr_choice.info['twoHundredDayAverage']
realh = float(high)
reall = float(low)

mid = realh - reall
print(float(realh), float(reall))
print(mid)

examples = usr_choice.info
print(inf, high, low, mp)
trend = graph.dtypes
print(examples)
print("")
print("")
longorshort = str(input("Do you want to invest long or short term? (L,S)"))
if longorshort == "L" or longorshort == "l":
    if checked:
        if inf >= high:
            print(colored("Sell, ", "red") + "This stock is passed its 52 week high of " + str(high))
        if inf <= high:
            if inf <= mid:
                print(colored("Buy, ", "green") + "this stock is closer to its 52 week low of " + str(
                    low) + " compared to its high of " + str(high))
        if inf <= high:
            if inf >= mid:
                print("Risky Sell/hold, this stock is closer to its 52 week high of " + str(
                    high) + " compared to its low of " + str(low))

    else:
        if inf >= high:
            print(colored("Sell, ", "red") + "This stock is passed its 52 week high of " + str(high))
        if inf <= high:
            if inf <= mid:
                print(colored("Buy, ", "green") + "this stock is closer to its 52 week low of " + str(
                    low) + " compared to its 52 week high of " + str(high))
        if inf <= high:
            if inf >= mid:
                print("Risky sell/hold, this stock is closer to its 52 week high of " + str(high))

elif longorshort == "S" or longorshort == "s":
    if checked:
        if inf >= mp:
            print(colored("Sell, ", "red") + "This stock is higher then its 200 day average of " + str(mp))
        if inf <= mp:
            print(colored("Buy, ", "green") + "This stock is lower then its 200 day average of " + str(mp))
    else:
        if inf >= mp:
            print(
                "Sell, This stock is higher then its 200 day average of " + str(mp) + ",but it has a low search volume")
        if inf <= mp:
            print(
                "Buy, This stock is lower then its 200 day average of " + str(mp) + ", but it has a low search volume")
print("")
print("")
askagain = str(input("Do you want to look at another stock? (Y, N)"))

if askagain == 'Y' or askagain == "y":
    go = True
elif askagain == 'N' or askagain == "n":
    go = False
    print("Thank you for using Rohin Phukan's \"simple stock analyzer\"")
