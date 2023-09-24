import db
import datetime as dt




class Transaction:
    def __init__(self, amount, acct_id, date, memo, category, payee):
        self.amount = amount
        self.acct_id = acct_id
        self.date = date
        self.memo = memo
        self.category = category
        self.payee = payee
        # updates an already input transaction and records a new entry

        # I'm not sure yet what the logic of the update is going  to be.

class Account:
    def __init__(self, balance, acct_type, name, date):
        self.balance = balance
        self.acct_type = acct_type
        self.name = name
        self.date = date
    def update(self, balance, acct_id):
        self.balance = balance
        self.acct_id = acct_id

    