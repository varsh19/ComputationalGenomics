# Background and Strategy Presentation
## Team 2 - time duration OK
6 of 6 presenting
### General Topics to mention
  1. background, overview, and core concepts
  1. description of tasks, algorithms uses, qualitative comparisons
  1. proposed approach and analysis workflow
  1. task descriptions and delegations

### Results Expected (to plan)
1. Compare genomes to perform outbreak analysis
1. What caused the outbreak (species/strain identity)? Use the table given with the original raw reads, which lists sample information for each isolate.
1. How are the isolates related to each other? How do they differ?
1. Which isolates correspond to outbreak, and which were sporadic strains (not directly linked to the ourbreak clade)?
1. What are the virulence and antibiotic resistance profiles of the outbreak isolates?
1. What is the recommended outbreak response and treatment?

### Deliverables Expected (to plan)
1. Deliverable #1 – comparative genomics pipeline on GitHub
1. Deliverable #2 – PDF with specific public health recommendations to CDC. Include at least 1 technical bioinformatics figure.

### Info Presented
- nice backgraound on ANI alignment based and alignment free (kmer faster, scalable)
- Mummer (ANIm) uses nucmer, promer and invokes maximal unique matches
- EDGAR: uses BSR (blast-based)
- nice comparison table on 3 tools and approach and limitations for each!
- MLST methods: StringMLST and STing exact kmer matches output phylogenetic tree
- Mentalist (in Julia, exotic language) specific algorithm involving colored de Bruijn graph well described
- SNP Typing: kSNP kmer-based on reads or assemblies, Parsnp mobile and genetic elements not included (not true, if all assemblies have them, they'll be in core and SNPs called), GSAlign global alignments
- nice comparison table again on 3 SNP tools focussing on scalability
- Task Delegations listed - great!

### Comments and Suggestions
- For EDGAR, as a warning, the web-based method I think has something like a 20 or so assembly limit so you won't be able to thoroughly evaluate your sample set with that approach, local install could be very difficult.
- Be sure both FastANI and ANIm (or ANIb) work well if EDGAR fails. No description on how you'll evaluate has be worried though, so consider how you'll visualize the results to quickly interprety which are closely related and which aren't. A heatmap could be valuable or GrapeTree MST possibly.
- For MLST: approach looks great! No visual emphasized again, so consider how you'll interpret. If all of them produce phylogentic trees that could be powerful but GrapeTree MST is often well-suited for this task to summarize too. Just don't use PhyloViz (outdated).
- For SNP tools, feel free to skip kSNP. I'm excited to see GSAlign results but parsnp might be focussed on first to get you a quick tree to view in [FigTree](https://github.com/rambaut/figtree/releases/tag/v1.4.4) or even iTol (web-based)
- Work delegation slide was good but 1 big point to discuss in the group:
    1. See Deliverable #2. Each person could certainly contribute their conclusion based on their tools used, but how you handle incongruent data technically as a group and report out is likely to be tough. One tool might suggest a genome is an sporadic genome not directly linked to the outbreak, whereas another might suggest it's close and within the outbreak. To handle this with care, using the epi sample info, and knowledge on the tools strengths and weakness takes time. Consider a deadline of everything presented prior to the class deadline so that you can then spend time (2 days?) on the PDF draft.
