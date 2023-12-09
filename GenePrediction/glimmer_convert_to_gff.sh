#!/bin/bash

# Set input and output directories
input_dir=/home/team2/group2/ALL_RESULTS/glimmer/iterated
output_dir=/home/team2/group2/ALL_RESULTS/glimmer/gff

# Iterate over input files and convert to GFF3 format
for file in "${input_dir}"/*; do
    # Extract file name without extension
    filename=$(basename "${file%.*}")

    # Convert Glimmer output to GFF3 format
    awk '/^>/ {name=$1} /^[^>]/ {OFS="\t"; split($2,start,"-"); print name,"Glimmer",$3,start[1]-1,start[2],".",$4,".",$5}' "${file}" > "${output_dir}/${filename}.gff3"
done
