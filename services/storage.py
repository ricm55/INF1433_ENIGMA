
"""
This file can get and write data in json file 
"""

import json
import re

def getRotor(rotor):
    with open('rotors.json') as f:
        rotors_data = json.load(f)
    try:
        return rotors_data[rotor]
    except:
        return None

def getReflecteur():
    with open('rotors.json') as f:
        rotors_data = json.load(f)
    try:
        return rotors_data["reflecteur"]
    except:
        return None

def getCle():
    #Obtenir la cle dans le fichier
    f = open("cle.txt","r")
    cleFichier = f.read()
    f.close()
    print(cleFichier)
    
    cle = []
    #Position ou demarrer la recherche
    demarreRecherche = 0
    for x in range(0,3):
        sectionCle = cleFichier[cleFichier.index('(',demarreRecherche)+1:cleFichier.index(')',demarreRecherche)]
        sectionCle = sectionCle.split(',')
        sectionCle[2] = int(sectionCle[2])
        print(f"la section de la cle: {sectionCle}")
        cle.append(sectionCle)
        print(f"ajout de la cle {cle}")
        #demarreRecherche = cleFichier.index(')')+1
        demarreRecherche += 9
    
    
    print(f'la cle: {cle}')
    #verifier la cle avec regex et mettre l'encadré en rouge

    return cle
def setCle(cle):
    #valider la cle
    #re.search (\(R\d,[G|D],[+|-]\d[0-6]?\)){3}
    valide = bool( re.search("(\(R[1-3],[G|D],[+|-]\d[0-6]?\)){3}",cle) )
    print(f"regex: {valide}")
    #contient tous les rotors
    for x in ["R1","R2","R3"]:
        print(f"cherche la chaine {x} dans {cle}")
        if cle.find(x) == -1:
            print(f"pas trouve {x}")
            valide = False
    
    if valide:
        f = open("cle.txt","w")
        f.write(cle)
        f.close()
        return valide
    return valide