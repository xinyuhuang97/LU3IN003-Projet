import numpy as np
import sys
import string
M=4
N=5

# grille  rempli par sequence
s_grille=np.full((M+N,M+N),0)
# grille remplit par 0 -1 1
grille=np.full((M,N), -1)
#grille[1][0]=0
sequence1=[1,1]
sequence2=[2,1]
# non-colore -1
# blanche 0
# noire 1

def lire_fichier(s_grille):
    #file=sys.argv[1:]
    try:
        in_file = open(sys.argv[1], "r")
    except:
        sys.exit("ERROR. Can't read supplied filename.")
    text = in_file.read()
    lg=len(text)
    i=0
    nextline=0
    line=0
    colonne=0
    bool=0
    j=0
    while(i<lg-1):
            if(text[i]=='\n'):
                nextline=1
                if(bool==1):
                    bool=0
                else:
                    line=line+1
                i=i+1
                colonne=0
                continue
            else:
                if nextline==1:
                    if text[i]=="0x20":
                        if text[i+1]!="0x20" and text[i+1]!="\n":
                            s_grille[line][colonne]=0
                            colonne=colonne+1
                            nextline==1
                        else:
                            nextline==1
                    elif (text[i]>='1' and text[i]<='9'):
                        s_grille[line][colonne]=text[i]
                        colonne=colonne+1
                        nextline==0
                    elif text[i]=='#':
                        j=line-1
                        bool=1
                        nextline==0
                    else:
                        nextline==0
                if nextline==0:
                    #print("hi")
                    if (text[i]>='1' and text[i]<='9'):
                        s_grille[line][colonne]=text[i]
            i=i+1
            #print(s_grille)
    in_file.close()
    return s_grille


def compare_block_ligne(grille, i, j, sl):
    if ((j+1<N) and (grille[i][j+1]==1))or ((j-1>=0) and (grille[i][j-1]==1)):
        return False
    while(j>=0 and j<N and sl>0):
        if grille[i][j]==0:
            return False
        j=j+1
        sl=sl-1
    return True

def compare_block_colonne(grille, i, j, sl):
    if ((i+1<M) and (grille[i+1][j]==1))or ((i-1>=0) and (grille[i-1][j]==1)):
        return False
    while(i>=0 and i<M and sl>0):
        if grille[i][j]==0:
            return False
        i=i+1
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
        print("1false")
        return False
    else:
        val=sequence[l-1]
        print("s", sequence[l-1])
        # cas 2a : si j < sl -1
        if (j<(sequence[l-1]-1)):
            print("2false")
            return False
        # cas 2b : si j == sl-1
        #          -si l == 1, vrai
        #        -sinon faux
        elif (j==(sequence[l-1]-1)):
            cpt=j
            bool=0
            while(j>=0):
                if grille[i][j]==0 or cl==0:
                    bool=1
                    break
                j=j-1
            print(l, bool)
            if l==1 and bool==0:
                print("ABC true")
                return True
            print("3false")
            return False
        else:
         #cas 2c
            return coloriage_possible_ligne_rec(grille, sequence, i, j, l, -1, cl )#, case_j ,nb_block)

