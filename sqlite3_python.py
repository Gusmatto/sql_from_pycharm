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
    print("5 - Eliminar producto")
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
            c.execute('INSERT INTO Articulos (Nombre, Precio, Fab) VALUES(?, ?, (SELECT id FROM Fabricantes WHERE (Nombre = ?)))', (articulo, precio, fab))
            print("Carga de producto, precio y fabricante exitosa!!!")
            base.commit()
        else:
            articulo = input("Ingrese articulo: ")
            precio = input("Ingrese precio: ")
            fab = input("Ingrese fabricante: ")
            c.execute('INSERT INTO Articulos (Nombre, Precio, Fab) VALUES(?, ?, (SELECT id FROM Fabricantes WHERE (Nombre = ?)))', (articulo, precio, fab))
            print("Carga de producto, precio y fabricante exitosa!!!")
            base.commit()

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



    base.commit()
    base.close()

menu()