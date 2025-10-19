> result.salmon.txt
for i in {1..10}
do
	dir_name="SimulationSample$i"
	cd SimulationSample$i/salmon
	cp ../../Spearman.salmon.py .
	result=$(python Spearman.salmon.py)
	echo "$dir_name $result" >> ../../result.salmon.txt
	cd ../..
done
