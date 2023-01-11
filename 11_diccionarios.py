#Ing. Edison Meneses MSc.
#Ingeniero en Sistemas de Información
#Magister en Sistemas de Información mensión inteligencia de negocios y analítica de datos masivos
#tutorias@emenesesdevelopers.com


#Un diccionario es una colección de pares formados por una clave y un valor asociado a la clave.

#---------------------------EJEMPLO-----------------------------
# a = {'nombre':'EDISON', 'carrera': 'SOFTWARE', 'email':'tutorias@emenesesdevelopers.com','año':2023}

# print("****************************")
# print(a['nombre'])
# print(a['carrera'])
# print(a['email'])
# print(a['año'])

# print("****************************")
# print(a.get('carrera'))
# print(a.get('universidad','ISUS'))



#---------------------------EJEMPLO-----------------------------
# a = {'nombre':'EDISON', 'carrera': 'SOFTWARE', 'email':'tutorias@emenesesdevelopers.com','año':2023}
# print(len(a))
# print(min(a))#Devuelve la minima clave de un diccionario siempre y cuando sean comparables
# print(a.keys())#Devuelve las claves de un diccionario
# print(a.values())#Devuelve los valores que toman cada clave de un diccionario
# print(a.items())#Devuele los pares de clave-valor de un diccionario

#---------------------------EJEMPLO-----------------------------
# a = {'nombre':'EDISON', 'carrera': 'SOFTWARE', 'email':'tutorias@emenesesdevelopers.com','año':2023}
# a['universidad']='ISUS' #Agrega una clave-valor al diccionario
# print(a)

# a.pop('carrera') #Elimina la clave-valor del diccionario
# print(a)

# a.clear()#Elimina toda el contenido del diccionario
# print(a)



#---------------------------EJEMPLO-----------------------------
# a = {'nombre':'EDISON', 'carrera': 'SOFTWARE', 'email':'tutorias@emenesesdevelopers.com','año':2023}
# for valor in a:
#     print(a[valor])
    
# for clave in a:
#     print(clave)

# for valor in a.values():
#     print(valor)

# for clave, valor in a.items():
#     print('La clave es: ',clave, 'y su valor: ',valor)