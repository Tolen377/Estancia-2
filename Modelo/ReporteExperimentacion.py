from Modelo.DB_CONNECTION import DataBase


class ReporteExperimentacion:
    def __init__(self):
        self.coneccion = DataBase();


    def insertar(self, responsable, fecha, clase, comentarios,cantidadImagenes,rutaCheckpoint):
        sql = "INSERT INTO reporteExperimentacion(responsable,fecha,clase,comentarios,cantidadImagenes,rutaCheckpoint) VALUES (%s,%s,%s,%s,%s,%s)"
        datos = (responsable,fecha,clase,comentarios,cantidadImagenes,rutaCheckpoint)

        try:
            self.coneccion.getCursor().execute(sql,datos)
            self.coneccion.getConnection().commit()

        except Exception as e:
            raise


    def consultaGeneral(self):
        sql = 'SELECT * FROM reporteExperimentacion'
        try:
            self.coneccion.getCursor().execute(sql)
            data = self.coneccion.getCursor().fetchall()
            return data

        except Exception as e:
            raise




    def close(self):
        self.connection.close()