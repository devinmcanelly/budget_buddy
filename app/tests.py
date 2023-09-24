import db
import usr_input as ui
import classes as cl



# Basic testing of account creation.
db.initialize() # Bring up and make a new db.

ui.get_new() # bad name, needs to error if acct doesn't exist.
# Posting new transaction works. Need to break up into better testing steps.


ui.make_acct()
