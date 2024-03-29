#Ing. Edison Meneses MSc.
#Ingeniero en Sistemas de Información
#Magister en Sistemas de Información Mención en Inteligencia de Negocios y Analítica Datos Masivos
#tutorias@emenesesdevelopers.com

#Ejercicio de funciones


#Funciones (def)

#Una función es un bloque de código asociado un nombre, de manera que cada vez que se quiera ejecutar el bloque de código basta con invocar el nombre de la función.


#---------------------------EJEMPLO-----------------------------
# print("***Estructura de una función***")
# def emeneses(): #función 
#     print("Hola Edison como estas") #bloque de código que se ejecutara cuando se invoque la función
# emeneses() #Invocación de la función
# print("\n")

#---------------------------EJEMPLO-----------------------------
# print("***Parámetros y argumentos de una función***")
# def funcion(nombre):
#     print("Estamos estudiando Python", nombre)
# funcion("Edison")
# print("\n")

#---------------------------EJEMPLO-----------------------------
## Los argumentos se pueden pasar de dos formas:
## Argumentos posicionales: Se asocian a los parámetros de la función en el mismo orden que aparecen en la definición de la función.
## Argumentos nominales: Se indica explícitamente el nombre del parámetro al que se asocia un argumento de la forma parametro = argumento.
# print("***Paso de argumentos a una función***")
# def datos(nombre, apellido):
#     print("Estamos estudiando Python", nombre, apellido)
# datos("Edison","Meneses")# Argumentos posicionales
# datos(nombre="Edison",apellido="Meneses")# Argumentos nominales
# print("\n")


#---------------------------EJEMPLO-----------------------------
# print("***Retorno de una función***")
# def area_triangulo(base, altura):
#     calc=base*altura/2
#     print(calc)
# area_triangulo(2,3)#Ejemplo 1 con diferentes datos de base y altura
# area_triangulo(4,5)#Ejemplo 1 con diferentes datos de base y altura
# print("\n")

# ---------------------------EJEMPLO-----------------------------
# print("***Argumentos por defecto***")
# def welcome(nombre, lenguaje = 'Python'):
#     print('¡Bienvenido a', lenguaje, nombre + '!')
# welcome("EMENESES")#Ejemplo con los datos originales de la función
# welcome("EMENESES","PHP")#ejemplo con cambio de datos en el lenguaje de la función
# #NOTA:Los parámetros con un argumento por defecto deben indicarse después de los parámetros sin argumentos por defectos. De lo contrario se produce un error.
# print("\n")

#---------------------------EJEMPLO-----------------------------
# print("***Pasar un número indeterminado de argumentos***")
# #*parametro: Se antepone un asterisco al nombre del parámetro y en la invocación de la función se pasa el número variable de argumentos separados por comas.
# def menu(*platos):
#     print('Hoy tenemos: ', end='')
#     for plato in platos:
#         print(plato, end=', ')
# menu('pasta', 'pizza', 'ensalada')
# print("\n")

#---------------------------EJEMPLO-----------------------------
# #**parametro: Se anteponen dos asteriscos al nombre del parámetro y en la invocación de la función se pasa el número variable de argumentos por pares nombre = valor, separados por comas.
# def contacto(**info):
#     print("Datos del contacto")
#     for clave, valor in info.items():
#         print(clave, ":", valor)
# contacto(Nombre = "EMENESES", Email = "emeneses@tecnologicosucre.edu.ec")
# print("\n")
# contacto(Nombre = "EMENESES", Email = "emeneses@tecnologicosucre.edu.ec", Dirección = "Quito-Ecuador")
# print("\n")

#---------------------------EJEMPLO-----------------------------
# print("***Paso de argumentos por asignación***")
# primer_curso = ['POO II', 'APP']#Lista
# def añade_asignatura(curso, asignatura):
#     curso.append(asignatura)
# añade_asignatura(primer_curso, 'WEB')
# print(primer_curso)
# print("\n")

