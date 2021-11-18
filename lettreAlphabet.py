
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel

class lettreAlphabet(QWidget):
    def __init__(self):
        super().__init__()
      
        self.lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.ref_composants = []

        for lettre in self.lettres:
            lineEdit = QLineEdit(lettre,self)
            lineEdit.setReadOnly(True)
            self.ref_composants.append(lineEdit)
         
        layout = QHBoxLayout(self)
         
        for w in self.ref_composants:
            layout.addWidget(w)
        
        layout.setContentsMargins(0,10,0,10)
        

