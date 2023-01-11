#Ing. Edison Meneses MSc.
#Ingeniero en Sistemas de Información
#Magister en Sistemas de Información Mención en Inteligencia de Negocios y Analítica Datos Masivos
#tutorias@emenesesdevelopers.com


#---------------------------EJEMPLO-----------------------------
# # Acceso a los elementos de una lista
# a=['E','M','E','N','E','S','E','S']
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])
# # print(a[8]) #Este valor no se encuentra en la lista
    
    
#---------------------------EJEMPLO-----------------------------
# Sublistas
# a=['E','M','E','N','E','S','E','S']
# print(a[1:5])
# print(a[:-5])
# print(a[:])

# print(a[0:7:2])#El primer valor es la posición de donde inicia el segundo hasta donde termina en posición el tercero es el salto que va a tene

#---------------------------EJEMPLO-----------------------------
# print("\nEjemplo de invertir lista")
# a=[1,2,3,4,5,6,2]
# b=[7,8,9]
# print(len(a),"len devuelve el número de elementos que tiene la lista")
# print(min(a),"min devuelve el número menor que existe en la lista")
# print(max(a),"max devuelve el número más alto que hay en la lista")
# print(sum(a),"sum devuelve la suma de todos los valores de la lista")
# print(a.index(3),"Devuelve la posición que toma el primer valor de la lista")
# print(a.count(2),"Cuenta la cantidad de coincidencias en la lista")
# c=a+b #Concatena las dos listas
# print(c)
# c.sort()#Ordena la lista
# print(c)


#---------------------------EJEMPLO-----------------------------
#Utilizando while e ingresando la longitud de la lista imprimir los elementos de la lista principal
# a=['E','M','E','N','E','S','E','S']
# print(len(a))
# i=0
# dato=int(input("Ingrese hasta que posición quiere imprimir: "))
# while i<=dato-1:
#     if dato<=len(a):
#         print(a[i])
#     else:
#         print("El valor es mayor a ",len(a))
#         break
#     i+=1

#---------------------------EJEMPLO-----------------------------
# inicio = True
# apellido = ["A","n","t","o","n","y"]
# n = int(input("Ingrese el limite del valor a imprimir"))
# while inicio:
    
#     if n <0 or n > len(apellido):
#         n = int(input("Ingrese el limite del valor a imprimir: "))
#     else:
#         for i in range(0, n):
#             print(apellido[i])
#         inicio = False

#---------------------------EJEMPLO-----------------------------
# i = 0
# tp = ('e','r','i','c','k')
# lis = []
# li = int(input('Ingrese el limite del rango : '))
# if li <= len(tp):
#     while i+1 <= li:
#         lis.append(tp[i])
#         i += 1
#         print(lis)
#     else:
#         print('Fin del proceso')
# else:
#     print('Invalido')

    
#---------------------------EJEMPLO-----------------------------
# lista = ['j','o','e','l']
# i=int(input('Indique el numero:'))
# j=0

# if i<=len(lista):
#     if j <= len(lista):
#         while j<i:
#             print(lista[j])
#             j+=1
# else:
#     print('Numero fuera de rango')

#---------------------------EJEMPLO-----------------------------
# a=['j','e','s','s','i','c','a','G','u','a','g','c','h','a']
# print("En su lista tiene ",(len(a)), "posiciones", 'la lista es: ',a)

# p=int(input("Hasta que posición quiere imprimir " ))
# i=0
# while i<p:
#     if p<=len(a):
#         print(a[i])
#     else:
#         print("el valor esta mal ")
#         break
#     i+=1 

#---------------------------EJEMPLO-----------------------------
# while True:
#     nombre = ("E","M","E","N","E","S","E","S")
#     num = int(input("Ingresar longitud a imprimir: "))

#     if  num <= len(nombre):
#         i = 0
#         while i < num:
#             print(nombre[i], end="")
#             i += 1
#         break
#     else:
#         print("ERROR: El valor supera la longitud del nombre.\n")
#         continue

#---------------------------EJEMPLO-----------------------------
# lista = ['E','S','T','E','B','A','N','S']

# i = 0

# print("Ingrese el rango que desea que se imprima de la lista")
# rango = int(input(""))

# if ((rango <= len(lista)) and (rango > 0)):
#     print("--------------------------")
#     while i <= (rango-1):
#         print(lista[i])
#         i = i+1

# else:
#     print("El rango ha excedido el largo de la lista o es menor que '0'")

