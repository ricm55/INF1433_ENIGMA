"""
* Nom: reflecteur
* Date: 11/17/2021
*
* Description : Element qui contient tous les informations sur le reflecteur
* 
* Copyright 2021 @Marc-Antoine Ricard
"""

from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel

class Reflecteur(QWidget):
    def __init__(self,reflecteur):
        super().__init__()

        self.reflecteur = reflecteur
        self.ref_composants = []

        layout = QHBoxLayout(self)

        #Mettre chaque nombre du reflecteur dans une case 
        for x in self.reflecteur:
            suffixe = ''
            if x > 0:
                suffixe = '+'
            lineEdit = QLineEdit(suffixe + str(x),self)
            lineEdit.setReadOnly(True)
            layout.addWidget(lineEdit)
        
        #Inscrire sur la fenetre qu'il s'agit d'un reflecteur
        label = QLabel()
        label.setText("Réflecteur")
        layout.addWidget(label)
        
        #Gerer les espacements entre les differents elements
        layout.setContentsMargins(0,0,0,10)
        

