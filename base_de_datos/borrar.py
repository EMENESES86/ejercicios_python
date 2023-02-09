#Ejecutar este progrma para borrar registros de la tabla user
from conexion import conexion #Se esta llamando a la funcion que contiene la cadena de conexion
borrar=int(input("Ingrese la cedula para borrar el registro: "))

conexion1=conexion()
cursor1=conexion1.cursor()
cursor1.execute("DELETE FROM user WHERE cedula = '%s'" % borrar)
conexion1.commit()
print(cursor1.rowcount, "record(s) affected")
conexion1.close() 
