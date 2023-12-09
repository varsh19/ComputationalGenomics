# Team2-ComparativeGenomics

## ANI-Based Method

### FastANI

FastANI is a software tool that calculates the average nucleotide identity (ANI) between two genomes. This method uses k-mer sampling and hashing to calculate ANI values. Thus, it reduces computational complexity and memory requirements. This tool is computationally efficient and scalable and hence can be used for analyzing large number of bacterial genomes. 

It has three modes- one to one, one to many and many to many. One-to-one computes ANI between single query and single reference genome. One to many compute ANI between single query genome and multiple reference genomes. Many to many is used when there are multiple query genomes and multiple reference genomes.

#### Installation

`conda install -c bioconda fastANI`

#### Usage

FastANI has three different modes. This project uses the many-to-many mode because to run multiple assembled fasta files against multiple reference genomes. More information about different modes of this tool can be found on the FastANI developers’ Github page. 

`FastANI --ql <list-of-fasta-files> --rl <list-of-fasta-files> --threads 10 -o output.out`

#### Visualization

We used the output file of FastANI to generate heatmap using various python libraries like matplotlib and seaborn. The exact script is in the “fastani_run()” function in our script "run_fastANI.py".

![image](https://github.gatech.edu/comgenomics2023/Team2-ComparativeGenomics/blob/main/Results/FastANIPhylogeneticTree.png)

![image](https://github.gatech.edu/comgenomics2023/Team2-ComparativeGenomics/blob/main/Results/FastANIHeatmap.png)

## SNP-Based Typing Method 

### ParSNP

Parsnp was designed to align the core genome of hundreds to thousands of bacterial genomes within a few minutes to few hours. Input can be both draft assemblies and finished genomes, and output includes variant (SNP) calls, core genome phylogeny and multi-alignments. Parsnp leverages contextual information provided by multi-alignments surrounding SNP sites for filtration/cleaning, in addition to existing tools for recombination detection/filtration and phylogenetic reconstruction.

#### Installation

`conda create -n par`

`conda install -c bioconda parsnp`

#### Usage

ParSNP takes in contigs.fasta files as input. It also requires a reference genome. If you do not have any reference just put ! in that -r flag and it would pick a random reference genome. 

`parsnp -d contigs -r GCF_000006945.2_ASM694v2_genomic.fna -o parsnp_outdir -p 4`

#### Visualization

ParSNP generates 4 files. Out of which .tree files helps in phylogenetic analysis.

`conda create -n harvestsuite -c bioconda figtree`

To view the phylogenetic tree (a GUI will pop up from this terminal command) 

`figtree parsnp_outdir/parsnp.tree`

![image](https://github.gatech.edu/comgenomics2023/Team2-ComparativeGenomics/blob/main/Results/ParSNP%20rsults.PNG)

## Anti Microbial Resistance Analysis

### AMRFinderPlus and hAMRonization

This software and the accompanying database (CARD) identify acquired antimicrobial resistance genes in bacterial protein and/or assembled nucleotide sequences as well as known resistance-associated point mutations for several taxa. We had the AMRFinderplus output from the functional annotation group. The hAMRonization module combines the outputs of 18 (as of 9/25/22) disparate antimicrobial resistance gene detection tools into a single unified format.

#### Installation 

`pip install hAMRonization`

#### Usage

hAMRonization gives a lot of options to combine our results. One of the options is summarize. It summarizes unique enteries across input reports of AMRFinderPlus. 

`hamronize summarize CGT2* -t tsv --summary_type tsv -o out.tsv`

#### Output

The output is processed in MS Excel.

![image](https://github.gatech.edu/comgenomics2023/Team2-ComparativeGenomics/blob/main/Results/hAMRonization%20output%20table.PNG)

## Recommendations to the CDC 

### Course of Action 

* Investigate the storage and distribution facilities of Georgia, Tennessee, Florida and South Carolina to identify the potential source of the items suspected to harbor the organism. The water treatment facilities of these states need to be analyzed and tested for Salmonella.
* Since Salmonella can spread via contaminated poultry, it is important to investigate the conditions in which poultry is raised for consumption. The food the poultry consumes, the cleanliness and hygiene are some things to be evaluated.
* Based on these results, it is important to recall batches of poultry suspected to be contaminated, and to unshelve these products from stores as soon as possible.
* Investigate the condition of public restrooms - make sure water is always running and that essentials like toilet paper, seat covers and disinfecting hand soap are always available. Also check the cleaning schedules of these restrooms to ensure regular disinfecting.

### General guidelines to prevent Salmonella infection:
* Always wash your hands after going out, contact with animals, using the washroom and other public places, cooking and eating.
* Do not touch your mouth or face after coming in contact with animals. Make sure your hands are disinfected before doing so.
* Keep raw foods and meats separated.
* Always ensure your food is heated/cooked enough by waiting or by using a cooking thermometer.
* Refrigerate perishable food within 2 hours of making, and thaw before consumption. The refrigerator should have a temperature of at least 40 °F and the freezer should be at 0 °F or lower.
