#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#count the COG functional categories
from collections import Counter

#eggNog file
f=open("/Users/marwa/Desktop/M2/TODOOOOO/GEGO/projet/python_script/eggnog_COG.csv", "r")

#store the file in a list 
LEFICHIER = f.readlines()

#create 5 lists for the 5 genomes
Mesoplasma_florum = Mesoplasma_chauliocola= Mesoplasma_coleopterae= list()
Entomoplasma_somnilux = Entomoplasma_melaleucae = list()

for ligne in LEFICHIER:
    #split using ;
    header = ligne.split(';')
    #csv file containt only COG information in each columns we have differents genomes 
    Mesoplasma_florum.append(header[0].strip())
    Mesoplasma_coleopterae.append(header[1].strip())
    Mesoplasma_chauliocola.append(header[2].strip())
    Entomoplasma_melaleucae.append(header[3].strip())
    Entomoplasma_somnilux.append(header[4].strip())

#Counter: return a dictionnary of the number of COG key = COG category, values = associated number
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