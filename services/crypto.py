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
        self.compteurLettres = 0
        
        #config l'interface
        #Disable le output
        
        self.etapeSuivante()
        print("mode encryption")

    def decryption(self):
        self.mode = "DECRYPT"
        self.determineTexteATraiter()
        self.compteurLettres = len(self.texteATraiter) - 1
        self.etapeSuivante()
        print("mode decryption")

    def etapeSuivante(self):

        #L'utilisateur n'a choisi aucun mode d'encryption
        if self.mode == "NEUTRE":
            return

        self.NettoyerAffichage()

        lettreAEncrypt = self.texteATraiter[self.compteurLettres]

        #Permet de savoir quel range du rotor colorier
        range_rotor = 1

        #Obtenir le numero de la lettre et la colorier
        numCase = ord(lettreAEncrypt.upper())-65
        self.colorierComposant(self.lettres.lettres_composants[numCase],range_rotor)
        
        composants = [self.rotor1,self.rotor2,self.rotor3]
       
        #Colorier la montee
        for x in range(0,3):
                valCalcule = composants[x].rotor[range_rotor][numCase]
                self.colorierComposant(composants[x].edit[range_rotor][numCase],range_rotor)
                numCase = (valCalcule + numCase) % 26
        
        #Colorier le reflecteur
        self.colorierComposant(self.reflect.ref_composants[numCase],range_rotor)
        print(f"{numCase} + {self.reflect.reflecteur[numCase]}",end=' = ')
        numCase = ( numCase + self.reflect.reflecteur[numCase] ) % 26
        print(numCase)
        #Changer la rangee des rotors
        range_rotor = 0
        
        #Colorier la descente
        for x in range(2,-1,-1):
            valCalcule = composants[x].rotor[range_rotor][numCase]
            self.colorierComposant(composants[x].edit[range_rotor][numCase],range_rotor)
            numCase = valCalcule + numCase
        
        #Colorier la lettre final
        self.colorierComposant(self.lettres.lettres_composants[numCase],range_rotor)
        
        #Mettre la lettre final dans le output
        
        if self.mode == "ENCRYPT":
            self.texteInput_Decryption.edit.insertPlainText(self.lettres.lettres[numCase])
            self.compteurLettres +=1
        
        elif self.mode == "DECRYPT":
            self.texteInput_Encryption.edit.insertPlainText(self.lettres.lettres[numCase])
            self.compteurLettres -=1
            print(f"compteur: {self.compteurLettres}")
        
        if self.compteurLettres == len(self.texteATraiter) or self.compteurLettres <0:
            print("Fini l'encryption")
            self.finaliserEncryption()
            self.mode = "NEUTRE"
            return
    def determineTexteATraiter(self):
        #Obtenir le input de l'utilisateur
        if self.mode == "ENCRYPT":
            self.texteATraiter = self.texteInput_Encryption.edit.toPlainText()
        elif self.mode == "DECRYPT":
            self.texteATraiter = self.texteInput_Decryption.edit.toPlainText()
    
    def colorierComposant(self,x,range_rotor):
        if range_rotor:
            x.setStyleSheet(
            "color:red;\
            background-color:#E0E0E0;"
            )
        else:
            x.setStyleSheet(
            "color:blue;\
            background-color:#E0E0E0;"
            )
    def NettoyerAffichage(self):
        #composants_a_nettoyer = [self.lettres.lettres_composants,self.rotor1,self.rotor2,self.rotor3,self.reflecteur.reflecteur]
        #Nettoyer les lettres
        for lettre in self.lettres.lettres_composants:
            lettre.setStyleSheet("color:None;")

        #Nettoyer les rotors
        rotors = [self.rotor1,self.rotor2, self.rotor3]
        for rotor in rotors:
            for case in rotor.edit[0]:
                case.setStyleSheet("color:None;")
            for case in rotor.edit[1]:
                case.setStyleSheet("color:None;")
                
        #Nettoyer le reflecteur
        for case in self.reflect.ref_composants:
            case.setStyleSheet("color:None;")
        
    def finaliserEncryption(self):
        if self.mode == "ENCRYPT":
            self.texteInput_Decryption.edit.setStyleSheet("border: 2px solid blue;")
        else:
            self.texteInput_Encryption.edit.setStyleSheet("border: 2px solid blue;")
        
        self.mode = "NEUTRE"
        

        



