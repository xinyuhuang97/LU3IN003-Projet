from abc import ABC, abstractmethod
from enum import Enum
import numpy as np
import sys


class Couleur(Enum):
    Blanc=0
    Noir=1
    PasColore=-1

class Statut(Enum):
    Vrai=1
    Faux=0
    NeSaitPas=-1

#M=5
#N=5
#grille=np.full((M,N), Statut.Vrai)
#print(grille)


class Grille:
    """
    Classe definissant un Grille par
    - Une matrice de cases colore (x,y)
    - Une matrice de forme T(j,l) horizontal => ligne x fixe, y=j
    - Une matrice de forme T(j,l) vertical => colonne y fixe, x=j
    """
    def __init__(self, namefile):
        try:
            in_file = open(sys.argv[1], "r")
        except:
            sys.exit("ERROR. Can't read supplied filename.")
        text = in_file.read()
        lg=len(text)
        cpt_l=1
        M=0
        N=0
        i=0
        newline=0
        while(i<lg-1):
            if(text[i]=='\n'):
                cpt_l=cpt_l+1
            if(text[i]=='#'):
                M=cpt_l-1
            i+=1
        N=cpt_l-M-1
        self.M=M
        self.N=N
        somme=self.M+self.N
        s_grille=np.full((somme,somme),0)
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
                            if (text[i+1]>='1' and text[i]<='9'):
                                last_caratere=1
                                val=10*text[i]
                            else:
                                s_grille[line][colonne]=text[i]
                                colonne=colonne+1
                                last_caratere=1
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
        self.grille_d=s_grille

#s_grille=np.full((M+N,M+N),0)
g=Grille(sys.argv[1])

print(g.M, g.N, g.grille_d)
