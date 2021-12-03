"""
* Nom: command_button
* Date: 11/17/2021
*
* Description : Element qui contient les boutons de controle pour l'utilisateur. Il
*               peut donc decider s'il doit encrypter, decrypter, changer les configurations...
* 
* Copyright 2021 @Marc-Antoine Ricard
"""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
import services.configurerRotors as configRotors
import services.storage as storage

class command_buttons(QWidget):
    def __init__(self):
        super().__init__()

        #Creation des boutons
        self.ConfigurerRotors = QPushButton("Configurer Rotors")
        self.Encrypter = QPushButton("Encrypter")
        self.EtapeSuivante = QPushButton("Étape suivante")
        self.Decrypter = QPushButton("Décrypter")

        #Configurer les layouts
        layout = QHBoxLayout(self)
        layout.addWidget(self.ConfigurerRotors)
        layout.addWidget(self.Encrypter)
        layout.addWidget(self.EtapeSuivante)
        layout.addWidget(self.Decrypter)
        
        #Etablir les signals
        self.Encrypter.clicked.connect(self.activerEncryption)
        self.Decrypter.clicked.connect(self.activerDecryption)

        #Espacer les boutons entre eux
        layout.setSpacing(50)
    
    def activerEncryption(self):
        self.Decrypter.setStyleSheet("background-color: None")
        self.Encrypter.setStyleSheet("background-color: yellow")
    
    def activerDecryption(self):
        self.Encrypter.setStyleSheet("background-color: None")
        self.Decrypter.setStyleSheet("background-color: yellow")
    
    
        
