#!/usr/bin/python3
""" """
from sqlalchemy import create_engine
from sqlalchemy import MetaData
import sys

"""
Create the following variables:
HBNB_ENV: running environment.
 It can be “dev” or “test” for the moment (“production” soon!)
HBNB_MYSQL_USER: the username of your MySQL
HBNB_MYSQL_PWD: the password of your MySQL
HBNB_MYSQL_HOST: the hostname of your MySQL
HBNB_MYSQL_DB: the database name of your MySQL
HBNB_TYPE_STORAGE: the type of storage used.
 It can be “file” (using FileStorage) or db (using DBStorage)
"""
for arg in sys.argv[1:]:
    ls = arg.split('=')
    if len(ls) = 2
    exec(arg)

class DBStorage():
    """ """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}',
            echo=True,
            pool_pre_ping=True,            
        )
        if HBNB_MYSQL_DB == "test":
            MetaData.drop_all(self.__engine)
        
            
