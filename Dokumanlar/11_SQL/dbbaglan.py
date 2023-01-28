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

    def __del__(self):
        self.db.commit()
        self.db.close()

