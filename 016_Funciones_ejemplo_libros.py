# Este programa permite:

# Agregar libros a la biblioteca.
# Prestar un libro específico de la biblioteca.
# Devolver un libro prestado.
# Mostrar información sobre un libro en la biblioteca.
# Salir del programa.
# Se utiliza la clase Libro para representar cada libro con atributos como título, autor, género y estado de préstamo. El programa principal utiliza un bucle while y un menú para interactuar con el usuario, permitiendo así realizar diversas operaciones de gestión de la biblioteca.
class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.prestado = False  # Por defecto, el libro no está prestado

    def prestar_libro(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver_libro(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def informacion_libro(self):
        estado_prestamo = "prestado" if self.prestado else "disponible"
        return f"Libro: {self.titulo} - Autor: {self.autor} - Género: {self.genero} - Estado: {estado_prestamo}"


def mostrar_menu():
    print("\n--- Gestión de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar información de un libro")
    print("5. Salir")


biblioteca = []

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        nuevo_libro = Libro(titulo, autor, genero)
        biblioteca.append(nuevo_libro)
        print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

    elif opcion == "2":
        if len(biblioteca) > 0:
            titulo = input("Ingrese el título del libro a prestar: ")
            encontrado = False
            for libro in biblioteca:
                if libro.titulo.lower() == titulo.lower():
                    libro.prestar_libro()
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró el libro '{titulo}' en la biblioteca.")
        else:
            print("La biblioteca está vacía. No hay libros para prestar.")

    elif opcion == "3":
        if len(biblioteca) > 0:
            titulo = input("Ingrese el título del libro a devolver: ")
            encontrado = False
            for libro in biblioteca:
                if libro.titulo.lower() == titulo.lower():
                    libro.devolver_libro()
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró el libro '{titulo}' en la biblioteca.")
        else:
            print("La biblioteca está vacía. No hay libros para devolver.")

    elif opcion == "4":
        if len(biblioteca) > 0:
            titulo = input("Ingrese el título del libro a buscar: ")
            encontrado = False
            for libro in biblioteca:
                if libro.titulo.lower() == titulo.lower():
                    print(libro.informacion_libro())
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró el libro '{titulo}' en la biblioteca.")
        else:
            print("La biblioteca está vacía.")

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
