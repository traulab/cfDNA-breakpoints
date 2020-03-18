# cfDNA-breakpoints

Source code for PrimerNuc online tool available at http://www.primer-suite.com/primernuc/

This code requires Python 3 to run.

Tested on Spyder (Python 3.8) running on Windows 7 Enterprise operating system                                                                
Tested using Python 3.4.3 on Linux server.


**Description:**

PrimerNuc is search tool that enables users to locate all predicted nucleosome protection peaks within an input chromosomal region or the two nearest protection peaks flanking a specified nucleotide position. Along with peak positions, this software outputs the adjusted WPS (WPS divided by the mean WPS of the sample pool), the adjusted sequencing depth (coverage divided by the mean coverage of the sample pool), and distances (bp) of the output peak positions to the two input nucleotide positions.


**Instructions:**

Insert chromosomal regions (GRCh37/hg19 assembly) to search for nucleosome protection peaks into the **_input.bed_** file 

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

chr1	10000000	10000700	region                                                                                                      
chr1	1000000	1000000	single base                                                                                                       

Example output:

chr1	10000000	10000700	region	BRA01	9999792	-208	-908	5' flanking	'n/a'	0.35                                                      
chr1	10000000	10000700	region	BRA01	10000007	7	-693	within	'n/a'	0.38                                                      
chr1	10000000	10000700	region	BRA01	10000222	222	-478	within	'n/a'	0.26                                                           
chr1	10000000	10000700	region	BRA01	10000439	439	-261	within	0.96	0.24                                                      
chr1	10000000	10000700	region	BRA01	10000658	658	-42	within	0.74	0.22                                                      
chr1	10000000	10000700	region	BRA01	10000750	750	50	3' flanking	0.64	0.21                                                      
chr1	1000000	1000000	single base	BRA01	999850	-150	-150	5' flanking	1.28	0.18                                                      
chr1	1000000	1000000	single base	BRA01	1000036	36	36	3' flanking	'n/a'	0.16                                                      

**Note: "n/a" in the WPS column means no peak exists but greather than 370 bp (twice the mode interpeak distance from the CH01 and CA01 comprehnsive nucleosome maps of Snyder et al. (2016)) seperates the two nearest nucleosome protection peaks in this region. Additional points are placed in these regions for users to check if the lack of peak is due either to poor sequencing coverage or broader nucleosome protection.**

Samples include: 

CH01 #nucleosome protection peaks from Snyder et al. (2016)                                                                             
BRA01 #Brain cancer sample pool                                                                                                 
BRE01 #Breast cancer sample pool                                                                                                         
COL01 #Colorectal cancer sample pool                                                                                                    
BBC01 #Pool of BRA01, BRE01 and COL01                                                                                                                                   

To alter the sample being searched, change edit the _**PrimerNucleosome.py**_ script file at line 222:

results = Nucleosome("input.bed", "output.txt", "BRA01") # input file, output file, sample name


**References:**

Snyder, M. W., Kircher, M., Hill, A. J., Daza, R. M., & Shendure, J. (2016). Cell-free DNA comprises an in vivo nucleosome footprint that informs its tissues-of-origin. Cell, 164(1-2), 57-68.
