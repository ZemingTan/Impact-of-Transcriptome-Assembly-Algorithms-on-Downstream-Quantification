# A pipeline to analysis The Impact of Transcriptome Assembly Algorithms on Downstream Quantification in RNA-seq Data Analysis. 
## Simulation
We use RSEM to simulate RNA-seq data and get groundtruth for assembly and quantification.
RSEM was used to estimate transcript expression levels from the real RNA-seq data:
```Reference prepared with rsem-prepare-reference --hisat2-hca```
Expression calculated using：
```rsem-calculate-expression --paired-end```
Read Simulation: Simulated paired-end RNA-seq reads (100 bp reads matching the input data characteristics) were generated using ```rsem-simulate-reads``` based on the estimated expression profiles. Multiple replicates were generated per species (10 for human, 5 for mouse, 3 for Arabidopsis).
## Transcriptome Assembly
Assemblers were run using the ```HISAT2```-generated BAM file (sorted, indexed).
StringTie2: ```StringTie2 -e -G -o (-e indicates expression estimation mode using reference annotations)```
Scallop: ```scallop -i -o (Does not require reference GTF)```
Cufflinks: ```cufflinks -G -o```
Annotation Comparison and Filtering (Post-Assembly for all):
Assembled GTF files were compared to the reference annotation using gffcompare (```gffcompare -r```) to identify perfectly matching transcript IDs (class code '=').
Assembled transcripts were extracted to FASTA format using gffread (```gffread -w -g```).
Transcript Quantification Based on Assembly (Salmon)
A Salmon index was built for each assembler's transcript FASTA file: ```salmon index -t -k 31 -i```
The corresponding real RNA-seq reads (FASTQ files) were quantified against this index: ```salmon quant -i -l A -1 -2 -o```
The transcript ID and TPM columns were extracted from the resulting ```quant.sf``` files.
## Salmon Quasi-Mapping Quantification (Reference Transcriptome)
The human reference transcriptome FASTA file (based on GRCh38.p14) was downloaded.
A Salmon index was built:```salmon index -t -k 31 -i ```
The real RNA-seq reads were directly quantified against this index: ``` salmon quant -i -l A -1 -2 -o```
The transcript ID and TPM columns were extracted from ```quant.sf```.
