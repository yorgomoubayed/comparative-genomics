### 1. Authors
Yorgo EL MOUBAYED   
Maroua CHAHDIL  

### 2. Purpose
Select four close and distant genomes to a chosen bacterial genome on which comparative genomics will be carried out.

### 3. Genome selection

#### 3.1. Select bacterial genome
**Requirements:** complete genome, CDS ranging from 500 to 1000 and in the COGs list.  

Mesoplasma florum W37 (CDS: 723).   
**NCBI link:**    
**COG link:** 

#### 3.2. Select two other genomes from the same genre
**Requirements:** complete genome.  

Mesoplasma chauliocola.     
**NCBI link:**  

Mesoplasma coleopterae.     
**NCBI link:**    

#### 3.3. Select two other genomes from a neighbor genre
**Requirements:** complete genome.  

Entomoplasma somnilux.  
**NCBI link:**    

Entomoplasma melaleucae.    
**NCBI link:**    

### 4. Download RefSeq FTP repositories

### 5. Create summary table to compare features
Check the google doc on the drive.  
**Link:** 

### 6. eggNOG analysis

eggNOG-mapper is a tool for functional annotation of large sets of sequences based on fast orthology assignments using precomputed eggNOG clusters and phylogenies. 

#### 6.1. Sequence search on target CDS
We chose the first CDS from Mesoplasma florum (mesoplasma_florum_proteom.faa) and stored it in mesoplasma_florum_single_protein.faa. To get the results you should resubmit the job because we couldn't recover the results.

#### 6.2. eggNOG-mapper-v2 (mandatory for one genome and optional for other genomes)
Job was submitted for Mesoplasma florum.    
**Link to results:** 

Job was submitted for Mesoplasma chauliocola.    
**Link to results:**  

Job was submitted for Mesoplasma coleopterae.    
**Link to results:**  

Job was submitted for Entomoplasma somnilux.    
**Link to results:**  

Job was submitted for Entomoplasma melaleucae.    
**Link to results:**  

#### 6.3. Compare eggNOG and COG functional categories (refer to summary table)
eggNOG functional categories were stored in eggnog_cog.csv.  
COGs functional categories were stored in ftp_cog.csv.  
Final values were calculated through the eggnog_cog.py and cog.py scripts and reported in the summary table.    

### 7. Genome signatures

#### 7.1. Create table for dinucleotides

#### 7.2. Create table for cumulative frequency

### 8. MUMmer
MUMmer is a system for rapidly aligning large DNA sequences to one another. It can align:

* Whole genomes to other genomes.
* Large genome assemblies to one another.
* Partial (draft) genomes sequences to one another.

**Task:** Align chosen genome against one close and one distant genome.

### 9. Core & Pan-genome

### 10. Final report 
Write a final report on comparative genome analysis of the five species.

### References
**Fast genome-wide functional annotation through orthology assignment by eggNOG-mapper.** Jaime Huerta-Cepas, Kristoffer Forslund, Luis Pedro Coelho, Damian Szklarczyk, Lars Juhl Jensen, Christian von Mering & Peer Bork.


**eggNOG 5.0: a hierarchical, functionally and phylogenetically annotated orthology resource based on 5090 organisms and 2502 viruses.** Jaime Huerta-Cepas, Damian Szklarczyk, Davide Heller, Ana Hernández-Plaza, Sofia K Forslund, Helen Cook, Daniel R Mende, Ivica Letunic, Thomas Rattei, Lars J Jensen, Christian von Mering, Peer Bork


**NCBI Resource Coordinators. Database resources of the National Center for Biotechnology Information.** Nucleic Acids Res. 

**MUMmer4 and nucmer4 are described in "MUMmer4: A fast and versatile genome alignment system"** G. Marçais , A.L. Delcher, A.M. Phillippy, R. Coston, S.L. Salzberg, A. Zimin, PLoS computational biology (2018). 10.1371/journal.pcbi.1005944>

Villesen, P (2007), **FaBox: an online fasta sequence toolbox**, 