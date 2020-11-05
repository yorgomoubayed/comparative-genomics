#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#count the COG functional categories
from collections import Counter

#ftp file
f=open("/Users/marwa/Desktop/M2/TODOOOOO/GEGO/projet/python_script/COG.csv","r")

#skip the first line of this file because it doesn't provide significant information
f.readline() 

#put the file in a list 
LEFICHIER = f.readlines()
col_interet=[]

#loops on the list (which containts the file)
for ligne in LEFICHIER:
    #split using ;
    header = ligne.split(';')
    #the COG information is on the fourth colunm
    col_interet.append(header[3].strip())
    #print(type(header[3]))
    
#print(type(int_convert))
print("Lenght : ",len(col_interet)) #+23 car certaines proteines sont dans plrs categories de fonctions
#print(col_interet)

print("Mesoplasma_florum") 

#return a dictionnary of the number of COG key = COG category, values = associated number
print(Counter(col_interet),'\n\n')