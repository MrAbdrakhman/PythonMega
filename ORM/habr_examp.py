from peewee import *
import datetime
with db:
    komunallka=Expense(name='komunalka').save()
    benzin=Expense.create (name='Fuel')
    inet=Expense.insert(name='internet').execute()

print('DONE')