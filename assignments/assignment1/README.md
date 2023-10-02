# Problem Statement


Implementing a mini-reverse ETL application that can copy data from a data warehouse to SaaS applications.
We will use a Postgres DB as our data warehouse and will have this seed data.
Create a new Customer database.
    CREATE DATABASE customerdb;
Create a customer table.
    CREATE TABLE customer (
        customer_id serial PRIMARY KEY,
        first_name VARCHAR ( 50 ) UNIQUE NOT NULL,
        last_name VARCHAR ( 50 ) NOT NULL,
        email VARCHAR ( 255 ) UNIQUE NOT NULL,
        created_on TIMESTAMP NOT NULL
    );
On the SaaS application side, we will use Google Sheets as a SaaS application to transform data into.

**Use Cases**
Fetch data from Postgres using the below query and populate the data into a new sheet.
FROM
    SELECT customer_id, first_name, last_name, email from customer;
TO
    Sheet Name: customer
    Column Names:
    customer_id | first_name | last_name | email


# Implemented using Google OAuth API

Follow: 
https://developers.google.com/sheets/api/quickstart/python 
to enable API and create "credentials.json" and save in root folder.

