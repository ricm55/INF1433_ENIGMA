"""
* Nom: mainWindow
* Date: 11/17/2021
*
* Description : Fenetre principale du logiciel enigma
* 
* Copyright 2021 @Marc-Antoine Ricard
"""
import os #installer pyQt6 pour l'interface graphique
import sys # Obtenir les arguments venant de la ligne de commande
import json # Permet de lire les fichiers de configuration comme les rotors ou la clé

#installation de l'interface graphique
os.system("pip install pyQt6")

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget
)

from PyQt6.QtGui import QIcon

#Importation des widgets custom 
from customWidgets.reflecteur import Reflecteur
from customWidgets.rotor import Rotor
from customWidgets.lettreAlphabet import lettreAlphabet 
from customWidgets.cle_input import cle_input
from customWidgets.texte_input import texte_input
from customWidgets.command_buttons import command_buttons

import services.storage as storage
import services.configurerRotors as configRotors
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("enigma")
        self.setWindowIcon(QIcon('img/enigma.jpg'))

        main_layout = QVBoxLayout()

        #Creation des widgets de la fenetre
        reflect = Reflecteur(storage.getReflecteur())
        rotor3 = Rotor(3,storage.getRotor("rotor 3"))
        rotor2 = Rotor(2,storage.getRotor("rotor 2"))
        rotor1 = Rotor(1,storage.getRotor("rotor 1"))
        lettres = lettreAlphabet()
        cleInput = cle_input()
        texteInput_Encryption = texte_input(True)
        commandButtons = command_buttons()
        texteInput_Decryption = texte_input(False)

        #Envoie des signals entre widget
        commandButtons.ConfigurerRotors.clicked.connect(lambda: configRotors.configurerRotors(rotor1))
        commandButtons.Encrypter.clicked.connect(lambda: configRotors.testRotor(rotor1))

        #Ajout des widgets dans le layout principal
        main_layout.addWidget(reflect)
        main_layout.addWidget(rotor3)
        main_layout.addWidget(rotor2)
        main_layout.addWidget(rotor1)
        main_layout.addWidget(lettres)
        main_layout.addWidget(cleInput)
        main_layout.addWidget(texteInput_Encryption)
        main_layout.addWidget(commandButtons)
        main_layout.addWidget(texteInput_Decryption)
        
        #Mettre le layout principal dans le widget central
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    #Creation de l'application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
