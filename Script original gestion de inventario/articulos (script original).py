import tkinter as tk
import sqlite3
from tkinter import messagebox

######## VENTANA PARA INSETAR DATOS 

def ventana_agregar():
    #windows.withdraw()
    window=tk.Toplevel()
    window.geometry("512x512")
    e1=tk.Label(window, text="AGREGAR PRODUCTOS :",bg="white",fg="black").place(x=50, y=50),
 

   
# variable producto
    entryproducto=tk.StringVar()
    productotx=tk.Entry(window,textvariable=entryproducto).place(x=50, y=150)



# variable  precio
    entryprecio=tk.StringVar()
    preciotx=tk.Entry(window,textvariable=  entryprecio).place(x=50, y=230)
    

    entrycant=tk.StringVar()
    preciotx=tk.Entry(window,textvariable=  entrycant).place(x=50, y=310)


# Etiqueta para "INGRESE NOMBRE DEL PRODUCTO"
    etiquetanombre=tk.Label(window, text="INGRESE NOMBRE DEL PRODUCTO.", padx=10 ).place(x=30, y=115)
   
    

#Etiqueta para "INGRESE PRECIO DEL PRODUCTO"
    etiquetaprecio = tk.Label(window, text="INGRESE PRECIO DEL PRODUCTO", padx=10 ).place(x=30, y=200)

    etiquetacant = tk.Label(window, text="INGRESE CANTIDAD DEL PRODUCTO", padx=10 ).place(x=30, y=285)
   
## Boton menu  

    menu=tk.Button(window, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = window.destroy)
    menu.pack()
    menu.place(x=50,y=350)
   
    def guarda():

            db = sqlite3.connect("articulos.s3db")
            c = db.cursor()

            nombre = entryproducto.get()
            precio = entryprecio.get()
            cantidad = entrycant.get()

            c.execute("insert into articulos (nombre,precio,cantidad) values ('"+nombre+"','"+precio+"','"+cantidad+"')")
            db.commit()
            c.close()
            messagebox.showinfo("MODIFICACION","ARTICULO INGRESADO" )
            window.destroy()
            ventana_agregar()

    btguardar = tk.Button(window, text =  "GUARDAR", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = guarda)
    btguardar.pack()
    btguardar.place(x=300,y=350)

    


######## VENTANA PARA VER LOS DATOS
def ventana_ver():
    #.withdraw()
    window=tk.Toplevel()
    window.geometry("512x512")
    e1=tk.Label(window, text="BUSCAR PRODUCTOS :",bg="white",fg="black").place(x=50, y=50),
    e_codigo=tk.Label(window, text="CODIGO",bg="white",fg="black").place(x=50, y=70)
    e_nombre=tk.Label(window, text="NOMBRE",bg="white",fg="black").place(x=150, y=70)
    e_precio=tk.Label(window, text="PRECIO",bg="white",fg="black").place(x=250, y=70)
    e_cant=tk.Label(window, text="CANTIDAD",bg="white",fg="black").place(x=350, y=70)
    def mostrar():
##        codigo
        lista=tk.Listbox(window, width = 30, font=("arial", 12), height =15 )
        lista.pack()
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()
        c.execute("select * from articulos ORDER BY (codigo)DESC")
        for row in c:
            lista.insert(0,row[1]+"-------------"+ row[2]+"---------------"+ row[3])
        lista.place(x=150,y=90)
##        nombre
        lista_1=tk.Listbox(window, width = 10, font=("arial", 12), height =15 )
        lista_1.pack()
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()
        c.execute("select codigo from articulos ORDER BY (codigo)DESC")
        for row in c:
            lista_1.insert(0,row[0])
        lista_1.place(x=50,y=90)

  

    menu=tk.Button(window, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = window.destroy)
    menu.pack()
    menu.place(x=50,y=400)

    bt_mostrar = tk.Button(window, text =  "MOSTRAR PRODUCTOS", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = mostrar)
    bt_mostrar.pack()
    bt_mostrar.place(x=280,y=400)




    
########## VENTANA PARA ELIMINAR DATOS

def ventana_eliminar():
    window=tk.Toplevel()
    window.geometry("512x512")
    e1=tk.Label(window, text=" ELIMINAR PRODUCTOS :",bg="white",fg="black").place(x=50, y=50)
    
