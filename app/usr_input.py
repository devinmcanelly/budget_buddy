import datetime as dt
import transactions
"""Input
    simple class to record test transaction data
    """
    
def get_new():
    print("Recording new transaction\n")
    amount = input("Amount: ")
    account = input("Account: ")
    memo = input("Memo: ")
    category = input("Category: ")
    payee = input("Payee: ")
    new = transactions.Transaction(id=None,amount=amount, account=account, date=dt.date.today(), memo=memo, category=category, payee=payee)
    new.record()
    # display matching db entry.