"""
* Nom: rotor
* Date: 11/17/2021
*
* Description : Element qui contient tous les informations sur les rotors
* 
* Copyright 2021 @Marc-Antoine Ricard
"""
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout

class Rotor(QWidget):
    def __init__(self,id,data_rotor):
        super().__init__()
        self.id = id
        self.rotor = data_rotor

        #Configurer les layouts  
        layoutH = QHBoxLayout(self)
        layoutV = QVBoxLayout()
        layoutH_row1 = QHBoxLayout()
        layoutH_row2 = QHBoxLayout()
        
        layoutV.addLayout(layoutH_row1)
        layoutV.addLayout(layoutH_row2)
        layoutH.addLayout(layoutV)

        #Mettre chaque element du rotor dans une case
        for idx, row in enumerate(self.rotor):
            for nbre in row:
                suffixe = ''
                if nbre > 0:
                    suffixe = '+'
                lineEdit = QLineEdit(suffixe + str(nbre) ,self)
                lineEdit.setReadOnly(True)
                if idx == 0:
                    layoutH_row1.addWidget(lineEdit)
                else:
                    layoutH_row2.addWidget(lineEdit)

        #Inscrire de quel rotor il s'agit
        label = QLabel()
        label.setText(f"Rotor {self.id}")
        layoutH.addWidget(label)
        


