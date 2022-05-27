import datetime
from models import  *

# with db:
#     db.create_tables([Expense,Payment])
with db:
    # komunallka=Expense(name='komunalka').save()
    # benzin=Expense.create (name='Fuel')
    # inet=Expense.insert(name='internet').execute()

    expenses=Expense.select()
    payments = [
        {'amount':13, 'payment_date':datetime.date(2021,2,13), 'expense_id':expenses[0]},
        {'amount': 14, 'payment_date': datetime.date(2021, 2, 14), 'expense_id':expenses[0]},
        {'amount': 15, 'payment_date': datetime.date(2021, 2, 15), 'expense_id':expenses[0]},
        {'amount': 16, 'payment_date': datetime.date(2021, 2, 16), 'expense_id':expenses[0]}
    ]
print('DONE')