#---------------------------EJEMPLO-----------------------------
# print("***Las funciones son objetos***")
# #OJO OJO OJO OJO
# #En Python las funciones son objetos como el resto de tipos de datos, de manera que es posible asignar una función a una variable y luego utilizar la variable para hacer la llamada a la función.
# def saludo(nombre):
#     print("Hola como estas", nombre)
#     return
# bienvenida = saludo #asignar una función a una variable y luego utilizar la variable para hacer la llamada a la función
# bienvenida("EMENESES")
# print("\n")

#---------------------------EJEMPLO-----------------------------
# print("***Funciones recursivas***")
# def cuenta_regresiva(numero):
#     numero -= 1
#     if numero > 0:
#         print (numero)
#         cuenta_regresiva(numero)
#     else:
#         print ("Boooooooom!")
#     print ("Fin de la función", numero)
# cuenta_regresiva(5)
# print("\n")

#---------------------------EJEMPLO-----------------------------
# print("***Función recursiva con retorno***")
# #Es el ejemplo del calculo del factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número. Es el ejemplo con retorno más utilizado para mostrar la utilidad de este tipo de funciones:
# def factorial(numero):
#     print ("Valor inicial ->",numero)
#     if numero > 1:
#         numero = numero * factorial(numero -1)
#     print ("valor final ->",numero)
#     return numero
# print (factorial(5))

#---------------------------EJEMPLO-----------------------------
# def sum():
#     suma=5+6
#     print("La suma es",suma)
# sum()

#---------------------------EJEMPLO-----------------------------
# def cuadrado():
#     c=6**2
#     print("El área",c)
# cuadrado()

#---------------------------EJEMPLO-----------------------------
#Una clase en Python es un plano para crear objetos. Proporciona una estructura que define las propiedades y comportamientos de los objetos que se van a crear a partir de ella.
# El método __init__ generalmente se centran en la creación de clases y la inicialización de atributos al momento de instanciar un objeto.

# class Persona:
#     def __init__(self, nombre, edad, ocupacion):
#         self.nombre = nombre
#         self.edad = edad
#         self.ocupacion = ocupacion

#     def descripcion(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"

# # Creamos objetos de tipo Persona
# persona1 = Persona("Juan", 30, "Ingeniero")
# persona2 = Persona("María", 25, "Doctora")

# # Mostramos la descripción de cada persona
# print(persona1.descripcion())
# print(persona2.descripcion())

#---------------------------EJEMPLO-----------------------------
# class Persona:
#     def __init__(self, nombre, edad, ocupacion):
#         self.nombre = nombre
#         self.edad = edad
#         self.ocupacion = ocupacion

#     def descripcion(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"

# # Pedimos al usuario que ingrese información para crear objetos Persona
# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# ocupacion = input("Ingresa tu ocupación: ")

# # Creamos un objeto de tipo Persona con la información proporcionada por el usuario
# nueva_persona = Persona(nombre, edad, ocupacion)

# # Mostramos la descripción de la persona creada
# print("\nInformación de la persona creada:")
# print(nueva_persona.descripcion())


#---------------------------EJEMPLO-----------------------------
# Este programa permite:

# Agregar personas a una lista.
# Mostrar todas las personas en la lista.
# Buscar una persona por su nombre en la lista.
# Salir del programa.
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"


def mostrar_menu():
    print("\n--- Gestión de Personas ---")
    print("1. Agregar persona")
    print("2. Mostrar todas las personas")
    print("3. Buscar persona por nombre")
    print("4. Salir")


personas = []

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        ocupacion = input("Ingrese la ocupación de la persona: ")
        nueva_persona = Persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(f"La persona '{nombre}' ha sido agregada.")

    elif opcion == "2":
        if len(personas) > 0:
            print("\n--- Lista de Personas ---")
            for persona in personas:
                print(persona.descripcion())
        else:
            print("No hay personas en la lista.")

    elif opcion == "3":
        if len(personas) > 0:
            nombre_buscar = input("Ingrese el nombre de la persona a buscar: ")
            encontrada = False
            for persona in personas:
                if persona.nombre.lower() == nombre_buscar.lower():
                    print("Persona encontrada:")
                    print(persona.descripcion())
                    encontrada = True
                    break
            if not encontrada:
                print(f"No se encontró a '{nombre_buscar}' en la lista.")
        else:
            print("No hay personas en la lista.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


