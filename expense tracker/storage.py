import csv
import os
from models import Expense
from datetime import date
FILE_PATH = 'expense.csv'
HEADER = ['date', 'item', 'amount', 'category']


def save_expense(expense:Expense)->None:
    file_exists = os.path.exists(FILE_PATH)
    file_is_empty = (not file_exists) or (os.path.getsize(FILE_PATH) == 0)
    
    with open(FILE_PATH, 'a', newline='', encoding='UTF-8')as f:
        writer = csv.writer(f)

        if file_is_empty:
            writer.writerow(HEADER)
        
        writer.writerow([expense.date, expense.item, expense.amount, expense.category])

        

def load_expenses()->list[Expense]:
    expense_storage = []
    file_exists = os.path.exists(FILE_PATH)
    if not file_exists:
        return []
    with open(FILE_PATH, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                expense_date = parse_date(row['date'])
                item = row['item']
                amount = float(row['amount'])
                category = row['category']
                myExpense = Expense(date = expense_date, item = item, amount = amount, category = category)
                expense_storage.append(myExpense)
            except(KeyError, ValueError, TypeError):
                continue
    return expense_storage
            
def parse_date(s):
    s = s.strip()
    sep_found = None
    sep = ['.', '-', '/']
    for _ in sep:
        if _ in s:
            sep_found = _
            break
    if sep_found is None:
        raise ValueError
    parts = s.split(sep_found)
    if len(parts) != 3:
        raise ValueError
    elif len(parts[0]) == 4:
        y = parts[0]
        m = parts[1]
        d = parts[2]
    else:
        d = parts[0]
        m = parts[1]
        y = parts[2]
    y = int(y)
    m = int(m)
    d = int(d)
    return date(y,m,d)
