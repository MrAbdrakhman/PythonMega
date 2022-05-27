import psycopg2
from pprint import pprint
import random

conn = psycopg2.connect(
    dbname = 'school',
    password = '12345',
    user = 'app',
    host = 'localhost',
    port = 5432
)
cur = conn.cursor()
name = ['Aibek', 'Alina', 'Nazgul', 'Jibek']
phone = random.randint(1, 6)
email = ['com', 'net', 'ru']
# for i in range(30):
#     cur.execute(f"INSERT INTO school (name, phone, email) VALUES ('{random.choice(name)}', '0{random.randint(7, 9)}{phone}', '{random.choice(name)}@gmail.{random.choice(email)}')")
#     conn.commit()
cur.execute('SELECT * FROM school')


pprint(cur.fetchall())