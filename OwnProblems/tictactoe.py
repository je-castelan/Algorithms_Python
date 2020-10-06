

class TickTackToe():
    
    def __init__(self,turno = 0):
        # Inicializa con quien va a empezar
        self.turno = turno # 0 o 1
        self.ganador = None
        self.matrix = [[None,None,None],[None,None,None],[None,None,None]]
    
    def movimiento(self, x, y):
        if self.ganador is None and self.matrix[x][y] is None:
            self.matrix[x][y] = 1 if self.turno == 1 else 0
            self.__validaGanador()
            self.turno = 1 if self.turno == 0 else 0
            ejecutado = True
            
        else:
            ejecutado = False
        return self.ganador, self.matrix, ejecutado

    def __validaGanador(self):
        if (
            ((self.matrix[0][0] == self.turno) and (self.matrix[0][1] == self.turno) and (self.matrix[0][2] == self.turno)) or
            ((self.matrix[1][0] == self.turno) and (self.matrix[1][1] == self.turno) and (self.matrix[1][2] == self.turno)) or
            ((self.matrix[2][0] == self.turno) and (self.matrix[2][1] == self.turno) and (self.matrix[2][2] == self.turno)) or
            ((self.matrix[0][0] == self.turno) and (self.matrix[1][0] == self.turno) and (self.matrix[2][0] == self.turno)) or
            ((self.matrix[0][1] == self.turno) and (self.matrix[1][1] == self.turno) and (self.matrix[2][1] == self.turno)) or
            ((self.matrix[0][2] == self.turno) and (self.matrix[1][2] == self.turno) and (self.matrix[2][2] == self.turno)) or
            ((self.matrix[0][0] == self.turno) and (self.matrix[1][1] == self.turno) and (self.matrix[2][2] == self.turno)) or
            ((self.matrix[0][2] == self.turno) and (self.matrix[1][1] == self.turno) and (self.matrix[2][0] == self.turno)) 
        ):
            self.ganador = self.turno



if __name__ == "__main__":
    gato = TickTackToe(1)
    ganador, matrix, ejecutado = gato.movimiento(1,1)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #1
    ganador, matrix, ejecutado = gato.movimiento(1,1)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #Este no sale
    ganador, matrix, ejecutado = gato.movimiento(1,2)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #0
    ganador, matrix, ejecutado = gato.movimiento(0,1)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #1
    ganador, matrix, ejecutado = gato.movimiento(2,1)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #0
    ganador, matrix, ejecutado = gato.movimiento(2,2)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #1
    ganador, matrix, ejecutado = gato.movimiento(2,0)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #0
    ganador, matrix, ejecutado = gato.movimiento(0,0)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #1 - gana
    ganador, matrix, ejecutado = gato.movimiento(0,2)
    print("{} - {} - {}".format(matrix,ganador,ejecutado)) #0 - no sale, ya hay ganador
