"""
Ce fichier contient les algorithmes d'encryption et de décryption
"""
from PyQt6.QtGui import QColor

#lettres,rotor1,rotor2,rotor3,reflect,texteInput_Encryption,texteInput_Decryption
class Crypto:
    def __init__(self,lettres,rotor1,rotor2,rotor3,reflect,texteInput_Encryption,texteInput_Decryption):
        self.mode = "NEUTRE"
        self.lettres = lettres
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflect = reflect
        self.texteInput_Encryption = texteInput_Encryption
        self.texteInput_Decryption = texteInput_Decryption
        
        self.texteATraiter = None
        self.compteurLettres = None
    def encryption(self):
        self.mode = "ENCRYPT"
        self.determineTexteATraiter()
        self.etapeSuivante()
        print("mode encryption")

    def decryption(self):
        self.mode = "DECRYPT"
        self.determineTexteATraiter()
        self.etapeSuivante()
        print("mode decryption")

    def etapeSuivante(self):
        
        if self.mode == "ENCRYPT":
            self.compteurLettres = 0
        
        elif self.mode == "DECRYPT":
            self.compteurLettres = len(self.texteATraiter) - 1
        else:
            #L'utilisateur est dans aucun mode
            return;
        
        lettreAEncrypt = self.texteATraiter[self.compteurLettres]

        rotor_mode = 1
        #Obtenir le numero de la lettre et la colorier
        numLettre = ord(lettreAEncrypt.upper())-65
        self.colorierComposant(self.lettres.lettres_composants[numLettre],rotor_mode)
        
        composants = [self.rotor1,self.rotor2,self.rotor3]
        
        for x in range (0,2):
            for x in range(0,3):
                valCalcule = composants[x].rotor[rotor_mode][numLettre]
                self.colorierComposant(composants[x].edit[1][numLettre],rotor_mode)
                numLettre = valCalcule + numLettre
            self.colorierComposant(self.reflect.ref_composants[numLettre],rotor_mode)
            numLettre = valCalcule + self.reflect.reflecteur[numLettre]
            rotor_mode = 0
        """    
        #Obtenir la valeur dans le rotor et colorier cette valeur
        val_r1 = self.rotor1.rotor[1][numLettre]
        self.rotor1.edit[1][numLettre].setStyleSheet("color:red;")
        caseAColorier = val_r1 + numLettre

        val_r2 = self.rotor2.rotor[1][caseAColorier]
        self.rotor2.edit[1][caseAColorier].setStyleSheet("color:red;")
        caseAColorier = val_r2 + caseAColorier
        
        val_r3 = self.rotor3.rotor[1][caseAColorier]
        self.rotor3.edit[1][caseAColorier].setStyleSheet("color:red;")
        caseAColorier = val_r3 + caseAColorier
        """
        """
        val_ref = self.reflect.reflecteur[caseAColorier]
        self.reflect.ref_composants.edit[1][caseAColorier].setStyleSheet("color:red;")
        
        caseAColorier = val_ref + caseAColorier
        """
        
    def determineTexteATraiter(self):
        #Obtenir le input de l'utilisateur
        if self.mode == "ENCRYPT":
            self.texteATraiter = self.texteInput_Encryption.edit.toPlainText()
        elif self.mode == "DECRYPT":
            self.texteATraiter = self.texteInput_Decryption.edit.toPlainText()
    
    def colorierComposant(self,x,montee):
        if montee:
            x.setStyleSheet(
            "color:red;\
            background-color:#E0E0E0;"
            )
        else:
            x.setStyleSheet(
            "color:blue;\
            background-color:#E0E0E0;"
            )
        

        



