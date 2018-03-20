import sqlite3
import sys


# SELECT COUNT(*)
# FROM Product

# COUNT just counts rows, it takes one argument (a column or *)
# You can use WHERE to be more selective

''' SELECT COUNT(ProductName)
	FROM Product
	WHERE UnitsInStock > 10'''
# --- this will return an int of the amount of items satisfying the query -----

# SELECT SUM(UnitsInStock)
# FROM Product

''' SELECT MAX(UnitsInStock)
	FROM Product

	SELECT MIN(UnitsInStock)
	FROM Product '''

# -- The DISTINCT flag can be used within SELECT to indicate that
# -- We only want to work with unique values

''' SELECT DISTINCT ReorderLevel
	FROM Product 

	OR

	SELECT COUNT(DISTINCT ReorderLevel)
	FROM Product '''


# PRACTICE 1 -- How many different job titles are there?
statement = ''' SELECT COUNT(DISTINCT Title)
				FROM Employee '''

# PRACTICE 2 -- What is the average Reorder Level for Products?
statement2 = ''' SELECT AVG(ReorderLevel)
				 FROM Product '''

# PRACTICE 3 -- How many orders were placed in April 2014?
statement3 = ''' SELECT COUNT(OrderDate)
				 FROM [Order]
				 WHERE OrderDate BETWEEN "2014-04-01" AND "2014-04-30" '''

statement4 = ''' SELECT COUNT(OrderDate)
				 FROM [ORDER]
				 WHERE OrderDate LIKE "2014-04-_" '''


#--------------------GROUPING--------------------------#

''' You can use GROUP BY to indicate a column that you want
	to use for forming groups. '''

''' SELECT COUNT(*)
	FROM Product
	GROUP BY CategoryId. '''


# We can also order the results by using ORDER BY

''' SELECT CategoryId, COUNT(*)
	FROM Product
	GROUP BY CategoryId
	ORDER BY COUNT(*) (either ASC or DESC) '''


# Practice 5 -- Return ranked list of employees by the number of orders they placed 
statement5 = '''SELECT EmployeeID, COUNT(*)
				FROM [Order]
				GROUP BY EmployeeID
				ORDER BY COUNT(*) DESC '''



#------------------JOINS WITH GROUPS AND AGGREGATES -----------#


''' SELECT CategoryName, COUNT(*)
	FROM Product
		JOIN Category
		ON Product.CategoryId = Category.Id
	GROUP BY CategoryName
	ORDER BY COUNT(*) DESC '''

# Practice 6 -- Change the statement 5 to print employee name rather than ID
statement6 = '''SELECT FirstName, LastName, COUNT(*)
				FROM [Order]
					JOIN Employee
					ON [Order].EmployeeId = Employee.Id
				GROUP BY EmployeeId
				ORDER BY COUNT(*) DESC '''

#-----------------------LIMIT--------------------------#
# You can limit the number of rows returned

# -- Top 10 Most expensive Products
''' SELECT *
	FROM Product
	ORDER BY UnitPrice DESC
	LIMIT 10 '''


# -- Products ranked by total value in inventory
''' SELECT ProductName, UnitPrice * UnitsInStock AS Value
	FROM Product
	ORDER BY UnitPrice * UnitsInStock DESC
	LIMIT 10 '''


# PRACTICE 7 -- Print out the CompanyNames of the top 10 most regular customers
# Along with the number of orders they've placed
statement7 = '''SELECT CompanyName, COUNT(*) 
				FROM [Order]
					JOIN Customer
					ON Customer.Id = [Order].CustomerId
				GROUP BY CompanyName
				ORDER BY COUNT(*) DESC'''



#-------------------------HAVING-----------------------#
# Essentially WHERE for groups, specifying criteria for groups 
# that have been created using GROUP BY

# This example uses criteria for having that is based on COUNT

''' SELECT CompanyName, COUNT(*)
	FROM [ORDER] as R
		JOIN Customer
		ON R.CustomerId=Customer.Id
	GROUP BY CustomerId
	HAVING COUNT(*) >= 20
	ORDER BY COUNT(*) DESC ''' 


# This example doesnt use aggregates but rather returns those
# whose shipping region ends with "Europe"

''' SELECT CompanyName, COUNT(*)
	FROM [Order] as R
		JOIN Customer
		ON R.CustomerId = Customer.Id
	GROUP BY CustomerId
	HAVING ShipRegion LIKE '%Europe'
	ORDER BY COUNT(*) DESC '''

# PRACTICE 8 -- Write a query that tallys up the number of
# products that come from suppliers in each country, but only countries
# whose total number of products is more than 5 (use HAVE) 

statement8 = '''SELECT Supplier.Country, COUNT(*)
				FROM Product as R
					JOIN Supplier
					ON R.SupplierId = Supplier.Id
				GROUP BY Country
				HAVING COUNT(*) > 5
				ORDER BY COUNT(*) DESC '''













