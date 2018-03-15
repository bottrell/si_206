import sqlite3
import sys
import csv

def init_db():
	conn = sqlite3.connect('airports.db')
	cur = conn.cursor()

	statement = '''
		CREATE TABLE 'Airports' (
			'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
			'Iata' TEXT NOT NULL,
			'Airport' TEXT NOT NULL,
			'City' TEXT NOT NULL,
			'State' TEXT NOT NULL,
			'Country' TEXT NOT NULL,
			'Lat' INTEGER Not Null,
			'Long' INTEGER Not Null,
			'Traffic_Count' INTEGER
			);
			'''
	cur.execute(statement)
	conn.commit()
	conn.close()

init_db()
conn = sqlite3.connect('airports.db')
cur = conn.cursor()
with open('airports.csv', 'r') as f:
	reader = csv.reader(f)
	airports = []
	for row in reader:
		airports.append(row)

	airports = airports[1:]
	
	for airport in airports:
		insertion = (None, airport[0], airport[1], airport[2], airport[3],airport[4],airport[5],airport[6],airport[7])
		statement = 'INSERT INTO "Airports" '
		statement += 'VALUES (?, ?, ?, ?, ?, ? ,? ,? ,?)'
		cur.execute(statement, insertion)
	conn.commit()

	new_traffic = 8500
	iata = "DTW"
	t = (new_traffic, iata)
	update_statement = 'UPDATE Airports '
	update_statement += 'SET Traffic_Count=?'
	update_statement += 'WHERE Iata=?'
	cur.execute(update_statement, t)
	conn.commit()
	conn.close()

'''
- It turns out the data for DTW is incorrect. Update the traffic count in your DB to be 8500 instead of what it is now.
- Using a query, print out the 3-letter code, city name, and traffic count for all of the airports in Michigan.
'''
