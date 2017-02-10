#!/Users/asherbor/anaconda3/bin/python

####
#This script takes a sample file with column headings "Name, Normal path to Bam, Tumour path to Bam" and loops trough MuTect1
####
import sys

def usage():
    print ("Usage:")
    print ("Mutect1.py sample_paths_file out_path")
    sys.exit()

def samples(sample_paths_file, out_path):
    """This function loads the sample names and paths from file"""
    header = []
    samples = []
    
    with open('%s' % sample_paths_file, 'r') as paths:        
        count = 0
        for line in paths:
            line = line.rstrip("\n")
            line = line.split("\t")
            if count == 0:
                header = line
                count += 1
            else:
                samples.append(line)
                count += 1
    paths.close()
    print ("# There are %s samples in the file\n" % (count - 1))
    
    #find column numbers
    name_idx = header.index("Name")
    normal_idx = header.index("Normal path to Bam")
    tumor_idx = header.index("Tumor path to Bam")

    """This runs MuTect1 for all the samples looped through"""
    for line in samples:
        ref_genome = ("/scratch/DMP/MYEGRP/asherborne01/Refs/Illumina_hg19/genome.fa")
        name = line[name_idx]
        normal = line[normal_idx]
        tumor = line[tumor_idx]
        out = "%s/%s.out.txt" % (out_path, name)
        cov = "%s/%s.wig.txt" % (out_path, name)
        vcf = "%s/%s.vcf.txt" % (out_path, name)
        
        print ("bash MuTect1_ALS.sh somaticSNVs_MuTect %s %s %s %s %s\n\n" % (normal, tumor, out, cov, vcf))

if (len(sys.argv) != 3):
    usage()
else:
    samples(sys.argv[1], sys.argv[2])
