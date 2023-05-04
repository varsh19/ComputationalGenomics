#!/bin/bash


mkdir {gff,fna,log} # Make directories for the generated files to move into

FILES=*.fasta  # assign the list of .fasta files in the folder to var FILES
for FILE in $FILES   # Loop over the list FILES
do
	FILE_NAME="$(basename -s .fasta $FILE)"	# Isolating file name
        FILE_NAME_FASTA="$(basename -s .gz $FILE)"

	prodigal -i $FILE -c -m -f gff -o $FILE_NAME.gff 2>&1 | tee $FILE_NAME.log	# Running Prodigal for that file
	bedtools getfasta -fi $FILE_NAME.fasta -bed $FILE_NAME.gff -fo $FILE_NAME.fna     # Running bedtools for the output from prodigal
done

# to remove the intermediate files
rm *.fasta.fai

# to move the generated files to their relevant directories
mv *.gff gff
mv *.fna fna
mv *.log log


