import sqlite3

base = sqlite3.connect('/home/gusmatoo/informatica.db')
c = base.cursor()


def RegresarMenu():
    print("------------------------------------------------------------")

    input("Presione cualquier tecla para volver al Menu")

    menu()

def menu():
    print("""------------------------------------------------

                Opciones Disponibles

-------------------------------------------------""")
    print("1 - Ver lista de fabricantes")
    print("2 - Ver lista de articulos")
    print("3 - Ver lista articulos+fabricantes")
    print("4 - Ingresar articulo, precio y fabricante")
    print("5 - Eliminar articulo o fabricante")
    print("6 - Modificar precio")
    print("")

    opc = {1: "FABRICANTES",
      2: "ARTICULOS"}


    opcion = int(input("Ingrese opción: "))
    if opcion == 3:
        c.execute('''SELECT Articulos.id, Articulos.Nombre, Articulos.Precio, Fabricantes.Nombre
        FROM Articulos INNER JOIN Fabricantes ON Fabricantes.id = Articulos.Fab''')
        a = c.fetchall()
        print("ID NOMBRE PRECIO FABRICANTE")
        for i in a:
            print(i[0], i[1], i[2], i[3])
        RegresarMenu()

    if opcion < 3:
        c.execute('SELECT * FROM {};'.format(opc[opcion]))

    if opcion == 4:
        n = input("Nuevo fabricante? s/n: ")
        if n == "s" or n == "S":
            nombre = input("Ingrese fabricante: ")
            c.execute('INSERT INTO Fabricantes(Nombre) VALUES("{}");'.format(nombre))
            print("Ingreso exitoso!!!")
            print("")
            articulo = input("Ingrese articulo: ")
            precio = input("Ingrese precio: ")
            fab = input("Ingrese fabricante: ")
            c.execute('INSERT INTO Articulos (Nombre, Precio, Fab) VALUES(?, ?, (SELECT id FROM Fabricantes\
                      WHERE (Nombre = ?)))', (articulo, precio, fab))
            print("")
            print("Carga de producto, precio y fabricante exitosa!!!")
            base.commit()
        else:
            articulo = input("Ingrese articulo: ")
            precio = input("Ingrese precio: ")
            fab = input("Ingrese fabricante: ")
            c.execute('INSERT INTO Articulos (Nombre, Precio, Fab) VALUES(?, ?, (SELECT id FROM Fabricantes\
                      WHERE (Nombre = ?)))', (articulo, precio, fab))
            print("Carga de producto, precio y fabricante exitosa!!!")
            print("")
            base.commit()
            RegresarMenu()

    if opcion != 3:
        a = c.fetchall()
        if opcion == 1:
            print("ID NOMBRE")
            for i in a:
                print(i[0], i[1])

            RegresarMenu()

    if opcion == 2:
        print("ID NOMBRE PRECIO ID_FAB")
        for i in a:
            print(i[0], i[1], i[2], i[3])

        RegresarMenu()

    if opcion == 5:
        a = input("Para eliminar producto (p) - Para eliminar fabricante (f): ")
        if a == "p" or a == "P":
            pro = input("Qué producto quiere borrar?: ")
            c.execute('DELETE FROM Articulos WHERE Nombre = "{}"'.format(pro))
            print("Producto borrado!!!")
            RegresarMenu()

        if a == "f" or a == "F":
            fab = input("Qué fabricante quiere borrar?: ")
            c.execute('DELETE FROM Fabricantes, Articulos WHERE Nombre = "{}"'.format(fab))
            print("Fabricante borrado!!!")
            RegresarMenu()
    base.commit()


menu()