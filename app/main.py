import os.path, datetime as dt
import usr_input as ui, classes as cl, tests as test, db


db_path = "data/budget.db"
chk_acct_info = cl.Account(100,"Checking","Test Checking", dt.date.today())
sav_acct_info = cl.Account(0,"Savings","Test Saving", dt.date.today())

if os.path.exists(db_path):
    print("database populated")
else:
    db.initialize(db_path)
    db.create_acct(chk_acct_info)
    db.create_acct(sav_acct_info)
    ui.single_transaction()