# _*_ coding:utf-8 _*_
from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame
import time
import tkinter.messagebox
from tkinter import *





class Ventana(Frame):
    def __init__(self, master, model):
        super().__init__(master)
        self.menu = True
        self.color = True

        self.nombre = StringVar()
        self.Correo = StringVar()
        self.Contrasena = StringVar()
        self.buscar = StringVar()
        self.buscar_actualiza = StringVar()
        self.id = StringVar()
        self.controlador = model


        self.frame_inicio = Frame(self.master, bg='darkorange', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row=0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='darkorange', width=50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row=1, sticky='nsew')
        self.frame_top = Frame(self.master, bg='darkorange', height=50)
        self.frame_top.grid(column=1, row=0, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='darkorange')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.widgets()

    def pantalla_inicial(self):
        self.paginas.select([self.frame_uno])


    def pantalla_datos(self):
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.columnconfigure(1, weight=1)
        self.frame_dos.rowconfigure(2, weight=1)
        self.frame_tabla_uno.columnconfigure(0, weight=1)
        self.frame_tabla_uno.rowconfigure(0, weight=1)

    def pantalla_escribir(self):
        self.paginas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.columnconfigure(1, weight=1)

    def pantalla_actualizar(self):
        self.paginas.select([self.frame_cuatro])
        self.frame_cuatro.columnconfigure(0, weight=1)
        self.frame_cuatro.columnconfigure(1, weight=1)

    def pantalla_buscar(self):
        self.paginas.select([self.frame_cinco])
        self.frame_cinco.columnconfigure(0, weight=1)
        self.frame_cinco.columnconfigure(1, weight=1)
        self.frame_cinco.columnconfigure(2, weight=1)
        self.frame_cinco.rowconfigure(2, weight=1)
        self.frame_tabla_dos.columnconfigure(0, weight=1)
        self.frame_tabla_dos.rowconfigure(0, weight=1)

    def pantalla_ajustes(self):
        self.paginas.select([self.frame_seis])

    def mostrar(self):
        self.master.deiconify()  # Muestra una ventana

    def ocultar(self):
        self.master.withdraw()  # Oculta una ventana


    def menu_lateral(self):
        if self.menu is True:
            for i in range(50, 170, 10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
                clik_inicio = self.bt_cerrar.grid_forget()
                if clik_inicio is None:
                    self.bt_inicio.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_inicio.grid_propagate(0)
                    self.bt_inicio.config(width=i)
                    self.pantalla_inicial()
            self.menu = False
        else:
            for i in range(170, 50, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
                clik_inicio = self.bt_inicio.grid_forget()
                if clik_inicio is None:
                    self.frame_menu.grid_propagate(0)
                    self.bt_cerrar.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_cerrar.grid_propagate(0)
                    self.bt_cerrar.config(width=i)
                    self.pantalla_inicial()
            self.menu = True

    def cambiar_color(self):
        if self.color == True:
            self.bt_color['image'] = self.dia
            self.titulo.config(fg='deep sky blue')
            self.frame_seis.config(bg='black')
            self.text_ajustes.config(bg='black')
            self.texto.config(bg='black')
            self.bt_color.config(bg='black', activebackground='black')
            self.color = False
        else:
            self.bt_color['image'] = self.noche
            self.titulo.config(fg='DarkOrchid1')
            self.frame_seis.config(bg='white')
            self.text_ajustes.config(bg='white')
            self.texto.config(bg='white')
            self.bt_color.config(bg='white', activebackground='white')
            self.color = True


    def salir(self):
        self.controlador.vistaGestionU_VistaMenuA()




    def widgets(self):
        self.imagen_inicio = PhotoImage(file=r'..\Imagenes\inicio.png')
        self.imagen_menu = PhotoImage(file=r'..\Imagenes\menu.png')
        self.imagen_datos = PhotoImage(file=r'..\Imagenes\datos.png')
        self.imagen_registrar = PhotoImage(file=r'..\Imagenes\escribir.png')
        self.imagen_actualizar = PhotoImage(file=r'..\Imagenes\actualizar.png')
        self.imagen_buscar = PhotoImage(file=r'..\Imagenes\buscar.png')
        self.imagen_ajustes = PhotoImage(file=r'..\Imagenes\regresar.png')

        self.logo = PhotoImage(file=r'..\Imagenes\escuela.png')
        self.imagen_uno = PhotoImage(file=r'..\Imagenes\imagen_uno.png')
        self.imagen_dos = PhotoImage(file=r'..\Imagenes\imagen_dos.png')
        self.dia = PhotoImage(file=r'..\Imagenes\dia.png')
        self.noche = PhotoImage(file=r'..\Imagenes\noche.png')

        self.bt_inicio = Button(self.frame_inicio, image=self.imagen_inicio, bg='darkorange', activebackground='darkorange', bd=0,
                                command=self.menu_lateral)
        self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
        self.bt_cerrar = Button(self.frame_inicio, image=self.imagen_menu, bg='darkorange', activebackground='darkorange', bd=0,
                                command=self.menu_lateral)
        self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)

        # BOTONES Y ETIQUETAS DEL MENU LATERAL
        Button(self.frame_menu, image=self.imagen_datos, bg='darkorange', activebackground='darkorange', bd=0,
               command=self.pantalla_datos).grid(column=0, row=1, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_registrar, bg='darkorange', activebackground='darkorange', bd=0,
               command=self.pantalla_escribir).grid(column=0, row=2, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_actualizar, bg='darkorange', activebackground='darkorange', bd=0,
               command=self.pantalla_actualizar).grid(column=0, row=3, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_buscar, bg='darkorange', activebackground='darkorange', bd=0,
               command=self.pantalla_buscar).grid(column=0, row=4, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_ajustes, bg='darkorange', activebackground='darkorange', bd=0,
               command=self.salir).grid(column=0, row=5, pady=20, padx=10)

        Label(self.frame_menu, text='Base Datos', bg='darkorange', fg='black', font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text='Registrar', bg='darkorange', fg='black', font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text=' Actualizar', bg='darkorange', fg='black', font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text='Eliminar', bg='darkorange', fg='black', font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=4, pady=20, padx=2)
        Label(self.frame_menu, text='Regresar', bg='darkorange', fg='black', font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=5, pady=20, padx=2)

        #############################  CREAR  PAGINAS  ##############################
        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook", background='darkorange', foreground='black', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='darkorange', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="darkorange", borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected", 'darkorange')])
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'darkorange')], foreground=[("selected", 'darkorange')]);

        # CREACCION DE LAS PAGINAS
        self.paginas = ttk.Notebook(self.frame_principal, style='TNotebook')  # , style = 'TNotebook'
        self.paginas.grid(column=0, row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='darkorange')
        self.frame_dos = Frame(self.paginas, bg='white')
        self.frame_tres = Frame(self.paginas, bg='white')
        self.frame_cuatro = Frame(self.paginas, bg='white')
        self.frame_cinco = Frame(self.paginas, bg='white')
        self.frame_seis = Frame(self.paginas, bg='white')
        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)
        self.paginas.add(self.frame_tres)
        self.paginas.add(self.frame_cuatro)
        self.paginas.add(self.frame_cinco)
        self.paginas.add(self.frame_seis)

        ##############################         PAGINAS       #############################################

        ######################## FRAME TITULO #################
        self.titulo = Label(self.frame_top, text='UNIVERSIDAD POLITÉCNICA DEL ESTADO DE MORELOS', bg='darkorange',
                            fg='black', font=('Freehand521 BT', 15, 'bold'))
        self.titulo.pack(expand=1)

        ######################## VENTANA PRINCIPAL #################

        Label(self.frame_uno, image=self.logo, bg='white').pack(expand=1)

        # MOSTRAR TODOS LOS REGISTROS DE LA BASE DE DATOS MYSQL
        Button(self.frame_dos, text='ACTUALIZAR', fg='black', font=('Arial', 11, 'bold'), command=self.datos_totales,
               bg='#ff4040', bd=2, borderwidth=2).grid(column=1, row=0, pady=5)

        # ESTILO DE LAS TABLAS DE DATOS TREEVIEW
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font=('Helvetica', 10, 'bold'), foreground='black',
                               background='white')  # , fieldbackground='yellow'
        estilo_tabla.map('Treeview', background=[('selected', '#ff4040')], foreground=[('selected', 'black')])
        estilo_tabla.configure('Heading', background='white', foreground='black', padding=3, font=('Arial', 10, 'bold'))
        estilo_tabla.configure('Item', foreground='white', focuscolor='DarkOrchid1')
        estilo_tabla.configure('TScrollbar', arrowcolor='DarkOrchid1', bordercolor='black', troughcolor='DarkOrchid1',
                               background='white')

        # TABLA UNO

        self.frame_tabla_uno = Frame(self.frame_dos, bg='gray90')
        self.frame_tabla_uno.grid(columnspan=3, row=2, sticky='nsew')


        scroll_x = Scrollbar(self.frame_tabla_uno, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame_tabla_uno, orient=VERTICAL)

        self.tabla_uno = ttk.Treeview(self.frame_tabla_uno, columns=("Nombre", "Correo", "Contraseña"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.tabla_uno.xview)
        scroll_y.config(command=self.tabla_uno.yview)

        self.tabla_uno.heading("Nombre", text="Nombre")
        self.tabla_uno.heading("Correo", text="Correo")
        self.tabla_uno.heading("Contraseña", text="Contraseña")
        self.tabla_uno['show'] = 'headings'
        self.tabla_uno.column("Nombre", width=100)
        self.tabla_uno.column("Correo", width=100)
        self.tabla_uno.column("Contraseña", width=100)
        self.tabla_uno.pack(fill=BOTH, expand=1)


        ######################## REGISTRAR  #################
        Label(self.frame_tres, text='Agregar Nuevos Datos', fg='black', bg='white',
              font=('Kaufmann BT', 24, 'bold')).grid(columnspan=2, column=0, row=0, pady=5)

        Label(self.frame_tres, text='Nombre', fg='black', bg='white', font=('Rockwell', 13, 'bold')).grid(column=0,
                                                                                                         row=2, pady=15)
        Label(self.frame_tres, text='Correo', fg='black', bg='white', font=('Rockwell', 13, 'bold')).grid(column=0,
                                                                                                         row=3, pady=15)
        Label(self.frame_tres, text='Contraseña', fg='black', bg='white', font=('Rockwell', 13, 'bold')).grid(column=0,
                                                                                                         row=4, pady=15)



        Entry(self.frame_tres, textvariable=self.nombre, font=('Comic Sans MS', 12), highlightbackground="red",
              highlightcolor="darkorange", highlightthickness=5).grid(column=1, row=2)
        Entry(self.frame_tres, textvariable=self.Correo, font=('Comic Sans MS', 12), highlightbackground="red",
              highlightcolor="darkorange", highlightthickness=5).grid(column=1, row=3)
        Entry(self.frame_tres, textvariable=self.Contrasena, font=('Comic Sans MS', 12), highlightbackground="red",
              highlightcolor="darkorange", highlightthickness=5).grid(column=1, row=4)

        Button(self.frame_tres, command=self.agregar_datos, text='Registrar', font=('Arial', 10, 'bold'),
               bg='darkorange').grid(column=1, row=6, pady=10, padx=4)
        Label(self.frame_tres, image=self.imagen_uno, bg='white').grid(column=3, rowspan=5, row=0, padx=50)
        self.aviso_guardado = Label(self.frame_tres, bg='white', font=('Comic Sans MS', 12), fg='black')
        self.aviso_guardado.grid(columnspan=2, column=0, row=6, padx=5)

        ########################   ACTUALIZAR     #################
        Label(self.frame_cuatro, text='Actualizar Datos', fg='black', bg='white',
              font=('Kaufmann BT', 24, 'bold')).grid(columnspan=4, row=0)
        Label(self.frame_cuatro, text='Ingrese el nombre del evaluador a actualizar', fg='black', bg='white',
              font=('Rockwell', 12, 'bold ')).grid(columnspan=2, row=1)
        Entry(self.frame_cuatro, textvariable=self.buscar_actualiza, font=('Comic Sans MS', 12),
              highlightbackground="red",highlightcolor="darkorange", width=12, highlightthickness=5).grid(column=2, row=1, padx=5)
        Button(self.frame_cuatro, command=self.mostrarDatosActualizar, text='Buscar', font=('Arial', 12, 'bold'),
               bg='darkorange').grid(column=3, row=1, pady=5, padx=15)
        self.aviso_actualizado = Label(self.frame_cuatro, fg='black', bg='white', font=('Arial', 12, 'bold'))
        self.aviso_actualizado.grid(columnspan=2, row=7, pady=10, padx=5)



        Label(self.frame_cuatro, text='Correo', fg='black', bg='white', font=('Rockwell', 13, 'bold')).grid(column=0,row=3,pady=15)
        Label(self.frame_cuatro, text='Contraseña', fg='black', bg='white', font=('Rockwell', 13, 'bold')).grid(column=0,row=4, pady=15)


        Entry(self.frame_cuatro, textvariable=self.Correo, font=('Comic Sans MS', 12),
              highlightbackground="red", highlightcolor="darkorange", highlightthickness=5).grid(column=1, row=3)
        Entry(self.frame_cuatro, textvariable=self.Contrasena, font=('Comic Sans MS', 12),
              highlightbackground="red", highlightcolor="darkorange", highlightthickness=5).grid(column=1, row=4)

        Button(self.frame_cuatro, command=self.actualizar, text='Actualizar', font=('Arial', 12, 'bold'),bg='darkorange').grid(column=3, row=6, pady=5, padx=15)





        ######################## BUSCAR y ELIMINAR DATOS #################
        Label(self.frame_cinco, text='Buscar y Eliminar Datos', fg='black', bg='white',
              font=('Kaufmann BT', 24, 'bold')).grid(columnspan=4, row=0, sticky='nsew', padx=2)
        Entry(self.frame_cinco, textvariable=self.buscar, font=('Comic Sans MS', 12), highlightbackground="red",
              highlightcolor="darkorange", highlightthickness=5).grid(column=0, row=1, sticky='nsew', padx=2)
        Button(self.frame_cinco, command=self.buscar_nombre, text='Buscar por nombre', font=('Arial', 8, 'bold'),
               bg='darkorange').grid(column=1, row=1, sticky='nsew', padx=2)
        Button(self.frame_cinco, command=self.eliminar_fila, text='Eliminar', font=('Arial', 8, 'bold'), bg='red').grid(
            column=2, row=1, sticky='nsew', padx=2)
        self.indica_busqueda = Label(self.frame_cinco, width=15, text='', fg='purple', bg='white',
                                     font=('Arial', 12, 'bold'))
        self.indica_busqueda.grid(column=3, row=1, padx=2)

        # TABLA DOS
        self.frame_tabla_dos = Frame(self.frame_cinco, bg='gray90')
        self.frame_tabla_dos.grid(columnspan=4, row=2, sticky='nsew')



        scroll_x = Scrollbar(self.frame_tabla_dos, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame_tabla_dos, orient=VERTICAL)

        self.tabla_dos = ttk.Treeview(self.frame_tabla_dos, columns=("Nombre", "Correo", "Contraseña"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.tabla_dos.xview)
        scroll_y.config(command=self.tabla_dos.yview)

        self.tabla_dos.heading("Nombre", text="Nombre")
        self.tabla_dos.heading("Correo", text="Correo")
        self.tabla_dos.heading("Contraseña", text="Contraseña")
        self.tabla_dos['show'] = 'headings'
        self.tabla_dos.column("Nombre", width=100)
        self.tabla_dos.column("Correo", width=100)
        self.tabla_dos.column("Contraseña", width=100)
        self.tabla_dos.pack(fill=BOTH, expand=1)
        self.tabla_dos.bind("<<TreeviewSelect>>", self.obtener_fila)


        ########################  #################
        self.text_ajustes = Label(self.frame_seis, text='Configuracion', fg='purple', bg='white',
                                  font=('Kaufmann BT', 28, 'bold'))
        self.text_ajustes.pack(expand=1)
        self.bt_color = Button(self.frame_seis, image=self.noche, command=self.cambiar_color, bg='white', bd=0,
                               activebackground='white')
        self.bt_color.pack(expand=1)
        self.texto = Label(self.frame_seis, text='@autor:Arturo Israel Tolentino Morales \n Desarrollado en Python', fg='red', bg='white',
                           font=('Kaufmann BT', 18))
        self.texto.pack(expand=1)

    def datos_totales(self):
        datos = self.controlador.consultarGeneralUsuario()
        self.tabla_uno.delete(*self.tabla_uno.get_children())
        i = -1
        for dato in datos:
            i = i + 1
            self.tabla_uno.insert('', END, values=dato)



    def agregar_datos(self):
        nombre = self.nombre.get()
        correo = self.Correo.get()
        contrasena = self.Contrasena.get()
        if (nombre and correo and contrasena != '') and (not nombre.isspace() and not correo.isspace() and not contrasena.isspace()):

            if self.controlador.verificarUser(nombre) and self.controlador.verificarCorreo(correo):
                self.controlador.insertarUsuario(nombre,correo,contrasena)
                self.aviso_guardado['text'] = 'Datos Guardados'
                self.limpiar_datos()
                self.aviso_guardado.update()
                time.sleep(1)
                self.aviso_guardado['text'] = ''
            else:
                tkinter.messagebox.showerror("Alerta", "Este usuario ya esta registrado")
                self.limpiar_datos()

        else:
            self.aviso_guardado['text'] = 'Ingrese todos los datos'
            self.aviso_guardado.update()
            time.sleep(1)
            self.aviso_guardado['text'] = ''


    def mostrarDatosActualizar(self):

        dato = self.buscar_actualiza.get()
        dato = str(dato)
        nombre_buscado = self.controlador.select_user(dato)


        if len(nombre_buscado) == 0:
            print(nombre_buscado)
            self.aviso_actualizado['text'] = 'No existe'
            self.indica_busqueda.update()
            time.sleep(1)
            self.limpiar_datos()
            self.aviso_actualizado['text'] = ''
        else:
            i = -1
            for dato in nombre_buscado:
                i = i + 1
                self.Correo.set(nombre_buscado[i][1])
                self.Contrasena.set(nombre_buscado[i][2])
            self.auxCorreo = self.Correo.get()



    def actualizar(self):
        correo = str(self.Correo.get())
        contrasena = str(self.Contrasena.get())
        nombreB = str(self.buscar_actualiza.get())


        if self.auxCorreo == correo:
            self.controlador.update_user(nombreB, correo, contrasena)
            self.aviso_actualizado['text'] = 'Datos actualizados'
            self.indica_busqueda.update()
            time.sleep(1)
            self.limpiar_datos()
            self.buscar_actualiza.set("")
            self.aviso_actualizado['text'] = ''
        else:

            if self.controlador.verificarCorreo(correo):
                self.controlador.update_user(nombreB,correo,contrasena)
                self.aviso_actualizado['text'] = 'Datos actualizados'
                self.indica_busqueda.update()
                time.sleep(1)
                self.limpiar_datos()
                self.buscar_actualiza.set("")
                self.aviso_actualizado['text'] = ''
            else:
                tkinter.messagebox.showerror("Alerta", "Ese correo no esta disponible")
                self.limpiar_datos()
                self.buscar_actualiza.set("")



    def limpiar_datos(self):
        self.nombre.set('')
        self.Correo.set('')
        self.Contrasena.set('')


    def buscar_nombre(self):
        nombre = self.buscar.get()
        nombre= str(nombre)
        nombre_buscado = self.controlador.select_user(nombre)

        i = -1
        for dato in nombre_buscado:
            i = i + 1
            self.tabla_dos.insert('', END, values=dato)
        self.buscar.set("")

    def eliminar_fila(self):
        fila = self.tabla_dos.selection()
        if len(fila) != 0:
            self.tabla_dos.delete(fila)
            nombre = (str(self.nombre_borrar))
            self.controlador.eliminarUsuario(nombre)
            self.indica_busqueda['text'] = 'Eliminado'
            self.indica_busqueda.update()
            self.tabla_dos.delete(*self.tabla_dos.get_children())
            time.sleep(1)
            self.indica_busqueda['text'] = ''
            self.limpiar_datos()
        else:
            self.indica_busqueda['text'] = 'No se Elimino'
            self.indica_busqueda.update()
            self.tabla_dos.delete(*self.tabla_dos.get_children())
            time.sleep(1)
            self.indica_busqueda['text'] = ''
            self.buscar.set('')
            self.limpiar_datos()

    def obtener_fila(self, event):
        current_item = self.tabla_dos.focus()
        if not current_item:
            return
        data = self.tabla_dos.item(current_item)
        self.nombre_borrar = data['values'][0]
        print(self.nombre_borrar)





