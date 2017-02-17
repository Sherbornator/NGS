#!/bin/bash
#
#BSUB -J "BWAindex"
#BSUB -n 4
#BSUB -P DMPGJMAAG
#BSUB -W 75:00
#BSUB -o /scratch/DMP/MYEGRP/asherborne01/MiSeq/AmpliconPanel/170217_AK2RK_ARE44_COMB/BWAindex.output.%J
#BSUB -e /scratch/DMP/MYEGRP/asherborne01/MiSeq/AmpliconPanel/170217_AK2RK_ARE44_COMB/BWAindex.errors.%J

module load bwa/0.7.12/bwa
echo "Starting BWA index"
bwa index -a bwtsw /scratch/DMP/MYEGRP/asherborne01/Refs/Illumina_hg19/genome.fa Illumina_hg19
echo "Finished"
