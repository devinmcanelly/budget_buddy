import datetime as dt
import classes as classes
import db
"""Input
    simple class to record test transaction data
    """
    
def get_new():
    print("Recording new transaction\n")
    # Get list of accounts so they can be displayed.
    amount = input("Amount: ")
    account = input("Account ID is : ") # Needs to select from existing account
    memo = input("Memo: ")
    category = input("Category: ")
    payee = input("Payee: ")
    new = classes.Transaction(amount=amount, account=account, date=dt.date.today(), memo=memo, category=category, payee=payee)
    db.record(new)
    # TODO display matching db entry.

def make_acct():
    print("Create a new Account: \n")
    balance = input("Starting Balance: ")
    acct_type = input("Account Type: ") # Need to make this a selector
    name = input("Account Name: ")
    acct_info = classes.Account(balance, acct_type, name, date=dt.date.today() )
    db.create_acct(acct_info) 

# def remove_transaction():

# def 