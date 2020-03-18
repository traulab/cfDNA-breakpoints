# cfDNA-breakpoints

Source code for PrimerNuc online tool available at http://www.primer-suite.com/primernuc/

This code requires Python 3 to run.

Tested on Spyder (Python 3.8) running on Windows 7 Enterprise operating
Test using Python 3.4.3 on Linux server.

Instructions:

Insert chromosomale regions (GRCh37/hg19 assembly) to search for nucleosome protection peaks into the "input.bed" file 
e.g. chr1	1000000	1000500	Descriptor

Run the PrimerNucleosome.py script

Open the "output.txt" file for results


Results table is formatted with the following columns:

Chromosome #chromosome of search region from "input.bed"
Start position (hg19) #first base of searched region from "input.bed"
End position (hg19) #last base of search region from "input.bed"
Region descriptor #fourth column of "input.bed"
Sample #name of sample being search (i.e., CH01, BRA01, BRE01, COL01, BBC01)
Nucleosome peak position (hg19) #Protection peak position
Distance from start (bp) #distance of protection peak from first base of search region
Distance from end (bp) #distance of protection peak from first base of search region
Within or Flanking? #whether the peak inside the searhed region or is one of the two peaks flanking the searched region
WPS (mean = 1) #Adjusted windowed protection score (WPS divided by the mean WPS of the sample (e.g. 0.5 = half mean WPS, 2 = twice mean)
Read depth (mean = 1) #mean coverage of 180 bp around nucleosome protection peak divided by mean coverage of all bases in the sample


Example output:

chr1	1525652	1526652	1	BRA01	1525635	-17	-1017	5' flanking	'n/a'	0.35
chr1	1525652	1526652	1	BRA01	1525825	173	-827	within	0.64	0.3
chr1	1525652	1526652	1	BRA01	1526055	403	-597	within	0.85	0.31
chr1	1525652	1526652	1	BRA01	1526278	626	-374	within	'n/a'	0.22
chr1	1525652	1526652	1	BRA01	1526501	849	-151	within	'n/a'	0.32
chr1	1525652	1526652	1	BRA01	1526724	1072	72	3' flanking	0.53	0.23

