# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 21:08:40 2025

@author: frome
"""

import random
def tirarDados():
    return random.randrange(1,7)

pista=["_"]*15
pista[0]="C"


ronda=0
index=0
print("ESTADO INICIAL")
print(pista)
while pista[14]!="R":
    saltos=tirarDados()
    pista[index]="_"
    if ronda%2==0:
        if index+saltos>len(pista)-1:
            pista[14]="R"
            index=14
        else:
            pista[index+saltos]="R"
            index+=saltos        
    else:
        if index-saltos<0:
            pista[0]="R"
            index=0
        else:
            pista[index-saltos]="R"
            index-=saltos
        
    ronda+=1
    print(f"Ronda {ronda}:  DADO --> {saltos}")
    print(pista)
