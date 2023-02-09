#Ejecutar este progrma para consultar los datos de la tabla user
from conexion import conexion #Se esta llamando a la funcion que contiene la cadena de conexion
conexion1=conexion()
cursor1=conexion1.cursor()
cursor1.execute("select name, lastname, cedula,email from user")
for fila in cursor1:
    print(fila)
conexion1.close() 