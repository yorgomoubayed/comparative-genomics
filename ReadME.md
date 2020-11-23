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

* Mesoplasma chauliocola.     
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/17787?genome_assembly_id=328413> 

* Mesoplasma coleopterae.     
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/65381?genome_assembly_id=355498>   

#### 3.3. Select two other genomes from a neighbor genre
**Requirements:** complete genome.  

* Entomoplasma somnilux.  
**NCBI link:** <https://www.ncbi.nlm.nih.gov/genome/31059?genome_assembly_id=355484>   

* Entomoplasma melaleucae.    
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
* Job was submitted for Mesoplasma florum.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_roi_s3js>

* Job was submitted for Mesoplasma chauliocola.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_eqwo9l8l> 

* Job was submitted for Mesoplasma coleopterae.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_q3od6t4t> 

* Job was submitted for Entomoplasma somnilux.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_vmfu5790> 

* Job was submitted for Entomoplasma melaleucae.    
**Link to results:** <http://eggnog-mapper.embl.de/job_status?jobname=MM_fftg5l_n> 

#### 6.3. Compare eggNOG and COG functional categories (refer to summary table)
eggNOG functional categories were stored in eggnog_cog.csv.  
COGs functional categories were stored in ftp_cog.csv.  
Final values were calculated through the eggnog_cog.py and cog.py scripts and reported in the summary table.    

### 7. Genome signatures

#### 7.1. Create a table with the ratios of dinucleotides frequencies for each genome (observed/expected)
* The dinucleotides frequencies were determined by:
    * generating random genomes through **shuffleseq**. All random genomes are stored in the "random genomes" directory.
    * **compseq** for the observed and expected genomes.

* The observed/expected ratio was calculated using the **ratio_obsexp.py** script.  

#### 7.2. Create table of the cumulative frequency of the codon usage (RSCU) for each genome
* The frequency of codon usage was calculated using **compseq**.
* The cumulative frequency of codon usage was calculated using the **cumulative_frequence_codon.py** script.
* The RSCU was calculated using the **rscu.py** script.

Summary results were reported in **dinucleotide_ratio.ods** and **trinucleotide_cumulative_frequence_rcsu.ods**

* **Link to compseq:** <http://bioinfo.nhri.org.tw/cgi-bin/emboss/compseq>    
* **Link to shuffleseq:** <http://www.bioinformatics.nl/cgi-bin/emboss/shuffleseq>

### 8. MUMmer: align chosen genome against one close and one distant genome
MUMmer is a system for rapidly aligning large DNA sequences to one another. It can align:

* Whole genomes to other genomes.
* Large genome assemblies to one another.
* Partial (draft) genomes sequences to one another.

#### 8.1. Installing MUMmer
To **install** the MUMmer package (v3.23) and dependencies (gnuplot v5.2.7) with conda run the following:
~~~~
conda install -c bioconda mummer
conda install -c conda-forge gnuplot
~~~~

Or just setup the following conda environment:
~~~~
conda env create -f mummer.yml
~~~~

* **Conda source:** <https://anaconda.org/bioconda/mummer>, <https://anaconda.org/conda-forge/gnuplot>
* **MUMmer GitHub page (for detailed explanations):** <https://mummer4.github.io/index.html>

#### 8.2. Running mummer
~~~~
mummer -mum -b -c mesoplasma_florum_genome.fna entomoplasma_melaleucae_genome.fna > distant_mummer.mums
~~~~

~~~~
mummer -mum -b -c mesoplasma_florum_genome.fna mesoplasma_chauliocola_genome.fna > close_mummer.mums
~~~~
#### 8.3. Running mummerplot
~~~~
mummerplot -x "[0,825824]" -y "[0,85478]" -postscript -p mummer close_mummer.mums
~~~~

~~~~
mummerplot -x "[0,825824]" -y "[0,845295]" -postscript -p mummer distant_mummer.mums
~~~~

The following output files were generated for both distant and close genomes analysis:
* mummer.gp
* mummer.fplot
* mummer.rplot
* mummer.ps (plot figure)

### 9. Core & Pan-genome

