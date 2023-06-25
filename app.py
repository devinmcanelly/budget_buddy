import datetime

class transaction:
    def __init__(self, id, amount, account, date, memo, category, payee):
        self.id = id
        self.amount = amount
        self.account = account
        self.date = date
        self.memo = memo
        self.category = category
        self.payee = payee
        
class account:
    def __init__(self, name, balance, transactions):
        self.name = name
        self.balance = 0
        self.transactions = []