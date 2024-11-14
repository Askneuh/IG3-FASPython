#Exercice 1:
def dico(cle, valeur):
    dico = {}
    dico[cle] = valeur
    return dico

#Exercice 2
def dicoListe(cles, valeurs):
    dic : dict = {}
    for i in range(len(cles)):
        dic[cles[i]] = valeurs[i]
    return dic

cles = ["MPL", "DUB", "CDG", "ORY", "YYZ", "LHR", "LAX"]
valeurs = ["Montpellier", "Dublin", "Paris Charles-De-Gaulle", "Paris Orly", "Toronto", "London", "Los Angeles"]
print(dicoListe(cles, valeurs))
dictionnaire = dicoListe(cles, valeurs)
dictionnaire["LCY"] = "London City"
print(dictionnaire)

#Exercice 3
def getKeyFromValue(dic, value):
    for keys in dic:
        if dic[keys] == value:
            return keys

#Exercice 4
dictionnaire2 = dicoListe(cles, valeurs)
dictionnaire2["LCY"] = "London City"
for elt in sorted(dictionnaire2.keys()):
    print(elt, dictionnaire2[elt])
print("\n")
for elt in sorted(dictionnaire2.values()):
    print(getKeyFromValue(dictionnaire2, elt), elt)


#Partie 2 REGEX

#Exercice 6

from re import *

def estEmail(arg):
    return search("^.*@.*$", arg) != None

mail = "seb.pintas@gmail.com"
mail2 = "seb.pintasgmail.com"
print(estEmail(mail))
print(estEmail(mail2))

#Exercice 7
#Bon bah c'est deja fais dans l'exercice 6.

#Exercice 8

def fullVerifMail(arg):
    return search("^(\W|\w)*@(\W|\w)*(\.)(com|fr|org)$", arg) != None
mail2 = "1234@trrrrrrrr.com"
mail3 = "seb.pintas@gmail.ty"
mail4 = "seb.pintasgmail.com"
mail5 = "séb.pintas@gmail.com"
mail6 = "az32 $ac@test.frzfr."
print(fullVerifMail(mail2))
print(fullVerifMail(mail3))
print(fullVerifMail(mail4))
print(fullVerifMail(mail5))
print(fullVerifMail(mail6))


#Exercice 9
def estNumTel(arg):
    search("^(\+[0-9]{2}[?(\.)[0-9]]{9}|0[0-9]{1}[?(\.)[0-9]]{9})$")
    return search("^(\+[0-9]{2}|\([0-9]{2}\)|0)[0-9]{9}$", arg) != None
    
print("\n")
tel = "+33781639592"
tel2 = "0781639592"
tel3 = "(33)81639592"
tel4 = "le mal"
tel5 = "lal07816395952"
print(estNumTel(tel))
print(estNumTel(tel2))
print(estNumTel(tel3))
print(estNumTel(tel4))
print(estNumTel(tel5))