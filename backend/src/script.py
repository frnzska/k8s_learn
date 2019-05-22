#!/usr/bin/python
import time
import pandas as pd
from sqlalchemy import create_engine

print('Doing stuff...')
for i in range(0,10):
    print('========stuff========')
    time.sleep(3)


def engine_conf():
    """
    Generates db engine config
    :return: (str) db engine conf
    """
    host = 'db'
    port = 5432
    user = 'user'
    db_name = 'dev'
    password = 'password'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'




df = pd.DataFrame({"a": [1, 2], "b": ['one', 'two']})
conn_str = engine_conf()
engine = create_engine(conn_str)

df.to_sql('my_table', engine, if_exists='append', index=False)

