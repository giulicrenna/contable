from tkinter import * 
from tkinter import ttk, font
import getpass
raiz = Tk()
raiz.geometry('500x300')
raiz.configure(bg = 'beige')
raiz.title('Algoritmo de selección')
raiz.resizable(0,0)
miframe=Frame()
miframe.pack(fill='both', expand='true')
miframe.configure(bg = 'beige')
miframe.configure(width=500, height=300)

ttk.Button(miframe, text='De a dos candidatos').grid(row=0, column=5)
ttk.Button(miframe, text='De a tres candidatos').grid(row=2, column=5)
ttk.Button(miframe, text='De a cuatro candidatos').grid(row=4, column=5)
ttk.Button(miframe, text='De a cinco candidatos').grid(row=6, column=5)
ttk.Button(miframe, text='Salir', command=quit).grid(row=8, column=5)






raiz.mainloop()