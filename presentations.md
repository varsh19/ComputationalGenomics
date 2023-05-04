# Background and Strategy Presentation
## Team 2 - 8:40 to 8:59 (19 min)
6 of 6 presenting
### General Topics to mention
  1. background, overview, and core concepts
  1. description of tasks, algorithms uses, qualitative comparisons
  1. proposed approach and analysis workflow
  1. task descriptions and delegations
### Info Presented
- local -vs- global end-to-end alignment (great!)
- FASTA and ggsearch packages
- HMM based on markov chain, reviewed content well
- ab initio based on signal and content sensors
1. GeneMarkS2: uses HMM, pseudogenes can be an issue
1. Glimmer: higher false positives; unique output format
1. Prodigal
- table on pros/cons for ab initio and homology methods (great!)
- Algorithm comparison: ORForise - takes a bunch of features for ensemble
- description of pipelines and why they're useful
1. Prokka
1. PGAP (by NCBI)
### Comments
- prokka and PGAP are full blown annotation piplines that do gene prediction (this group's task) but also also functional annotation (the following group's task), so please **skip** both
- FASTA and ggsearch are crazy old, almost no practical use these days, but there's a weird reason I still occasionally use ggsearch36 (for older 16S bacterial taxonomy projects)
- ORForise is new to me, and I'm hopeful it'll handle all your needs, but very excited to see what you find on its utility
- Instead of performing homology tools in addition, be sure to spend time identifying how you can track a system call's performance beyond just `time` to evaluate CPU and RAM usage. Python libraries exist for it but you'll need to run those system calls then inside python. There's plenty of other non-python ways too. Some tools you'll specify 8 CPUs but tracking it you'll see you only used less than half that most of the time, so knowing which are efficient is valuable.

### Suggestions
- please don't use PGAP and Prokka. Both are full-scale pipelines that perform well beyond this specific task.
- please use Genemark, Glimmer, and Prodigal for all assemblies
- with 3 datasets, spend time formulating ideas how to evaluate which makes 1 better than the others, and formulate it into a script to automate your comparison -or- find a tool that can compare all (less likely but maybe ORForise will handle it)
- I didn't see task delegations. Be sure to clear those roles up ASAP and get moving independently on the details, collaborate to decrease error handling and information sharing.

### Grade
- to be determined by @hsong343
- no significant issues by me
