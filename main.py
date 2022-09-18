""""
    Pavel Ivan Montes Bissio,
    Ivan Fernando Garcia Olvera,
    Jesús Manuel Lozoya Morales;
    18 / sep / 2022
    Titulo: ProblemaDeJarras

    Hay 2 jarras una de 3 litros y una de 4 litros, el objetivo del programa
    sera que la jarra de 4 litros llegue a tener 2 litros. Aunque las jarras solo se pueden vaciar completamente, llenar completamente o llenar la otra jarra con el espacio disponible
"""

from jarras import *

def main():
    estados = list()
    jarra3LInicio = None
    jarra4LInicio = None
    # Esta loop sirve para poder ingresar los datos hasta que esten correctos
    while True:
        # Para que el usuario pueda ingresar los datos de la jarra de 3L
        jarra3LInicio = int(input("Ingresa el valor de la jarra de 3L, (no es valido el 2): "))
        # Para que el usuario pueda ingresar los datos de la jarra de 4L
        jarra4LInicio = int(input("Ingresa el valor de la jarra de 4L, (no es valido el 2): "))

        if jarra3LInicio != 2 and jarra4LInicio != 2 and jarra4LInicio >= 0 and jarra4LInicio <= 4 and jarra3LInicio >= 0 and jarra3LInicio <= 3:
            break
    
        print("No se posible esa cantidad, ingresa de nuevo")

    # Este va a ser nuestro estado inicial
    estado = (jarra3LInicio, jarra4LInicio) #El estado inicial
    jarras = Jarras(estado)
    accion = None
    # Estados guardara todos los procedimientos por los que va a pasar el problema
    estados.append(estado)

    # Es un bucle infinito que se repite hasta que la jarra de 4 sea de 2 litros
    while not jarras.es_estado_final(estado):
        accion = jarras.acciones(estado)
        estado = jarras.aplica(estado, accion)
        estados.append(estado)
    # Muestra los estados por lo que paso el programa
    print(estados)
    # Muestra las reglas
    print(jarras.getReglas())

    
# Para correr el programa
if __name__ == "__main__":
    main()