from tkinter import *
from tkinter import ttk, font
raiz = Tk()
raiz.configure(bg = 'beige')
raiz.title('Algoritmo de selección')
miframe=Frame()
miframe.pack(fill='both', expand='true')
miframe.configure(bg = 'beige')
miframe.configure(width=500, height=300 )

ttk.Button(raiz, text='Salir',command=quit).pack(side=BOTTOM)
################################################################# De a dos candidatos
def de_a_2():
        #candidato 1
        preguntanombre = Label(miframe, text='nombre del candidato').pack(side=BOTTOM)
        nombre_cand1 = Entry(raiz).pack(side=BOTTOM)
        preguntaedad = Label(miframe, text='edad del candidato').pack(side=BOTTOM)
        edad_cand1 = Entry(raiz).pack(side=BOTTOM)
        pregunta1 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta3 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta4 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta5 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()  
        pregunta6 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta7 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        #candidato 2
        preguntanombre_2 = Label(miframe, text='nombre del candidato').pack(side=BOTTOM)
        nombre_cand2 = Entry(raiz).pack(side=BOTTOM)
        preguntaedad = Label(miframe, text='edad del candidato').pack(side=BOTTOM)
        edad_cand2 = Entry(raiz).pack(side=BOTTOM)
        pregunta1_2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta2_2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta3_2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta4_2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta5_2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta6_2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()
        pregunta7_2 = Label(miframe, text='¿?', font=25).place(x=225,y=50)
        ttk.Button(miframe, text='si').grid()
        ttk.Button(miframe, text='no').grid()

de_a_2








raiz.mainloop()