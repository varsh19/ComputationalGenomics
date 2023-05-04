#!/bin/bash

outdir="/Users/kc/downloads/iterated"

for fasta_file in *.fasta; do
    output_name=$(basename "$fasta_file" .fasta)
    output_file="$outdir/$output_name.glimmer"
    glimmer_iterated.sh "$fasta_file" "$output_file"
done