#### VARIABLE PARA ID
    
    entry_id=tk.StringVar()
    productotx=tk.Entry(window,textvariable=entry_id).place(x=50, y=150)

#### ETIQUETA PARA ID

    etiquetanombre=tk.Label(window, text="INGRESE CODIGO DEL PRODUCTO", padx=10 ).place(x=30, y=115)

    def eliminar():
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()

        id_producto = entry_id.get()
    
        c.execute("DELETE  from articulos where codigo = ('"+id_producto+"')")
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACION","ARTICULO ELIMINADO" )
        window.destroy()
        ventana_eliminar()
        
#### BOTON PARA MENU
    
    menu=tk.Button(window, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = window.destroy)
    menu.pack()
    menu.place(x=50,y=350)
#### BOTON PARA ELIMINAR
    bt_eliminar = tk.Button(window, text =  "ELIMINAR PRODUCTOS", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = eliminar)
    bt_eliminar.pack()
    bt_eliminar.place(x=280,y=350)

###### VENTANA PARA MODIFICAR



def modificar_producto():
    window=tk.Toplevel()
    window.geometry("512x512")
    e1=tk.Label(window, text=" MODIFICAR PRODUCTOS :",bg="white",fg="black").place(x=50, y=50)
    
#### VARIABLE PARA ID
    
    entry_id=tk.StringVar()
    productotx=tk.Entry(window,textvariable=entry_id).place(x=50, y=150)

#### ETIQUETA PARA ID

    etiquetanombre=tk.Label(window, text="INGRESE CODIGO DEL PRODUCTO", padx=10 ).place(x=30, y=100)


#### VARIABLE PARA VALOR NUEVO
    
    entry_valor=tk.StringVar()
    valortx=tk.Entry(window,textvariable=entry_valor).place(x=50, y=250)

    entry_cant=tk.StringVar()
    valortx=tk.Entry(window,textvariable=entry_cant).place(x=50, y=350)

#### ETIQUETA PARA NUEVO VALOR

    etiquetanombre=tk.Label(window, text="INGRESE EL NUEVO PRECIO PARA EL PRODUCTO", padx=10 ).place(x=30, y=200)

    etiquetacant=tk.Label(window, text="INGRESE LA NUEVA CANTIDAD PARA EL PRODUCTO", padx=10 ).place(x=30, y=300)



    
    def modificar():
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()

        id_producto = entry_id.get()
        nuevo_precio = entry_valor.get()
    
        c.execute("update articulos set precio =('"+nuevo_precio+"') where codigo = ('"+id_producto+"')")
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACION","ARTICULO MODIFICADO" )
        window.destroy()
        modificar_producto()
        
    def modificar2():
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()

        id_producto = entry_id.get()
        nuevo_cant = entry_cant.get()
    
        c.execute("update articulos set precio =('"+nuevo_cant+"') where codigo = ('"+id_producto+"')")
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACION","ARTICULO MODIFICADO" )
        window.destroy()
        modificar_producto()

#### BOTON PARA MENU
    
    menu=tk.Button(window, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = window.destroy)
    menu.pack()
    menu.place(x=50,y=400)
#### BOTON PARA MODIFICAR
    bt_modificar = tk.Button(window, text =  "MODIFICAR PRODUCTO", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = modificar)
    bt_modificar.pack()
    bt_modificar.place(x=280,y=400)

    
    
windows=tk.Tk()
windows.title("INVENTARIO DE PRODUCTOS");
windows.geometry("400x500")



b1=tk.Button(windows,text="Agregar Producto", fg="blue", font=("arial", 14), borderwidth=10,cursor = "hand2",relief = "raised", command = ventana_agregar,)
b1.pack()
b1.place(x=5,y=50)

b2=tk.Button(windows,text="Buscar Producto", fg="blue", font=("arial", 14), borderwidth=10,cursor = "hand2",relief = "raised", command = ventana_ver)
b2.pack()
b2.place(x=5,y=150)

b3=tk.Button(windows,text="Eliminar Producto", fg="blue", font=("arial", 14), borderwidth=10, cursor = "hand2",relief = "raised", command = ventana_eliminar)
b3.pack()
b3.place(x=5,y=250)

b4=tk.Button(windows,text="Modificar Producto", fg="blue", font=("arial", 14), borderwidth=10,cursor = "hand2",relief = "raised", command = modificar_producto)
b4.pack()
b4.place(x=5,y=350)





windows.mainloop()
