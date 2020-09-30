import random
import os


class TicTacToe:
    M = []

    def __init__(self):
        self.M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __show(self):
        for i in self.M:
            for j in i:
                if j == 0:
                    print
                    "_\t",
                elif j == 1:
                    print
                    "X\t",
                else:
                    print
                    "0\t",
            print

    def realPlayerTurn(self):
        i = int(input("Enter Row: "))
        j = int(input("Enter Column: "))
        if i > 2 or j > 2:
            print("----->Out of bounds!!!Please choose another location<-----")
            self.realPlayerTurn()
        elif self.M[i][j] == 0:
            self.M[i][j] = 1
        else:
            print("----->This location is already taken, Please choose another location<-----")

            self.realPlayerTurn()

    def iaTurn(self):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if self.M[i][j] == 0:
            self.M[i][j] = -1
        else:
            self.iaTurn()

    def verifyDraw(self):
        listaAux = []
        listaAux.extend(self.M[0])
        listaAux.extend(self.M[1])
        listaAux.extend(self.M[2])
        return listaAux.count(0)

    def countRow(selft, M, dato):
        return M[0].count(dato) == 3 or M[1].count(dato) == 3 or M[2].count(dato) == 3

    def mapRowColumn(self, a, b, c):
        x = []
        x.append(a)
        x.append(b)
        x.append(c)
        return x

    def verifyWinner(self):
        realPlayerWin = False
        iaPlayerWin = False

        # verify winner by rows
        realPlayerWin = self.countRow(self.M, 1)
        iaPlayerWin = self.countRow(self.M, -1)

        if realPlayerWin:
            print("----->Congrats!!! you win!!<-----")
            return True
        if iaPlayerWin:
            print("----->You lost!! better luck next time<-----")
            return True

        # verify columns
        matrixAux = list(map(self.mapRowColumn, self.M[0], self.M[1], self.M[2]))

        realPlayerWin = self.countRow(matrixAux, 1)
        iaPlayerWin = self.countRow(matrixAux, -1)

        if realPlayerWin:
            print("----->Congrats!!! you win!!<-----")

            return True
        if iaPlayerWin:
            print("----->You lost!! better luck next time<-----")
            return True

        # verify diagonals
        matrixAux = []
        listaCol = []
        for i in range(0, 3):
            listaCol.append(self.M[i][i])
        matrixAux.append(listaCol)

        listaCol = []
        for i in range(0, 3):
            listaCol.append(self.M[i][2 - i])
        matrixAux.append(listaCol)

        realPlayerWin = matrixAux[0].count(1) == 3 or matrixAux[1].count(1) == 3
        iaPlayerWin = matrixAux[0].count(-1) == 3 or matrixAux[1].count(-1) == 3

        if realPlayerWin:
            print("----->Congrats!!! you win!!<-----")
            return True
        if iaPlayerWin:
            print("----->You lost!! better luck next time<-----")
            return True

        # verify draw
        if self.verifyDraw() == 0:
            print("----->Draw!! try again<-----")
            return True

        return False

    def playrun(self):
        op = 0
        while True:
            os.system('clear')
            self.__show()

            if op % 2 == 0:
                self.realPlayerTurn()
            else:
                self.iaTurn()

            op += 1

            if self.verifyWinner():
                break

        print("=======> FINAL RESULT <=======")
        self.__show()
