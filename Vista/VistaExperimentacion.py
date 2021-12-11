# _*_ coding:utf-8 _*_
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import os
from tkinter import filedialog


class Experimentacion(Frame):
	def __init__(self, master,model):
		super().__init__(master)
		self.controlador = model

		title=Label(self.master,text="Sistema Identificación de Aves", bd=10,font=("Freehand521 BT", 28,"bold"),bg="gray17", fg="black")
		title.pack(side=TOP)

		Exit_btn=Button(self.master,text="Regresar", width=7, bg="darkorange", font=("Arial",15,"bold"),command=self.regresar)
		Exit_btn.place(x=1200, y=40)

		#====Variables=====
		self.responsable=StringVar()
		self.fecha=StringVar()
		self.clase=StringVar()
		self.comentarios=StringVar()
		self.cantidadImagenes=StringVar()

		self.buscar_por=StringVar()
		self.buscar_txt=StringVar()

		Manage_Frame=Frame(self.master,bd=4,relief=RIDGE, bg="gray17")
		Manage_Frame.place(x=20,y=100,width=520,height=600)

		m_title=Label(Manage_Frame,text="Formulario de experimentación", bg="gray17", fg="black", font=("Lucida Sans",20,"bold"))
		m_title.grid(row=0,columnspan=2,pady=20)

		#labels ,Entry  Responsable --------------------------------------------->
		lbl_responsble=Label(Manage_Frame,text="Responsable:", bg="gray17", fg="black", font=("Lucida Sans",17,"bold"))
		lbl_responsble.grid(row=1,column=0,pady=10,padx=20,sticky="w")

		self.txt_responsable=Entry(Manage_Frame, textvariable=self.responsable, font=("Arial",15), bd=1,highlightcolor="darkorange", highlightthickness=5)
		self.txt_responsable.grid(row=1,column=1,pady=10,padx=20,sticky="w")
		# Fecha------------------------------------------------------------>
		lbl_fecha=Label(Manage_Frame,text="Fecha:", bg="gray17", fg="black", font=("Lucida Sans",17,"bold"))
		lbl_fecha.grid(row=2,column=0,pady=10,padx=20,sticky="w")

		self.cal = DateEntry(Manage_Frame, width=12, background='darkorange', foreground='black', borderwidth=2,date_pattern='yyyy/mm/dd',font=("Arial",15))
		self.cal.grid(padx=10, pady=10, row=2,column=1)

		# Clase------------------------------------------------------------->
		lbl_clase=Label(Manage_Frame,text="Clase", bg="gray17", fg="black", font=("Lucida Sans",17,"bold"))
		lbl_clase.grid(row=3,column=0,pady=10,padx=20,sticky="w")

		self.txt_clase=Entry(Manage_Frame, textvariable=self.clase, font=("Arial",15), bd=1,highlightcolor="darkorange", highlightthickness=5)
		self.txt_clase.grid(row=3,column=1,pady=10,padx=20,sticky="w")

		# Comentarios_______________________________________________________________>
		lbl_comentarios=Label(Manage_Frame,text="Comentarios:", bg="gray17", fg="black", font=("Lucida Sans",17,"bold"))
		lbl_comentarios.grid(row=5,column=0,pady=10,padx=20,sticky="w")

		self.txt_comentarios=Text(Manage_Frame,font=("Arial",15), bd=5, relief=GROOVE,height=5,width=20,highlightcolor="darkorange", highlightthickness=5)
		self.txt_comentarios.grid(row=5,column=1,pady=10,padx=20,sticky="w")
		self.txt_comentarios.delete("0.0", "end")
		# Cantidad de imagenes--------------------------------------------------------------------->
		label_imagenes = Label(Manage_Frame,text="Num.imagenes:", bg="gray17", fg="black", font=("Lucida Sans",17,"bold"))
		label_imagenes.grid(row=6,column=0,pady=10,padx=20,sticky="w")

		self.txtImagenes = Entry(Manage_Frame, textvariable=self.cantidadImagenes, font=("Arial",15), bd=1,highlightcolor="darkorange", highlightthickness=5)
		self.txtImagenes.grid(row=6,column=1,pady=10,padx=20,sticky="w")


		Add_btn=Button(Manage_Frame,text="Comenzar", width=9, command=self.abrir_archivo, bg= "darkorange",font=("Arial",15,"bold"))
		Add_btn.grid(row=7, column=0, padx=10, pady=10)

		#Tablas -------------------------------------------------------------------------------->
		Detail_Frame=Frame(self.master,bd=4,relief=RIDGE, bg="darkorange")
		Detail_Frame.place(x=550,y=100,width=810,height=600)

		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE, bg="darkorange")
		Table_Frame.place(x=10,y=70,width=760,height=500)


		consultar = Button(Detail_Frame, text="Consultar", width=9, command=self.mostrar, bg="gray17",
						 font=("Arial", 15, "bold"))
		consultar.grid(row=0, column=0, padx=10, pady=10)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

		self.identificaciones_table=ttk.Treeview(Table_Frame,columns=("ID","Responsable", "Fecha", "Clase", "Comentarios","Imagenes","Checkpoint"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.identificaciones_table.xview)
		scroll_y.config(command=self.identificaciones_table.yview)
		self.identificaciones_table.heading("ID", text="ID")
		self.identificaciones_table.heading("Responsable", text="Responsable")
		self.identificaciones_table.heading("Fecha", text="Fecha")
		self.identificaciones_table.heading("Clase", text="Clase")
		self.identificaciones_table.heading("Comentarios", text="Comentarios")
		self.identificaciones_table.heading("Imagenes", text="Imagenes")
		self.identificaciones_table.heading("Checkpoint", text="Checkpoint")
		self.identificaciones_table['show']= 'headings'
		self.identificaciones_table.column("ID", width=100)
		self.identificaciones_table.column("Responsable", width=100)
		self.identificaciones_table.column("Fecha", width=100)
		self.identificaciones_table.column("Clase", width=90)
		self.identificaciones_table.column("Comentarios", width=100)
		self.identificaciones_table.column("Imagenes", width=100)
		self.identificaciones_table.column("Checkpoint", width=100)
		self.identificaciones_table.pack(fill=BOTH,expand=1)



	def regresar(self):

		self.tipo_user = self.controlador.rescatarTipoUsuario()

		if self.tipo_user == 1:
			self.controlador.vistaExperimentacion_vistaMenuA()
		if self.tipo_user == 2:
			self.controlador.vistaExperimentacion_vistaMenuE()





	def abrir_archivo(self):
		responsable = str(self.responsable.get())
		fecha = str(self.cal.get())
		clase = str(self.clase.get())
		comentarios = str(self.txt_comentarios.get("0.0", "end"))
		imagenes = str(self.cantidadImagenes.get())
		print(responsable, fecha, clase, comentarios)
		comentarios = comentarios[:-1]

		if (responsable == "" or responsable.isspace()) or (fecha == "") or (clase == "" or clase.isspace()) or (comentarios == "" or comentarios.isspace()) or (imagenes == "" or imagenes.isspace()):
			tkinter.messagebox.showerror("Alerta", "Ingrese todos los datos")

		else:
			self.responsable.set("")
			self.clase.set("")
			self.txt_comentarios.delete("0.0", "end")
			self.cantidadImagenes.set("")
			respuesta = tkinter.messagebox.askquestion(message="Se borraran los archivos actuales para la identificación ¿Desea continuar?", title="Título")

			if respuesta == "yes":
				self.controlador.comenzar_entrenamiento(responsable, fecha, clase, comentarios, imagenes)
			else:
				tkinter.messagebox.showinfo(message="Operacion cancelada", title="Título")



	def mostrar(self):
		datos = self.controlador.consultaReportesExperimentacion()
		self.identificaciones_table.delete(*self.identificaciones_table.get_children())
		i = -1
		for dato in datos:
			i = i + 1
			self.identificaciones_table.insert('',END,values=dato)


	def clear(self):
		self.matricula_var.set("")
		self.nombre_var.set("")
		self.email_var.set("")
		self.genero_var.set("")
		self.telefono_var.set("")
		self.fdn_var.set("")
		self.txt_direccion.delete("1.0",END)




