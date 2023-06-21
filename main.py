from openpyxl import worksheet as ws

class transaction:
    def __init__(self, id, amount, account, date, memo, category):
    self.id
    self.amount = amount
    self.account = account
    self.date = date
    self.memo
    self.category
    
class account:
    def __init__(self, name):
    self.name = name
    self.balance = 0
    self.transactions = []