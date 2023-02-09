#Ejecutar este progrma para actualizar registros de la tabla user
from conexion import conexion #Se esta llamando a la funcion que contiene la cadena de conexion
cedula=input("Ingrese la cedula para actualizar el registro: ")
email=input("Ingrese el nuevo email: ")
conexion1=conexion()
cursor1=conexion1.cursor()
cursor1.execute("update user set email='%s' where cedula='%s'" %(email, cedula)) #actualizar
conexion1.commit()
cursor1.execute("select name, lastname, cedula, email from user")
for fila in cursor1:
    print(fila)
conexion1.close()