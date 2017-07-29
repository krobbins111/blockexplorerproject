from MyClient import connect


from blockgetter import GetBlock
from blockchain import statistics

#connect('10.0.0.141',3000)

block1 = GetBlock() #For later real-time block info
stats = statistics.get()
bitprice = stats.market_price_usd
btcPriceString = '"BitPrice": ' + '"' + str(bitprice) + '"'
print(btcPriceString)

import googlefinance
import json
with open('data.json','w') as outfile:
    json.dump({'Stock':googlefinance.getQuotes(['.INX'])}, outfile, indent=4)
jsonfile = open('data.json')
for lines in jsonfile.readlines():
    if lines.find('LastTradePrice') != -1:
        inxPriceString = lines[12:len(lines)-2]
        print(inxPriceString)
        break
from MongoModule import MongoSync
#MongoSync(btcPriceString, inxPriceString) #sends data to db
