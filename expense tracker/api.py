from fastapi import FastAPI
from storage_sqlite import init_db
from services import reload_expenses
from pydantic import BaseModel
from datetime import date
from services import add_expense
from typing import Optional
from analytics import filter_by_category, filtered_by_date_range
from fastapi import HTTPException
from typing import List

class ExpenseCreate(BaseModel):
    date:date
    item: str
    amount: float
    category: str

class ExpenseOut(BaseModel):
    date: date
    item:str
    amount:float
    category:str

app = FastAPI()

@app.on_event('startup')
def startup():
    init_db()

@app.get('/health')
def health():
    return {'status':'ok'}

@app.get('/expenses')
def get_expenses(
    category: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    expenses = reload_expenses()
    if category:
        expenses = filter_by_category(expenses, category.strip().lower())
    if start_date and end_date:
        expenses = filtered_by_date_range(expenses, start_date, end_date)
    if (start_date and not end_date) or (end_date and not start_date):
        raise HTTPException(status_code=400, detail='Provide both start_date and end_date in YYYY-MM-DD format.')
    
    return [ExpenseOut(date=e.date, item=e.item, amount=e.amount, category=e.category) for e in expenses]

@app.post('/expenses', response_model=ExpenseOut)
def create_expense(payload: ExpenseCreate):
    expense = reload_expenses()
    e = add_expense(
        expenses=expense,
        date = payload.date,
        item = payload.item,
        amount = payload.amount,
        category = payload.category.strip().lower(),
    )
    return ExpenseOut(date = e.date, item = e.item, amount = e.amount, category = e.category)