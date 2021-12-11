from Modelo.DB_CONNECTION import DataBase


class Usuario:
    def __init__(self):
        self.coneccion = DataBase();

    def insertar(self, nombre, correo, contrasena):
        sql = "INSERT INTO usuario VALUES (%s,%s,%s,%s)"
        datos = (nombre, correo, contrasena, 2)

        try:
            self.coneccion.getCursor().execute(sql,datos)
            self.coneccion.getConnection().commit()

        except Exception as e:
            raise


    def consultaGeneral(self):
        sql = 'SELECT * FROM usuario'
        try:
            self.coneccion.getCursor().execute(sql)
            users = self.coneccion.getCursor().fetchall()
            return users

        except Exception as e:
            raise


    def select_user(self, nombre):
        sql = 'SELECT * FROM usuario WHERE nombre_usuario=%s'

        try:
            self.coneccion.getCursor().execute(sql,nombre)
            user = self.coneccion.getCursor().fetchall()
            return user
        except Exception as e:
            raise


    def select_password(self, password):
        sql = 'SELECT * FROM usuario WHERE contraseña=%s'

        try:
            self.coneccion.getCursor().execute(sql,password)
            user = self.coneccion.getCursor().fetchall()
            return user

        except Exception as e:
            raise




    def eliminar(self,nombre):
        sql="DELETE FROM usuario WHERE nombre_usuario=%s"

        try:
            self.coneccion.getCursor().execute(sql, nombre)
            self.coneccion.getConnection().commit()

        except Exception as e:
            raise


    def update_user(self,nombre,correo,contrasena):
        sql = "UPDATE usuario SET correo='{}', contraseña='{}' WHERE nombre_usuario='{}'".format(correo,contrasena,nombre)

        try:
            self.coneccion.getCursor().execute(sql)
            self.coneccion.getConnection().commit()
        except Exception as e:
            raise




    def select_correo(self, correo):
        sql = 'SELECT * FROM usuario WHERE correo=%s'

        try:
            self.coneccion.getCursor().execute(sql, correo)
            user = self.coneccion.getCursor().fetchall()
            return user

        except Exception as e:
            raise




    def close(self):
        self.connection.close()
