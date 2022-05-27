from peewee import *
#set database
db=SqliteDatabase('database.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database=db
        order_by='id'

class Expense(BaseModel):

    name= CharField()

    class Meta:
       db_table='expenses'

class Payment(BaseModel):
    id = PrimaryKeyField(unique=True)
    amount =FloatField()
    payment_date =DateField
    expense_id=ForeignKeyField(Expense)

    class Meta:
        db_table = 'payments'