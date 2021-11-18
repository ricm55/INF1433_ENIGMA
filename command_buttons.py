from PyQt6.QtWidgets import QWidget, QLabel, QTextEdit, QHBoxLayout, QPushButton

class command_buttons(QWidget):
    def __init__(self):
        super().__init__()

        ConfigurerRotors = QPushButton("Configurer Rotors")
        Encrypter = QPushButton("Encrypter")
        EtapeSuivante = QPushButton("Étape suivante")
        Decrypter = QPushButton("Décrypter")

        layout = QHBoxLayout(self)
        layout.addWidget(ConfigurerRotors)
        layout.addWidget(Encrypter)
        layout.addWidget(EtapeSuivante)
        layout.addWidget(Decrypter)

        layout.setSpacing(50)
        
        