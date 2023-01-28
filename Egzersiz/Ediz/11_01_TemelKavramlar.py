import sys
sys.path.append(".")
from dbbaglan import DBsql
def selectOrnek():
    db = DBsql()
    sorgu = """
    SELECT *
    FROM ORNEK
    """
    table = db.select(sorgu)
    from tabulate import tabulate
    print(tabulate(table))

def insertOrnek(adi,soyadi):
    try:
        db = DBsql()
        sorgu = f"""
        INSERT INTO ORNEK (adi,soyadi) VALUES
        ('{adi}','{soyadi}')
        """
        sonuc = db.insert(sorgu)
        db.db.commit()
        print(sonuc)
    except Exception as hata:
        print(hata)
        db.db.rollback()
    finally:
        db.db.close()

def updateOrnek(_id,adi,soyadi):
    try:
        db = DBsql()
        sorgu = f"""
                UPDATE ORNEK
                    SET adi = '{adi}',
                    soyadi = '{soyadi}'
                WHERE ornekID = {_id}
                """
        sonuc = db.update(sorgu)
        db.db.commit()
        print(sonuc)
    except Exception as hata:
        print(hata)
        db.db.rollback()
    finally:
        db.db.close()

def deleteOrnek(sart=""):
    try:
        db = DBsql()
        sorgu = f"""
            DELETE FROM ornek WHERE {sart}
        """
        if db.delete(sorgu):
            db.db.commit()
        else:
            raise Exception("HATAAAA")
    except Exception as hata:
        print(hata)
        db.db.rollback()
    finally:
        db.db.close()


if __name__ == "__main__":
    deleteOrnek("ornekID=17 OR 1=1")
    selectOrnek()
