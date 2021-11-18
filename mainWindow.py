"""
Entete

"""
import os
import sys

#installation de l'interface graphique
os.system("pip install pyQt6")

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QWidget
)

from gui_reflecteur import Reflecteur

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("enigma")
        
        main_layout = QVBoxLayout()
        reflect = Reflecteur()
        main_layout.addWidget(reflect)
        
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
