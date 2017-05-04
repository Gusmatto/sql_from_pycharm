import sqlite3

base = sqlite3.connect('/home/gusmatoo/informatica.db')
c = base.cursor()

c.execute('SELECT * FROM Fabricantes;')
print(c)
