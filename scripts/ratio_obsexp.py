


def file_to_listfreq(f):
    #read two useless line in the begining
    f.readline()
    f.readline()

    LEFICHIER = f.readlines() #read file
    list_codon=[] #put SPLITED in a list

    for ligne in LEFICHIER:
        header = ligne.split('\t')
        list_codon.append(header)
    #print(list_codon)

    list_freq_codon=[]#put only frequency of dinucleotide
    i=0
    while i < len(list_codon):

        freq_codon=list_codon[i][3]   
        #print(freq_codon) 
        list_freq_codon.append(float(freq_codon))
        i=i+1

    print(len(list_freq_codon))
    print((list_freq_codon))

    return list_freq_codon

#genre different
#f=open("/Users/marwa/Downloads/Entomoplasma_somnilux/dinu.txt","r")
#f=open("/Users/marwa/Downloads/Entomoplasma_melaleucae/dinu.txt","r")

#genome proche
#f=open("/Users/marwa/Downloads/Mesoplasma_chauliocola/dinu.txt","r")
#f=open("/Users/marwa/Downloads/Mesoplasma_coleopterae/dinu.txt","r")

#genome d'interet
f=open("/Users/marwa/Downloads/Mesoplasma_florum_W37/dinu.txt","r")

genome=file_to_listfreq(f)


############################################
#genre different
#g=open("/Users/marwa/Downloads/Entomoplasma_somnilux/dinuR.txt","r")
#g=open("/Users/marwa/Downloads/Entomoplasma_melaleucae/dinuR.txt","r")

#genome proche
#g=open("/Users/marwa/Downloads/Mesoplasma_chauliocola/dinuR.txt","r")
#g=open("/Users/marwa/Downloads/Mesoplasma_coleopterae/dinuR.txt","r")

#genome d'interet
g=open("/Users/marwa/Downloads/Mesoplasma_florum_W37/dinuR.txt","r")

Random=file_to_listfreq(g)

#Ratio Obs/Exp Exp = ramdom

def ratio(obs,exp):

    i = 0
    ratio =[] #the order of dinu is the same for the two list thus only numeric data here
    while i < len(exp):
        ratio.append(obs[i]/exp[i])
        #print(ratio)
        i=i+1

    return ratio

ratio(genome,Random)
