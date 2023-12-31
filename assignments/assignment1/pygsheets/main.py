import psycopg2
import pandas as pd   
import pygsheets
from psycopg2 import Error
from connection import connection
from dbconfig import dbconfig
import os
import json

def table_to_sheets():
    print("Inside")
    conn = None
    try:
        # read connection parameters
        params = connection()

        print (params)
 
        print('connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        config_data = dbconfig()

        credential_file_name = config_data['credential_file_name']

        #Using pandas library, get the data from the table as a dataFrame
        df = pd.read_sql('SELECT * FROM {tname}'.format(tname = config_data['table_name']), conn)
        print('successfully read in data')

        #get working directory path
        dirpath = os.getcwd()
        credential_file_location = dirpath + '/' +credential_file_name

        #authorise connection to your google sheets
        gc = pygsheets.authorize(service_file = credential_file_location)
        print('successfully authorised and connected to google sheets')

        #open the google spreadsheet with the provided sheet name
        sh = gc.open(config_data['sheet_name'])
        print('opened the sheet with the sheet name provided as ' + config_data['sheet_name'])
        
        #select the first sheet as the worksheet
        wks = sh[0]

        #clear the worksheet
        wks.clear(start='A1', end=None, fields='*')
        print('worksheet has been cleared')

        #update the first sheet with the dataFrame df, starting at cell B2. 
        wks.set_dataframe(df,(1,1))
        print('data from the database table has been transferred to the google spreadsheet')

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:")
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('database connection closed')
 
table_to_sheets()

