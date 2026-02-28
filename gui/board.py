from PyQt6 import QtCore, QtGui, QtWidgets
from worlds.world import World
from organisms.organism import Organism
from organisms.animals.animal import Animal
from organisms.plants.plant import Plant


class BoardFrame(QtWidgets.QFrame):
    def __init__(self, parent, world: World):
        super().__init__(parent)
        self.__world = world
        # Używamy // dla liczb całkowitych
        self.__rectWidth: int = self.width() // self.__world.getWidth()
        self.__rectHeight: int = self.height() // self.__world.getHeight()

        self.brushBoardLithend = QtGui.QBrush(QtGui.QColor(115, 114, 78).lighter(130))
        self.brushAnimalLithend = QtGui.QBrush(QtGui.QColor(130, 72, 1).lighter(130))
        self.brushPlantLithend = QtGui.QBrush(QtGui.QColor(33, 150, 12).lighter(130))
        self.brushBoard = QtGui.QBrush(QtGui.QColor(115, 114, 78))
        self.brushAnimal = QtGui.QBrush(QtGui.QColor(130, 72, 1))
        self.brushPlant = QtGui.QBrush(QtGui.QColor(33, 150, 12))
        self.__r = []

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        # Obliczamy wymiary kafelków
        self.__rectWidth = self.width() // self.__world.getWidth()
        self.__rectHeight = self.height() // self.__world.getHeight()
        pickedPosition = self.__world.getHuman().getPickedPosition()

        # Generowanie siatki prostokątów
        self.__r = []
        for x in range(self.__world.getWidth()):
            rtemp = []
            for y in range(self.__world.getHeight()):
                # x to wiersz (pion), y to kolumna (poziom)
                rtemp.append(QtCore.QRect(y * self.__rectWidth, x * self.__rectHeight,
                                          self.__rectWidth, self.__rectHeight))
            self.__r.append(rtemp)

        # Rysowanie tła planszy
        for x in range(self.__world.getWidth()):
            for y in range(self.__world.getHeight()):
                if pickedPosition[0] == x and pickedPosition[1] == y:
                    painter.setBrush(self.brushBoardLithend)
                else:
                    painter.setBrush(self.brushBoard)
                painter.drawRect(self.__r[x][y])

        # Rysowanie organizmów
        organisms = self.__world.getOrganisms()
        for org in organisms:
            pos = org.getPosition()
            x, y = pos[0], pos[1]

            # Zabezpieczenie przed wyjściem poza zakres tablicy __r
            if x >= len(self.__r) or y >= len(self.__r[0]):
                continue

            if isinstance(org, Animal):
                if pickedPosition[0] == x and pickedPosition[1] == y:
                    painter.setBrush(self.brushAnimalLithend)
                else:
                    painter.setBrush(self.brushAnimal)
            elif isinstance(org, Plant):
                if pickedPosition[0] == x and pickedPosition[1] == y:
                    painter.setBrush(self.brushPlantLithend)
                else:
                    painter.setBrush(self.brushPlant)

            painter.drawRect(self.__r[x][y])

            # Rysowanie symbolu organizmu
            text = org.getMark()
            # NAPRAWA CRASHA: horizontalAdvance zamiast width
            text_width = painter.fontMetrics().horizontalAdvance(text)
            text_height = painter.fontMetrics().height()

            # Wyśrodkowanie tekstu
            rect = self.__r[x][y]
            text_x = rect.x() + (rect.width() - text_width) // 2
            text_y = rect.y() + (rect.height() + text_height) // 2 - 2  # mała korekta pionu

            painter.setPen(QtGui.QColor(255, 255, 255))  # Biały tekst
            painter.drawText(text_x, text_y, text)

        painter.end()