from urllib.request import Request, urlopen
import bs4 as bs
import pickle
req = Request('https://support.binance.com/hc/en-us/categories/115000056351', headers={'User-Agent': 'Mozilla/5.0'})
sauce = urlopen(req).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
lists = soup.findAll('li')
with open('lists/globallists.txt', 'wb') as fp:
    pickle.dump(lists, fp)

coinList = ['ETH', 'LTC', 'NEO', '123', 'QTUM', 'EOS', 'SNT', 'BNT', 'BCC', 'GAS', 'BTC', 'ETH', 'HSR', 'OAX', 'DNT', 'MCO', 'ICN', 'MCO', 'WTC', 'WTC', 'LRC', 'LRC', 'QTUM', 'YOYO', 
            'OMG', 'OMG', 'ZRX', 'ZRX', 'STRAT', 'STRAT', 'SNGLS', 'SNGLS', 'BQX', 'BQX', 'KNC', 'KNC', 'FUN', 'FUN', 'SNM', 'SNM', 'NEO', 'IOTA', 'IOTA', 'LINK', 'LINK', 'XVG', 'XVG', 'CTR', 'CTR', 'SALT', 
            'SALT', 'MDA', 'MDA', 'MTL', 'MTL', 'SUB', 'SUB', 'EOS', 'SNT', 'ETC', 'ETC', 'MTH', 'MTH', 'ENG', 'ENG', 'DNT', 'ZEC', 'ZEC', 'BNT', 'AST', 'AST', 'DASH', 'DASH', 'OAX', 'ICN', 'BTG', 'BTG', 'EVX', 
            'EVX', 'REQ', 'REQ', 'VIB', 'VIB', 'HSR', 'TRX', 'TRX', 'POWR', 'POWR', 'ARK', 'ARK', 'YOYO', 'XRP', 'XRP', 'MOD', 'MOD', 'ENJ', 'ENJ', 'STORJ', 'STORJ', 'BNB', 'VEN', 'YOYO', 'POWR', 'VEN', 'VEN', 
            'KMD', 'KMD', 'NULS', 'RCN', 'RCN', 'RCN', 'NULS', 'NULS', 'RDN', 'RDN', 'RDN', 'XMR', 'XMR', 'DLT', 'WTC', 'DLT', 'DLT', 'AMB', 'AMB', 'AMB', 'BCC', 'BCC', 'BCC', 'BAT', 'BAT', 'BAT', 'BCPT', 'BCPT', 
            'BCPT', 'ARN', 'ARN', 'GVT', 'GVT', 'CDT', 'CDT','GXS', 'GXS', 'NEO', 'NEO', 'POE', 'POE', 'QSP', 'QSP', 'QSP', 'BTS', 'BTS', 'BTS', 'XZC', 'XZC', 'XZC', 'LSK', 'LSK', 'LSK', 'TNT', 'TNT', 'FUEL', 'FUEL', 
            'MANA', 'MANA', 'BCD', 'BCD', 'DGD', 'DGD', 'IOTA', 
            'ADX', 'ADX', 'ADX', 'ADA', 'ADA', 'PPT', 'PPT', 'CMT', 'CMT', 'CMT', 'XLM', 'XLM', 'XLM', 'CND', 'CND', 'CND', 'LEND', 'LEND', 'WABI', 'WABI', 'WABI', 'LTC', 'LTC', 'LTC', 'TNB', 'TNB', 
            'WAVES', 'WAVES', 'WAVES', 
            'GTO', 'GTO', 'GTO', 'ICX', 'ICX', 'ICX', 'OST', 'OST', 'OST', 'ELF', 'ELF', 'AION', 'AION', 'AION', 'NEBL', 'NEBL', 'NEBL', 'BRD', 'BRD', 'BRD', 'MCO', 'EDO', 'EDO', 'WINGS', 'WINGS', 'NAV', 'NAV', 
            'NAV', 'LUN', 
            'LUN', 'TRIG', 'TRIG', 'TRIG', 'APPC', 'APPC', 'APPC', 'VIBE', 'VIBE', 'RLC', 'RLC', 'RLC', 'INS', 'INS', 'PIVX', 'PIVX', 'PIVX', 'IOST', 'IOST', 'CHAT', 'CHAT', 'STEEM', 'STEEM', 'STEEM', 'NANO', 
            'NANO', 'NANO', 
            'VIA', 'VIA', 'VIA', 'BLZ', 'BLZ', 'BLZ', 'AE', 'AE', 'AE', 'RPX', 'RPX', 'RPX', 'NCASH', 'NCASH', 'NCASH', 'POA', 'POA', 'POA']

positive = ['Competition','Contest','Trade','Win','Draw','Giveaway','Bounty', 
    'competition', 'contest', 'trade', 'win', 'draw', 'giveaway', 'bounty']

negative = [
    'thing','system','extend', 'Thing', 'System', 'Extend'
    'update','concluded','community', 'Update', 'Concluded', 'Community',
    'referral','upgrade','account', 'Referral', 'Upgrade', 'Account',
    'disable','monthly','statement', 'Disable', 'Monthly', 'Statement',
    'deposit','finished','beta', 'Deposit', 'Finished', 'Beta',
    'policy','distributes','api', 'Policy', 'Distributes', 'API', 'Api',
    'pc','distributed','suspend', 'PC', 'Pc', 'Distributed', 'Suspend', 
    'plan','burn','pc', 'Plan', 'Burn', 'PC'
    ]

with open('lists/coinList.txt', 'wb') as fp:
    pickle.dump(coinList, fp)
with open('lists/positive.txt', 'wb') as sp:
    pickle.dump(positive, sp)
with open('lists/negative.txt', 'wb') as gp:
    pickle.dump(negative, gp)