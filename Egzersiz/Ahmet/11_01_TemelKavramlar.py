import sys
sys.path.append(".")
from dbbaglan import DBsql
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
