##############################################################
from random import randint
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = {nombre: detalles for nombre, detalles in platos.items()}
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def recibir_pedidos(self, clientes):
        # print(clientes)
        calificaciones = []
        
        for cliente in clientes:
            calificacion_pedido = sum(randint(1, 5) for _ in cliente.platos_preferidos) / len(cliente.platos_preferidos)
            calificaciones.append(calificacion_pedido)
        
        self.calificacion = sum(calificaciones) / len(calificaciones) if calificaciones else 0

### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        print("restaurante.py: ")
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("La picá del profe'", PLATOS_PRUEBA, [], [])
        print(un_restaurante.__dict__)
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
