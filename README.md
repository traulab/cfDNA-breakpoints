# cfDNA-breakpoints

Source code for PrimerNuc online tool available at http://www.primer-suite.com/primernuc/

This code requires Python 3 to run.

Tested on Spyder (Python 3.8) running on Windows 7 Enterprise operating                                                                 
Tested using Python 3.4.3 on Linux server.

**Instructions:**

Insert chromosomale regions (GRCh37/hg19 assembly) to search for nucleosome protection peaks into the **_input.bed_** file 

Run the _**PrimerNucleosome.py**_ script

Open the **_output.txt_** file for results


Results table is formatted with the following columns:

**Chromosome** #chromosome of search region from _input.bed_                                                                       
**Start position (hg19)** #first base of searched region from _input.bed_                                                              
**End position (hg19)** #last base of search region from _input.bed_                                                                    
**Region descriptor** #fourth column of _input.bed_                                                                                    
**Sample** #name of sample being search (i.e., CH01, BRA01, BRE01, COL01, BBC01)                                                         
**Nucleosome peak position (hg19)** #Protection peak position                                                                           
**Distance from start (bp)** #distance of protection peak from first base of search region                                               
**Distance from end (bp)** #distance of protection peak from first base of search region                                                 
**Within or Flanking?** #whether the peak inside the searhed region or is one of the two peaks flanking the searched region             
**WPS (mean = 1)** #Adjusted windowed protection score (WPS divided by the mean WPS of the sample (e.g. 0.5 = half mean WPS, 2 = twice mean)                                                                                                                                  
**Read depth (mean = 1)** #mean coverage of 180 bp around nucleosome protection peak divided by mean coverage of all bases in the sample (e.g. 0.06 = 6% of the mean coverage, 4.5 = 450% of the mean coverage)    

Example input:

chr1	1525652	1526652	descriptor

Example output:

chr1	1525652	1526652	descriptor	BRA01	1525635	-17	-1017	5' flanking	'n/a'	0.35                                                         
chr1	1525652	1526652	descriptor	BRA01	1525825	173	-827	within	0.64	0.3                                                             
chr1	1525652	1526652	descriptor	BRA01	1526055	403	-597	within	0.85	0.31                                                             
chr1	1525652	1526652	descriptor	BRA01	1526278	626	-374	within	'n/a'	0.22                                                             
chr1	1525652	1526652	descriptor	BRA01	1526501	849	-151	within	'n/a'	0.32                                                             
chr1	1525652	1526652	descriptor	BRA01	1526724	1072	72	3' flanking	0.53	0.23                                                         

**Note: "n/a" in the WPS column means no peak exists but greather than 370 bp (twice the mode interpeak distance from the CH01 and CA01 comprehnsive nucleosome maps of Snyder et al. (2016)) seperates the two nearest nucleosome protection peaks in this region. Additional points are placed in these regions for users to check if the lack of peak is due to either poor the sequencing coverage or broader nucleosome protection.**

Samples include: 

CH01                                                                                                                                     
BRA01                                                                                                                                   
BRE01                                                                                                                                   
COL01                                                                                                                                   
BBC01                                                                                                                                   

To alter the sample being searched, change edit the _**PrimerNucleosome.py**_ script file at line 222:

results = Nucleosome("input.bed", "output.txt", "BRA01") # input file, output file, sample name


References:

Snyder, M. W., Kircher, M., Hill, A. J., Daza, R. M., & Shendure, J. (2016). Cell-free DNA comprises an in vivo nucleosome footprint that informs its tissues-of-origin. Cell, 164(1-2), 57-68.
