from Models.Transaction import Transaction 

class BlockChain:

    TPCoins = []

    @staticmethod
    def dump_blockchain (self):
        print ("Number of blocks in the chain: " + str(len (self)))
        for x in range (len(self.TPCoins)):
            block_temp = self.TPCoins[x]
            print ("block # " + str(x))
            for transaction in block_temp.verified_transactions:
                Transaction.display_transaction (transaction)
                print ('--------------')
            print ('=====================================')