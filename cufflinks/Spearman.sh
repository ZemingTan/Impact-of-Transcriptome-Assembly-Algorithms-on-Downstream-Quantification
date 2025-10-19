> result.cufflinks.txt
for i in {1..10}
do
	dir_name="SimulationSample$i"
	cd SimulationSample$i/cufflinks
	result=$(python Spearman.py)
	echo "$dir_name $result" >> ../../result.cufflinks.txt
	cd ../..
done
