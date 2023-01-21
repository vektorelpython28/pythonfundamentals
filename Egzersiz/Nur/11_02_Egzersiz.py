from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT CustomerId,
        FirstName,
        LastName
    FROM customers WHERE FirstName LIKE 'F%'
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))

    # customer tablosunda ülke ismi u ile başlayan müşterilerin ismi a ile başlayanlarını bilgilerini City sütununa göre sıralayınız.