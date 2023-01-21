from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT CustomerId,
        FirstName,
        LastName
    FROM customers WHERE FirstName LIKE 'U%'
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))
