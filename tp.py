#Exercice 1
def ProduitsEntiersPairs(n):
    """
    Calcule la somme des entiers pairs de 0 à n inclus.
    
    Paramètres :
    n (int) : Un entier naturel, limite supérieure de la somme des entiers pairs.
    
    Retourne :
    int : La somme des entiers pairs de 0 à n.
    """
    somme = 0
    for i in range(0, n+1, 2):
        somme += i
    return somme
print("Tests ex 1")
print(ProduitsEntiersPairs(9))
print(ProduitsEntiersPairs(6))
print(ProduitsEntiersPairs(100))
#Exercice 2
def SansDiviseurs(n, k):
    """
    Vérifie si k est un diviseur de n dans l'intervalle [2, n-1].
    
    Paramètres :
    n (int) : L'entier à tester.
    k (int) : L'entier à vérifier s'il divise n.
    
    Retourne :
    bool : True si k n'est pas un diviseur de n, False sinon.
    """
    assert(k <= n, "pre condition non valide")
    res = True
    while k < n and res:
        if n%k ==0:
            res = False
        k += 1
    return res

def estPremier(n):
    """
    Vérifie si un nombre n est premier.
    
    Paramètres :
    n (int) : Le nombre à tester.
    
    Retourne :
    bool : True si n est un nombre premier, False sinon.
    """
    if n != 1:
        return SansDiviseurs(n, 2)
    return False
print("Tests ex2")
print(estPremier(12))
print(estPremier(13))
print(estPremier(7))
print(estPremier(4))


#Exercice 3
def sommeNbPremier(k):
    """
    Calcule la somme des nombres premiers strictement inférieurs à k.
    
    Paramètres :
    k (int) : Limite supérieure jusqu'à laquelle les premiers sont sommés.
    
    Retourne :
    int : La somme des nombres premiers strictement inférieurs à k.
    """
    somme = 0
    for i in range(k):
        if estPremier(i):
            somme += i
    return somme
print("Tests ex3")
print(sommeNbPremier(7))
print(sommeNbPremier(15))
#Exercice 4
def NbOccur(T,x):
    """
    Compte le nombre d'occurrences de l'élément x dans la liste T.
    
    Paramètres :
    T (list) : Une liste d'éléments.
    x : L'élément dont on veut compter les occurrences dans T.
    
    Retourne :
    int : Le nombre d'occurrences de x dans T.
    """
    compte = 0
    for i in range(len(T)):
        if T[i] == x:
            compte += 1
    return compte
print("Tests ex 4, NbOccur")
T = [4, 8, 2, 3 ,6 ,9 ,4 ,7]
print(NbOccur(T, 4))
print(NbOccur(T, 7))

def estPresent(T, x):
    """
    Vérifie si l'élément x est présent dans la liste T.
    
    Paramètres :
    T (list) : Une liste d'éléments.
    x : L'élément à rechercher dans T.
    
    Retourne :
    bool : True si x est présent dans T, False sinon.
    """
    res = False
    i = 0
    while i < len(T) and not res:
        if T[i] == x:
            res = True
        i += 1
    return res
print("Tests ex 4, estPresent")
print(estPresent(T, 1))
print(estPresent(T, 4))
def Indice(T, x):
    """
    Trouve l'indice de l'élément x dans la liste T.
    
    Paramètres :
    T (list) : Une liste d'éléments.
    x : L'élément à rechercher dans T.
    
    Retourne :
    int : L'indice de x dans T, ou -1 si x n'est pas dans T.
    """
    i = 0
    found = False
    while i < len(T) and not found:
        if T[i] == x:
            found = True
        else:
            i += 1
    if not found:
        return -1
    else:
        return i
print("Tests ex 4, Indice")
print(Indice(T, 4))
print(Indice(T, 3))
#Exercice 5
def Compare(T1, T2):
    """
    Compare deux listes T1 et T2 élément par élément.
    
    Paramètres :
    T1 (list) : La première liste à comparer.
    T2 (list) : La deuxième liste à comparer.
    
    Retourne :
    int : -1 si T1 < T2, 1 si T1 > T2, 0 si T1 == T2.
    """
    assert(len(T1) == len(T2), "T1 pas de la taille de T2")
    res = 0
    i = 0
    while i < len(T1) and res != 1:
        if T1[i] < T2[i]:
            res = -1
        if T1[i] > T2[i]:
            res = 1
        i += 1
    return res
print("Tests ex 5")
T1 = ['a', 'b', 'a']
T2 = ['a', 'b', 'c']
print(Compare(T1, T2))
T1 = ['d', 'b', 'e']
T2 = ['d', 'b', 'e']
print(Compare(T1, T2))
T1 = ['a', 'd', 'a']
T2 = ['a', 'b', 'c']
print(Compare(T1, T2))

#Exercice 6
def Est_Sous_Tab(P, G):
    """
    Vérifie si la liste P est un sous-tableau de G.
    
    Paramètres :
    P (list) : La liste à vérifier comme sous-tableau.
    G (list) : La liste dans laquelle chercher P.
    
    Retourne :
    bool : True si P est un sous-tableau de G, False sinon.
    """
    i = 0
    trouve = False
    while i < len(G) - len(P) and not trouve:
        if G[i] == P[0]:
            j = 0
            res = False
            while j != len(P) and G[i + j] == P[j]:
                j += 1
            if j == len(P):
                trouve = True
        i += 1
    return trouve
print("Tests ex 6")
P=['c','d','e']
G = ['a', 'b', 'c','d', 'e', 'f']
print(Est_Sous_Tab(P, G))
G = ['a', 'c', 'b','d', 'e', 'f']
print(Est_Sous_Tab(P, G))
G = ['a', 'c', 'd']
print(Est_Sous_Tab(P, G))
#Exercice 7
def NiemePremier(n):
    compte = 0
    i = 1
    while compte < n:
        if estPremier(i):
            compte += 1
        i += 1
    return i - 1
print("Tests ex 7")
print(NiemePremier(12))
