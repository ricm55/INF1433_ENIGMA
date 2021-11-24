"""
* Nom: cle_input
* Date: 11/17/2021
*
* Description : Element qui demande a l'utilisateur d'inserer la cle d'encryption et l'enregistre
* 
* Copyright 2021 @Marc-Antoine Ricard
"""

from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout
import services.storage as storage

class cle_input(QWidget):
    def __init__(self):
        super().__init__()
        
        label = QLabel("Clé")
        
        #Creer le input pour l'utilisateur
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Zone pour saisir la clé sous forme de trois triplets. Exemple: (R3,G,+7)(R1,D,-6)(R2,D,+5)")
        self.edit.setMaxLength(30)
        #self.edit.setMaximumWidth(100)
        self.edit.editingFinished.connect(self.sauvegarderCle)

        #Configurer les layouts
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.edit)
        
        #Gerer les espacements entre les differents elements
        layout.setContentsMargins(380,80,380,10)


    def sauvegarderCle(self):
        print("save la cle")
        success = storage.setCle(str(self.edit.text()))
        if success == True:
            self.cle_valide()
        else:
            self.cle_invalide()
    def cle_invalide(self):
        self.edit.setStyleSheet("border: 1px solid red");
    def cle_valide(self):
        self.edit.setStyleSheet("border: 1px solid blue");