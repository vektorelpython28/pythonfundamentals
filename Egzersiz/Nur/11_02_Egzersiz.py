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

selectOrnek()

    # customer tablosunda ülke ismi u ile başlayan müşterilerin ismi a ile başlayanların bilgilerini City sütununa göre sıralayınız.
    # artist ismi Bl ile başlayan sanatçıların albumlerini listeleyen sorguyu yazınız.