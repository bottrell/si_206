#------- Show the number of products supplied by each supplier, but only for suppliers with at least 5 products
statement = ''' SELECT Supplier.Id, COUNT(*)
				FROM Product as R
					JOIN Supplier
					ON R.SupplierId = Supplier.Id
				GROUP BY Supplier.Id
				HAVING COUNT(*) >=5 
				ORDER BY COUNT(*) DESC '''

#----------- Show the number of customer in each region, sorted from most to least
statement2 = '''SELECT Region, COUNT(*)
				FROM Customer
				GROUP BY Region
				ORDER BY COUNT(*) DESC '''

#----------- Show the number of order placed by Sales Reps in April 2014
# ranked from most to least (showing the name and title of the employee)
statment3 = ''' SELECT LastName, FirstName, Title, COUNT(*)
				FROM [ORDER] as R
					JOIN Employee
					On R.EmployeeId = Employee.Id
				WHERE OrderDate BETWEEN "2014-04-01" AND "2014-04-30"
				GROUP BY LastName
				ORDER BY COUNT(*) DESC '''


#------------ List names of top ten products in terms of the number of times they were orderd in 2013
statement4 = '''SELECT ProductName, COUNT(*)
				FROM OrderDetail as O
					JOIN Product, [Order] AS A
					WHERE O.ProductId = Product.Id AND O.OrderId = A.Id AND A.OrderDate BETWEEN "2013-01-01" AND "2013-12-31"
					GROUP BY ProductName
				ORDER BY COUNT(*) DESC
				LIMIT 10 '''