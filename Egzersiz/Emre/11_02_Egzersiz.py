from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT CustomerId,
        FirstName,
        LastName
    FROM customers WHERE FirstName LIKE 'U%' ORDER BY City
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))