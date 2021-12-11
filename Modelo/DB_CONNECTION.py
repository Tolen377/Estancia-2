# _*_ coding:utf-8 _*_
import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='Tolentino',
            password='elseptimohokague377',
            db='estancia_DB'
        )

        self.cursor = self.connection.cursor()
        print("Conecxion establecida!")




    def getCursor(self):
        return self.cursor


    def getConnection(self):
        return self.connection


    def close(self):
        self.connection.close()

