#Combining one-to-many joins with many-to-many joins
statement1 = """
SELECT p.ProductName, o.Id, o.OrderDate, 
       s.CompanyName, e.FirstName, e.LastName
-- many-to-many through OrderDetail
FROM Product as p
        JOIN OrderDetail as d
        ON d.ProductId=p.Id
                JOIN [Order] as o
                ON d.OrderId = o.Id
        -- one-to-many (Order -> Employee)
        JOIN Employee as e
        ON o.EmployeeId=e.Id
        -- one-to-many(Order -> Shipper)
        JOIN Shipper as s
        ON o.ShipVia=s.Id
WHERE o.OrderDate = '2014-04-20' """

statement2 = """

    SELECT ProductName, o.Id, o.OrderDate
    FROM Product as p
            JOIN OrderDetail as d
              ON d.ProductId=p.Id
            JOIN [Order] as o
              ON d.OrderId = o.Id
    WHERE o.OrderDate = '2014-04-20'
"""