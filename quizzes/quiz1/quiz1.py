import duckdb
import bloomfilter as b1
import csv

data = duckdb.read_csv('students.csv')

bloomfilter = b1.BloomFilter(size=100, num_hashes=3)
#data = duckdb.sql(f"SELECT * FROM read_csv('students.csv', delim=',', header=true, columns={'SJSU_ID': 'INT64', 'Name': 'VARCHAR'});")

with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bloomfilter.add(row['SJSU_ID'])

print(data.SJSU_ID)
#print(data.rows)
#bloomfilter.add(element = data.SJSU_ID)

ID = input("check ID: ")
if bloomfilter.lookup(element= ID):
    print("True")
    duckdb.sql(f'SELECT * FROM "students.csv" WHERE SJSU_ID = {ID}')
    #duckdb.sql(f'SELECT * FROM "students.csv" WHERE SJSU_ID = {ID}').fetchnumpy()
    
else:
    print("False")