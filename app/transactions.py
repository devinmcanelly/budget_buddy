
import datetime as dt


## Transaction information
# TODO


class Transaction:
    def __init__(self, id, amount, account, date, memo, category, payee):
        self.id = id = None
        self.amount = amount
        self.account = account
        self.date = date
        self.memo = memo
        self.category = category
        self.payee = payee
    
    def record(self):
       print(self)
       #write to db



# transaction_0 = main.transaction(0, 150.23, "Checking", datetime.date.today(), "testing memo", "testing category", "test payee")


# def record_transaction wb.append('transaction column, withdrawal_0')