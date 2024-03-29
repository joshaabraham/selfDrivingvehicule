
import datetime
import collections
import binascii
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Transaction:

    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()


    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time' : self.time})


    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')


    @staticmethod
    def display_transaction(transaction):
            #for transaction in transactions:
            dict = transaction.to_dict()
            print ("sender: " + dict['sender'])
            print ('-----')
            print ("recipient: " + dict['recipient'])
            print ('-----')
            print ("value: " + str(dict['value']))
            print ('-----')
            print ("time: " + str(dict['time']))
            print ('-----')