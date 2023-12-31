import json

with open('config.json') as config_file:
    data = json.load(config_file)

#google sheets details

def dbconfig():

    config_data = {}
    config_data['table_name'] = data['gsheets']['table_name']
    config_data['sheet_name'] = data['gsheets']['sheet_name']
    config_data['credential_file_name'] = data['gsheets']['credential_file_name']
    return config_data