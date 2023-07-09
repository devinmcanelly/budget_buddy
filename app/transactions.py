import db
import datetime as dt


## Transaction information
# TODO


class Transaction:
    def __init__(self, amount, account, date, memo, category, payee):
        self.amount = amount
        self.account = account
        self.date = date
        self.memo = memo
        self.category = category
        self.payee = payee
    
    # def new(self):
    #    db.record(self)
    
    
    def update(self):
        print(self)
        # updates an already input transaction and records a new entry
        # I'm not sure yet what the logic of the update is going  to be.

# def record_transaction wb.append('transaction column, withdrawal_0')