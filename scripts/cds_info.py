from statistics import mean


#f=open("/Users/marwa/Downloads/Mesoplasma florum W37.txt","r")
#f=open("/Users/marwa/Downloads/Mesoplasma_chauliocola.txt","r")
#f=open("/Users/marwa/Downloads/Mesoplasma_coleopterae.txt","r")
#f=open("/Users/marwa/Downloads/Entomoplasma_somnilux.txt","r")
f=open("/Users/marwa/Desktop/M2 /TODOOOOO/GEGO/projet/files/Entomoplasma_melaleucae.txt","r")





f.readline() # la premier colonne osf
LEFICHIER = f.readlines()
col_interet = []
int_convert=0
for ligne in LEFICHIER:
    header = ligne.split('\t')

    if (header[0] == "gene"):
        int_convert = int(header[17])
        col_interet.append(int_convert)

    
    

#print(type(int_convert))
print("taille : ",len(col_interet))
#print(col_interet)
print("heelok")

CDS_lenght=[]
i=0
while (i < len(col_interet)):
    #print(col_interet[i])
    CDS_lenght.append(col_interet[i])
    i=i+1
    
    
print("Le nombre de  de CDS est de ",len(CDS_lenght))
print("La taille max des CDS est de  ",max(CDS_lenght))
print("La taille moyenne des CDS est de ",mean(CDS_lenght))

"""
    if (header[0] == "CDS" and header[1]=="with_protein"):
        int_convert = int(header[17])
        col_interet.append(int_convert)
"""

