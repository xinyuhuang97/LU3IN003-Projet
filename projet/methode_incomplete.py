import numpy as np
M=4
N=4

grille=np.zeros((M,N))
sequence=[1,1]
# non-colore -1
# blanche 0
# noire 1


def coloriage_possible(grille, sequence, i, j, l):
    # problem de syntaxe
    # cas a: si l depasse le nb d'element de la sequence, inviolement de syntaxe
    # cas b, i n'est pas compris entre 0 et N-1, inviolement de syntaxe
    # cas c, j < 0 , inviolement de syntaxe
    if (len(sequence)<l) or (i<0) or (i>N-1) or(j<0) or (j>M-1):
        return False


            return coloriage_possible_rec(grille, sequence, i, j, l, -1)

def coloriage_possible_rec(grille, sequence, i, j, l, check):
    # cas 1 : l=0:
    #        -si j=0, vrai
    #        -sinon faux
    if (l==0):
        if (j==0):
            return True
        return False
    else:
        val=sequence[l-1]
        # cas 2a : si j < sl -1
        if (j<(sequence[l-1]-1)):
            return False
        # cas 2b : si j == sl-1
        #          -si l == 1, vrai
        #        -sinon faux
        elif (j==(sequence[l-1]-1)):
            if l==1:
                return True
            return False
        else:
            if (l==0) and (j>=0):
                return True
            if j<0:
                return False
            """if grille[i][j]==0:
                print(j,"\t",l,"\t",sequence[l-1])
                print(j-(sequence[l-1]-1))
                return coloriage_possible_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1)
            elif grille[i][j]==1:
                return coloriage_possible_rec(grille, sequence, i ,j-(sequence[l-1]), l-1)"""
            # Pour la premiere iteration, on ne sait pas si c'est une case blanche ou noire
                return coloriage_possible_rec(grille, sequence, i ,j-1, l, 0) or coloriage_possible_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1 ,0)
            print("Syntaxe erreur, pas colore ou valeur different que -1 0 1")
            exit()

print(coloriage_possible(grille, sequence, 1, 1, 2))
#print(coloriage_possible(grille, sequence, 1, 0, 0))
