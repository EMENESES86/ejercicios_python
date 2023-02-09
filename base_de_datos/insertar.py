#Ejecutar este progrma para insertar datos en la tabla user
from conexion import conexion #Se esta llamando a la funcion que contiene la cadena de conexion
conexion1=conexion()

cursor1=conexion1.cursor()
sql="insert into user(name, lastname, cedula, email) values (%s,%s,%s,%s)"
datos=("EMENESES","EMENESES", 'XXXXXXXXXX','emeneses@emenesesdevelopers.com')
cursor1.execute(sql, datos)
datos=("qqqqqq","qqqqqq",1111111111,'ejemplo@ejemplo.com')
cursor1.execute(sql, datos)
datos=("eeeeeee","eeeeee", 2222222222,'ejemplo1@ejemplo.com')
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 