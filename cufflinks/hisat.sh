for i in {3..10}
do
	cd SimulationSample$i
	/home/yuting/tzm/Hisat/hisat2/hisat2 --dta -x ../../HisatIndex/Index \
       		-1 SimulationSample_1.fq -2 SimulationSample_2.fq  \
       		-S SimulationSample.sam \
       		-p 10
	samtools sort -@ 8 -o SimulationSample.bam SimulationSample.sam
	samtools index SimulationSample.bam
	cd ..
done
