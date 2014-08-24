import sqlalchemy

__author__ = 'durgadas_kamath'

from sqlalchemy import *
import os
print sqlalchemy.__version__

os.remove('example.db') #Removing the example.db since below create operations will fail if it already exists

db = create_engine('sqlite:///example.db') #this will create example.db in your working directory
db.echo = False

metadata = MetaData(db)

users = Table('users', metadata,
    Column('user_id',Integer, primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String),
)
users.create()

'''
if the table already exists , then you can use below with autoload = true
users = Table('users', metadata, autoload=true)
'''

i = users.insert()
i.execute(name='user1', age=25, password='secret')

'''
Either you can add single row or you can add multiple using dictionary within a tuple.
If you don't specify certain columns then it sets it to None except the primary key which is uniquely generated
'''
i.execute({'name': 'user2', 'age': 23},
          {'name': 'user3', 'age': 24})

s = users.select()
rs = s.execute()
for row in rs:
    print row.user_id, '--', row.name, ' -- ',row.age, '---',row.password
