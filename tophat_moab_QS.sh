#!/bin/csh
##### These lines are for Moab
#MSUB -l nodes=16
#MSUB -l partition=ALL
#MSUB -l walltime=99:00:00
#MSUB -m be
#MSUB -V
#MSUB -o /home/SherborneA/RNAseq/QS

##### These are shell commands
date
cd /home/SherborneA/RNAseq/QS
tophat2 -o tophat_QS --fusion-search --keep-fasta-order --no-coverage-search -r 0 --mate-std-dev 80 --max-intron-length 100000 --fusion-min-dist 100000 --fusion-anchor-length 13 --fusion-ignore-chr
omosomes chrM /home/SherborneA/RNAseq/bowtie_index/hg19 QS_R1_001.fastq QS_R2_001.fastq
echo 'Done'
