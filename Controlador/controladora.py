from tkinter import *
from Vista.VistaLogin import Login
from Vista.VistaGestionUsuarios import Ventana
from Modelo.logica import Logica
from Vista.VistaMenuAdmin import MenuAdministrador
from Vista.VistaFormulario import Evaluacion
from Vista.VistaExperimentacion import Experimentacion
from Vista.VistaMenuEvaluador import MenuEvaluador




class Controladora:
    def __init__(self):

        #Logica
        self.logica = Logica()


        #Creacion de ventana raiz(Login)
        self.root = Tk()
        self.root.config(bg='darkorange')
        self.root.geometry('350x500+500+50')
        self.root.overrideredirect(1)
        self.root.resizable(0, 0)
        self.vistaLogin = Login(self.root,self)


        # Creacion de menu para administradores
        self.ventanaMenuA = Toplevel()
        self.ventanaMenuA.title('')
        self.ventanaMenuA.config(bg="gray17")
        self.ventanaMenuA.geometry("400x600+850+50")
        self.ventanaMenuA.overrideredirect(1)
        self.vistaMenuA = MenuAdministrador(self.ventanaMenuA,self)
        self.vistaMenuA.master.withdraw()


        #Creacion de ventana par a la gestion de usuarios
        self.ventanaGestionU = Toplevel()
        self.ventanaGestionU.title('')
        self.ventanaGestionU.minsize(height=475, width=795)
        self.ventanaGestionU.geometry('1000x500+180+80')
        self.ventanaGestionU.overrideredirect(1)
        self.vistaGestioU = Ventana(self.ventanaGestionU,self)
        self.vistaGestioU.master.withdraw()


        #Creacion de ventana de evaluacion
        self.ventanaEvaluacion = Toplevel()
        self.ventanaEvaluacion.geometry("1370x750+00+0")
        self.ventanaEvaluacion.config(bg="gray17")
        self.ventanaEvaluacion.resizable(0, 0)
        self.ventanaEvaluacion.overrideredirect(1)
        self.vistaEvaluacion = Evaluacion(self.ventanaEvaluacion,self)
        self.vistaEvaluacion.master.withdraw()


        #Creacion de ventana experimentacion
        self.ventanaExperimentacion = Toplevel()
        self.ventanaExperimentacion.geometry("1370x785+00+0")
        self.ventanaExperimentacion.config(bg="gray17")
        self.ventanaExperimentacion.resizable(0, 0)
        self.ventanaExperimentacion.overrideredirect(1)
        self.vistaExperimentacion = Experimentacion(self.ventanaExperimentacion,self)
        self.vistaExperimentacion.master.withdraw()


        #Creacion menu para evaluadores
        self.ventanaMenuE = Toplevel()
        self.ventanaMenuE.title('')
        self.ventanaMenuE.config(bg="gray17")
        self.ventanaMenuE.geometry("400x600+850+50")
        self.ventanaMenuE.overrideredirect(1)
        self.vistaMenuE = MenuEvaluador(self.ventanaMenuE, self)
        self.vistaMenuE.master.withdraw()






    #Correr ventana raiz login
    def run(self):
        self.vistaLogin.mainloop()


    #Gestion de vistas y logica------------------------------


    def VistaLoging_VistaGestionU(self):
        self.vistaLogin.master.withdraw()
        self.vistaGestioU.master.deiconify()


    def VistaGestionU_VistaLogin(self):
        self.vistaGestioU.master.withdraw()
        self.vistaLogin.master.deiconify()


    def insertarUsuario(self,nombre,correo,contrasena):
        self.logica.insertarUsuario(nombre,correo,contrasena)


    def consultarGeneralUsuario(self):
        return self.logica.consultarGeneralUsuario()


    def select_user(self, nombre):
        return self.logica.select_user(nombre)


    def select_password(self,password):
        return self.logica.select_password(password)


    def eliminarUsuario(self, nombre):
        self.logica.eliminarUsuario(nombre)


    def rescatarNombreUsuario(self):
        return self.vistaLogin.name_user


    def rescatarTipoUsuario(self):
        return self.vistaLogin.tipo_user


    def VistaLogin_VistaMenuA(self):
        self.vistaLogin.master.withdraw()
        self.vistaMenuA.master.deiconify()


    def VistaMenuA_VistaLogin(self):
        self.vistaMenuA.master.withdraw()
        self.vistaLogin.master.deiconify()


    def VistaMenuA_VistaGestionU(self):
        self.vistaMenuA.master.withdraw()
        self.vistaGestioU.master.deiconify()


    def vistaGestionU_VistaMenuA(self):
        self.vistaGestioU.master.withdraw()
        self.vistaMenuA.master.deiconify()


    def VistaMenuA_VistaEvaluacion(self):
        self.vistaMenuA.master.withdraw()
        self.vistaEvaluacion.master.deiconify()


    def vistaEvaluacion_vistaMenuA(self):
        self.vistaEvaluacion.master.withdraw()
        self.vistaMenuA.master.deiconify()


    def comenzar_identificacion(self, nombreDir,responsable,fecha,clase,comentarios,checkpoint):
        self.logica.comenzar_identificacion(nombreDir,responsable,fecha,clase,comentarios,checkpoint)


    def consultarReportesEvaluaciones(self):
        return self.logica.consultarReportesEvaluaciones()


    def update_user(self,nombre,correo,contrasena):
        self.logica.update_user(nombre,correo,contrasena)


    def vistaMenuA_vistaExperimentacion(self):
        self.vistaMenuA.master.withdraw()
        self.vistaExperimentacion.master.deiconify()


    def vistaExperimentacion_vistaMenuA(self):
        self.vistaExperimentacion.master.withdraw()
        self.vistaMenuA.master.deiconify()


    def consultaReportesExperimentacion(self):
        return self.logica.consultaReportesExperimentacion()


    def comenzar_entrenamiento(self, responsable, fecha, clase, comentarios, cantidadImagenes):
        self.logica.comenzar_entrenamiento(responsable,fecha,clase,comentarios,cantidadImagenes)


    #----------------------------------->
    def vistaLogin_vistaMenuE(self):
        self.vistaLogin.master.withdraw()
        self.vistaMenuE.master.deiconify()


    def vistaMenuE_vistaLogin(self):
        self.vistaMenuE.master.withdraw()
        self.vistaLogin.master.deiconify()


    def vistaMenuE_vistaEvaluacion(self):
        self.vistaMenuE.master.withdraw()
        self.vistaEvaluacion.master.deiconify()


    def vistaEvaluacion_vistaMenuE(self):
        self.vistaEvaluacion.master.withdraw()
        self.vistaMenuE.master.deiconify()


    def vistaMenuE_vistaExperimentacion(self):
        self.vistaMenuE.master.withdraw()
        self.vistaExperimentacion.master.deiconify()


    def vistaExperimentacion_vistaMenuE(self):
        self.vistaExperimentacion.master.withdraw()
        self.vistaMenuE.master.deiconify()

    def consultaEspecificaEval(self,nombre):
        return self.logica.consultaEspecificaEval(nombre)


    def verificarUser(self, nombre):
        return self.logica.verificarUser(nombre)


    def verificarCorreo(self, correo):
        return self.logica.verificarCorreo(correo)










