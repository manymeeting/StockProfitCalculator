import urllib2
from bs4 import BeautifulSoup
from time import gmtime, strftime

BASE_URL = "https://finance.google.com/finance?q=NASDAQ%3A"

def buildURL(symbol):
    return BASE_URL + symbol

def extractInfo(soup, key):
    return soup.find("meta", attrs={"itemprop": key})["content"]


def getOutputFormat():
    return "Output:\n%s\n%s (%s)\n%s %s (%s)\n"



def main():
    while True:
        symbol = raw_input("Input:\nPlease enter a symbol ('exit' to quit) :\n").strip()
        if(symbol == "exit"):
            exit()

        elif (symbol == ""):
            continue

        else:
            # specify the url
            url = buildURL(symbol)
            try:
                page = urllib2.urlopen(url)
            except:
                print("Error: Failed to load data")
                continue
            soup = BeautifulSoup(page, "html.parser")

            # print info
            try:
                time = strftime("%a %b %d %H:%M:%S %z %y", gmtime()) # Mon Oct 10 17:23:48 PDT 2016
                tickerSymbol = extractInfo(soup, "tickerSymbol")
                companyName = extractInfo(soup, "name")
                price = extractInfo(soup, "price")
                priceChange = extractInfo(soup, "priceChange")
                priceChangePercent = extractInfo(soup, "priceChangePercent")
                print(getOutputFormat() % (time, companyName, tickerSymbol, price, priceChange, priceChangePercent))
            except:
                print("Error: Invalid symbol (If you see this messge every time, then the data source format may have changed).")
                continue

# run program
main()