#!/bin/bash

# Function for using MuTect to identify somatic SNPs (modified on 2015 Feb 2)
# Expected variables - to be declared before function is run (ie variables shared by diffrent functions in the pipeline)
# DIRLOGID: directory containing log files associated with each sample ID (as indicated by input file name)
# FLAG_FAIL: flag used to indicate that something went wrong
# Function parameters:
# $1: input normal BAM file
# $2: input tumor BAM file
# $3: output call_stats.txt file
# $4: output coverage_file .coverage.wig.txt
# $5: output vcf file

somaticSNVs_MuTect()
{
  echo "Note: MuTect requires an older version of java"
  module unload java
  module load java/sun6/1.6.0u45
  which java
  export _JAVA_OPTIONS=-Djava.io.tmpdir=/scratch/DMP/MYEGRP/asherborne01/temp/  # to avoid running out of space in the default tmp directory

  # Select reference genome
  local ref_genome="/scratch/DMP/MYEGRP/asherborne01/Refs/Illumina_hg19/genome.fa"

  # Select known sites 
  # Recommended sets of known sites: Mills indels 1KG indels
  #local known_SNPs="/scratch/cancgene/dchubb/references/dbSNP_138_feb_2014.vcf" 
  #local Mills_1KG_indels="/scratch/cancgene/dchubb/references/Mills_and_1000G_gold_standard.indels.b37.sites.vcf"

  echo "Identifying somatic SNPs using MuTect"
  echo " input normal: ""$1"
  echo " input tumor: ""$2"
  echo " refernce genome: ""$ref_genome"
  #echo " known indels: ""$Mills_1KG_indels"
  #echo " dbsnp file:""$known_SNPs"
  echo " output call stats: ""$3"
  echo " output coverage file: ""$4"
  echo " output vcf file: ""$5"
  # maybe copare with and without -XX:+UseSerialGC

  java -jar -Xms10G -Xmx10G /apps/mutect/1.1.4/muTect-1.1.4.jar \
    --analysis_type MuTect \
    --reference_sequence "$ref_genome" \
    --input_file:normal "$1" \
    --input_file:tumor "$2" \
    --out "$3" \
    --coverage_file "$4" \
    --vcf "$5"
    
}

# call arguments verbatim:
"$@"
