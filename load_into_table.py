import pandas as pd
from pandas.io import sql
import sqlalchemy
import os

def load_into_sql():
    engine = sqlalchemy.create_engine('sql_String')
    for root, dirs, files in os.walk(".", topdown=False):
         for name in files:
            csv_to_read = f'{root}/{name}'
            a = pd.read_csv(csv_to_read)
            table_name = name[:-4]
            a.to_sql(con=engine, name=table_name, if_exists='replace' )
