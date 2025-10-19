for i in {2..10}
do
	mkdir SimulationSample$i/cufflinks
	cd SimulationSample$i/cufflinks
	/home/yuting/Software/cufflinks-2.2.1.Linux_x86_64/cufflinks -p 16 -G ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.gtf -o SimulationSample ../SimulationSample.bam
	cp SimulationSample/transcripts.gtf ../SimulationSample.gtf
	/home/yuting/Software/gffcompare-0.12.6.Linux_x86_64/gffcompare -o gffall -r ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.gff SimulationSample.gtf
	gffread SimulationSample.gtf -g ../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.fna -w SimulationSample.fa
	cd ../..
done
