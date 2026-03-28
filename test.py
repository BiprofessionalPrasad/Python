# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:37:02 2019

@author: pgaiton
"""

import sqlalchemy
import pandas as pd

#----- sql alchemy (does not work) ------
#sqlalchemy engine connection
engine = sqlalchemy.create_engine("mssql+pyodbc://ftwdb2/TempDB?driver=SQL+Server+Native+Client+10.0?trusted_connection=yes")

#2b. write py df to sql
# this part is failing....
# dfExcel.to_sql(name='TemplateForUpload_py',con=engine,schema='dbo',if_exists='append')
#df.to_sql(name='new_table',con=engine,if_exists='append')
#check data inserted
result=engine.execute("SELECT * FROM [LearningPlans].[dbo].[TemplateForUpload_py]")
for row in result:
    print(row[:])

########## --------========== https://docs.sqlalchemy.org/en/13/orm/tutorial.html 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     fullname = Column(String)
     nickname = Column(String)

     def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.name, self.fullname, self.nickname)
        
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')        
ed_user.fullname

# We’re now ready to start talking to the database. 
from sqlalchemy.orm import sessionmaker
# create a session
Session = sessionmaker(bind=engine)

#initiate a session
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first() 


session.close()
result.close()