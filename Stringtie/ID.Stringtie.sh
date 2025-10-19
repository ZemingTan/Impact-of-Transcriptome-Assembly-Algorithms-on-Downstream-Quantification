for i in {3..10}
do
	cd SimulationSample$i/stringtie
	awk '{print $2,$5 arr[0]}' Extract.txt  > ID.tmp.txt
	awk '{sub(/^rna-/,"",$1); print $1, $2}' ID.tmp.txt > ID.txt
	rm ID.tmp.txt
	cd ../..
done
