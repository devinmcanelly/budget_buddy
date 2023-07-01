# A class to store and retrive account information
# TODO
# 
# connect db
# read and write account balances and transaction record.

class account:
    def __init__(self, name, balance, transactions):
        self.name = name
        self.balance = 0
        self.transactions = []