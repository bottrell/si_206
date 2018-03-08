"""

'''Some terminology:

- Row: a set of associated data
- Column: a particular type of data to be associated with each Row in a Table
- Field: a particular piece of data in a row (each field also corresponds to a Column)
- Table: a grouping of Rows and associated Columns
- Entity: a higher-level concept describing a “thing” of interest to be represented in 
the database. In this example “airport” is the main Entity being respresented.'''

'''
- Columns have particular data types. Examples include
  - TEXT
  - NUMERIC
  - INTEGER
  - REAL
  - BLOB'''

#---------------------------------------------------------------------------------------------------------

#SQL
	#Declarative, not procedural
	#
 	#- Create databases and database structures (e.g., Tables)
  	#- Put stuff into databases
 	#	 - Update stuff that’s already in databases
  	#	- Query stuff that’s in databases
#---------------------------------------------------------------------------------------------------------

#"SELECT * FROM Employee"
'''
     - SELECT: introduces a clause that tells SQL that we are querying (or “selecting”) a subset of data from the DB
     - FROM: tells SQL the location of the data from which we are selecting (e.g., the Table)
     - *: a wildcard that means “select all”--in this case it means “select all columns”'''
#---------------------------------------------------------------------------------------------------------

#"SELECT LastName, FirstName FROM Employee"
	''' Here, we limited the columns we were interested in. Instead of ‘*’ we specified ‘LastName, FirstName.’

	| Sidebar: Case-sensitivity
	SQL commands are not case sensitive. We could have just as easily said:

	select LastName, FirstName from Employee
	or 
	sElEcT LastName, FirstName FRoM Employee

	and it would have worked fine. Typically, SQL commands are capitalized by convention to make the statements easier to read (and debug!). I will adhere to this convention as often as possible, and you should too.

	Table names and Column names are sometimes case sensitive. This actually depends on the database. Ugh. In sqlite, they are not case sensitive, so you could write

	SELeCT LASTname, firstNAME FROm empLoyEE

	but please don’t. |
	'''
#---------------------------------------------------------------------------------------------------------

#SELECT LastName, FirstName FROM Employee WHERE Title='Sales Representative'
	''' WHERE: introduces selection criteria. The stuff after WHERE will resolve to True or False for each row in the DB that is examined. '''
#---------------------------------------------------------------------------------------------------------

#SQL is whitespace delimited so you can type whatever the fuck you want and if it works then the whitespace doesn't matter

#---------------------------------------------------------------------------------------------------------

"""
import sqlite3
conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()
cur.execute("SELECT LastName, FirstName FROM Employee WHERE Title='Sales Representative'")
for row in cur:
	print(row[1] + ' ' + row[0],end='\n\n\n')
conn.close()

#There areother ways you can deal with cursors includeing:
	#cur.fetchone() #gets the net row in the cursor, or None if there are none left
	#cur.fetchall() #gets all of the remaining row in the cursor as a python list object
	#cur.fetchmany(size=N) #Gets N rows as a list



















