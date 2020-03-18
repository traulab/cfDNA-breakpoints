# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:14:34 2018
@author: s4142554

"""

from collections import OrderedDict
import time

#############################################################
def readBed2Dict(inputBedFile):
    
    BedDict = OrderedDict()
    with open(inputBedFile, 'r') as bedFile:
        for line in bedFile:
            #only reads lines which starts with chr
            if line.startswith("chr"):
                line = line.strip().split("\t")
    
                chrom = line[0]
                start = int(line[1])
                end = int(line[2])
                
                #check name of region
                try:
                    name = line[3]
                except:
                    name = ''.join([chrom, ':', line[1], '-', line[2]])
                
                rline = [chrom, start, end, name]
                #add to dict with the chrom as the key
                if chrom in BedDict:
                    BedDict[chrom].append(rline)
                else:
                    BedDict[chrom] = [rline]
            
    return BedDict

#############################################################

def getFirstPeak(start, L_Coveragepeaks):

    search_region = [0, len(L_Coveragepeaks)-1]
    prev_reg = ''
    
    first_NPP = search_region[0]
    last_NPP = search_region[1]
    middle_NPP = int(len(L_Coveragepeaks[first_NPP:last_NPP])/2)    
    
    
    while search_region != prev_reg or search_region[1] - search_region[0] > 1:
        
        prev_reg = search_region
        
        if start in range(L_Coveragepeaks[first_NPP][0], L_Coveragepeaks[middle_NPP][0]):
            search_region = [first_NPP, middle_NPP]
        elif start in range(L_Coveragepeaks[middle_NPP][0], L_Coveragepeaks[last_NPP][0]):
            search_region = [middle_NPP, last_NPP]
        else:
            return None
        
        first_NPP = search_region[0]
        last_NPP = search_region[1]
        middle_NPP = first_NPP + int(len(L_Coveragepeaks[first_NPP:last_NPP])/2)    
    
    return search_region[0]

#############################################################
    
#retrieves a list of coords and scores of all peaks within the region of interest (start, end)
def getPeaks(start, end, L_Coveragepeaks):

    flank = 1000 #bp of flanking region from start/end coord
    
    PeakTable = L_Coveragepeaks #result table for peakList
    
    ###
    #determine 3 regions
    flank5Start = start-flank #1-5' flanking region start
    flank5End = start #2 - start of region

    #determine 5' end
    flank3Start = end #3 - end of region
    flank3End = end+flank #4 - 3' flanking region end

    #add relavent region into dict
    PeakDict = OrderedDict()
    flank5pList = []
    #withinList = []
    flank3pList = []
    
    first_peak = getFirstPeak(flank5Start, L_Coveragepeaks)
    
    #within, 5', 3' 

    #pull all relavent coords into dict.
    for i, line in enumerate(PeakTable[first_peak:]):
        coord = line[0]
        score = line[1:]

        #if within fragment
        if coord in range(start, end):
            region = 'within'
            to5p = coord - start #start - coord #to 5' start
            to3p = coord - end #end - coord #to 3' end
            PeakDict[coord]=[region]
            PeakDict[coord].extend([to5p, to3p])
            PeakDict[coord].extend(score)
        
        #if within the 5' flank region #check
        elif coord in range(flank5Start, flank5End):
            region = "5' flanking"
            to5p = coord - start #start - coord #to 5' start
            to3p = coord - end #end - coord #to 3' end
            rlist = [coord, region]
            rlist.extend([to5p, to3p])
            rlist.extend(score)
            flank5pList.append(rlist)

        #if within the 3' flank region #check        
        elif coord in range(flank3Start, flank3End):
            region = "3' flanking"
            to5p = coord - start #start - coord #to 5' start
            to3p = coord - end #end - coord #to 3' end
            rlist = [coord, region]
            rlist.extend([to5p, to3p])
            rlist.extend(score)
            flank3pList.append(rlist)
            
        elif coord > flank3End:
            break
            
    #add last to 5p to dict
    if flank5pList:
        line = flank5pList[-1]
        coord = line[0]
        value = line[1:]
        
        PeakDict[coord] = value

    #add first to 3p to dict
    if flank3pList:
        line = flank3pList[0]
        coord = line[0]
        value = line[1:]
        
        PeakDict[coord] = value    

    return PeakDict

#############################################################
def Result2Report(NucResultTable, resultFile):

    with open(resultFile, 'w') as rfile:
    
        for line in NucResultTable:
            line = '\t'.join(line)+'\n'
            rfile.write(line)

    return rfile

#############################################################

#main function for nucleosome protection peaks (NNPs)    

def Nucleosome(inputBedFile, resultFile, sample):

    title = ['chromosome', 'Start position (hg19)', 'End position (hg19)', 'Region descriptor', 'Sample',
             'Nucleosome peak position (hg19)', 'Distance from start (bp)', 'Distance from end (bp)',
             'Within or Flanking?', 'WPS (mean = 1)', 'Read depth (mean = 1)']
    
    resultsTable = [title]

    BedDict = readBed2Dict(inputBedFile) #dictionary of input nucleosome regions

    for chrom in BedDict:
        regions = BedDict[chrom]

        #go through each line in the region
        if regions:
            L_Coveragepeaks = []
            
            #call file with list of NPPs based on sample and chromosome
            with open(sample + "_" + chrom + "_peaks.txt") as F_input:
                for line in F_input:
                    line = line.strip().split("\t")
                    line[0] = int(line[0])

                    L_Coveragepeaks.append(line)
        
            for line in regions:
                chromo = line[0]
                start = line[1]
                end = line[2]
                name = line[3]    
                
                PeakDict =  getPeaks(start, end, L_Coveragepeaks) #Dictionary of peaks within the region

                for coord in sorted(PeakDict):
                    rline = PeakDict[coord]
                    region = rline[0]
                    to5p = rline[1]
                    to3p = rline[2]
                    score = rline[3:]

                    value = [chromo, start, end, name, sample, coord]
                    value.extend([to5p, to3p, region])
                    value.extend(score)
                    
                    value = [str(n) for n in value]
                    resultsTable.append(value)   
    
    #write results to report
    Result2Report(resultsTable, resultFile)

    return resultsTable

start_time = time.time()

#Run script
results = Nucleosome("input.bed", "output.txt", "BRA01") # input file, output file, sample name

end_time = time.time()
        
print(round(end_time - start_time,2), "seconds")