import sys
sys.path.append(".")
from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT adi, soyadi, FROM ORNEK WHERE FirstName LIKE 'İ%'
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))

def insertOrnek():
    try:
        db = DBsql()
        sorgu = """
        INSERT INTO ORNEK (adi, soyadi) VALUES ('E','T')
        """
        sonuc = db.insert(sorgu)
        print(sonuc)
    except Exception as hata:
        print(hata)
    finally:
        del db

if __name__ == "__main__":
    insertOrnek()