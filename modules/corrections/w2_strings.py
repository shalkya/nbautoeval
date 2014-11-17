# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline


# @BEG@ 2 8 affichage
def affichage(s):
    # pour ignorer les espaces et les tabulations 
    # le plus simple est de les enlever
    s=s.replace(' ', '').replace('\t','')
    # la liste des mots s�par�s par une virgule 
    # nous est donn�e par un simple appel � split
    mots = s.split(',')
    # si on n'a m�me pas deux mots, on retourne None
    if len(mots) < 2:
        return None
    # maintenant qu'on sait qu'on a deux mots
    # on peut extraire le pr�nom et le nom
    prenom = mots.pop(0)
    nom = mots.pop(0)
    # on veut afficher "??" si l'�ge est inconnu
    age = "??"
    # mais si l'�ge est pr�cis� dans la ligne
    if len(mots) >= 2:
        # alors on le prend
        age = mots.pop(1)
    # il ne reste plus qu'� formater
    return "N:>{}< P:>{}< A:>{}<".format(nom, prenom, age)
# @END@

inputs_affichage = [
    "Joseph, Dupont",
    "Jules , Durand, G123, 21",
    "Jean", 
    "Ted, Mosby, F321, ",
    " Jacques , Martin, L119, \t24 ,",
    "Sheldon, Cooper ,",
    "\t Sam, Does\t, F321, 23",
]

exo_affichage = Exercice_1arg(affichage, inputs_affichage,
                              correction_columns=(40, 40, 40),
                              exemple_columns=(40, 40),
                              exemple_how_many=4)

##############################
# @BEG@ 2 8 carre
def carre(s):
    # on enl�ve les espaces et les tabulations
    s = s.replace(' ', '').replace('\t','')
    # la ligne suivante fait le plus gros du travail
    # d'abord on appelle split() pour d�couper selon les ';'
    # dans le cas o� on a des ';' en trop, on obtient dans le 
    #    r�sultat du split un 'token' vide, que l'on ignore 
    #    ici avec le clause 'if token'
    # enfin on convertit tous les tokens restants en entiers avec int()
    entiers = [int(token) for token in s.split(";") if token]
    # il n'y a plus qu'� mettre au carr�, et � recoudre (join) avec ':'
    return ":".join (["{}".format(entier**2) for entier in entiers])
# @END@

inputs_carre = [
    "1;2;3",
    " 2 ;  5;6;",
    "; 12 ;  -23;\t60; 1\t",
    "; -12 ; ; -23; 1 ;;\t",
]

exo_carre = Exercice_1arg(carre, inputs_carre, exemple_how_many=0)
