# A class to store and retrieve account information
# TODO
# 
# connect db
# read and write account balances and transaction record.

class account:
    def __init__(self,s name, balance, transactions):
        self.name = name
        self.balance = 0
        self.transactions = []