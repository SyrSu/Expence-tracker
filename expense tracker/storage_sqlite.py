import sqlite3
from storage import parse_date
import os
from models import Expense

def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
        date TEXT,
        item TEXT,
        amount REAL,
        category TEXT
        )"""
    )
    conn.commit()
    conn.close()

def save_expense(expense: Expense):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO expenses (date, item, amount, category) VALUES (?, ?, ?, ?)""", (str(expense.date), expense.item, expense.amount, expense.category)
    )
    conn.commit()
    conn.close()

def load_expenses():
    if not os.path.exists('expenses.db'):
        return []
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute(
        """SELECT date, item, amount, category FROM expenses"""
    )
    rows = cursor.fetchall()
    expenses = []
    for row in rows:
        expense_date = parse_date(row[0])
        item = row[1]
        amount = float(row[2])
        category = row[3]
        expenses.append(Expense(expense_date, item, amount, category))

    conn.close()
    return expenses