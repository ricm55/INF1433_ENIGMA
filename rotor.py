
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel, QVBoxLayout

class Rotor(QWidget):
    def __init__(self,id,row1, row2):
        super().__init__()
        self.id = id
        self.row1 = row1
        self.row2 = row2

        self.row1_composants = []
        self.row2_composants = []
        
        layoutH = QHBoxLayout(self)
        layoutV = QVBoxLayout()
        layoutH_row1 = QHBoxLayout()
        layoutH_row2 = QHBoxLayout()
        
        layoutV.addLayout(layoutH_row1)
        layoutV.addLayout(layoutH_row2)
        layoutH.addLayout(layoutV)

        for x in self.row1:
            lineEdit = QLineEdit(str(x),self)
            lineEdit.setReadOnly(True)
            self.row1_composants.append(lineEdit)
        
        for w in self.row1_composants:
            layoutH_row1.addWidget(w)

        for x in self.row2:
            lineEdit = QLineEdit(str(x),self)
            lineEdit.setReadOnly(True)
            self.row2_composants.append(lineEdit)
        
        for w in self.row2_composants:
            layoutH_row2.addWidget(w)

        label = QLabel()
        label.setText(f"Rotor {self.id}")
        layoutH.addWidget(label)
        


