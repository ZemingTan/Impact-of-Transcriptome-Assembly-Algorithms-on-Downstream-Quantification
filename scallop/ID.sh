for i in {3..10}
do
	cd SimulationSample$i/scallop
	awk '{sub(/^rna-/, "", $2); match($0, /gene\.[0-9]*\.[0-9]*\.[0-9]*/, arr); print $2,$5 arr[0]}' Extract.txt > ID.txt
	cd ../..
done
