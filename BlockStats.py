from blockgetter import GetBlock
from blockchain import statistics

block1 = GetBlock()
stats = statistics.get()
print(stats.estimated_transaction_volume_usd)
print(stats.market_price_usd)
