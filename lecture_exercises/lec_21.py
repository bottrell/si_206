statement = '''
INSERT INTO EmployeeTerritory (Id, EmployeeId, TerritoryId)
SELECT Employee.Id || '/' || Territory.Id, Employee.Id, Territory.Id
FROM Employee, Territory
WHERE Employee.FirstName = 'Anne' 
  AND Employee.LastName = 'Dodsworth'
  AND Territory.TerritoryDescription = 'Ann Arbor'
  '''


def add_territory_slick(zip_code, desc, region_name):
    conn = sqlite3.connect('Northwind_small.sqlite')
    cur = conn.cursor()
    insert = '''
        INSERT INTO Territory (Id, TerritoryDescription, RegionId)
        SELECT ?, ?, Region.Id
        FROM Region
        WHERE Region.RegionDescription=?
    '''
    params = (zip_code, desc, region_name, )
    cur.execute(insert, params)

    print(cur.rowcount, 'rows inserted')
    conn.commit()
    conn.close()

add_territory_slick('48104', 'Ann Arbor', 'Northern')

