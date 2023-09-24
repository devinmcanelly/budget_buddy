import sqlite3
import classes as classes

db_conn = None
db_cur = None

def initialize():
    global db_conn
    global db_cur
    print("Initalizing db")
    db_conn = sqlite3.connect(":memory:")
    db_cur = db_conn.cursor()
    db_cur.execute('''
        CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER NOT NULL PRIMARY KEY,
            balance REAL,
            type TEXT,
            acct_name TEXT
            
        );
                ''')
    db_cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id INTEGER NOT NULL PRIMARY KEY,
            amount REAL,
            acct_id INTEGER,
            date TEXT,
            memo TEXT,
            category TEXT, 
            payee TEXT,
            FOREIGN KEY (acct_id) REFERENCES accounts(id)
        );
    """)
    db_conn.commit()

# def db.commit(commit) to be able to pass values for different tables with n values first. 
def record(transactions):
    global db_cur
    global db_conn
    query = """
                INSERT INTO transactions(amount, acct_id, date, memo, category, payee)
                VALUES (?, ?, ?, ?, ?, ?)"""

    try:
        db_cur.execute(query, (transactions.amount, transactions.account, transactions.date, transactions.memo, transactions.category, transactions.payee))
        db_conn.commit()
    except sqlite3.Error as e:
            print("Error:", e)


def create_acct(acct_info): 
    global db_cur
    global db_conn 
    query = """
         INSERT INTO accounts(balance, type, acct_name)
         VALUES (?, ?, ?)"""
    try:
        db_cur.execute(query, (acct_info.balance, acct_info.acct_type, acct_info.name))
        db_conn.commit()
    except sqlite3.Error as e:
       print("Error: ", e)
#  def update_acct(self):
