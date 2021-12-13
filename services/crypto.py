"""
* Nom: storage
* Date: 11/17/2021
*
* Description : Ce fichier contient les algorithmes d'encryption et de décryption
* 
* Copyright 2021 @Marc-Antoine Ricard
"""
from re import match
from PyQt6.QtGui import QColor

import services.storage as storage

#lettres,rotor1,rotor2,rotor3,reflect,texteInput_Encryption,texteInput_Decryption
class Crypto:
    def __init__(self,lettres,rotor1,rotor2,rotor3,reflect,texteInput_Encryption,texteInput_Decryption,commandButtons,cleInput):
        self.mode = "NEUTRE"
        self.lettres = lettres
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflect = reflect
        self.texteInput_Encryption = texteInput_Encryption
        self.texteInput_Decryption = texteInput_Decryption
        self.commandButtons = commandButtons
        self.cleInput = cleInput
        
        self.texteATraiter = None
        self.compteurLettres = None
        
        self.cle = None

        #Contient le nombre de fois qu'un rotor s'est fait decaler
        self.decalage = 0

        #Contient le rotor a decaler
        self.rotor_decalage = 0

        self.resetEncryption = False
        
        #Decide si l'etape suivante est l'encryption d'un caractere ou simplement un decalage
        self.etapeSuivante_EncrypteCaractere = True
    def encryption(self):
        """
        Mettre l'application en mode encryption
        """
        if self.resetEncryption:
            self.resetInterface()
            self.resetEncryption = False
            print("reseter pour encryption")
            

        cle = storage.getCle()
        if cle == None:
            self.cleInput.cle_invalide()
            return
        self.cle = cle

        self.mode = "ENCRYPT"

        #Aucun test n'est a encrypter
        self.determineTexteATraiter()
        if self.texteATraiter == None or self.texteATraiter == '':
            self.texteInput_Encryption.edit.setStyleSheet("border: 2px solid red;")
            self.texteInput_Decryption.edit.setStyleSheet("border: 1px solid black;")
            self.mode = "NEUTRE"
            return
        else:
            self.texteInput_Encryption.edit.setStyleSheet("border: 2px solid green;")
            self.texteInput_Decryption.edit.setStyleSheet("border: 1px solid black;")

        #Graphique
        self.commandButtons.Encrypter.setStyleSheet("color: red;")
        self.commandButtons.Decrypter.setStyleSheet("color: None;")

        self.compteurLettres = 0
        
        #config l'interface
        #Disable le texteInput_Encryption
        self.etapeSuivante(True)
        print("mode encryption")

    def decryption(self):
        """
        Mettre l'application en mode decryption
        """
        if self.resetEncryption:
            self.resetInterface()
            self.resetEncryption = False
            print("reseter pour decryption")
        
        cle = storage.getCle()
        if cle == None:
            self.cleInput.cle_invalide()
            return
        self.cle = cle
        self.mode = "DECRYPT"

        #Aucun test n'est a decrypter
        self.determineTexteATraiter()
        if self.texteATraiter == None or self.texteATraiter == '':  
            self.texteInput_Decryption.edit.setStyleSheet("border: 2px solid red;")
            self.texteInput_Encryption.edit.setStyleSheet("border: 1px solid black;")
            self.mode = "NEUTRE"
            return
        else:
            self.texteInput_Decryption.edit.setStyleSheet("border: 2px solid green;")
            self.texteInput_Encryption.edit.setStyleSheet("border: 1px solid black;")

        #Graphique
        self.commandButtons.Encrypter.setStyleSheet("color: None")
        self.commandButtons.Decrypter.setStyleSheet("color: red")
        
        #Initialiser le compteur de lettres
        self.compteurLettres = 0
       
        
        self.etapeSuivante(True)
        print("mode decryption")

    def etapeSuivante(self,firstStep=False):
        """
        Permet d'encrypter ou de decrypter le caractere dont on est rendu dans la chaine
        """
        #L'utilisateur n'a choisi aucun mode d'encryption
        if self.mode == "NEUTRE":
            return
        self.NettoyerAffichage()
        
        #Decaler le rotor
        if self.etapeSuivante_EncrypteCaractere != True:
            
            #Obtenir la direction du decalage
            directionDecalage = self.cle[self.rotor_decalage][1]
            rotor_a_decaler = self.cle[self.rotor_decalage][0]
            
            if directionDecalage == 'D':
                rotation = 1
            else:
                rotation = -1
            
            if rotor_a_decaler == 'R1':
                    self.rotor1.rotor[0].rotate(rotation)
                    self.rotor1.rotor[1].rotate(rotation)
                    self.rotor1.updateAffichage()

            if rotor_a_decaler == 'R2':
                    self.rotor2.rotor[0].rotate(rotation)
                    self.rotor2.rotor[1].rotate(rotation)
                    self.rotor2.updateAffichage()

            if rotor_a_decaler == 'R3':
                    self.rotor3.rotor[0].rotate(rotation)
                    self.rotor3.rotor[1].rotate(rotation)
                    self.rotor3.updateAffichage()
            
            #Ajuster les decalages pour la suite
            self.decalage+=1
            if self.decalage == 26:
                self.rotor_decalage+=1
                self.decalage = 0
                if self.rotor_decalage >2:
                    self.rotor_decalage = 0
            self.etapeSuivante_EncrypteCaractere = True
            return

        #Recuperer la lettre a encrypter
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
            valCalcule = composants[x].rotor[range_rotor][numCase] %26
            self.colorierComposant(composants[x].edit[range_rotor][numCase],range_rotor)
            numCase = (valCalcule + numCase ) %26
        
        #Colorier la lettre final
        print(f"LA LETTRE FINAL: {numCase}")
        self.colorierComposant(self.lettres.lettres_composants[numCase],range_rotor)
        
        #Mettre la prochaine etape comme un simple decalage
        self.etapeSuivante_EncrypteCaractere = False

        if self.mode == "ENCRYPT":
            self.texteInput_Decryption.edit.insertPlainText(self.lettres.lettres[numCase])
            self.compteurLettres +=1
        
        elif self.mode == "DECRYPT":
            self.texteInput_Encryption.edit.insertPlainText(self.lettres.lettres[numCase])
            self.compteurLettres +=1
            print(f"compteur: {self.compteurLettres}")
        
        if self.compteurLettres == len(self.texteATraiter) or self.compteurLettres <0:
            print("Fini l'encryption")
            self.finaliserEncryption()
            return

    def determineTexteATraiter(self):
        """
        Obtenir le input de l'utilisateur
        """
        if self.mode == "ENCRYPT":
            self.texteATraiter = self.texteInput_Encryption.edit.toPlainText()
        elif self.mode == "DECRYPT":
            self.texteATraiter = self.texteInput_Decryption.edit.toPlainText()
    
    def colorierComposant(self,x,range_rotor):
        """
        Permet de colorier les composants des rotors et reflecteurs afin de tracer un chemin
        """
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
        """
        Effacer un chemin d'encryption pour la derniere lettre 
        """
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
        """
        Lorsque l'encryption est fini, encadrer le message final
        """
        if self.mode == "ENCRYPT":
            self.texteInput_Decryption.edit.setStyleSheet("border: 2px solid blue;")
        else:
            self.texteInput_Encryption.edit.setStyleSheet("border: 2px solid blue;")
        
        #Reinitialiser les variables pour la prochaine encryption
        self.mode = "NEUTRE"
        self.resetEncryption = True
        self.texteATraiter = None
        self.decalage = 0
        self.rotor_decalage = 0
        self.compteurLettres = None
        self.etapeSuivante_EncrypteCaractere = True
    def resetInterface(self):
        """
        Effacer les input et output
        """
        self.texteInput_Encryption.edit.setText("")
        self.texteInput_Encryption.edit.setStyleSheet("border:1px solid black")
        
        self.texteInput_Decryption.edit.setText("")
        self.texteInput_Decryption.edit.setStyleSheet("border:1px solid black")

        self.commandButtons.Encrypter.setStyleSheet("color: None")
        self.commandButtons.Decrypter.setStyleSheet("color: None")

        

        
        

        



