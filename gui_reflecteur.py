
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel

class Reflecteur(QWidget):
    def __init__(self):
        super().__init__()
      
        self.nombre = [25,23,21,19,17,15,13,11,9,7,5,3,1,-1,-3,-5,-7,-9,-11,-13,-15,-17,-19,-21,-23,-25]
        self.ref_composants = []

        for x in self.nombre:
            lineEdit = QLineEdit(str(x),self)
            lineEdit.setReadOnly(True)
            self.ref_composants.append(lineEdit)
         
        layout = QHBoxLayout(self)
         
        for w in self.ref_composants:
            layout.addWidget(w)
        
        label = QLabel()
        label.setText("Reflecteur")
        layout.addWidget(label)
        

