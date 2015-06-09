from sqlalchemy import *
from sqlalchemy.orm import *

'''
--------
???
--------
??mysql
--------
engine = create_engine("mysql://root:19950126@localhost/firstdb",encoding='latin1', echo=True)

--------------------------------------------
linux??????
engine = create_engine('sqlite:////absolute/path/to/foo.db')
--------------------------------------------
??????str = 'sqlite:///my.db'
engine = create_engine(str)
---------------
??????
str = 'sqlite:///C:\\Users\\Administrator\\Desktop\\python\\flask\\test01\\my.db'
-------------
'''

engine = create_engine("mysql://root:19950126@localhost/firstdb",encoding='latin1', echo=True)
metadata = MetaData(engine)
user_table = Table('person',metadata,autoload=True)

'''
------------
????
---------------
i = user_table.insert()
i.execute(name='liupeng',addr='111',pwd='111')
'''


'''

-------
orm??
-------
'''


class User(object):
    def __repr__(self):
        pass

mapper(User,user_table)

'''
----------
????
---------
session = create_session()
query = session.query(User)
u = query.filter_by(name='11').first()
'''

'''
----------
????
---------

session = sessionmaker(bind=engine)
session = session()
u = User()
u.name='new'
u.addr='12313'
u.pwd='123123'
session.add(u)
session.flush()
session.commit()
'''


'''
----------
????
------------
session = create_session()
session.query(User).filter(User.addr == '3').delete()
#session.query(User).filter_by(addr = '3').delete()
session.flush()
'''


'''
------
????
------
session = create_session()
session.query(User).filter(User.id==15).update({'name' : '2'})
session.flush()
'''



