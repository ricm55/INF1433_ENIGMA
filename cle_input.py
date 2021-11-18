from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout

class cle_input(QWidget):
    def __init__(self):
        super().__init__()
        
        label = QLabel("Clé")
        
        edit = QLineEdit()
        edit.setPlaceholderText("Zone pour saisir la clé sous forme de trois triplets. Exemple: (R3,G,+7)(R1,D,-6)(R2,D,+5)")
        edit.setMaxLength(10)

        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(edit)
        
        layout.setContentsMargins(550,80,550,10)
