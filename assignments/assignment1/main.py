from __future__ import print_function

import os.path
from connection import connection
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import psycopg2

import pandas as pd
from psycopg2 import Error

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

TABLENAME = "customer"

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        #print("Inside")
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            #print("Inside2")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            #print("Inside3")
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        SAMPLE_SPREADSHEET_ID = create("customer", creds)

        data = table_to_dataframe()
        update_values(creds, SAMPLE_SPREADSHEET_ID, "USER_ENTERED", data)
    except HttpError as err:
        print(err)

def create(title, creds):
    """
    Creates the Sheet the user has access to.
    Load pre-authorized user credentials from the environment.
    """
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
        #print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get('spreadsheetId')
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def table_to_dataframe():
    #print("Inside")
    conn = None
    try:
        # read connection parameters
        params = connection()

        print (params)
 
        print('connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        #Using pandas library, get the data from the table as a dataFrame
        #df = pd.read_sql("SELECT customer_id,first_name,last_name,email,to_char(created_on, 'yyyy-MM-dd HH:mm:ss') FROM {tname}".format(tname = TABLENAME), conn)
        df = pd.read_sql("SELECT customer_id,first_name,last_name,email FROM {tname}".format(tname = TABLENAME), conn)
        print('successfully read in data')
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:")
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('database connection closed')
            return df

def update_values(creds, spreadsheet_id, value_input_option, data):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    """
    try:

        service = build('sheets', 'v4', credentials=creds)
        columns = data.columns.values.tolist()
        '''
        del columns[-1]
        columns.append("created_on")
        '''
        values = [columns] + data.values.tolist()
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range = "Sheet1",
            valueInputOption=value_input_option, body=body).execute()
        print(f"Data loaded successfully!")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

if __name__ == '__main__':
    main()