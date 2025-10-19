for i in {3..10}
do
	cd SimulationSample$i
	mkdir stringtie
	cd stringtie
	/home/yuting/Software/stringtie-2.2.1.Linux_x86_64/stringtie -p 8 -e -G ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.gff -o SimulationSample.gtf ../SimulationSample.bam
	/home/yuting/Software/gffcompare-0.12.6.Linux_x86_64/gffcompare -o gffall -r ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.gff SimulationSample.gtf
	gffread SimulationSample.gtf -g ../../../GCFReference/GCF_000001405.40_GRCh38.p14_genomic.fna -w SimulationSample.fa
	cd ../../
done
