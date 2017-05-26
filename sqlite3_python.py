import sqlite3

base = sqlite3.connect('/home/gusmatoo/informatica.db')
c = base.cursor()


print("1 - Ver lista de fabricantes")
print("2 - Ver lista de articulos")
print("3 - Ingresar fabricante")
print("4 - Ver lista articulos+fabricantes")
print("5 - Ingresar articulo, precio y fabricante")
print("")

opc = {1: "FABRICANTES",
      2: "ARTICULOS"}


opcion = int(input("Ingrese opción: "))
if opcion == 4:
   c.execute('''SELECT Articulos.id, Articulos.Nombre, Articulos.Precio, Fabricantes.Nombre
   FROM Articulos INNER JOIN Fabricantes ON Fabricantes.id = Articulos.Fab''')
   a = c.fetchall()
   print("ID NOMBRE PRECIO FABRICANTE")
   for i in a:
       print(i[0], i[1], i[2], i[3])

if opcion < 3:
   c.execute('SELECT * FROM {};'.format(opc[opcion]))

if opcion == 3:
   nombre = input("Ingrese nombre: ")
   c.execute('INSERT INTO Fabricantes(Nombre) VALUES("{}");'.format(nombre))
   base.commit()

if opcion == 5:
    articulo = input("Ingrese articulo: ")
    precio = input("Ingrese precio: ")
    id_fab = input("Ingrese id de fabricante: ")
    c.execute('INSERT INTO Articulos (Nombre, Precio, Fab) VALUES(?, ?, (SELECT id FROM Fabricantes WHERE (Nombre = ?)))', (articulo, precio, id_fab))

if opcion != 3:
   a = c.fetchall()
   if opcion == 1:
       print("ID NOMBRE")
       for i in a:
           print(i[0], i[1])

   if opcion == 2:
       print("ID NOMBRE PRECIO ID_FAB")
       for i in a:
           print(i[0], i[1], i[2], i[3])


   base.commit()
   base.close()

