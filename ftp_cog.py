#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:47:41 2020

@author: marwa
"""

from collections import Counter


#FTP
f=open("/Users/marwa/Desktop/M2 /TODOOOOO/GEGO/projet/python_script/COG.csv","r")

f.readline() #utile pour FTP pas pour eggnog

LEFICHIER = f.readlines()
col_interet=[]

for ligne in LEFICHIER:
    header = ligne.split(';')
    col_interet.append(header[3].strip())
    #print(type(header[3]))
    
    
#print(type(int_convert))
print("taille : ",len(col_interet)) #+23 car certaine proteine sont dans plrs categorie de fonction
print(col_interet)
print("heelok")


#C  	 G  	 E  	 F  	 H  	 I  	 P  	 Q  	 R  	 S 
# J  	 A  	 K  	 L  	 B  	 D  	 Y  	 V  	 T  	 M  	 N  	 Z  	 W  	 U  	 O  	 X  	


print("Mesoplasma_florum")  
print(Counter(col_interet),'\n\n')



