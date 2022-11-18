import sys
import re
import random as rd
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap,QRegion

class ejemplo_Gui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui",self)

        self.Entrada.textChanged.connect(self.validar)
        self.ejemplos.itemAt(0).widget().clicked.connect(self.inicial)
        self.ejemplos.itemAt(1).widget().clicked.connect(self.pastor)
        self.ejemplos.itemAt(2).widget().clicked.connect(self.reinaColor)
        self.ejemplos.itemAt(3).widget().clicked.connect(self.errorcito)

    global piezasPng
    piezasPng = ['bB.png', 'bK.png', 'bN.png', 'bP.png', 'bQ.png', 'bR.png', 'wB.png', 'wK.png', 'wN.png', 'wP.png',
                 'wQ.png', 'wR.png']
    global piezasLetra
    piezasLetra = ["b", "k", "n", "p", "q", "r", "B", "K", "N", "P", "Q", "R"]
    global imagenesCorrecto
    imagenesCorrecto=['a1 (1).png','a1 (2).png','a1 (3).png','a1 (4).png','a1 (5).png','a1 (6).png','a1 (7).png','a1 (8).png','a1 (9).png','a1 (10).png','b (1).png','b (2).png','b (3).png','b (4).png','b (5).png','b (6).png','b (7).png','b (8).png','b (9).png','b (10).png','b (11).png','ajedrecista.png']

    def inicial(self):
        self.Entrada.setText("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    def pastor(self):
        self.Entrada.setText("r1bqk1nr/pppp1Qpp/2n5/2b1p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    def reinaColor(self):
        self.Entrada.setText("QqQqQqQq/qQqQqQqQ/QqQqQqQq/qQqQqQqQ/QqQqQqQq/qQqQqQqQ/QqQqQqQq/qQqQqQqQ b - - 0 4")
    def errorcito(self):
        self.Entrada.setText("8/6.app/p1n2k2/1fp6/3N#P/1q6/5K2/8 s qk e6 51 1")

    def validar(self,text):
        global error
        error = ""

        validez = True

        def posi(n):
            for i in range(12):
                if piezasLetra[i] == n:
                    return i
            return 1

        def imprimirLineas(filas):
            for i in range(len(filas)):
                i + 2

        def validarFila(fila):
            global error
            piezas = "[KkQqRrBbNnPp]"
            numeros = "[1-8]"
            numsEnFila = re.findall(numeros, fila)
            sumaNumeros = 0
            for x in range(len(numsEnFila)):
                sumaNumeros += int(numsEnFila[x])
            fichasEnFila = re.findall(piezas, fila)
            cantCasillasValidas = sumaNumeros + len(fichasEnFila)
            cantCaracteresValidos = len(numsEnFila) + len(fichasEnFila)
            # Se retorna la cantidad de casillas validas de la expresion, y la cantidad de caractes validos
            return (cantCasillasValidas, cantCaracteresValidos)

        def intrusosEnFila(fila):
            intrusos = re.findall("[^KkQqRrBbNnPp1-8]", fila)
            return intrusos

        def detallando():
            detalles = re.findall(segundaParte, prueba)
            new = ""
            for i in detalles:
                new += i
            detalles = re.findall("[^\s]+", new)
            global error
            valido = True
            if len(detalles) == 5:
                for j in range(len(detalles)):
                    correcto = bool(re.match(expresionesSegundaParte[j], detalles[j]))
                    if (correcto == False):
                        valido = False
                        error += nombresExpSegPart[j] + " - erroneo\n"
            if len(detalles) < 5:
                valido= False
                error += "Falta(n) " + str(5 - len(detalles)) + " detalle(s) de la partida"
            elif (len(detalles) > 5):
                valido = False
                error += "Hay " + str(len(detalles) - 5) + " mas detalles de los debidos(5)\n"
            return valido

        prueba = str(text)

        validador = "((^([^\/]+\/){7}[^\/^\s]+){1})"
        deseslash = "[^\/]+"
        segundaParte = "(\s[^\s]+)"
        expresionesSegundaParte = ["^[w|b]$", "^(((((KQ|[KQ])([qk]|kq))|((KQ)|k|K|q|Q|)))|-|kq)$", "^(([a-h][3|6])|-)$",
                                   "^([0-9]|[1-4][0-9]|50)$", "^(([1-9][0]*)+)$"]
        nombresExpSegPart = ["Piezas a mover", "Enroques permitidos", "Captura al paso", "Ultima captura",
                             "Siguiente jugada"]

        modeloPos1 = "((([^\n^\/]+)[\/]){1})"
        modeloPos2 = "(([\/]([^\n^\/^\s]+)){1})[\s]"

        numSlashes = len(re.findall("[\/]", prueba))
        if (numSlashes < 7):
            validez=False
            error += ("Faltan " + str(7 - numSlashes) + "  filas")
        elif (numSlashes == 7):
            posicionesTipo1 = re.findall(modeloPos1, prueba)
            posicionesTipo2 = re.findall(modeloPos2, prueba)
            if (len(posicionesTipo2) + len(posicionesTipo1)) < 8:
                validez=False
                error += ("Alguna(s) fila(s) no tiene(n) información")
            else:
                posiciones = bool(re.match(validador, prueba))
                if (posiciones):
                    extraidoPosicion = re.findall(validador, prueba)[0][0]
                    filasExtraidas = re.findall(deseslash, extraidoPosicion)
                    imprimirLineas(filasExtraidas)
                    for i in range(len(filasExtraidas)):
                        fila = str(i + 1)
                        caracteresIngresados = len(filasExtraidas[i])
                        casillasValid = validarFila(filasExtraidas[i])[0]
                        caracteresValid = validarFila(filasExtraidas[i])[1]
                        if (caracteresIngresados == caracteresValid and casillasValid == 8):
                            i = 0
                        elif (caracteresIngresados > caracteresValid):
                            validez = False
                            intrusos = intrusosEnFila(filasExtraidas[i])
                            error += "En fila " + fila + " se encontro cosa(s) que no va(n) ahí\n"

                            error += "[==> "
                            for intruso in intrusos:
                                error += "'" + intruso + "'" + " "
                            error += "<==]\n"

                        elif (caracteresIngresados == caracteresValid and casillasValid != 8):
                            validez = False
                            if (casillasValid - 8 > 0):
                                error += "En fila " + fila + " se indica " + str(
                                    casillasValid - 8) + " casilla(s) de mas\n"
                            else:
                                error += "En fila " + fila + " falta(n) " + str(8 - casillasValid) + " casilla(s)\n"
                if (validez == True):
                    validoDetalles = bool(re.match(
                        "(^([^\/]+\/){7}[^\/^\s]+){1}\s[wb]\s((^(((((KQ|[KQ])([qk]|kq))|((KQ)|k|K|q|Q|))|kq)|-)$)|-)\s([a-h][3|6]|-)\s(^([0-9]|[1-4][0-9]|50)$)\s(^(([1-9][0]*)+)$)",
                        prueba))
                    if (validoDetalles == False):
                        v = detallando()
                        if (v == False):
                            validez = False
        else:
            validez=False
            error += ("Sobran " + str(numSlashes - 7) + " filas")

        if (validez):
            #self.setImage()
            self.resultado.setText("¡¡¡Notacion FEN Valida!!!")
            lista = [[], [], [], [], [], [], [], []]
            for i in range(8):
                for j in range(len(filasExtraidas[i])):
                    if (bool(re.match("[1-8]", filasExtraidas[i][j]))):
                        for s in range(int(filasExtraidas[i][j])):
                            lista[i].append(" ")
                            j += 1
                    else:
                        lista[i].append(filasExtraidas[i][j])

            for x in range(8):
                for y in range(8):
                    if (y + x) % 2 == 0:
                        self.tablerito.itemAtPosition(x, y).widget().setStyleSheet(
                            "background-color: rgb(248, 222, 190);")
                        self.tablerito.itemAtPosition(x, y).widget().setFixedSize(55, 46)

                    else:
                        self.tablerito.itemAtPosition(x, y).widget().setStyleSheet(
                            "background-color : rgb(192,105,57);")
                        self.tablerito.itemAtPosition(x, y).widget().setFixedSize(55, 46)

            for l in range(8):
                for t in range(8):
                    if lista[l][t]!=' ':
                        pos=posi(lista[l][t])
                        pixmap1 = QtGui.QPixmap(piezasPng[pos])
                        pixmap1 = pixmap1.scaled(pixmap1.size().boundedTo(pixmap1.size() / 1.3))
                        self.tablerito.itemAtPosition(l, t).widget().setPixmap(pixmap1)
                        self.tablerito.itemAtPosition(l, t).widget().setAlignment(QtCore.Qt.AlignHCenter)
                    else:
                        self.tablerito.itemAtPosition(l, t).widget().clear()


            numImagen=rd.randint(0,len(imagenesCorrecto)-1)
            pixo = QPixmap(imagenesCorrecto[numImagen])
            pixo = pixo.scaled(pixo.size().boundedTo(pixo.size() / 4))
            self.errores.setPixmap(pixo)

        else:
            self.errores.setText(error)
            self.resultado.setText("Notacion FEN Invalida")
            for x in range(8):
                for y in range(8):
                    if (y + x) % 2 == 0:
                        self.tablerito.itemAtPosition(x, y).widget().clear()
                        self.tablerito.itemAtPosition(x, y).widget().setStyleSheet(
                            "background-color: rgb(248, 222, 190);")
                        self.tablerito.itemAtPosition(x, y).widget().setFixedSize(55, 46)


                    else:
                        self.tablerito.itemAtPosition(x, y).widget().clear()
                        self.tablerito.itemAtPosition(x, y).widget().setStyleSheet(
                            "background-color : rgb(192,105,57);")
                        self.tablerito.itemAtPosition(x, y).widget().setFixedSize(55, 46)

if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI=ejemplo_Gui()
    GUI.show()
    sys.exit(app.exec_())