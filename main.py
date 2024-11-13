##############################################################
# from random import seed
from random import seed, randint, choice
from restaurante import Restaurante
from personas import Cocinero, Repartidor, Cliente
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 4 ###

def crear_repartidores(): 
    return [Repartidor(nombre=f"Repartidor_{i}", tiempo_entrega=randint(20, 30)) for i in range(2)]

def crear_cocineros(): 
    return [Cocinero(nombre=f"Cocinero_{i}", habilidad=randint(1, 10)) for i in range(5)]

def crear_clientes(): 
    cantidad_clientes = 5
    nombres = ["Cristian", "Antonio", "Francisca", "Juan", "Jorge", "Pablo", "Luis", "Sofia", "Macarena"]
    info_platos = ["Jugo Natural", "Empanadas", "Lomo a lo Pobre", "Papas Duqueza"]
    return [Cliente(nombre=choice(nombres), platos_preferidos=[choice(info_platos)]) for _ in range(cantidad_clientes)]

def crear_restaurante(): 
    info_platos = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Coca-Cola": ["Coca-Cola", "Bebestible"],
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Agua": ["Agua", "Bebestible"],
        
        "Papas Duquesa": ["Papas Duquesa", "Comestible"],
        "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        "Mariscos": ["Mariscos", "Comestible"],
    }

    cocineros = crear_cocineros()
    # print(len(cocineros))
    repartidores = crear_repartidores()
    # print(len(repartidores))
    return Restaurante("La picá del profe'", info_platos, cocineros, repartidores)

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Cristian", "Antonio", "Francisca", "Juan", "Jorge", "Pablo", "Luis", "Sofia", "Macarena"]

if __name__ == "__main__":
    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("DSP")
    restaurante = crear_restaurante()
    clientes = crear_clientes() 

    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) 
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
