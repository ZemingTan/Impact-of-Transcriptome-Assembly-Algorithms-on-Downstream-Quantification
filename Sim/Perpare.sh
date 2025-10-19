../Hisat/hisat2/hisat2-build -p 16 ../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.fna hisat_index/Index
../../Software/RSEM-1.3.3/rsem-prepare-reference --gtf ../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.gtf ../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.fna hisat_index/Index --hisat2-hca --hisat2-path ../Hisat/hisat2/ >log 2>log2
../../Software/RSEM-1.3.3/rsem-calculate-expression --paired-end SRR7807484_1.fastq SRR7807484_2.fastq hisat_index/Index Multi --hisat2-hca --hisat2-path ../Hisat/hisat2/ -p 20
