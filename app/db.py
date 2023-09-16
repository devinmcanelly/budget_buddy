import sqlite3
import transactions
import sqlalchemy as sqla

def initialize():
    con = sqlite3.connect("budget.db")
    cur = con.cursor()

    # Create table if not exists

    cur.execute('''
        CREATE TABLE IF NOT EXISTS accounts(
            account_id INTEGER NOT NULL PRIMARY KEY,
            balance REAL,
            account_type TEXT,
            account_name TEXT
            
        );
                ''')
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id INTEGER NOT NULL PRIMARY KEY,
            amount REAL,
            account_id INTEGER,
            date TEXT,
            memo TEXT,
            category TEXT, 
            payee TEXT,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id)
        );
    """)
    con.commit()
    con.close()


def record(self):
    con = sqlite3.connect("budget.db")
    cur = con.cursor()
    query = """
                INSERT INTO transactions (amount, account_id, date, memo, category, payee)
                VALUES (?, ?, ?, ?, ?, ?)
    """
    cur.execute(query, (self.amount, self.account, self.date, self.memo, self.category, self.payee))
    con.commit()
    con.close()

# def create_account(self):
#     con = sqlite3.connect("budget.db")
#     cur = con.cursor()
#     query = """
#         INSERT INTO account
#     """
