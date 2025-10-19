for i in {1..10}
do
	cd SimulationSample$i/salmon
	awk '{print $1,$4 arr[0]}' transcripts_quant/quant.sf > TPM.zero.txt
	awk 'NR==1 || $2 !=0' TPM.zero.txt > TPM.txt
	rm TPM.zero.txt
	cd ../..
done
