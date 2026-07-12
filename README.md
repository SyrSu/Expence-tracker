# Expense Tracker

## Overview

Expense Tracker is a Python application for tracking personal expenses. It allows users to store expenses in a SQLite database, view and filter records, generate reports, and interact with the data through both a command-line interface (CLI) and a REST API built with FastAPI.

The project was created to practice Python programming, object-oriented design, working with databases, and building APIs.

---

## Features

* Add new expenses
* Store expenses in a SQLite database
* View all expenses
* Filter expenses by category
* Filter expenses by date range
* Sort expenses by amount
* Calculate total expenses
* Calculate total spending by category
* Generate summary reports
* REST API with FastAPI
* Input validation using Pydantic

---

## Technologies

* Python 3
* FastAPI
* SQLite
* Pydantic
* Dataclasses

---

## Project Structure

```text
.
├── api.py                # FastAPI application
├── analytics.py          # Reporting and analytics functions
├── services.py           # Business logic
├── storage.py            # CSV utilities and date parsing
├── storage_sqlite.py     # SQLite database operations
├── models.py             # Expense data model
├── main.py               # Command-line interface
├── expenses.db           # SQLite database
└── expense.csv           # Sample CSV file
```

---

## Running the CLI

```bash
python main.py
```

The CLI allows you to:

* Add expenses
* List all expenses
* View total spending
* Filter by category
* Filter by date
* Sort by amount
* Generate reports

---

## Running the API

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start the server:

```bash
uvicorn api:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Get Expenses

```
GET /expenses
```

Optional query parameters:

* category
* start_date
* end_date

Example:

```
GET /expenses?category=food
```

```
GET /expenses?start_date=2026-06-01&end_date=2026-06-30
```

---

### Add Expense

```
POST /expenses
```

Example request:

```json
{
  "date": "2026-07-12",
  "item": "Coffee",
  "amount": 4.5,
  "category": "food"
}
```

---

## Reports

The application can generate reports that include:

* Number of expenses
* Total amount spent
* Spending by category
* Top N largest expenses
* Expenses within a selected date range

---
