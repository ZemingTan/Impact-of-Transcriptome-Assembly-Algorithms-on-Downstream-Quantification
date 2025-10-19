> result.stringtie.txt
for i in {1..10}
do
	dir_name="SimulationSample$i"
	cd SimulationSample$i/stringtie
	cp ../../Stringtie/Spearman.Stringtie.py .
	result=$(python Spearman.Stringtie.py)
	echo "$dir_name $result" >> ../../result.stringtie.txt
	cd ../..
done
