> result.scallop.txt
for i in {1..10}
do
	dir_name="SimulationSample$i"
	cd SimulationSample$i/scallop
	cp ../../scallop/Spearman.py .
	result=$(python Spearman.py)
	echo "$dir_name $result" >> ../../result.scallop.txt
	cd ../..
done
