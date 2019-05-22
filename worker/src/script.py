import time
import pandas as pd
import os
from sqlalchemy import create_engine

INPUT = 'events.csv'

def engine_conf():
    """
    Generates db engine config
    :return: (str) db engine conf
    """
    host = 'db'
    port = 5432
    user = os.environ['POSTGRES_USER']
    db_name = 'dev'
    password = os.environ['POSTGRES_PASSWORD']
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'


time.sleep(20) # for now just sleep till db is set up TODO
df = pd.read_csv(INPUT)
engine = create_engine(engine_conf())
df.to_sql('my_worker_table', engine, if_exists='append', index=False)
