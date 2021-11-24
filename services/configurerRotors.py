
import services.storage as storage

def configurerRotors(rotor1):
    cle = storage.getCle()
    #test.edit[0][0].setStyleSheet("color: red;")
    #get rotors
    
    print(f"la cle: {cle}")
    
    for x in cle:
        if "R1" in x:
            decalage1 = x[2]
        elif "R2" in x:
            decalage2 = x[2]
        elif "R3" in x:
            decalage3 = x[2]
    
    #Decaler les rotors
    rotor1.rotor[0].rotate(decalage1)
    rotor1.rotor[1].rotate(decalage1)
    print(f"decalage 1 {decalage1}")
    print(rotor1.rotor)
    
    #update l'affichage des rotors
    rotor1.updateAffichage()

def testRotor(rotor1):
    print(rotor1.rotor)