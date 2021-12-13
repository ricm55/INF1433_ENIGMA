"""
* Nom: configurerRotors
* Date: 11/17/2021
*
* Description : Contient tous les elements permettant de configurer les rotors
* 
* Copyright 2021 @Marc-Antoine Ricard
"""
import services.storage as storage
from collections import deque

def configurerRotors(rotor1,rotor2,rotor3,cleInput):
    """
    Decale les rotors selon la cle inseré
    """
    #Obtenir la cle et les decalages
    cle = storage.getCle()
    if cle == None:
        cleInput.cle_invalide()
        return
    
    for x in cle:
        if "R1" in x:
            decalage1 = x[2]
        elif "R2" in x:
            decalage2 = x[2]
        elif "R3" in x:
            decalage3 = x[2]
    
    #Obtenir les rotors initials
    init_rotors_nom = ["rotor 1", "rotor 2","rotor 3"]
    init_rotors = []
    for nom in init_rotors_nom:
        init_rotors.append(storage.getRotor(nom))

    #Convertir en queue et decaler les rotors
    decalage = [decalage1, decalage2, decalage3]
    for idx, rotor in enumerate(init_rotors):  
        rotor[0] = deque(rotor[0])
        rotor[0].rotate(decalage[idx])
        rotor[1] = deque(rotor[1])
        rotor[1].rotate(decalage[idx])

    #Changer la valeur des rotors actifs dans le systeme
    rotor_real = [rotor1,rotor2,rotor3]
    for idx, rotor in enumerate(init_rotors):
        rotor_real[idx].rotor[0] = rotor[0]
        rotor_real[idx].rotor[1] = rotor[1]

    #update l'affichage des rotors
    rotor1.updateAffichage()
    rotor2.updateAffichage()
    rotor3.updateAffichage()

def testRotor(rotor1):
    print(rotor1.rotor)