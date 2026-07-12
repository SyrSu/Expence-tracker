from models import Expense
from storage_sqlite import save_expense, load_expenses
from analytics import report


def add_expense(expenses, date, item, amount, category)->Expense:
    myExpense = Expense(date=date, item=item, amount=amount, category=category)
    save_expense(myExpense)
    expenses.append(myExpense)
    return myExpense

def reload_expenses()->list[Expense]:
    return load_expenses()

def make_report(expenses, start_date, end_date, top_n = 3):
    rep = report(expenses, start_date, end_date, top_n=top_n)
    return rep