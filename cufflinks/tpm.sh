for i in {1..10}
do
	cd SimulationSample$i/cufflinks
	awk '{print $1,$4 arr[0]}' salmon.quant/quant.sf > TPM.zero.txt
	awk 'NR==1 || $2 !=0' TPM.zero.txt > TPM.rna.txt
	awk '{sub(/^rna-/,"",$1); print $1, $2}' TPM.rna.txt > TPM.txt
	rm TPM.zero.txt
	rm TPM.rna.txt
	cp ../../cufflinks/tpm.py .
	python tpm.py
	rm TPM.txt
	mv TPM.extract.txt TPM.txt
	sed -i '1iName TPM' TPM.txt	
	cd ../..
done
