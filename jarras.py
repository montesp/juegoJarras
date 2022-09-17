import random

def main():
    jarras = list()
    # Llenado de jarras
    # Las jarras llenan en 0
    # Jarra 4L
    jarras.append(0)
    # Jarra 3L
    jarras.append(0)

    # Funcion recursiva que cumple el objetivo
    llenadoJarra(jarras)

# Esta funcion hace que la jarra se llenen
def llenadoJarra(jarra):
    meta = 2
    # Jarra 4L = Jarra[0] x
    # Jarra 3L = Jarra[1] y
    # Paso 1
    if jarra[0] < 4:
        jarra[0] = 4
    # Paso 2
    elif jarra[1] < 3:
        jarra[1] = 3

    # Paso 5
    elif jarra[0] > 0 :
        jarra[0] = 0
    # Paso 7
    elif jarra[0] + jarra[1] >= 4 and jarra[1] > 0:
        jarra[1] = jarra[1] - (4 - jarra[0])
    # Paso 8
    elif jarra[0] + jarra[1] >= 3 and jarra[0] > 0:
        jarra[0] = jarra[1] - (4 - jarra[0])
    # Paso 9
    elif jarra[0] + jarra[1] <= 4 and jarra[1] > 0:
        jarra[0] = jarra[0] + jarra[1]
        jarra[1] = 0
    # Paso 10
    elif jarra[0] + jarra[1] <= 3 and jarra[0] > 0:
        jarra[0]= 0
        jarra[1] = jarra[0] + jarra[1]
        


    print("[" + str(jarra[0]) + ", " + str(jarra[1]) + "]")

    # Este if termina el loop
    if jarra[0] == meta or jarra[1] == meta:
        print('end')
    else:
        llenadoJarra(jarra)


    

# Main para correr el programa
if __name__ == "__main__":
    main()