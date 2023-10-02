# Implemented using pygsheets

Enable API and create service account, then create keys in service account. download the json as client_secret.json in root folder.

# PostgresSQL to Google Sheets Python Script

Description and usage:

This script connects to a Postgres database and reads the data from a specified table into a specified spreadsheet (by name). It depends on the correct credentials having already been set up and made available in the named files below. All files must be in the same directory.

To call the function in the script, see the example in test_table_to_sheets.py

Files required:


connection.py - returns the database connection details

main.py

dbconfig.py – returns the google sheets connection details

client_secret.json – the credentials for accessing your Google Drive API (do not check in to GIT)

dbconfig.json – holds the database connection details and the google spreadsheet details


Set up required:
• Add your db connection details and google spreadsheet details to the config.json file file in the same working directory as the python scripts

• Install the Python libraries shown below

Python Libraries:

psycopg2 pandas pygsheets json

• Carry out the following steps to connect to the Google Drive API in your code

Go to the Google APIs Console.
Create a new project.
Click Enable API. Search for and enable the Google Drive API.
Create credentials for a Web Server to access Application Data.
Name the service account and grant it a Project Role of Editor.
Download the JSON file.
Copy the JSON file to your code directory and rename it to client_secret.json
Create a new google sheet with the same name as that specified in your config.py
Share the sheet with the email in your client_secret.json(service account email)
