# Database handler


import sqlite3
import pandas as pd

from sqlite3 import Error


def create_connection(path):

    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except Error as e:

        print(f"The error '{e}' occurred")


    return connection


def csv_to_sql(csv_name, db_conn):
    """[Write csv to sql db]
    Example: ('data\MunichParsedDt.csv', db)

    Args:
        csv_name ([type]): [description]
        db_conn ([type]): [description]
    """
    try:
        df = pd.read_csv(csv_name, sep='\t', encoding='utf-8')
        df.to_sql('df', db_conn)

    except Error as e:
        print('Could not convert csv to sql')

def sql_get(conn, columns='', condition=''):
    """[summary]

    Args:
        conn ([type]): [description]
        condition ([type]): [description]

    Returns:
        [type]: [description]
    """
    if columns == '':
        col_q = '*'
    else:
        col_q = ', '.join(columns)

    if condition == '':
        query = 'SELECT {} FROM df'.format(col_q)
    else:
        query = 'SELECT *\
                FROM df\
                WHERE {}'.format(condition)

    df = pd.read_sql(query, conn)
    print(len(df))

    return df

#df = pd.read_sql('SELECT * FROM df', db)
#df = pd.read_sql('SELECT flair FROM df', db)
#df = pd.read_sql('SELECT * FROM df WHERE flair == "Picture"', db)
#df = pd.read_sql('SELECT * FROM df WHERE upvotes > 100', db)


from pprint import pprint as pp
db = create_connection('redditMucDS.sqlite')
#df_100ups = sql_get(db, 'upvotes > 200')
#pprint.pprint(df_100ups)

#? Example with double constraints
#?df = pd.read_sql('SELECT * FROM df WHERE upvotes > 100 AND flair != "Picture"', db)

df = pd.read_sql('SELECT upvotes, commentsNumber FROM df\
                WHERE commentsNumber > 50',
                db)
pp(df)
