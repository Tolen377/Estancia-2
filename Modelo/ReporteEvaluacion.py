from Modelo.DB_CONNECTION import DataBase



class ReporteEvaluacion:
    def __init__(self):
        self.coneccion = DataBase();


    def insertar(self, responsable, fecha, clase, comentarios,identificaciones,rutaVideo):
        sql = "INSERT INTO reporteEvaluacion(responsable,fecha,clase,comentarios,identificaciones,rutaVideo) VALUES (%s,%s,%s,%s,%s,%s)"
        datos = (responsable,fecha,clase,comentarios,identificaciones,rutaVideo)

        try:
            self.coneccion.getCursor().execute(sql,datos)
            self.coneccion.getConnection().commit()

        except Exception as e:
            raise


    def consultaGeneral(self):
        sql = 'SELECT * FROM reporteEvaluacion'
        try:
            self.coneccion.getCursor().execute(sql)
            data = self.coneccion.getCursor().fetchall()
            return data

        except Exception as e:
            raise



    def consultaEspecifica(self,nombre):
        sql = 'SELECT * FROM reporteEvaluacion WHERE responsable=%s'

        try:
            self.coneccion.getCursor().execute(sql,nombre)
            eval = self.coneccion.getCursor().fetchall()
            return eval
        except Exception as e:
            raise





    def close(self):
        self.connection.close()



