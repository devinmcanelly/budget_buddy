import datetime as dt
import transactions
import db
"""Input
    simple class to record test transaction data
    """
    
def get_new():
    print("Recording new transaction\n")
    # Get list of accounts so they can be displayed.
    amount = input("Amount: ")
    account = input("Account: ")
    memo = input("Memo: ")
    category = input("Category: ")
    payee = input("Payee: ")
    new = transactions.Transaction(amount=amount, account=account, date=dt.date.today(), memo=memo, category=category, payee=payee)
    db.record(new)
    # TODO display matching db entry.
    
    
    
# def retrieve_account_info


# def create account