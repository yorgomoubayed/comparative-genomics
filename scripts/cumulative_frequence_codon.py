
#genre different
#g=open("/Users/marwa/Downloads/Entomoplasma_somnilux/codon.txt","r")
#g=open("/Users/marwa/Downloads/Entomoplasma_melaleucae/codon.txt","r")

#genome proche
#g=open("/Users/marwa/Downloads/Mesoplasma_chauliocola/codon.txt","r")
g=open("/Users/marwa/Downloads/Mesoplasma_coleopterae/codon.txt","r")

#genome d'interet
#g=open("/Users/marwa/Downloads/Mesoplasma_florum_W37/codon.txt","r")


#cumulative fonction 
g.readline()
g.readline()

LEFICHIER = g.readlines()
list_codon=[]

for ligne in LEFICHIER:
    header = ligne.split('\t')

    list_codon.append(header)


print(list_codon)

list_freq_codon=[]
i=0
while i < len(list_codon):

    if 'TAG' in list_codon[i][0]:
        print("1condon stop")
    elif 'TGG' in list_codon[i][0]:
        print("2condon stop")
    elif 'TAA' in list_codon[i][0]:
        print("3condon stop")
    else:
        freq_codon=list_codon[i][3]   
        #print(freq_codon) 
        list_freq_codon.append(float(freq_codon))
    i=i+1

print(len(list_freq_codon))
print(sum(list_freq_codon))