def coloriage_possible_ligne_rec(grille, sequence, i, j, l, check ,cl):#, case_j ,nb_block):

    if (l==0) and j>=-1 :
        print("ABC True")
        return True
    if j<0:
        print(i, j, l)
        print(grille)
        print("0false")
        return False
    # Pour la premiere iteration, on ne sait pas si c'est une case blanche ou noire
    print(grille)
    if check ==-1:
        if cl==0:
            compare=compare_block_ligne(grille, i, j-sequence[l-1], sequence[l-1])
        else:
            compare=compare_block_ligne(grille, i, j-sequence[l-1]+1, sequence[l-1])
        print("i, j", i, j,"compare:", compare, "l", l)
        if grille[i][j]==-1:
            if not (compare):
                print("4false")
                return False
            else:
                if(j==0) and l==1 and sequence[0]==1:
                    return True
                print("here i j", i ,j-(sequence[l-1])-(1-cl)-1)
                if (j-(sequence[l-1])-(1-cl)-1<-1):
                    return  coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1]), l-1, 0, cl)

                return  coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-(1-cl)-1, l-1, 0, cl)

        elif grille[i][j]==1:
                if(j==0) and l==1 and sequence[0]==1:
                    return True
                if cl==0:
                    return False
                if  compare:
                    return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1 ,0, cl)
                return False
        elif grille[i][j]==0:
            if(j==0) and l==1 and sequence[0]==1:
                return False
            if cl==1:
                return False
            if  compare:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-2, l-1 ,0, cl)
            return False
        else:
            print("Syntaxe erreur valeur different que -1 0 1")
            exit()
    else:
        compare_1=compare_block_ligne(grille, i, j-sequence[l-1], sequence[l-1])
        compare_2=compare_block_ligne(grille, i, j-sequence[l-1]+1, sequence[l-1])
        print("i, j", i, j,"compare1:", compare_1, "l",l)
        print("i, j", i, j,"compare2:", compare_2, "l",l)
        if grille[i][j]==-1:
            if(j==0) and l==1 and sequence[0]==1:
                return True
            #print(i,j-sequence[l-1] ,sequence[l-1])
            if grille[i][j-sequence[l-1]-1]==1 and compare_1:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-2, l-1, 0, cl)

            elif grille[i][j-sequence[l-1]]==1 and compare_2:
                #if(j==0):
                #    return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1]), l-1 ,0, cl)
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1 ,0, cl)
            elif not (compare_1 or compare_2):
                print("6false")
                return False
            else:
                if grille[i][j-sequence[l-1]-1]==0:
                    l=len(sequence[l-1])
                    while(l>=0):
                        list[i][j-(sequence[l-1])+l]=1
                        l=l-1
                    return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1 ,0, cl)
                else:
                    print("or")
                    if (j==0) and sequence[l-1]==1:
                        print("ABC True")
                        return True
                    return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1 ,0, cl) or coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-2, l-1, 0, cl)
        elif grille[i][j]==1:
            if(j==0) and l==1 and sequence[0]==1:
                return True
            if  compare_2:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-1, l-1 ,0, cl)
            else:
                print("7false")
                return False
        elif grille[i][j]==0:
            if(j==0) and l==1 and sequence[0]==1:
                return False
            if  compare_1:
                return coloriage_possible_ligne_rec(grille, sequence, i ,j-(sequence[l-1])-2, l-1 ,0, cl)
            else:
                print("8false")
                return False
        else:
            print("Syntaxe erreur valeur different que -1 0 1")
            exit()

def coloriage_possible_colonne(grille, sequence, i, j, l ,cl):
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
        if (i==0):
            return True
        print("11false")
        return False
    else:
        print("i")
        val=sequence[l-1]
        # cas 2a : si j < sl -1
        if (i<(sequence[l-1]-1)):
            print("22false")
            return False
        # cas 2b : si j == sl-1
        #          -si l == 1, vrai
        #        -sinon faux
        elif (i==(sequence[l-1]-1)):
            cpt=i
            bool=0
            while(i>=0):
                if grille[i][j]==0 or cl==0:
                    bool=1
                    break
                i=i-1
            if l==1 and bool==0:
                print("ABC true")
                return True
            print("33false")
            return False
        else:
         #cas 2c
            return coloriage_possible_colonne_rec(grille, sequence, i, j, l, -1 ,cl)#, case_j ,nb_block)

