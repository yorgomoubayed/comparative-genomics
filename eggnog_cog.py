#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:47:41 2020

"""
#use counter which will help to count the COG
from collections import Counter

#EGGnog file
f=open("/Users/marwa/Desktop/M2/TODOOOOO/GEGO/projet/python_script/eggnog_COG.csv", "r")

#put the file in a list 
LEFICHIER = f.readlines()
#create 5 list for our 5 genomes
Mesoplasma_florum = Mesoplasma_chauliocola= Mesoplasma_coleopterae= list()
Entomoplasma_somnilux = Entomoplasma_melaleucae = list()

for ligne in LEFICHIER:
    #it's a csv file so we split using ;
    header = ligne.split(';')
    #cvs file containt only COG information in each columns we have differents genomes 
    Mesoplasma_florum.append(header[0].strip())
    Mesoplasma_coleopterae.append(header[1].strip())
    Mesoplasma_chauliocola.append(header[2].strip())
    Entomoplasma_melaleucae.append(header[3].strip())
    Entomoplasma_somnilux.append(header[4].strip())

#Counter :return a dictionnary of the number of COG key = COG categorie, values= their number
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