
from CAI import RSCU

#genre different
#f=open("/Users/marwa/Desktop/genome_singature/Entomoplasma_somnilux/Entomoplasma_somnilux.fna","r")
#f=open("/Users/marwa/Desktop/genome_singature/Entomoplasma_melaleucae/Entomoplasma_melaleucae.fna","r")

#genome proche
#f=open("/Users/marwa/Desktop/genome_singature/Mesoplasma_chauliocola/Mesoplasma_chauliocola.fna","r")
#f=open("/Users/marwa/Desktop/genome_singature/Mesoplasma_coleopterae/Mesoplasma_coleopterae.fna","r")

#genome d'interet
#f=open("/Users/marwa/Desktop/genome_singature/Mesoplasma_florum_W37/Mesoplasma_florum_W37.fna","r")

seq=""
ligne=f.readline() #lecture ligne par ligne

while ligne != "":
    #print( ligne)
    seq=seq+ligne[:len(ligne)-1]
    ligne=f.readline()

f.close()
#print(seq)
list_codon=[seq]

#print(list_codon)

RSCU_genome = RSCU(list_codon)
print(RSCU_genome)
RSCU_list=[]
somme=0
for key,value in RSCU_genome.items():
    RSCU_list.append(value)
    somme = somme + value
    print(value)

print(len(RSCU_list))
print(somme)


