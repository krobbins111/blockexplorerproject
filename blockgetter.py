from blockchain import blockexplorer

def GetBlock():
    latestblock = blockexplorer.get_latest_block()
    return blockexplorer.get_block(latestblock.hash)

# block1 = GetBlock()
# txs = block1.transactions
# outernum = 1
# for tx in txs:
#    print('Transaction ' + str(outernum))
#    outputs = tx.outputs
#    innernum = 1
#    for output in outputs:
#        print('output ' + str(innernum) + ':')
#        print(output.value)
#        innernum += 1
#    outernum += 1
#    print('--------------------------------------------------')
