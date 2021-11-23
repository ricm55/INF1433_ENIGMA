"""
* Nom: lettreAlphabet
* Date: 11/17/2021
*
* Description : Element qui afficher tous les lettres de l'alphabet dans des cases
* 
* Copyright 2021 @Marc-Antoine Ricard
"""
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout

class lettreAlphabet(QWidget):
    def __init__(self):
        super().__init__()
      
        self.lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lettres_composants = []
        
        layout = QHBoxLayout(self)
        
        #Mettre chaque lettre dans une case
        for lettre in self.lettres:
            lineEdit = QLineEdit(lettre,self)
            lineEdit.setReadOnly(True)
            lineEdit.setFixedWidth(40)
            self.lettres_composants.append(lineEdit)
            layout.addWidget(lineEdit)
        
        #Gerer les espacements entre les differents elements
        layout.setContentsMargins(0,10,0,10)
        

