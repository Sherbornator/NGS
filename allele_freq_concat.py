#!/usr/bin/python

####
#This script reads presentation and relapse allele frequency out files and concatenates them, combining rows where identical
####
import sys
import pandas as pd

def usage():
    print ('Usage:')
    print ('allele_freq_concat.py pres_filename relapse_filename')
    sys.exit()

def parsing(pres, relapse):
    'This script reads presentation and relapse allele frequency out files and concatenates them, combining rows where identical'
    #get sample name - specific for my naming convention, would need altering for differently named files
    sample = pres.split('_presentation')
    sample = sample[0]
    #read both tables and change MAF column headings
    dfP = pd.read_table(pres, sep='\t', index_col=False)
    dfP.rename(columns={'MAF': 'pres_MAF'}, inplace=True)
    dfR = pd.read_table(relapse, sep='\t', index_col=False)
    dfR.rename(columns={'MAF': 'relapse_MAF'}, inplace=True)
    #join together and sort
    data = pd.concat([dfP, dfR], join='outer', axis=0)
    data.sort_values(by=['chromosome', 'position'], inplace=True)
    data = data.reset_index(drop=True)
    #make a new column with 'True' if previous chromosome and position equal to current chromosome and position
    data['newcol1'] = (data['position'].shift() == data['position']) & (data['chromosome'].shift() == data['chromosome'])
    #loop through and where rows are identical, update the previous row with the relapse MAF of the following row
    for i in range(1, len(data.index)):
        if (data.loc[i, 'newcol1']) == True:
            data.loc[i-1, 'relapse_MAF'] =  data.loc[i, 'relapse_MAF']
    #drop all the rows that are identical to the previous row
    data = data[~(data['newcol1'] == True)]
    #replace NaNs with zeros
    data['pres_MAF'].fillna(0, inplace=True)
    data['relapse_MAF'].fillna(0, inplace=True)
    #save only the columns we want
    data_to_save = []
    data_to_save = pd.DataFrame(data, columns=['chromosome', 'position', 'ref', 'alt', 'pres_MAF', 'relapse_MAF', 'gene'])
    
    #print the output
    file = open(sample + '_concatenate.txt', 'w')
    file.write(data_to_save.to_csv(sep='\t', index=False))
    file.close()

if (len(sys.argv) != 3):
    usage()
else:
    parsing(sys.argv[1], sys.argv[2])
