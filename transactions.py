import app
from openpyxl import worksheet as ws
from openpyxl import load_workbook
wb = load_workbook(filename = 'budget.xlxs')





# test_acct = app.account("Checking", 700, transactions_list[])
withdrawal_0 = app.transaction(0, 150.23, "Checking", datetime.date.today(), "testing memo", "testing category", "test payee")

withdrawal_0.id += 1
print(test.id)