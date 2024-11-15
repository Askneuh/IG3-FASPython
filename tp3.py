def listenbDispo(T):
    resultat = [1, 2, 3 ,4 ,5 ,6 ,7 ,8, 9]
    for elt in T:
        if elt in resultat:
            resultat.remove(elt)
    return resultat
T = [9,1,0,0,0,3,8,0,0]
print(listenbDispo(T))

def affM(M):
    for i in range(len(M)):
        print(M[i])
    return

def valeursDispoLigne(grille, indice_ligne):
    return listenbDispo(grille[indice_ligne])

def valeursDispoColonne(grille, indice_colonne):
    T = []
    for i in range(len(grille)):
        T.append(grille[i][indice_colonne])
    return listenbDispo(T)

sudoku=[]
sudoku.append([0,5,0,4,0,0,0,0,0])
sudoku.append([9,1,0,0,0,3,8,0,0])
sudoku.append([0,0,3,0,1,0,0,0,7])
sudoku.append([0,0,0,0,4,0,0,3,0])
sudoku.append([7,0,1,6,0,8,4,0,2])
sudoku.append([0,2,0,0,3,0,0,0,0])
sudoku.append([1,0,0,0,9,0,5,0,0])
sudoku.append([0,0,5,8,0,0,0,6,9])
sudoku.append([0,0,0,0,0,4,0,2,0])
print(valeursDispoLigne(sudoku, 0))
print(valeursDispoColonne(sudoku, 8))

def valeursDispoRegion(grille, indice_ligne, indice_colonne):
    T = []
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            T.append(grille[3*indice_ligne + i][3*indice_colonne + j])
    return listenbDispo(T)
print(valeursDispoRegion(sudoku, 2, 2))

def valeursDispoCase(grille, indice_ligne, indice_colonne):
    T = []
    for i in range(1, 9, 1):
        l_region = indice_ligne // 3
        c_region = indice_colonne // 3
        if i in valeursDispoLigne(grille, indice_ligne) and i in valeursDispoColonne(grille, indice_colonne) and i in valeursDispoRegion(grille, l_region, c_region):
            T.append(i)
    return T
print(valeursDispoCase(sudoku, 2, 1))
print(valeursDispoCase(sudoku, 1, 2))

def listePositionARemplir(grille):
    T = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == 0:
                T.append((i, j))
    return T

print(listePositionARemplir(sudoku))

def grilleFinie(grille, listePos, indice):
    if indice == len(listePos) -1:
        if len(valeursDispoCase(grille, listePos[indice][0], listePos[indice][1])) > 0:
            grille[listePos[indice][0]][listePos[indice][1]] = valeursDispoCase(grille, listePos[indice][0], listePos[indice][1])[0]
            return True
        return False
    else:
        if len(valeursDispoCase(grille, listePos[indice][0], listePos[indice][1])) > 0:
            grille[listePos[indice][0]][listePos[indice][1]] = valeursDispoCase(grille, listePos[indice][0], listePos[indice][1])[0]
            affM(grille)
            print("\n")
            grilleFinie(grille, listePos, indice + 1)
        else:
            grilleFinie(grille, listePos, indice)

def sudokuResolver(grille):
    lpos = listePositionARemplir(grille)
    if len(lpos) > 0:
        return grilleFinie(grille, lpos, 0)
    else:
        return (grille, False)
print(" ")
print(sudokuResolver(sudoku))