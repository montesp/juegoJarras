class Jarras:
    def __init__(self, estado_inicial):
        self.estado_inicial = estado_inicial
        self.reglas = list()

    # Arregla las reglas
    def addReglas(self, rule):
        self.reglas.append(rule)
    
    # Devuelve las reglas
    def getReglas(self):
        return self.reglas

    # Esta funcion va a determinar las funciones que va a tener nuestro programa
    def acciones(self,estado):
        jarra_de_4=estado[0]
        jarra_de_3=estado[1]

        if jarra_de_3 < 3 and jarra_de_3 != 2 :
            return "llenar jarra de 3"
        elif jarra_de_4 == 4 and jarra_de_3 == 2:
            return "vaciar jarra de 4"
        elif jarra_de_4 < 4 and jarra_de_3 > 0:
            return "jarra de 3 a jarra de 4"
        elif jarra_de_4 > 0 and jarra_de_3 < 3:
            return "jarra de 4 a jarra de 3"
        else:
            return "vaciar jarra de 4"



    # Esta funcion aplica las diferentes reglas que se pueden aplicar con nuestro elementos de la tabla
    def aplica(self,estado,accion):
        j4=estado[0]
        j3=estado[1]
        if accion=="llenar jarra de 4":
            self.addReglas("Regla 1")
            return (4,j3)
        elif accion=="llenar jarra de 3":
            self.addReglas("Regla 2")
            return (j4,3)
        elif accion=="vaciar jarra de 4":
            self.addReglas("Regla 5")
            return (0,j3)
        elif accion=="vaciar jarra de 3":
            self.addReglas("Regla 6")
            return (j4,0)
        elif accion=="jarra de 4 a jarra de 3":
            if j3 + j4 >= 3:
                self.addReglas("Regla 8")
                return (j4-3+j3,3)
            else:
                self.addReglas("Regla 10")
                return (0,j3+j4)
        else: #  "jarra de 3 a jarra de 4"
            if j3 + j4 <= 4:
                self.addReglas("Regla 9")
                return (j3+j4,0)
            else:
                self.addReglas("Regla 7")
                return (4,j3-4+j4)


    def es_estado_final(self,estado):
        # Manda un booleano de vuelta para comprobar que este funcionando\
        return estado[0]==2