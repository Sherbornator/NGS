#!/usr/bin/python

####
#This script parses a MuTect1 outfile and adds the file name in the first column
####
import sys
import pandas as pd

def usage():
    print ("Usage:")
    print ("vcf_concatenate.py MuTect1outFile")
    sys.exit()


def parsing(MuTect1vcfFile):
        "This script parses a Mutect1 out file"
        sample = MuTect1outFile[0:17]
        #parsed lists
        header = []
        snps = []
        concatSNPs = []

        vcf = open(MuTect1vcfFile)
        for line in vcf:
            line = line.rstrip("\n")
            line = line.split("\t")
            #save the column header list
            if (line[0][0] == "#"):
                continue
            if (line[0] == "contig"):
                header = line
                continue
            snps.append(line)
        vcf.close()

        concatSNPs = pd.DataFrame(snps)
        concatSNPs.columns = header
        concatSNPs.insert(0, 'sample', sample)

        #print the output
        file = open(sample + "concatenate.txt", "w")
        file.write(concatSNPs.to_csv(sep='\t', index=False))
        file.close()

if (len(sys.argv) != 2):
    usage()
else:
    parsing(sys.argv[1])