#### 9.1. Bidirectional Best Hits (BBH) and calculate ANI, AF, AAI

##### 9.1.1. Installing blast
To **install** the blast package (v2.10.1) with conda run the following:
~~~~
conda install -c bioconda blast
~~~~
* **Conda source:** <https://anaconda.org/bioconda/blast>

Or run the following to create and activate the custom conda environment:
~~~~
conda env create blastenv
conda env activate blastenv
~~~~

##### 9.1.2. BBH and local blast
Perform BBH for each pair of genomes (AA: Criteria 30% identity / 80% coverage)

* Build a genome databse with only one genome (here we used florum_protein.faa > florumDB):
~~~~
makeblastdb -in florum_protein.faa -out florumDB -dbtype prot
~~~~

* Run blastp for proteins (i.e. for mesoplasma_chauliocola). 80% coverage is determined by -qcov_hsp_perc 80:
~~~~
blastp -query mesoplasma_chauliocola.faa -db florumDB -out QmesochauDBflorum -qcov_hsp_perc 80
~~~~

* To get to 30% identity we use the command awk and filter the third columns (which is the identity) then put the result into a new file named final_result.
~~~~
awk '$3>=30' QmesochauDBflorum >> final_result.txt
~~~~

#### 9.2. Calculate ANI, AF, AAI
Average Nucleotide Identity (ANI) and Alignment Fraction (AF) are calculated through the [IMG website](https://img.jgi.doe.gov/cgi-bin/m/main.cgi?section=ANI&page=pairwise)

AAI is similar to ANI. It's the measure of global protein similarity between the set of gene products (protein) between the genomes. 

#### 9.3. OrthoVenn2
OrthoVenn is a web platform for comparison and annotation of orthologous gene clusters among multiple species.

Job was submitted using the 5 species' proteoms files as input.    
**Link to results:** <https://orthovenn2.bioinfotoolkits.net/task/result/00a4e2ed85b530f9b9de2af5b4b1e2b0>

### 10. Final report 
Write a 20-25 pages report on comparative genome analysis of the five species.

### References
* **Fast genome-wide functional annotation through orthology assignment by eggNOG-mapper.** Jaime Huerta-Cepas, Kristoffer Forslund, Luis Pedro Coelho, Damian Szklarczyk, Lars Juhl Jensen, Christian von Mering & Peer Bork.

* **eggNOG 5.0: a hierarchical, functionally and phylogenetically annotated orthology resource based on 5090 organisms and 2502 viruses.** Jaime Huerta-Cepas, Damian Szklarczyk, Davide Heller, Ana Hernández-Plaza, Sofia K Forslund, Helen Cook, Daniel R Mende, Ivica Letunic, Thomas Rattei, Lars J Jensen, Christian von Mering, Peer Bork

* **NCBI Resource Coordinators. Database resources of the National Center for Biotechnology Information.** Nucleic Acids Res. 

* Kurtz S, Phillippy A, Delcher AL, Smoot M, Shumway M, Antonescu C, Salzberg SL. **Versatile and open software for comparing large genomes**. Genome biology. 2004 Jan 1;5(2):R12.

* Villesen, P (2007), **FaBox: an online fasta sequence toolbox**, <http://www.birc.au.dk/software/fabox>

* Rice P., Bleasby A and Ison J. **The EMBOSS Users Guide**. Cambridge University Press

* Xu L, Dong Z, Fang L, Luo Y, Wei Z, Guo H, Zhang G, Gu YQ, Coleman-Derr D, Xia Q, Wang Y. **OrthoVenn2: a web server for whole-genome comparison and annotation of orthologous clusters across multiple species**. Nucleic Acids Res. 2019 Jul.

* Chen IA, Chu K, Palaniappan K, Pillay M, Ratner A, Huang J, Huntemann M, Varghese N, White JR, Seshadri R, Smirnova T, Kirton E, Jungbluth SP, Woyke T, Eloe-Fadrosh EA, Ivanova NN, Kyrpides NC. **IMG/M v.5.0: an integrated data management and comparative analysis system for microbial genomes and microbiomes**. Nucleic Acids Res. 2019 Jan.