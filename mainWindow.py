"""
Entete

"""
import os
import sys



#installation de l'interface graphique
os.system("pip install pyQt6")

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QWidget
)

from PyQt6.QtGui import QGuiApplication

#from PyQt6.QtGui import QDesktopWidget

from reflecteur import Reflecteur
from rotor import Rotor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("enigma")
        """
        [
            [12,-1,23,10,2,14,5,-5,9,-2,-13,10,-2,-8,+10,-6,+6,-16,+2,-1,-17,-5,-14,-9,-20,-10],
            [1,16,5,17,20,8,-2,2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23]]
        """
        main_layout = QVBoxLayout()
        reflect = Reflecteur()
        rotor1 = Rotor(1,[12,-1,23,10,2,14,5,-5,9,-2,-13,10,-2,-8,+10,-6,+6,-16,+2,-1,-17,-5,-14,-9,-20,-10],[1,16,5,17,20,8,-2,2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23] )
        rotor2 = Rotor(2,[12,-1,23,10,2,14,5,-5,9,-2,-13,10,-2,-8,+10,-6,+6,-16,+2,-1,-17,-5,-14,-9,-20,-10],[1,16,5,17,20,8,-2,2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23] )
        rotor3 = Rotor(3,[12,-1,23,10,2,14,5,-5,9,-2,-13,10,-2,-8,+10,-6,+6,-16,+2,-1,-17,-5,-14,-9,-20,-10],[1,16,5,17,20,8,-2,2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23] )
        
        main_layout.addWidget(reflect)
        main_layout.addWidget(rotor1)
        main_layout.addWidget(rotor2)
        main_layout.addWidget(rotor3)
        
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
