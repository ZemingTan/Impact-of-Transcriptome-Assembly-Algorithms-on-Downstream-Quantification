for i in {3..10}
do
	mkdir SimulationSample$i/scallop
	cd SimulationSample$i/scallop
	/home/yuting/Software/scallop-0.10.4_linux_x86_64/scallop -i ../SimulationSample.bam -o SimulationSample.gtf
	/home/yuting/Software/gffcompare-0.12.6.Linux_x86_64/gffcompare -o gffall -r ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.gff SimulationSample.gtf
	gffread SimulationSample.gtf -g ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.fna -w SimulationSample.fa
	cd ../..
done
