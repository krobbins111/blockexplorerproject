import pymongo
from pymongo import MongoClient

def MongoSync(btcprice, inxprice):
    client = MongoClient()#localhost,port num
    database = client.data #data = database name
    collectioninx = db.inx #inx data
    collectionbtc = db.btc #btc data
    btcPost = collectioninx.insert_one(inxprice)
    inxPost = collectionbtc.insert_one(inxprice)
