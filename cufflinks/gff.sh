for i in {2..10}
do
	cd SimulationSample$i/cufflinks
	cp SimulationSample/transcripts.gtf SimulationSample.gtf
	/home/yuting/Software/gffcompare-0.12.6.Linux_x86_64/gffcompare -o gffall -r ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.gff SimulationSample.gtf
	gffread SimulationSample.gtf -g ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.fna -w SimulationSample.fa
	cd ../..
done
