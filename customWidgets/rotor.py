"""
* Nom: rotor
* Date: 11/17/2021
*
* Description : Element qui contient tous les informations sur les rotors
* 
* Copyright 2021 @Marc-Antoine Ricard
"""
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout
from collections import deque #Facilite les futurs decalage

class Rotor(QWidget):
    def __init__(self,id,data_rotor):
        super().__init__()
        self.id = id
        
        self.rotor = []
        for row in data_rotor:
            self.rotor.append(deque(row))
        self.edit = [[],[]]

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
                lineEdit.setFixedWidth(40)
                if idx == 0:
                    self.edit[0].append(lineEdit)
                    layoutH_row1.addWidget(lineEdit)
                else:
                    self.edit[1].append(lineEdit)
                    layoutH_row2.addWidget(lineEdit)

        #Inscrire de quel rotor il s'agit
        label = QLabel()
        label.setText(f"Rotor {self.id}")
        layoutH.addWidget(label)
    
    def updateAffichage(self):
        """
        Mettre a jour l'affichage des rotors dans la fenetre 
        """
        iter_rotor = iter(self.rotor)
        iter_edit = iter(self.edit)
        for y in range(0,2):
            try:
                iterateRotor = next(iter_rotor)
                iterateEdit = next(iter_edit)
            except:
                print("exception declenche")
                break

            for idx,x in enumerate(iterateRotor):
                prefix = ''
                if x>0:
                    prefix = '+'
                iterateEdit[idx].setText(prefix + str(x))
            
    def initialiserAffichage(self):
        pass
        


