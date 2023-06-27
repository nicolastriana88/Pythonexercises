import tkinter as tk 
from tkinter import messagebox 


class VentanaEventosMouse(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Eventos Mouse sobre ventana')
        self.geometry('400x400')

        frm_principal = tk.Frame(self, bg='green', height=400, width=400)

        frm_principal.bind('<Button-1>', self.mostrar_datos)
        frm_principal.bind('<Double-Button-1>', self.mostrar_datos)