# _*_ coding:utf-8 _*_
from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, END, HORIZONTAL, Frame, Toplevel
import tkinter
from tkinter import messagebox
from tkinter import *
import time




class Login(Frame):
    tipo_user = 0
    name_user=""
    def __init__(self, master,model):
        super().__init__(master)
        self.user_marcar = "Ingrese su nombre"
        self.contra_marcar = "Ingrese su contraseña"
        self.fila1 = ''
        self.fila2 = ''
        self.widgets()
        self.controlador = model



    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)

        if self.entry2.get() != 'Ingrese su password':
            self.entry2['show'] = ""

        if self.entry2.get() != 'Ingrese su correo':
            self.entry2['show'] = "*"

    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)

        if self.entry2.get() != 'Ingrese su password':
            self.entry2['show'] = "*"

        if self.entry2.get() == 'Ingrese su password':
            self.entry2['show'] = ""

    def salir(self):
        self.master.destroy()
        self.master.quit()

    def acceder_vistaMenuA(self):
        self.barra.place(x=75,y=353 )
        for i in range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.0050)
        self.barra['value'] = 0
        self.master.update()
        self.controlador.VistaLogin_VistaMenuA()
        self.barra.place_forget()


    def acceder_vistaMenuE(self):
        self.barra.place(x=75,y=353 )
        for i in range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.0050)
        self.barra['value'] = 0
        self.master.update()
        self.controlador.vistaLogin_vistaMenuE()
        self.barra.place_forget()



    def verificacion_users(self):
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        users_entry = self.entry1.get()
        password_entry = self.entry2.get()

        if users_entry != self.user_marcar and self.contra_marcar != password_entry:
            users_entry = str(users_entry)
            password_entry = str(password_entry)

            dato1 = self.controlador.select_user(users_entry)
            dato2 = self.controlador.select_password(password_entry)

            self.fila1 = dato1
            self.fila2 = dato2

            if self.fila1 == self.fila2:

                if len(dato1) == 0 and len(dato2) == 0:
                    self.indica2['text'] = 'Contraseña incorrecta'
                    self.indica1['text'] = 'Usuario incorrecto'
                    print ("los dos nulos")
                else:
                    datoN = dato1[0][0]
                    datoC = dato2[0][2]
                    datoT = dato1[0][3]
                    self.name_user = datoN
                    self.tipo_user = datoT

                    if datoT == 1:
                        self.acceder_vistaMenuA()
                    if datoT == 2:
                        self.acceder_vistaMenuE()


            else:
                self.indica1['text'] = 'Usuario incorrecto'
                self.indica2['text'] = 'Contraseña incorrecta'
                print ("no son iguales")

        else:
            print(messagebox.askretrycancel(message="No ha llenado nada", title="Título"))




    def widgets(self):
        #self.logo = PhotoImage(file=r'C:\Users\pc-dell\PycharmProjects\deteccionObjetos\Imagenes\Upemor.png')
        self.logo = PhotoImage(file=r'..\Imagenes\Upemor.png')
        Label(self.master, image=self.logo, bg='darkorange', height=150, width=150).pack()

        Label(self.master, text='Usuario', bg='darkorange', fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        self.entry1 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey',
                            highlightbackground="darkorange",
                            highlightcolor="#ff0000", highlightthickness=5)
        self.entry1.insert(0, self.user_marcar)
        self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: self.entry_out(self.entry1, self.user_marcar))
        self.entry1.pack(pady=4)

        self.indica1 = Label(self.master, bg='darkorange', fg='black', font=('Arial', 10, 'bold'))
        self.indica1.pack(pady=2)

        # contraseña y entry
        Label(self.master, text='Contraseña', bg='darkorange', fg='black', font=('Lucida Sans', 16, 'bold')).pack(
            pady=5)
        self.entry2 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey',
                            highlightbackground="darkorange",
                            highlightcolor="#ff0000", highlightthickness=5)
        self.entry2.insert(0, self.contra_marcar)
        self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: self.entry_out(self.entry2, self.contra_marcar))
        self.entry2.pack(pady=4)

        self.indica2 = Label(self.master, bg='darkorange', fg='black', font=('Arial', 10, 'bold'))
        self.indica2.pack(pady=2)

        Button(self.master, text='Iniciar Sesion', command=self.verificacion_users, activebackground='cyan3',
               bg='#ff4040', font=('Arial', 12, 'bold')).pack(pady=10)

        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TProgressbar", foreground='darkorange', background='red', troughcolor='darkorange',bordercolor='darkorange', lightcolor='darkorange', darkcolor='darkorange')
        self.barra = ttk.Progressbar(self.master, orient=HORIZONTAL, length=200, mode='determinate', maximum=100,style="TProgressbar")
        #self.barra.place(x=75,y=353 )
        Button(self.master, text='Salir', bg='#ff4040', activebackground='cyan3', bd=0, fg='black',font=('Arial', 15, 'bold'), command=self.salir).pack(pady=10)

