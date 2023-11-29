# 1. Ejercicio de cálculo de área de un triángulo usando la biblioteca math:
# Enunciado: Escribe un programa que calcule el área de un triángulo utilizando la fórmula de Herón. Utiliza la función sqrt de la biblioteca math para calcular la raíz cuadrada.
# Area = √(s(s-a)(s-b)(s-c))
# donde s representa el semiperímetro del triángulo (s = (a+b+c)/2), y a, byc representan las longitudes de sus lados.
# import math

# def calcular_area_triangulo(a, b, c):
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return area

# lado1 = float(input("Ingresa la longitud del primer lado: "))
# lado2 = float(input("Ingresa la longitud del segundo lado: "))
# lado3 = float(input("Ingresa la longitud del tercer lado: "))

# area_triangulo = calcular_area_triangulo(lado1, lado2, lado3)
# print(f"El área del triángulo es: {area_triangulo:.2f}")

#------------------------------------------------------------------------------------------

# 2. Ejercicio para mostrar la fecha actual usando la biblioteca datetime:
# Enunciado: Crea un programa que importe la biblioteca datetime y muestre la fecha y hora actuales.
# import datetime

# fecha_actual = datetime.datetime.now()
# print(f"La fecha y hora actual es: {fecha_actual}")

#------------------------------------------------------------------------------------------

# 3. Ejercicio para generar números aleatorios con la biblioteca random:
# Enunciado: Escribe un programa que utilice la biblioteca random para generar un número aleatorio entre un rango especificado por el usuario.
# import random

# limite_inferior = int(input("Ingresa el límite inferior del rango: "))
# limite_superior = int(input("Ingresa el límite superior del rango: "))

# numero_aleatorio = random.randint(limite_inferior, limite_superior)
# print(f"El número aleatorio generado es: {numero_aleatorio}")

#------------------------------------------------------------------------------------------

# 4. Ejercicio para trabajar con la biblioteca de manipulación de archivos:
# Enunciado: Escribe un programa que utilice la biblioteca os para listar todos los archivos y carpetas en el directorio actual.

# import os

# archivos_en_directorio = os.listdir()
# print("Archivos y carpetas en el directorio actual:")
# for archivo in archivos_en_directorio:
#     print(archivo)

#------------------------------------------------------------------------------------------
# 5. Ejercicio para trabajar con la biblioteca requests
# Vamos a realizar una solicitud GET a la API de JSONPlaceholder para obtener datos de usuarios. Aquí tienes un ejemplo:
# https://jsonplaceholder.typicode.com/users
# import requests

# url = 'https://jsonplaceholder.typicode.com/users'

# try:
#     respuesta = requests.get(url)

#     if respuesta.status_code == 200:
#         datos_usuarios = respuesta.json()

#         print("Direcciones de los usuarios:")
#         for usuario in datos_usuarios:
#             direccion = usuario['address']
#             print(f"Usuario: {usuario['name']}")
#             print(f"Email: {usuario['email']}")
#             print(f"Calle: {direccion['street']}")
#             print(f"Suite: {direccion['suite']}")
#             print(f"Ciudad: {direccion['city']}")
#             print(f"Código Postal: {direccion['zipcode']}")
#             print(f"Coordenadas (Latitud, Longitud): {direccion['geo']['lat']}, {direccion['geo']['lng']}")
#             print("\n")
#     else:
#         print(f"Error al obtener datos: Código de estado {respuesta.status_code}")

# except requests.RequestException as e:
#     print(f"Error de conexión: {e}")

