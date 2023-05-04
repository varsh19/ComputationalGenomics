#/bin/bash

FILES=Contigs/*
for FILE in $FILES      # Looping over the Contigs files
do
        FILE_NAME="$(basename -s .fasta.gz $FILE)"      # Isolating file name
        FILE_NAME_FASTA="$(basename -s .gz $FILE)"      # Isolating file name with fasta extension
        cd
        cd ../team2/group2/gms2_results
        mkdir $FILE_NAME        # To create directory with each file name
        cd $FILE_NAME           # Going to directory for that file
        gunzip -k ../../$FILE           # Unzipping the file
        perl ../../GeneMarkS2/gms2.pl --genome-type bacteria --gcode 11 --output gms2_$FILE_NAME.gff --format gff3 --gid 'gene_' --seq ../../Contigs/$FILE_NAME_FASTA
        cd                      # Leaving the directory so that the correct directory can be created for the next file
done
cd ../team2/group2/Contigs/
rm *.fasta
cd
