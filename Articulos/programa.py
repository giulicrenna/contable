import os, sys, sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gestiondearticulos.db")
with sqlite3.connect(db_path) as db:

    def Agregar_articulo():
        os.system('cls')
        print('--AGREGAR ARTÍCULO--')
        print('')

        nombre = input('Digite el nombre del artículo: ') 
        precio = input('Digite el precio del artículo: ')
        cantidad = input('Digite la cantidad de articulos: ')

        db = sqlite3.connect("gestiondearticulos.db")
        c = db.cursor()
        c.execute("insert into articulos (nombre,precio) values ('"+nombre+"','"+precio+"')")
        db.commit()
        c.close()


        #con = sqlite3.connect('gestiondearticulos.db') #Genera conexión con la base de datos y la crea como artículos.sdb, la cual va a
        #cursor = con.cursor()                   #estar en la carpeta del algoritmo
        #cursor.execute('create table articulos (id integer PRIMARY KEY, nombre text, precio real, cantidad real)') #como la concha puta de tabla no anduvo, la creo acá
        #cursor.execute("INSERT INTO articulos (nombre,precio,cantidad) values ('"+nombre+"','"+precio+"','"+cantidad+"')")  #el comando exucute genera la tabla 
        #con.commit #se aplican cambios en la base de datos
       # con.close   #el comando close cierra la conexión

        print('Artículo agregado.')
        print('')
        print('[a] Agregar otro artículo. ')
        print('[m] Volver al menú.')
        print('[s] Salir.')
        
        opcion = input('Digite su opción: ')          

        if opcion == 'm':
            menu()
        elif opcion == 's':
            sys.exit()
        elif opcion == 'a':
            Agregar_articulo()
        else:
            opcion == input('Digite una opción válida: ')
            Agregar_articulo(opcion)

    def Ver_articulo():
        os.system('cls')
        print('--ARTÍCULOS AGREGADOS--')
        print('')
        con = sqlite3.connect('gestiondearticulos.db')
        cursor = con.cursor()
        cursor.execute('select * from articulos')

        print('------\t\t------\t\t--------')   
        print('Nombre\t\tPrecio\t\tCantidad')
        print('------\t\t------\t\t--------')
        
        for articulo in cursor:
            print(articulo[1],'\t\t', articulo[2],'\t\t', articulo[3])
            print('')

        con.close() 


        print('')
        print('')
        print('[m] Volver al menú.')
        print('')
        print('[s] Salir.')
        opcion = input('Digite su opción: ') 

        if opcion == 'm':
                menu()    
        elif opcion == 's':
            sys.exit()
        else:
            opcion == input('Digite una opción válida: ')
            Ver_articulo(opcion)

    def Editar_articulo():
        os.system('cls')

        con = sqlite3.connect('gestiondearticulos.db')
        cursor = con.cursor()
        cursor.execute('select * from articulos')

        print('--MODIFICAR ARTÍCULOS--')
        print('')
        print('------\t\t------\t\t------\t\t--------')
        print('código\t\tNombre\t\tPrecio\t\tCantidad')   
        print('------\t\t------\t\t------\t\t--------')
        print('')

        for articulo in cursor():
            print(str(articulo[0]),'\t\t',articulo[1],'\t\t', articulo[2],'\t\t', articulo[3])
        
        print('')
        codigo = input('Digite el código del artículo a modificar: ')
        
        print('')
        nombre = input('Digite el nuevo nombre: ')
        precio = input('Digite el nuevo precio: ')
        cantidad = input('Digita la nueva cantidad: ')

        sql = 'update articulos set nombre='+nombre+', precio='+precio+', cantidad='+cantidad+' where id='+id
        cursor.execute(sql)
        con.commit()
        con.close

        opcion = input('Digite su opción: ')  
        print('[o] Para modificar otro artículo.')
        print('')
        print('[m] Volver al menú.')
        print('')
        print('[s] Salir.')

        if opcion == 'm':
                menu()    
        elif opcion == 'o':
            Editar_articulo()
        elif opcion == 's':
            sys.exit()
        else:
            opcion == input('Digite una opción válida: ')
            Editar_articulo(opcion)

    def Eliminar_articulo():

        os.system('cls')

        con = sqlite3.connect('gestiondearticulos.db')
        cursor = con.cursor()
        con.execute('select * from articulos')

        print('--ELIMINAR ARTÍCULOS--')
        print('')
        print('------\t\t------\t\t------\t\t--------')
        print('código\t\tNombre\t\tPrecio\t\tCantidad')   
        print('------\t\t------\t\t------\t\t--------')
        print('')

        for articulo in cursor:
            print(articulo[0],'\t\t',articulo[1],'\t\t', articulo[2],'\t\t', articulo[3])
            print('')
    
        codigo = input('Digite el código del artículo a eliminar: ')
        

        sql = 'delete from articulos where id='+id

        cursor.execute(sql)
        con.commit()
        con.close

        opcion = input('Digite su opción: ')  
        print('[e] Para eliminar otro artículo.')
        print('')
        print('[m] Volver al menú.')
        print('')
        print('[s] Salir.')

        if opcion == 'm':
                menu()    
        elif opcion == 'o':
            Eliminar_articulo()
        elif opcion == 's':
            sys.exit()
        else:
            opcion == input('Digite una opción válida: ')
            Eliminar_articulo(opcion)

    def menu():
        os.system('cls')
        print('--Información artículo--')
        print('')
        print('[1] Agregar artículo.')
        print('[2] Ver artículo. ')
        print('[3] Editar artículo ')
        print('[e] Eliminar artículo ')
        print('[s] Salir ')
        print('')

        opcion = input('Digite una opción: ')

        if opcion == '1':
            Agregar_articulo()
        elif opcion == '2':
            Ver_articulo()
        elif opcion == '3':
            Editar_articulo()
        elif opcion == 'e':
            Eliminar_articulo()
        elif opcion == 's':
            sys.exit()
        else:
            opcion =  input('Digite una opción válida: ')
            menu(opcion)
    menu()
