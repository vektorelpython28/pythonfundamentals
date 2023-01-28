import sqlite3 as sql
class DBsql:
    def __init__(self,adres="/workspace/pythonfundamentals/Dokumanlar/11_SQL/veritabani.db"):
        self.adres = adres
        self.db = sql.connect(self.adres)
        self.cur = self.db.cursor()

    def select(self,sorgu):
        sonuc = self.cur.execute(sorgu)
        return sonuc.fetchall()

    def insert(self,sorgu):
        self.cur.execute(sorgu)
        return self.cur.lastrowid
    
    def update(self,sorgu):
        self.cur.execute(sorgu)
        return self.cur.lastrowid

    def delete(self,sorgu):
        try:
            self.cur.execute(sorgu)
            return True
        except:
            raise Exception("Veritabanı HATASI")

        


