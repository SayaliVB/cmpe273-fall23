**Step 1: Download Postgres**

Download   ➜   Move to Applications folder   ➜   Double Click

If you don't move Postgres.app to the Applications folder, some features may not work 

Click "Initialize" to create a new server

Configure your $PATH to use the included command line tools (optional):

sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp

**Step2: Install psycopg2**

pip install psycopg2

install pgAdmin to create database

create table in pgAdmin


**Step 3: write code**
important links:
https://developers.google.com/sheets/api/quickstart/python -> Initiate
https://developers.google.com/sheets/api/guides/create -> Create spreadsheet
https://developers.google.com/sheets/api/guides/values -> Read/ write cells
https://developers.google.com/sheets/api/scopes -> Scopes for accessing spreadsheet
https://github.com/jaskamante/Postgres-to-google-sheets/tree/master -> different approach for the same
https://developers.google.com/sheets/api/guides/concepts#a1_notation -> defining sheet range
https://www.postgresqltutorial.com/postgresql-python/connect/ -> Postgres-Python guide


**Step 4: Create RDS instance on AWS**

Standard Create-> Free tier -> identifier -> password -> burstable classes-> db.t3.micro -> public access : yes -> additional configuration: db name


if public access is selected No{

You need to create a new Security Group Inbound Rules

Go to "Security group rules" (under "Connectivity & security")
Click the item "default" Security group
Click "Actions" > "Edit inbound rules" > "Add rule"
Select... Type: "All traffic", Source: "My IP", then click "Save rules"
}