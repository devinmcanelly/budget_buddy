import usr_input as ui
import db
import os.path


db_path = "data/budget.db"

if os.path.exists(db_path):
    ui.get_new()
else:
    db.initialize()
    ui.make_acct
    ui.get_new()
