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
        EtapeSuivante = QPushButton("Étape suivante")
        Decrypter = QPushButton("Décrypter")

        #Configurer les layouts
        layout = QHBoxLayout(self)
        layout.addWidget(self.ConfigurerRotors)
        layout.addWidget(self.Encrypter)
        layout.addWidget(EtapeSuivante)
        layout.addWidget(Decrypter)

        #Espacer les boutons entre eux
        layout.setSpacing(50)
        #ConfigurerRotors.clicked.connect(configRotors.configurerRotors())
    
        
