### 1. Authors
Yorgo EL MOUBAYED   
Maroua CHAHDIL  

### 2. Purpose
Select four close and distant genomes to a chosen bacterial genome on which comparative genomics will be carried out.

### 3. Genome selection

#### 3.1. Select bacterial genome
**Requirements:** complete genome, CDS ranging from 500 to 1000 and in the COGs list.  

Mesoplasma florum W37 (CDS: 723).   
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/1129?genome_assembly_id=170599>   
**COG link:** <https://ftp.ncbi.nih.gov/pub/COG/COG2014/static/lists/listMesflo.html?fbclid=IwAR2tomiADkkGKvWh3yXSz5esG87EctMiGbecWbNGTbg5TrNusD3Xm7G-e1A>

#### 3.2. Select two other genomes from the same genre
**Requirements:** complete genome.  

Mesoplasma chauliocola.     
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/17787?genome_assembly_id=328413> 

Mesoplasma coleopterae.     
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/65381?genome_assembly_id=355498>   

#### 3.3. Select two other genomes from a neighbor genre
**Requirements:** complete genome.  

Entomoplasma somnilux.  
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/31059?genome_assembly_id=355484>   

Entomoplasma melaleucae.    
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/31909?genome_assembly_id=355486>   

### 4. Download RefSeq FTP repositories

### 5. Create summary table to compare features
Check the google doc on the drive.  
**Link:** <https://docs.google.com/document/d/1C0SZWxOWL4sVVi6IUKGRYBFbmO15DUQLDtyrBipb7dE/edit?usp=sharing>

### 6. eggNOG analysis

eggNOG-mapper is a tool for functional annotation of large sets of sequences based on fast orthology assignments using precomputed eggNOG clusters and phylogenies. 

#### 6.1. Sequence search on target CDS
We chose the first CDS from Mesoplasma florum (mesoplasma_florum_proteom.faa) and stored it in mesoplasma_florum_single_protein.faa. To get the results you should resubmit the job because we couldn't recover the results.

#### 6.2. eggNOG-mapper-v2 (mandatory for one genome and optional for other genomes)
Job was submitted for Mesoplasma florum.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_roi_s3js>

Job was submitted for Mesoplasma chauliocola.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_eqwo9l8l> 

Job was submitted for Mesoplasma coleopterae.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_q3od6t4t> 

Job was submitted for Entomoplasma somnilux.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_vmfu5790> 

Job was submitted for Entomoplasma melaleucae.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_fftg5l_n> 

#### 6.3. Compare eggNOG and COG functional categories (refer to summary table)
eggNOG functional categories were stored in eggnog_cog.csv.  
COGs functional categories were stored in ftp_cog.csv.  
Final values were calculated through the eggnog_cog.py and cog.py scripts and reported in the summary table.    

### 7. Genome signatures

#### 7.1. Create table for dinucleotides

#### 7.2. Create table for cumulative frequency

### 8. Mummer
MUMmer is a system for rapidly aligning large DNA sequences to one another. It can align:

*Whole genomes to other genomes
*Large genome assemblies to one another
*Partial (draft) genomes sequences to one another

**Task: ** Align chosen genome against one close and one distant genome

### 9. Core & Pan-genome

### 10. Final report 

### References
**Fast genome-wide functional annotation through orthology assignment by eggNOG-mapper.** Jaime Huerta-Cepas, Kristoffer Forslund, Luis Pedro Coelho, Damian Szklarczyk, Lars Juhl Jensen, Christian von Mering & Peer Bork.
<https://academic.oup.com/mbe/article/34/8/2115/3782716>

**eggNOG 5.0: a hierarchical, functionally and phylogenetically annotated orthology resource based on 5090 organisms and 2502 viruses.** Jaime Huerta-Cepas, Damian Szklarczyk, Davide Heller, Ana Hernández-Plaza, Sofia K Forslund, Helen Cook, Daniel R Mende, Ivica Letunic, Thomas Rattei, Lars J Jensen, Christian von Mering, Peer Bork
<https://academic.oup.com/nar/article/47/D1/D309/5173662>

**NCBI Resource Coordinators. Database resources of the National Center for Biotechnology Information.** Nucleic Acids Res. <https://pubmed.ncbi.nlm.nih.gov/29140470/>

**MUMmer4 and nucmer4 are described in "MUMmer4: A fast and versatile genome alignment system"** G. Marçais , A.L. Delcher, A.M. Phillippy, R. Coston, S.L. Salzberg, A. Zimin, PLoS computational biology (2018). <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005944>
