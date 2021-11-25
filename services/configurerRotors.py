
import services.storage as storage
from collections import deque

def configurerRotors(rotor1,rotor2,rotor3):
    
    #Obtenir la cle et les decalages
    cle = storage.getCle()
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

    #Decaler les rotors
    """
    decalage = [decalage1, decalage2, decalage3]
    for idx,rotor in enumerate(init_rotors):
        rotor[0].rotate(decalage[idx])
        rotor[1].rotate(decalage[idx])
    """
    #Changer la valeur des rotors actifs dans le systeme
    rotor_real = [rotor1,rotor2,rotor3]
    for idx, rotor in enumerate(init_rotors):
        rotor_real[idx].rotor[0] = rotor[0]
        rotor_real[idx].rotor[1] = rotor[1]
    """   
    rotor1.rotor[0] = init_rotors[0][0]
    rotor1.rotor[1] = init_rotors[0][1]

    rotor2.rotor[0] = init_rotors[1][0]
    rotor2.rotor[1] = init_rotors[1][1]

    rotor3.rotor[0] = init_rotors[2][0]
    rotor3.rotor[1] = init_rotors[2][1]
    """
    """
    rotor1.rotor[0].rotate(decalage1)
    rotor1.rotor[1].rotate(decalage1)

    rotor2.rotor[0].rotate(decalage2)
    rotor2.rotor[1].rotate(decalage2)

    rotor3.rotor[0].rotate(decalage3)
    rotor3.rotor[1].rotate(decalage3)
    """
    #update l'affichage des rotors
    rotor1.updateAffichage()
    rotor2.updateAffichage()
    rotor3.updateAffichage()

def testRotor(rotor1):
    print(rotor1.rotor)