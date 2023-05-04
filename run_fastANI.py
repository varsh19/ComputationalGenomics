#!/bin/python3

import subprocess
import glob
import os
import argparse
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from Bio import Phylo
from scipy.cluster.hierarchy import linkage, dendrogram

parser = argparse.ArgumentParser(description="Comparative Genomics Analysis Pipeline. Use -help for usage details")
parser.add_argument('-f','--f', help = "for running fastANI", type = str)
parser.add_argument("-i", "--inputpath", help="path to the directory that has all the assembled genomes as sub-directories", required=True)
parser.add_argument("-fo","--fastani_output_file", help = "FastANI output directory", type = str)

args = parser.parse_args()

#FastANI output file generation
os.chdir(args.i)
files = glob.glob("*.fasta")
input_path = []
input_file_paths = open("inputs_paths.txt", "a")
for i in files:
	input_file_paths.write(args.i+i +"\n")	
input_file_paths.close()

# Running FastANI and creating visualizations
def fastani_run(input_file_paths, output):
	os.system(f"fastani --ql {input_file_paths} --rl {input_file_paths} -o {output})

	#Heatmap
	pairwise = []
	ids = {}
	count = 0
	with open(output, 'r') as fp:
	    fp = fp.readlines()
	    for line in fp:
	        line = line.rstrip().split()
	        if line[0].split('/')[-1][:-6] not in ids:
	            ids[line[0].split('/')[-1][:-6]] = count
	            count+=1
	        if line[1].split('/')[-1][:-6] not in ids:
	            ids[line[1].split('/')[-1][:-6]] = count
	            count+=1
	        pairwise.append((line[0].split('/')[-1][:-6], line[1].split('/')[-1][:-6], float(line[2])))
	print(len(pairwise))
	print(len(list(set(pairwise))))
	mat = np.zeros((50, 50))
	for i in pairwise:
	    #print(i)
	    mat[ids[i[0]]][ids[i[1]]] = i[2]
	
	df = pd.DataFrame(mat, columns=list(ids.keys()))
	df.index = list(ids.keys())
	print(df)
	sns.clustermap(df, cmap="magma")
	#plt.show()
	plt.savefig("clustermap.png", dpi=500)	

	#Phylogenetic Tree
	table = pd.read_csv(output, sep='\t', header=None)
	table = table[table[0] != table[1]]
	table[2] = 1 - (table[2] / 100)
	table = table.drop(columns=[3, 4])
	table = table.reset_index()
	table = table.pivot_table(index=1, columns=0, values=2)
	table = table.fillna(0)
	linkage_matrix = linkage(table, method='ward')
	fig, ax = plt.subplots(figsize=(10, 10))
	tree= dendrogram(linkage_matrix, labels=table.index, ax=ax, truncate_mode='lastp', p=100, orientation = 'left')


if args.f:
	print("running FastANI")
	fastani_run(input_file_paths, args.fo)
