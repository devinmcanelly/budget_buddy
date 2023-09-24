import usr_input as ui
import db
import os.path
import foo # This isn't a good sign.

db_path = "data/budget.db"

if os.path.exists(db_path):
    ui.get_new()
else:
    db.initialize()
    ui.make_acct
    ui.get_new()
