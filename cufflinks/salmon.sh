for i in {2..10}
do
	cd SimulationSample$i/cufflinks
	salmon index -t SimulationSample.fa -i salmon.index -p 10
	salmon quant -l A -i salmon.index -1 ../SimulationSample_1.fq -2 ../SimulationSample_2.fq -o salmon.quant -p 10
	cd ../..
done
