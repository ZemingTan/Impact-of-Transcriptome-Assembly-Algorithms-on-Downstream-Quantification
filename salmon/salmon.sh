for i in {1..10}
do
	cd SimulationSample$i
	mkdir salmon
	cd salmon
	salmon index -t ../../../GCF_000001405.40_GRCh38.p14_rna.fna -i transcripts_index -k 31
	salmon quant -i transcripts_index -l A -1 ../SimulationSample_1.fq.gz -2 ../SimulationSample_2.fq.gz --validateMappings -o transcripts_quant
	cd ../..
done
