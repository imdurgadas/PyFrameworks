__author__ = 'durgadas_kamath'

from sqlalchemy import *

db = create_engine('sqlite:///example.db') #reuse the db created in sql_basics.py
db.echo = True # True since we want to view the SQL's generated , if you aren't interested then turn it to False

metadata = MetaData(db)

users = Table('users',metadata,autoload=true) #table already exists hence use autoload=true

def execute_and_display(statement):
    rs = statement.execute()
    for row in rs:
        print row

stmt = users.select(users.c.name == 'user1') # where users.name='user1'
execute_and_display(stmt)

'''
We cannot use python and , or , not here since it cannot be overloaded. Instead, we will use sqlalchemy functions i.e and_ , or_ , not_
'''
stmt = users.select(and_(users.c.name != 'user1',users.c.age < 30))
execute_and_display(stmt)

'''
If you wish, you can also use & , | or ~ but you should be very careful with the precedence. Enclose your condtion appropriately
with the paranthesis else you will be greeted with shocking results.
'''
stmt = users.select((users.c.name != 'user1') & (users.c.age < 30))  # where users.name != 'user1' and users.age < 30
execute_and_display(stmt)


'''
Also , we have like , startswith , endswith
'''
stmt = users.select(users.c.name.like('%us%')) #where users.name like '%us%'
execute_and_display(stmt)

stmt = users.select(users.c.name.endswith('3')) #where users.name like '%3'
execute_and_display(stmt)

