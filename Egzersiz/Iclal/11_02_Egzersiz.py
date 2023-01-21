import sys
sys.path.append(".")
from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT CustomerId,
        FirstName,
        LastName
    FROM customers WHERE Country LIKE 'U%'
     AND FirstName LIKE 'F%' ORDER BY City;
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))



import sys
sys.path.append(".")
from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
SELECT
art.ArtistId,art.Name,alb.AlbumId,alb.Title
FROM albums as alb INNER JOIN
artists as art ON  art.ArtistId = alb.ArtistId
 WHERE art.Name LIKE 'Bl%'
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))