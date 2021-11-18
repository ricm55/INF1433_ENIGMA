from PyQt6.QtWidgets import QWidget, QLabel, QTextEdit, QHBoxLayout

class texte_input(QWidget):
    def __init__(self,encrypter):
        super().__init__()
        
        
        edit = QTextEdit()
        if encrypter:
            edit.setPlaceholderText("Zone de textes pour taper le message à encrypter ou pour afficher le résultat de décryption")
        else:
            edit.setPlaceholderText("Zone de textes pour taper le message à décrypter ou pour afficher le résultat d'encryption")
        
        layout = QHBoxLayout(self)
        layout.addWidget(edit)
        
        #layout.setContentsMargins(550,80,550,10)
