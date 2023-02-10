import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the database connection details from the environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


def create_database(db_host, db_user, db_password):

    conn = psycopg2.connect(
        host=db_host,
        database="postgres",
        user=db_user,
        password=db_password
    )
    conn.autocommit = True

    #creating the cursor object
    cur = conn.cursor()

    # Creating the database
    cur.execute("CREATE DATABASE shamiri")

    # Committing the changes
    conn.commit()

    # Closing the cursor and connection
    cur.close()
    conn.close()


def create_table(db_host, db_name, db_user, db_password):
    conn_db = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Create a cursor object
    cur_db = conn_db.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS xyz (
                                                id      integer ,
                                                first_name    text,
                                                last_name      text,
                                                email  text,
                                                gender text,
                                                ip_address  text,
                                                isAdmin   boolean) '''
    cur_db.execute(create_script)

    # Commit the changes
    conn_db.commit()

    # Close the cursor and connection
    cur_db.close()
    conn_db.close()


def insert_data(db_host, db_name, db_user, db_password):
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Create a cursor object
    cur = conn.cursor()

    # Load a sample DataFrame
    df = pd.read_csv('MOCK_DATA.csv')
    df.dropna(inplace=True)
    df = df.astype({'id': 'int'})
    
    # Iterate over the DataFrame rows and insert the data into the table
    cols = ",".join([str(i) for i in df.columns.tolist()])
    for i, row in df.iterrows():
        sql = "INSERT INTO xyz (" + cols + \
            ") VALUES (" + "%s,"*(len(row)-1) + "%s)"
        cur.execute(sql, tuple(row))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()


create_database(db_host, db_user, db_password)
create_table(db_host, db_name, db_user, db_password)
insert_data(db_host, db_name, db_user, db_password)
