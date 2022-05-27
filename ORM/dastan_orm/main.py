import peewee
import datetime
from views import savenewpost, noteslist


a = input()
savenewpost(a)

das = noteslist()

for i in das:
    print(f'{i.text} time {i.created}')

