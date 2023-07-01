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
    new = transactions.transaction(id=None,amount=amount, account=account, date=dt.now(), memo=memo, category=category, payee=payee)
    print(new[5:]) # write function goes here