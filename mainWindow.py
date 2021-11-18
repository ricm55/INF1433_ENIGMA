"""
Entete

"""
import os
import sys
import json

#installation de l'interface graphique
os.system("pip install pyQt6")

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget
)

from reflecteur import Reflecteur
from rotor import Rotor
from lettreAlphabet import lettreAlphabet 
from cle_input import cle_input
from texte_input import texte_input
from command_buttons import command_buttons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("enigma")
        
        with open('rotors.json') as f:
            rotors_data = json.load(f)

        main_layout = QVBoxLayout()
        reflect = Reflecteur()
        rotor1 = Rotor(1,rotors_data["rotor 1"])
        rotor2 = Rotor(2,rotors_data["rotor 2"] )
        rotor3 = Rotor(3,rotors_data["rotor 3"] )
        lettres = lettreAlphabet()
        cleInput = cle_input()
        texteInput_Encryption = texte_input(True)
        commandButtons = command_buttons()
        texteInput_Decryption = texte_input(False)

        main_layout.addWidget(reflect)
        main_layout.addWidget(rotor1)
        main_layout.addWidget(rotor2)
        main_layout.addWidget(rotor3)
        main_layout.addWidget(lettres)
        main_layout.addWidget(cleInput)
        main_layout.addWidget(texteInput_Encryption)
        main_layout.addWidget(commandButtons)
        main_layout.addWidget(texteInput_Decryption)
        
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
