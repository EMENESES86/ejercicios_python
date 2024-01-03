# La herencia en Python permite a una clase heredar atributos y métodos de otra clase. 
# En este ejemplo, Animal es la clase base que tiene un constructor para inicializar el nombre y la edad de un animal, así como un método hacer_sonido() que será implementado por las clases derivadas.

# Perro y Gato son clases que heredan de Animal. Tienen sus propios constructores para inicializar atributos específicos (raza para Perro y color para Gato) y sobrescriben el método hacer_sonido() para proporcionar el sonido respectivo de cada animal.

# Al crear instancias de Perro y Gato, se pueden acceder a sus atributos y métodos específicos, así como a los heredados de la clase base.

# Definición de la clase base (padre)
class Animal:
    def __init__(self, nombre, edad):  # Define el constructor de la clase Animal con atributos nombre y edad
        self.nombre = nombre  # Inicializa el atributo nombre del animal
        self.edad = edad  # Inicializa el atributo edad del animal

    def hacer_sonido(self):  # Método hacer_sonido que será implementado por las clases derivadas
        pass  # No hace nada en la clase base, se espera que se implemente en las clases derivadas

# Definición de una clase derivada (hijo) que hereda de la clase Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):  # Define el constructor de la clase Perro con atributos nombre, edad y raza
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base Animal
        self.raza = raza  # Inicializa el atributo raza específico de la clase Perro

    def hacer_sonido(self):  # Sobrescribe el método hacer_sonido de la clase base Animal para la clase Perro
        return "¡Guau!"  # Retorna el sonido característico de un perro

# Definición de otra clase derivada (hijo) que hereda de la clase Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):  # Define el constructor de la clase Gato con atributos nombre, edad y color
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base Animal
        self.color = color  # Inicializa el atributo color específico de la clase Gato

    def hacer_sonido(self):  # Sobrescribe el método hacer_sonido de la clase base Animal para la clase Gato
        return "¡Miau!"  # Retorna el sonido característico de un gato

# Creación de instancias de las clases derivadas
mi_perro = Perro("Bobby", 5, "Labrador")  # Crea una instancia de la clase Perro con nombre, edad y raza
mi_gato = Gato("Pelusa", 3, "Blanco")  # Crea una instancia de la clase Gato con nombre, edad y color

# Accediendo a los atributos y métodos de las instancias
print(f"{mi_perro.nombre} es un perro de raza {mi_perro.raza}. Dice: {mi_perro.hacer_sonido()}")  # Muestra información del perro y su sonido
print(f"{mi_gato.nombre} es un gato de color {mi_gato.color}. Dice: {mi_gato.hacer_sonido()}")  # Muestra información del gato y su sonido
