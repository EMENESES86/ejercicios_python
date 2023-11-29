# Ing. Edison Meneses MSc.
# Ingeniero en Sistemas de Información
# Magister en Sistemas de Información Mención en Inteligencia de Negocios y Analítica Datos Masivos
# tutorias@emenesesdevelopers.com


# ---------------------------EJEMPLO-----------------------------
# my_list = [2, 5,"EMENESES" ,7, 'EMENESES', 1.2, 5]
# print("Append Agregamos elementos a la lista")
# my_list.append(10) #agregamos el elemento 10 a la lista
# my_list.append([2,5]) #cuando agregamos una lista dentro de otra, esta lista se agrega como uno y solo un elemento.
# print(my_list)

# ---------------------------EJEMPLO-----------------------------
# my_list = [2, 5,"EMENESES" ,7, 'EMENESES', 1.2, 5]
# print("\nExtend Agregamos elementos a la lista")
# my_list.extend([11,86]) #agregar una lista, cada elemento de esta lista se agrega como un elemento más dentro de la otra lista.
# print(my_list)

# ---------------------------EJEMPLO-----------------------------
# my_list = [2, 5,"EMENESES" ,7, 'EMENESES', 1.2, 5]
# print("\nEliminamos el elemento 5 de la lista")
# my_list.remove(5)
# print(my_list)

# ---------------------------EJEMPLO-----------------------------
# list=[1,5,6,8,4,2,5,4,5,6,5,8,5]
# print(len(list))
# print(list)
# i=0
# while i<=len(list):
#     if 5 in list:
#         list.remove(5)
#     i+=1
# print(list)

# my_list=[2,2,2,2,2,2,5,6,3,2,7,2]
# longitud=len(my_list)
# print("La longitud de la lista es: ",longitud)
# i=0
# while 2 in my_list:
#     my_list.remove(2)
#     i+=1
# print(my_list)

# ---------------------------EJEMPLO-----------------------------
# print("\n*** La posicion del elemento EM en la lista")
# my_list1 = [2, 5,"EMENESES" ,7, 'DEVELOPERS','EM', 1.2, 5]
# print(my_list1.index('EM'))


# ---------------------------EJEMPLO-----------------------------
# print("\nContamos cuantos elementos de la lista tienen el 5")
# my_list1 = [2, 5,"EMENESES" ,7, 'EMENESES','EMENESES', 1.2, 5]
# print(my_list1.count(5))

# ---------------------------EJEMPLO-----------------------------
# print("\n invertir los elementos de la lista")
# my_list1 = [2, 5,"EMENESES" ,7, 'EMENESES','EMENESES', 1.2, 5]
# my_list1.reverse()
# print(my_list1)

# ---------------------------EJEMPLO-----------------------------
# print("\nEjemplo de invertir lista")
# original_list = [1,2,3,4,5]
# print("Lista orden original : ",original_list)
# original_list.reverse()
# print("Lista de atras a adelante : ",original_list)

# ---------------------------EJEMPLO-----------------------------
# print("\nEjemplo de invertir lista")
# original_list = [1, 2, 3, 4, 5]
# print("Lista orden original : ", original_list)
# reversed_list = []
# for value in original_list:
#     reversed_list = [value] + reversed_list
# print("Lista de atras a adelante : ", reversed_list)

# ---------------------------EJEMPLO-----------------------------
# print("\nEjemplo ciclo while con lista")
# b = ['s', 'e', 's', 'e', 'n', 'e', 'm']
# reverseCharList = []
# while b:
#     reverseCharList.append(b.pop())
#     print(reverseCharList)

# ---------------------------EJEMPLO-----------------------------
# print("Separa una cadena de caracteres y agregar en una lista")
# nombre=input("Ingrese su nombre: ")
# lista=[]
# for item in nombre:
#     lista.append(item)
# print(lista)

# ---------------------------EJEMPLO-----------------------------
# print("\nEjemplo ciclo for con lista")
# my_list = ["apple", "banana", "cherry"]
# for index, item in enumerate(my_list):
#     print(index, item)


# ---------------------------EJEMPLO-----------------------------
# print("Obtener la suma de los números pares en una lista:")
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_of_evens = 0
# for item in my_list:
#     if item % 2 == 0:
#         sum_of_evens += item
# print(sum_of_evens)

# ---------------------------EJEMPLO-----------------------------
# print("Obtener una nueva lista con los elementos de otra lista elevados al cuadrado")
# my_list = [1, 2, 3, 4, 5]
# squared_list = [item**2 for item in my_list]
# print(squared_list)

# ---------------------------EJEMPLO-----------------------------
# print("Determinar si un número está en una lista")
# my_list = [1, 2, 3, 4, 5]
# number_to_find = 3
# found = False
# for item in my_list:
#     if item == number_to_find:
#         found = True
#         break
# if found:
#     print(f'{number_to_find} esta en la lista')
# else:
#     print(f'{number_to_find} no esta en la lista')

# ---------------------------EJEMPLO-----------------------------
# print("Determinar el mayor y el menor elemento en una lista")
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_item = my_list[0]
# max_item = my_list[0]
# for item in my_list:
#     if item < min_item:
#         min_item = item
#     if item > max_item:
#         max_item = item
# print(f'menor: {min_item}, mayor: {max_item}')

#----------------------------------
# l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

# # replace first value
# l[0] = 'Shardul'

# # print list
# print(l)

#----------------------------------
# # Replace Values in a List using Lambda Function
# # define list
# l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
# # replace Pant with Ishan
# l = list(map(lambda x: x.replace('Pant', 'Ishan'), l))
# # print list
# print(l)
