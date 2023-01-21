from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT CustomerId,
        FirstName,
        LastName
    FROM customers WHERE Country LIKE '' 
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))
"""
Customer tablosunda ülke ismi U ile 
başlayan müşterilerin
ismi A ile başlayanlarını
bilgilerini City Sütununa göre sıralayınız
""" 