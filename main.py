from urllib.request import Request, urlopen
from binance.client import Client
from datetime import datetime as dt
import bs4 as bs
import pickle
import time
import os
import re


foundCoin = ''
possibleBuy = ''

def search():
    global globallists
    global foundCoin
    
    with open('lists/globallists.txt', 'rb') as fp:
        globallists = pickle.load(fp)

    sauce = urlopen(Request('https://support.binance.com/hc/en-us/categories/115000056351', headers = {'User-Agent': 'Mozilla/5.0'})).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    lists = soup.findAll('li')

    if lists == globallists:
        print('[' + str(dt.now().time()) + ']' +  ' No Updates')
        time.sleep(5)
        search()

    else:
        print('[' + str(dt.now().time()) + ']' + ' Lists differs from globallists, investigating further.')
        unmatched = ''.join(str(list(set(lists) - set(globallists))))                           # Loob unmatched variable lahutades globallists listi uuendatud listist.
        with open('lists/globallists.txt', 'wb') as fp:
            pickle.dump(lists, fp)
    
    # Qualification starts here.

    with open('lists/negative.txt', 'rb') as fp:
        negative = pickle.load(fp)
    with open('lists/positive.txt', 'rb') as gp:
        positive = pickle.load(gp)
    with open('lists/coinList.txt', 'rb') as hp:
        coinList = pickle.load(hp)
    
    if any(s in unmatched for s in negative):
        print ('[' + str(dt.now().time()) + ']' + "Encountered negative term in unmatched, dropping.")
        time.sleep(5)
        search()

    elif 'airdrop' in unmatched or 'Airdrop' in unmatched:
        print(unmatched)
        foundCoin = re.search(r'for (\w+) holders', unmatched)
        foundCoin = foundCoin.group(1)
        print('[' + str(dt.now().time()) + ']' + "Found good airdrop reference to coin:" + ' ' + foundCoin)
        buy()
    
    elif any(s in unmatched for s in positive):
        foundCoin = next(element for element in coinList if element in unmatched)
        print('[' + str(dt.now().time()) + ']' + "Found reference to coin:" + ' ' + foundCoin)
        buy()

    else: 
        print('[' + str(dt.now().time()) + ']' + 'Found no positive terms in unmatched, dropping.')
        time.sleep(5)
        search()

def buy():
    global foundCoin

    client = Client('YOUR API KEY HERE', 'YOUR SECRET KEY HERE')                                # Sisesta siia oma API key ja Secret API Key
    
    balanceDict = client.get_asset_balance(asset='BTC')
    balance = balanceDict.get('free')                                                           # Leiab vabade vahendite summa
    
    allPrices = client.get_all_tickers()
    coinInfo = next(item for item in allPrices if item["symbol"] == "%sBTC"%(foundCoin))
    foundPrice = coinInfo.get('price')

    print('[' + str(dt.now().time()) + ']' + 'Your BTC balance is:' + ' ' + str(balance))
    print('[' + str(dt.now().time()) + ']' + 'price is' + ' ' + foundPrice)

    possibleBuy = float(balance) / float(foundPrice) * 0.8                                      # Kordaja määrab, kui palju olemasolevast rahast kasutatakse tehingus
    possibleBuy = float(round(possibleBuy, 8))

    def order():
        order = client.create_order(
        symbol='%sBTC'%(foundCoin),
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=possibleBuy)
        print('[' + str(dt.now().time()) + ']' + 'Placed order for %f %s'%(possibleBuy, foundCoin))

    x = 8
    while True:
        try:
            order()
            break
        except:
            possibleBuy = float(round(possibleBuy, x - 1))
            x = x - 1
            print('[' + str(dt.now().time()) + ']' + 'Trying' + ' ' + str(possibleBuy))         # Erinevad coinid lubavad erinevat täpsust, nii et siin proovib
                                                                                                # järjest ebatäpsemat ümardamist.
    search()

def main():
    print("Binance scalper by https://github.com/karl-k-m")
    
    confirmStart = input("Type 'y' to start the bot")
    if confirmStart == 'y':
        search()

main()