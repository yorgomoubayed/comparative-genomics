#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:47:41 2020

"""
#use counter which will help to count the COG
from collections import Counter


#FTP file
f=open("/Users/marwa/Desktop/M2 /TODOOOOO/GEGO/projet/python_script/COG.csv","r")

#skip the first line of this file because it doesn't provide significiant informations
f.readline() 

#put the file in a list 
LEFICHIER = f.readlines()
col_interet=[]

#loops on the list (which containt the file)
for ligne in LEFICHIER:
    #it's a csv file so we split using ;
    header = ligne.split(';')
    #the COG information is on the fourth colunm
    col_interet.append(header[3].strip())
    #print(type(header[3]))
    
    
#print(type(int_convert))
print("Lenght : ",len(col_interet)) #+23 car certaine proteine sont dans plrs categorie de fonction
#print(col_interet)


print("Mesoplasma_florum")  
#return a dictionnary of the number of COG key = COG categorie, values= their number
print(Counter(col_interet),'\n\n')



