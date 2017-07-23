from MyClient import connect


from blockgetter import GetBlock
from blockchain import statistics

connect('10.0.0.141',3000)

block1 = GetBlock() #For later real-time block info
stats = statistics.get()
bitprice = stats.market_price_usd
print(stats.market_price_usd)

import googlefinance
import json
with open('data.json','w') as outfile:
    json.dump({'BitPrice':bitprice, 'Stock':googlefinance.getQuotes(['.INX','.DJI'])}, outfile, indent=4)