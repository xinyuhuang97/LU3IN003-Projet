import numpy as np
M=4
N=4

grille=np.full((M,N), -1)
grille[1][0]=0
sequence1=[1,1]
sequence2=[2,1]
# non-colore -1
# blanche 0
# noire 1

"""def annalyse_ligne(grille ,i):
    j=0
    case_j=-1
    nb_block=0
    while( j<N and grille[i][j]!=-1 ):
        if grille[i][j]==1:
            case_j=j
        else:
            if grille[i][j]==0 and case_j!=-1:
                nb_block=nb_block+1
        j=j+1
    if case_j!=-1 and nb_block==0:
        nb_block=1
    return [case_j, nb_block]
"""

def compare_block_ligne(grille, i, j, sl):
    while(j>=0 and j<N and sl>0):
        if grille[i][j]==0:
            return False
        j=j+1
        sl=sl-1
    return True

def coloriage_possible_ligne(grille, sequence, i, j, l, cl):
    # problem de syntaxe
    # cas a: si l depasse le nb d'element de la sequence, inviolement de syntaxe
    # cas b, i n'est pas compris entre 0 et N-1, inviolement de syntaxe
    # cas c, j < 0 , inviolement de syntaxe

    if (len(sequence)<l) or (i<0) or (i>N-1) or(j<0):
        return False

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
            cpt=j
            bool=0
            while(j>=0):
                if grille[i][j]!=1:
                    bool=1
                    break
            if l==1 and bool==0:
                return True
            return False
        else:
         #cas 2c
            return coloriage_possible_ligne_rec(grille, sequence, i, j, l, -1, cl )#, case_j ,nb_block)

def coloriage_possible_ligne_rec(grille, sequence, i, j, l, check ,cl):#, case_j ,nb_block):
    if (l==0) and (j>=0):
        return True
    if j<0:
        return False
    # Pour la premiere iteration, on ne sait pas si c'est une case blanche ou noire
    print(grille)
    if check ==-1:
        print(sequence[l-1],"\n")
        if cl==0:
            compare=compare_block_ligne(grille, i, j-sequence[l-1]-1, sequence[l-1])
        else:
            compare=compare_block_ligne(grille, i, j-sequence[l-1], sequence[l-1])
        if grille[i][j]==-1:
            if not (compare):
                print("1")
                return False
            else:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-(1-cl), l-1, 0, cl)

        elif grille[i][j]==1:
                return True
        elif grille[i][j]==0:
            print("2")
            return False
        else:
            print("Syntaxe erreur valeur different que -1 0 1")
            exit()
    else:
        compare_1=compare_block_ligne(grille, i, j-sequence[l-1]-1, sequence[l-1])
        compare_2=compare_block_ligne(grille, i, j-sequence[l-1], sequence[l-1])
        if grille[i][j]==-1:
            if grille[i][j-sequence[l-1]-1]==1 and compare_1:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1, 0, cl)
            elif grille[i][j-sequence[l-1]]==1 and compare_2:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1]), l-1 ,0, cl)
            elif not (compare_1 or compare_2):
                print("3")
                return False
            else:
                if grille[i][j-sequence[l-1]-1]==0:
                    return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1]), l-1 ,0, cl)
                else:
                    return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1]), l-1 ,0, cl) or coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1, 0, cl)
        elif grille[i][j]==1:
            if  compare_2:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1]), l-1 ,0, cl)
            else:
                print("4")
                return False
        elif grille[i][j]==0:
            if  compare_1:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1]-1), l-1 ,0, cl)
            else:
                print("5")
                return False
        else:
            print("Syntaxe erreur valeur different que -1 0 1")
            exit()

print(coloriage_possible_ligne(grille, sequence1, 1, 1, 2, 1))
if coloriage_possible_ligne(grille, sequence2, 1, 3, 2, 1)==True:
    grille[1][3]=1
    print(grille)
#print(coloriage_possible_ligne(grille, sequence2, 1, 3, 2, 0))
