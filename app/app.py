from flask import Flask
import pandas as pd
import psycopg2
import os

app = Flask(__name__)

DB = 'dev'
PASSWORD = os.environ['POSTGRES_PASSWORD']
USER = os.environ['POSTGRES_USER']
PORT = '5432'
HOST = 'db'
TABLE = 'my_worker_table'


@app.route('/')
def my_app():
    try:
        con = psycopg2.connect(f'dbname={DB} user={USER} host={HOST} password={PASSWORD}')
        sql = f'select * from {TABLE}'
        df = pd.read_sql(sql, con)
        display = df.to_html()
    except Exception as e:
        display = f'DATA says NO: {e}'
    return '<div> I am a flask app in a container. You gotta pack me the right way. </div>' \
           f'<p> Currently in the table <b>{TABLE}</b></p>' \
           f'{display}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # running at 0.0.0.0:5000
