#Ejecutar este progrma para mostrar las tablas de la base de datos llamada emenes_py 
from conexion import conexion #Se esta llamando a la funcion que contiene la cadena de conexion

conexion1=conexion()
cursor1 = conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()
