def main():
    count = 0
    # Jarra con capacidad de 3 litros
    jarra3L = 0
    # Jarra con capacidad de 4 litros
    jarra4L = 0

    # Corre el programa hasta que cumpla su meta
    while(True):
        jarra3L = jarra3L + 1
        comprobarLimiteJarra(jarra3L, 3)
        count = count + 1

        # Este if funciona para comprobar si alguna de las dos jarras tiene dos litros, deja 
        if jarra3L == 2 or jarra4L == 2:
            break

def llenadoJarra(jarra, tipoDeJarra):
    jarraLimite = comprobarLimiteJarra(jarra, tipoDeJarra)

    if jarra == 0:
        pass


    
# Comprueba que la jarra no exceda su limite y que no este abajo de 0 litros
def comprobarLimiteJarra(jarra, jarraLimite):
    if jarra <= jarraLimite and jarra >= 0:
        return jarra
    else:
        print("La jarra no esta en el limite")
        return jarraLimite

# Main para correr el programa
if __name__ == "__main__":
    main()