def coloriage_possible_colonne_rec(grille, sequence, i, j, l, check, cl):#, case_j ,nb_block):
    if (l==0) and (i>=-1):
        print("ABC true")
        return True
    if i<0:
        print("44false")
        return False
    # Pour la premiere iteration, on ne sait pas si c'est une case blanche ou noire

    print(grille)
    if check ==-1:
        if cl==0:
            compare=compare_block_colonne(grille, i-sequence[l-1], j, sequence[l-1])
        else:
            compare=compare_block_colonne(grille, i-sequence[l-1]+1, j, sequence[l-1])
        print("i, j", i, j,"compare:", compare, "l", l)
        if grille[i][j]==-1:
            if not (compare):
                print("55false")
                return False
            else:
                if(i==0) and l==1 and sequence[0]==1:
                    return True
                print("here i j", i-(sequence[l-1])-(1-cl)-1 ,j)
                if (i-(sequence[l-1])-(1-cl)-1<-1):
                    return coloriage_possible_ligne_rec(grille, sequence, i-(sequence[l-1]) ,j, l-1, 0, cl)
                return coloriage_possible_ligne_rec(grille, sequence, i-(sequence[l-1])-(1-cl)-1 ,j, l-1, 0, cl)

        elif grille[i][j]==1:
            if(i==0) and l==1 and sequence[0]==1:
                return True
            if  compare:
                return coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-1 ,j, l-1 ,0, cl)
            else:
                ##print("77false")
                return False
        elif grille[i][j]==0:
            return False
        else:
            print("Syntaxe erreur valeur different que -1 0 1")
            exit()
    else:
        compare_1=compare_block_colonne(grille, i-sequence[l-1], j, sequence[l-1])
        compare_2=compare_block_colonne(grille, i-sequence[l-1]+1, j, sequence[l-1])
        print("i, j", i, j,"compare1:", compare_1, "l",l)
        print("i, j", i, j,"compare2:", compare_2, "l",l)
        if grille[i][j]==-1:
            if grille[i][j-sequence[l-1]-1]==1 and compare_1:
                return coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-2 ,j, l-1, 0, cl)
            elif grille[i][j-sequence[l-1]]==1 and compare_2:
                if(i==0):
                    return coloriage_possible_ligne_rec(grille, sequence, i-(sequence[l-1]) ,j, l-1 ,0, cl)
                return coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-1 ,j, l-1 ,0, cl)
            elif not (compare_1 or compare_2):
                print("66false")
                return False
            else:
                if grille[i][j-sequence[l-1]-1]==0:
                    return coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-1 ,j, l-1 ,0, cl)
                else:
                    if (j==0) and sequence[l-1]==1:
                        print("ABC True")
                        return True
                    return coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-1 ,j, l-1 ,0, cl) or coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-2 ,j, l-1, 0, cl)
        elif grille[i][j]==1:
            if(i==0) and l==1 and sequence[0]==1:
                return True
            if  compare_2:
                return coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-1 ,j, l-1 ,0, cl)
            else:
                print("77false")
                return False
        elif grille[i][j]==0:
            if(i==0) and l==1 and sequence[0]==1:
                return False
            if  compare_1:
                return coloriage_possible_colonne_rec(grille, sequence, i-(sequence[l-1])-2 ,j, l-1 ,0, cl)
            else:
                print("88false")
                return False
        else:
            print("Syntaxe erreur valeur different que -1 0 1")
            exit()

def dupliquer(grille):
    grille_d=np.full((M,N), -1)
    for i in range(M):
        for j in range(N):
            grille_d[i][j]=grille[i][j]
    return grille_d

def creer_sequence(indice, direction):
    init=1
    k=0
    sequence=[]
    #print(s_grille)
    if direction==1:
        while(k<M):
            if(s_grille[indice][k]!=0 or init==1):
                sequence.append(s_grille[indice][k])
                #print("this",indice, k)
                #print(s_grille[indice][k])
                init=0
            k=k+1
    elif direction==2:
        while(k<N):
            if(s_grille[indice+M][k]!=0 or init==1):
                sequence.append(s_grille[indice+M][k])
                init=0
            k=k+1
    return sequence

def coloreLig(grille, i):
    sequence=creer_sequence(i,1)# 1 signifie ligne 2 signifie colonne
    l=len(sequence)
    a=0
    somme_sequence=0

    while (a<l):
        somme_sequence=somme_sequence+sequence[a]
        a=a+1
    j=N-1
    bool=0
    print("----------------------",sequence)
    while(j>=0 and l>0):
        print("i",i, "j", j, "l", l)
        resultat_blanc=(coloriage_possible_ligne(grille, sequence, i, j, l, 0))
        print("noir")
        resultat_noir=(coloriage_possible_ligne(grille, sequence, i, j, l, 1) )
        print("resultat_blanc, resultat_noir",resultat_blanc, resultat_noir)
        k=j


        if resultat_noir==True:
            bool=1
            if resultat_blanc==False:
                s=sequence[l-1]
                print(l-1)
                while(s>0):
                    print("in while")
                    print(sequence)
                    grille[i][k]=1
                    k=k-1
                    s=s-1
                del sequence[l-1]
            else:
                nb=j-1
                min=j
                max=-1
                while(nb>=0):
                    #print(grille[i][nb], nb)
                    if grille[i][nb]==1:
                        if(grille[i][nb]>max):
                            max=nb
                        if(grille[i][nb]<min):
                            min=nb
                    nb=nb-1
                print("max",max)
                print("min",min)

                l=len(sequence)
                print("************l",l,"max-min+1", max-min+1)
                print((l==1 and max-min+1==sequence[l-1]))
                if not (l==1 and max-min+1==sequence[l-1]):
                    print("why?")
                    del sequence[l-1]

        print("fin")
        if resultat_noir==False and resultat_blanc==False and j==N-1:
            print(i, j)
            return (False, grille)
        j=k-1
        l=len(sequence)
        if(j<0 and l>0):
            del sequence[l-1]
            j=M-1
        l=len(sequence)
    if(bool==1):
        return (True,grille)
    print("what")
    return (False, grille)


    return resultat
