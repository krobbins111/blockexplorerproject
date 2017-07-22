from blockgetter import GetBlock
from blockchain import statistics

block1 = GetBlock()
stats = statistics.get()
bitprice = stats.market_price_usd
print(stats.market_price_usd)

import googlefinance
import json
with open('data.json','w') as outfile:
    json.dump({'BitPrice':bitprice, 'Stock':googlefinance.getQuotes(['.INX','.DJI'])}, outfile, indent=4)