#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:47:41 2020

@author: marwa
"""

from collections import Counter

#eggnog
f=open("/Users/marwa/Desktop/M2/TODOOOOO/GEGO/projet/python_script/eggnog_COG.csv", "r")

LEFICHIER = f.readlines()
Mesoplasma_florum = Mesoplasma_chauliocola= Mesoplasma_coleopterae= list()
Entomoplasma_somnilux = Entomoplasma_melaleucae = list()

#col_interet=[]
for ligne in LEFICHIER:
    header = ligne.split(';')
    #col_interet.append(header[3].strip())
    Mesoplasma_florum.append(header[0].strip())
    Mesoplasma_coleopterae.append(header[1].strip())
    Mesoplasma_chauliocola.append(header[2].strip())
    Entomoplasma_melaleucae.append(header[3].strip())
    Entomoplasma_somnilux.append(header[4].strip())
    #print(type(header[3]))
    
#C  	 G  	 E  	 F  	 H  	 I  	 P  	 Q  	 R  	 S 
# J  	 A  	 K  	 L  	 B  	 D  	 Y  	 V  	 T  	 M  	 N  	 Z  	 W  	 U  	 O  	 X  	

print("Mesoplasma_florum")  
print(Counter(Mesoplasma_florum),'\n\n')

print("Mesoplasma_coleopterae")  
print(Counter(Mesoplasma_coleopterae),'\n\n')

print("Mesoplasma_chauliocola")  
print(Counter(Mesoplasma_chauliocola),'\n\n')

print("Entomoplasma_melaleucae")  
print(Counter(Entomoplasma_melaleucae),'\n\n')

print("Entomoplasma_somnilux")  
print(Counter(Entomoplasma_somnilux),'\n\n')