#Ejecutar este progrma para mostrar las bases de datos que tengo en mi servidor
from conexion import conexion1 #Se esta llamando a la funcion que contiene la cadena de conexion1

conexion=conexion1()
cursor1=conexion.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion.close() 