def coloreCol(grille, j):
    sequence=creer_sequence(j,2)# 1 signifie ligne 2 signifie colonne
    l=len(sequence)
    i=M-1
    bool=0
    print("----------------------",sequence)
    while(i>=0 and l>0):
        bool_del=0
        print("i",i, "j", j, "l", l)
        resultat_blanc=(coloriage_possible_colonne(grille, sequence, i, j, l, 0))
        print("noir")
        resultat_noir=(coloriage_possible_colonne(grille, sequence, i, j, l, 1) )
        print("resultat_blanc, resultat_noir",resultat_blanc, resultat_noir)
        print("l=",l)
        k=i
        if resultat_noir==True:
            bool=1
            if resultat_blanc==False:
                s=sequence[l-1]
                k=i
                while(s>0):
                    print("welcome")
                    grille[k][j]=1
                    k=k-1
                    s=s-1
                del sequence[l-1]
            else:
                nb=i-1
                min=i
                max=-1
                while(nb>=0):
                    #print(grille[i][nb], nb)
                    if grille[nb][j]==1:
                        if(grille[nb][j]>max):
                            max=nb
                        if(grille[nb][j]<min):
                            min=nb
                    nb=nb-1
                if not (l==1 and max-min+1==sequence[l-1]):
                    print("why?")
                    del sequence[l-1]
            #del sequence[-1]

        print("fin")
        #if resultat_blanc==True:
        #    if resultat_noir==False:

        if resultat_noir==False and resultat_blanc==False and i==M-1:
            print(i, j)
            return (False, grille)
        i=k-1
        #l=len(sequence)
        #if(i<=0 and l>0):
        #    if(bool_del!=1):
        #        del sequence[-1]
        #i=M-1"""
        l=len(sequence)
    if(bool==1):
        return (True,grille)
    print("what")
    return (False, grille)

def coloration(grille):
    grille_d=dupliquer(grille)
    LigneAVoir=set()
    ColonneAVoir=set()
    i=M-1
    j=N-1
    while (i>=0):
        LigneAVoir.add(i)
        i=i-1
    while(j>=0):
        ColonneAVoir.add(j)
        j=j-1
    while ((LigneAVoir!=set())or(ColonneAVoir!=set())):
        while (LigneAVoir):
            i=LigneAVoir.pop()
            (ok,grille_d)=coloreLig(grille_d, i)
            if ok==False:
                print("hi")
                print(grille_d)
                return (-1, [[]])#matrice vide!!
            Nouveaux=set()
            for j in range(N):
                if grille_d[i][j]==1:
                    Nouveaux.add(j)
            ColonneAVoir=ColonneAVoir.union(Nouveaux)
        while(ColonneAVoir):
            j=ColonneAVoir.pop()
            (ok,grille_d)=coloreCol(grille_d, j)
            if ok==False:
                print("hello")
                return (False, [[]])#matrice vide!
            Nouveaux=set()
            for i in range(M):
                if grille_d[i][j]==1:
                    Nouveaux.add(i)
            print("-------Nouveaux-------",Nouveaux)
            print("-------LigneAVoir-------",LigneAVoir)
            LigneAVoir=LigneAVoir.union(Nouveaux)
            print("-------LigneAVoir-------",LigneAVoir)
    for i in range(M) :
        for j in range(N) :
            if(grille_d[i][j]!=0 and grille_d[i][j]!=1):
                return (0, grille_d)
    return (1,grille_d)


#print(coloriage_possible(grille, sequence1, 1, 1, 2))
#print(coloriage_possible(grille, sequence2, 1, 3, 2))
lire_fichier(s_grille)
print(s_grille)
print(coloration(grille))
