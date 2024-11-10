##############################################################
from random import randint, choice
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 1.1 ###
class Plato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calidad = randint(1, 10)  # Asigna calidad aleatoria

### FIN PARTE 1.1 ###

### INICIO PARTE 1.2 ###
class Bebestible(Plato):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tamano = choice(["Pequeño", "Mediano", "Grande"])  # Tamaño aleatorio

### FIN PARTE 1.2 ###

### INICIO PARTE 1.3 ###
class Comestible(Plato):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.dificultad = randint(1, 5)  # Dificultad aleatoria de preparación

### FIN PARTE 1.3 ###

if __name__ == "__main__":
    print("platos.py: ")

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        un_bebestible = Bebestible("Coca-Cola")
        un_comestible = Comestible("Sopa")
        print(f"Esto es una {un_bebestible.nombre} de tamaño {un_bebestible.tamano} y calidad {un_bebestible.calidad}.")
        print(f"Esto es una {un_comestible.nombre} de dificultad {un_comestible.dificultad} y calidad {un_comestible.calidad}.")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")