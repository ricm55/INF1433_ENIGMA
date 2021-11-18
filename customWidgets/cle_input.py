"""
* Nom: cle_input
* Date: 11/17/2021
*
* Description : Element qui demande a l'utilisateur d'inserer la cle d'encryption et l'enregistre
* 
* Copyright 2021 @Marc-Antoine Ricard
"""

from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout

class cle_input(QWidget):
    def __init__(self):
        super().__init__()
        
        label = QLabel("Clé")
        
        #Creer le input pour l'utilisateur
        edit = QLineEdit()
        edit.setPlaceholderText("Zone pour saisir la clé sous forme de trois triplets. Exemple: (R3,G,+7)(R1,D,-6)(R2,D,+5)")
        edit.setMaxLength(10)

        #Configurer les layouts
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(edit)
        
        #Gerer les espacements entre les differents elements
        layout.setContentsMargins(550,80,550,10)
