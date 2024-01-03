# Definición de la clase base (padre)
class Vehiculo:
    def __init__(self, marca, modelo):  # Define el constructor de la clase Vehiculo con los atributos marca y modelo
        self.marca = marca  # Inicializa el atributo marca del vehículo
        self.modelo = modelo  # Inicializa el atributo modelo del vehículo

    def mostrar_info(self):  # Método para mostrar información del vehículo
        return f"Marca: {self.marca}, Modelo: {self.modelo}"  # Retorna la información de la marca y modelo del vehículo

# Definición de una clase derivada (hijo) que hereda de la clase Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):  # Define el constructor de la clase Coche con los atributos marca, modelo y color
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base Vehiculo para inicializar marca y modelo
        self.color = color  # Inicializa el atributo color del coche

    def mostrar_info(self):  # Sobrescribe el método mostrar_info() de la clase base Vehiculo para la clase Coche
        return f"Coche - {super().mostrar_info()}, Color: {self.color}"  # Retorna la información del coche con su color

# Creación de una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")  # Crea una instancia de la clase Coche con marca Toyota, modelo Corolla y color Rojo

# Accediendo a los métodos de las instancias
print(mi_coche.mostrar_info())  # Muestra la información del coche llamando al método mostrar_info() de la clase Coche
