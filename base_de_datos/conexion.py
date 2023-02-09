#Instalar mysql-connector en la terminal correr la siguiente linea que se encuentra comentada
# pip install mysql-connector 
import mysql.connector

def conexion():
    conexion1 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="emeneses_py")
    return conexion1

def conexion1():
    conexion1 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="")
    return conexion1
