## Team 2 - Gene Prediction

Our task was to take 50 assembled genomes (contigs) and find their CoDing Sequences (CDSs), and return files in .gff and .fna formats. 

We installed, used, and generated scripts for three tools of interest: Glimmer3, GeneMarkS2, and Prodigal. We ultimately chose to use Prodigal for our pipeline. We have included our scripts for the other two tools in the files above, however.

To run this pipeline, you need:
1) prodigal_script.sh (found in files)
2) contigs you would like analyzed (.fna or .fasta)
3) conda or miniconda previously installed

At the end of the pipeline, there will be two new folders, 'fna' and 'gff'. The 'gff' folder will contain the coordinates of all the CDSs found by prodigal. After these files are generated, the 'bedtools getfasta' command is used to map the .gff coordinates back onto the original .fasta sequences. These new .fna files, which are the corresponding nucleotide sequences of the predicted CDSs, will be found in the 'fna' folder. The 'bedtools getfasta' command is used with the following options:

  • -fi : input fasta file of the contigs  
  • -fo : output fasta file (.fna format here)  
  • -bed : BED/GFF/VCF file of ranges to extract from -fi

### Create & activate Conda environment

```
conda create -c gene_pred
conda activate gene_pred
```

### Install tools

```
conda install -c bioconda prodigal
conda install -c bioconda bedtools
```

### Setting up file structure

``` 
mkdir assembled_contigs
cd assembled_contigs
```

### Move files into the assembled_contigs directory

```
mv /your_path_to_prodigal_script.sh/ .
cp /your_path_to_contigs/ .
```

### Are your files in .gz or .fna format?

If your files are zipped or in .fna format, run these relevant command(s)-

```
gunzip *.gz
for f in *.fna; do mv -- "$f" "${f%.fna}.fasta"; done
```

### Run the Prodigal script

Prodigal is a fast, reliable protein-coding gene prediction tool used for prokaryotic genomes. Prodigal uses an unsupervised machine learning algorithm and predicts the correct translation initiation site for most genes. It can output information about every potential start site in the genome, including confidence score, RBS motif, and much more. By default, Prodigal produces one output file, which consists of gene coordinates and some metadata associated with each gene. The options used along with the prodigal command line include:

  • –i : input file parameter (.fasta format)
  • -o : name of output file generated
  • -f : format of output file (.gff format in this case)  
  • -c : closed ends - does not allow partial genes at end of sequence  
  • -m : gap-handling behavior - genes cannot run into gaps 
  
``` 
./prodigal_script.sh
```

The generated files can be found in their corresponding subfolders.

### Deactivate the Conda environment
``` 
conda deactivate
```
