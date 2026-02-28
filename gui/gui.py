from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui.main_frame import UiMainFrame
from gui.main_window import MainWindow
from worlds.world import World
import sys


class KeyPressFilter(QtCore.QObject):
    def eventFilter(self, obj, event):
        # PyQt6: Zmiana z QEvent.KeyPress na QEvent.Type.KeyPress
        if event.type() == QtCore.QEvent.Type.KeyPress:
            key = event.key()
        return False


class Gui:
    def __init__(self, world: World):
        self.__world = world

    def window(self):
        app = QApplication(sys.argv)

        screen = app.primaryScreen()
        mainWindow = MainWindow()

        mainFrame = UiMainFrame(mainWindow, self.__world)

        mainWindow.showMaximized()

        # PyQt6: Zmiana z exec_() na exec()
        sys.exit(app.exec())