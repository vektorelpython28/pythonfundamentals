import sys
sys.path.append(".")
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
   ############################
    """
Customer tablosunda ülke ismi U ile 
başlayan müşterilerin
ismi A ile başlayanlarını
bilgilerini City Sütununa göre sıralayınız
""" 
import sys
sys.path.append(".")
from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT CustomerId,
        FirstName,
        LastName
    FROM customers WHERE FirstName LIKE 'A%' and country LİKE 'U%' ORDER BY City
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))
    
    """
artist ismi Bl ile başlayan sanatçıların albumlerini 
listeleyen sorguyu yazınız.
""" 
import sys
sys.path.append(".")
from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT     
    art.ArtistId,art.Name,alb.AlbumId,alb.Titl
    FROM albums as alb INNER JOIN
artists as art ON  art.ArtistId = alb.ArtistId 
WHERE art.Name LIKE 'Bl%'
     """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))


    