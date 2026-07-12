from models import Expense
from storage_sqlite import init_db
from storage import parse_date
from analytics import filter_by_category, filtered_by_date_range, sorted_by_amount, total_by_category, total_expenses, report, top_n_by_amount
from services import add_expense, reload_expenses, make_report

#from storage import save_expense, load_expense


def tot_by_cat_ui(total_cat):
    for k,v in total_cat.items():
        print(f'{k}: {v:.2f}; ')

def input_date(prompt):
    while True:
        date = input(prompt)
        try:
            check = parse_date(date)
            return check
        except ValueError:
            print('Please, try again write down the date in DD/MM/YYYY or YYYY/MM/DD format')

def print_expenses(expenses:list):
    if expenses == []:
        print('No expenses yet')
    else:
        for e in expenses:
            print(e.date, e.item, e.amount, e.category)


if __name__ == '__main__':
    init_db()
    expenses = reload_expenses()
    while True:
        print('1.Add expense')
        print('2.Exit')
        print('3.List expenses')
        choice = input('Choose an option: ')
        if choice == '1':
            data = input_date("Please, write today's date: ")
            item = input('Choose the item: ')
            amount = float(input("Write the amount: "))
            category = input('Which category is it?: ').strip().lower()
            add_expense(expenses=expenses, date=data, item=item, amount=amount, category=category)
            print('SAVED')

        elif choice == '2':
            print('Thank you, goodbye')
            break
        elif choice == '3':
            while True:
                print('1. Reload your expenses')
                print('2. Your total expenses')
                print('3. Total by category ')
                print('4. Filtered by category ')
                print('5. Filtered by date ')
                print('6. Sort by amount ')
                print('7. Report about your spendings ')
                print('8. Exit') 
                choice1 = input('What are you looking for? ')
                if choice1 == '1':
                    print('Reloaded')
                    expenses = reload_expenses()
                    print_expenses(expenses) 
                elif choice1 == '2':
                    total = total_expenses(expenses)
                    print(f'Total expenses = {total:.2f}')
                elif choice1 == '3':
                    total_cat = total_by_category(expenses)
                    tot_by_cat_ui(total_cat)
                elif choice1 == '4':
                    filtered = filter_by_category(expenses, input('Tell me the category: ').strip().lower())
                    if filtered == []:
                        print('No expenses for this category')
                    print_expenses(filtered)    
                elif choice1 == '5':
                    start_date=input_date('Enter starting date: ')
                    end_date=input_date("Enter ending date: ")
                    filtered_by_date = filtered_by_date_range(expenses, start_date, end_date)
                    print_expenses(filtered_by_date) 
                elif choice1 == '6':
                    choice2 = input('Descending? (y/n): ').strip().lower()
                    if choice2 == 'y' or choice2 == 'yes':
                        print_expenses(sorted_by_amount(expenses, descending=True))
                    elif choice2 == 'n' or choice2 == 'no':
                        print_expenses(sorted_by_amount(expenses, descending=False))
                    else:
                        print('Please, answer y/n or yes/no ')   
                elif choice1 == '7':
                    start_date=input_date('Enter starting date: ')
                    end_date=input_date("Enter ending date: ")
                    rep = make_report(expenses=expenses, start_date=start_date,end_date=end_date,top_n=3)
                    print_expenses(rep['filtered'])
                    print(rep['count'])
                    print(f"{rep['total']:.2f}")
                    tot_by_cat_ui(rep['by_category'])
                    print_expenses(top_n_by_amount(rep['filtered']))
                elif choice1 == '8':
                    print('Thank you, goodbye')
                    break
                
                else:
                    print('Choose number between 1, 2, 3, 4, 5, 6, 7 please')
        else:
            print('Choose number between 1, 2 and 3 please')
