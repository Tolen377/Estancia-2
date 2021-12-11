# _*_ coding:utf-8 _*_
from Modelo.Usuario import Usuario
from Modelo.ReporteEvaluacion import ReporteEvaluacion
from Modelo.ReporteExperimentacion import ReporteExperimentacion
import os
import glob
from os import remove
from os import path
from Modelo.Deteccion_video import deteccion_video
from Modelo.Etiquetado_entrenamiento import Etiquetado_entrenamiento
from tkinter import *




class Logica:
    def __init__(self):
        self.usuarioCRUD = Usuario()
        self.evaluacionCRUD = ReporteEvaluacion()
        self.experimentacionCRUD = ReporteExperimentacion()




    def insertarUsuario(self,nombre,correo,contrasena):
        self.usuarioCRUD.insertar(nombre,correo,contrasena)


    def consultarGeneralUsuario(self):
        return self.usuarioCRUD.consultaGeneral()


    def select_user(self, nombre):
        return self.usuarioCRUD.select_user(nombre)


    def select_password(self,password):
        return self.usuarioCRUD.select_password(password)


    def eliminarUsuario(self,nombre):
        self.usuarioCRUD.eliminar(nombre)


    def update_user(self,nombre,correo,contrasena):
        self.usuarioCRUD.update_user(nombre,correo,contrasena)



    def verificarCorreo(self,correo):
        correoE = self.usuarioCRUD.select_correo(correo)

        if len(correoE) == 0:
            return True
        else:
            return False



    def comenzar_identificacion(self,nombreDir,responsable,fecha,clase,comentarios,checkpoint):
        self.deteccion = deteccion_video(nombreDir,checkpoint)
        self.deteccion.main()
        identificaciones = self.deteccion.getIdentificaciones()
        rutaVideo = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.evaluacionCRUD.insertar(responsable,fecha,clase,comentarios,identificaciones,rutaVideo)


    def consultarReportesEvaluaciones(self):
        return self.evaluacionCRUD.consultaGeneral()


    def consultaEspecificaEval(self,nombre):
        return self.evaluacionCRUD.consultaEspecifica(nombre)


    def comenzar_entrenamiento(self,responsable,fecha,clase,comentarios,cantidadImagenes):
        self.entrenamiento = Etiquetado_entrenamiento()
        self.entrenamiento.Etiquetado()
        self.entrenamiento.Entrenamiento()
        rutaFinal = self.entrenamiento.getRutaFinal()
        self.experimentacionCRUD.insertar(responsable, fecha, clase, comentarios, cantidadImagenes, rutaFinal)


    def consultaReportesExperimentacion(self):
        return self.experimentacionCRUD.consultaGeneral()


    def verificarUser(self,nombre):
        users = self.usuarioCRUD.select_user(nombre)

        if len(users) == 0:
            return True
        else:
            return False




















