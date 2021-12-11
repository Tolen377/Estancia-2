import tkinter as tk
from tkinter import *


class MenuEvaluador(Frame):
    def __init__(self, master ,modelo):
        super().__init__(master)

        # diccionario de colores
        self. color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
        self.btnState = False
        self.options = ["Evaluación", "Experimentación","Salir"]
        self.widgets()
        self.controlador = modelo


    def widgets(self):

        self.navIcon = PhotoImage(file=r'..\Imagenes\open.png')
        self.closeIcon = PhotoImage(file=r'..\Imagenes\close.png')
        self.logoAve = PhotoImage(file=r'..\Imagenes\ave3.png')

        self.topFrame = tk.Frame(self.master, bg=self.color["orange"])
        self.topFrame.pack(side="top", fill=tk.X)

        self.homeLabel = tk.Label(self.topFrame, text="UPEMOR", font="Bahnschrift 15", bg=self.color["orange"], fg="gray17", height=2,
                             padx=20)
        self.homeLabel.pack(side="right")

        self.brandLabel = tk.Label(self.master, text=" Sistema \n de \n Identificación", font="System 30", bg="gray17", fg="#ff4040")
        self.brandLabel.place(x=60, y=150)

        self.ave = tk.Label(self.master, image=self.logoAve, bg='gray17', height=200, width=278).place(x=60, y=300)

        # Boton para abrir
        navbarBtn = tk.Button(self.topFrame, image=self.navIcon, bg=self.color["orange"], activebackground=self.color["orange"], bd=0,
                              padx=20, command=self.switch)
        navbarBtn.place(x=10, y=10)

        # setting Navbar frame:
        self.navRoot = tk.Frame(self.master, bg="gray17", height=1000, width=300)
        self.navRoot.place(x=-300, y=0)
        tk.Label(self.navRoot, font="Bahnschrift 15", bg=self.color["orange"], fg="black", height=2, width=300, padx=20).place(
            x=0, y=0)


        tk.Button(self.navRoot, text=self.options[0], font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                activebackground="gray17", activeforeground="#ff4040", bd=0,command=self.abrirVistaEvaluacion).place(x=25, y=80)

        tk.Button(self.navRoot, text=self.options[1], font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                  activebackground="gray17", activeforeground="#ff4040", bd=0, command = self.abrirVistaExperimentacion).place(x=25, y=120)

        tk.Button(self.navRoot, text=self.options[2], font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                  activebackground="gray17", activeforeground="#ff4040", bd=0,command=self.salir).place(x=25, y=160)


        closeBtn = tk.Button(self.navRoot, image=self.closeIcon, bg=self.color["orange"], activebackground=self.color["orange"], bd=0,
                             command=self.switch)
        closeBtn.place(x=250, y=10)



    def salir(self):
        self.controlador.vistaMenuE_vistaLogin()
        self.navRoot.place(x=-300, y=0)
        self.brandLabel.config(bg="gray17", fg="#ff4040")
        self.homeLabel.config(bg=self.color["orange"])
        self.topFrame.config(bg=self.color["orange"])
        self.master.config(bg="gray17")
        self.btnState = False




    def abrirVistaEvaluacion(self):
        self.controlador.vistaMenuE_vistaEvaluacion()
        self.navRoot.place(x=-300, y=0)
        self.brandLabel.config(bg="gray17", fg="#ff4040")
        self.homeLabel.config(bg=self.color["orange"])
        self.topFrame.config(bg=self.color["orange"])
        self.master.config(bg="gray17")
        self.btnState = False


    def abrirVistaExperimentacion(self):
        self.controlador.vistaMenuE_vistaExperimentacion()
        self.navRoot.place(x=-300, y=0)
        self.brandLabel.config(bg="gray17", fg="#ff4040")
        self.homeLabel.config(bg=self.color["orange"])
        self.topFrame.config(bg=self.color["orange"])
        self.master.config(bg="gray17")
        self.btnState = False


    def switch(self):
        if self.btnState is True:
            # cierra
            for x in range(301):
                self.navRoot.place(x=-x, y=0)
                self.topFrame.update()

            # resetting widget colors:
            self.brandLabel.config(bg="gray17", fg="#ff4040")
            self.homeLabel.config(bg=self.color["orange"])
            self.topFrame.config(bg=self.color["orange"])
            self.master.config(bg="gray17")

            # turning button OFF:
            self.btnState = False
        else:
            # make root dim:
            self.brandLabel.config(bg=self.color["nero"], fg="#5F5A33")
            self.homeLabel.config(bg=self.color["nero"])
            self.topFrame.config(bg=self.color["nero"])
            self.master.config(bg=self.color["nero"])


            # abre:
            for x in range(-300, 0):
                self.navRoot.place(x=x, y=0)
                self.topFrame.update()
            self.btnState = True
