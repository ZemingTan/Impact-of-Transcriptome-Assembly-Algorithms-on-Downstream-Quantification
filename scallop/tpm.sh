for i in {3..10}
do
	cd SimulationSample$i/scallop
	awk '{print $1,$4 arr[0]}' salmon.quant/quant.sf > TPM.txt
	awk 'NR==1 || $2 !=0' TPM.txt > TPM.nonzero.txt
	rm TPM.txt
	awk '{sub(/^transcript:/,"",$1); print $1, $2}' TPM.nonzero.txt > TPM.txt
	cp ../../tpm.py .
	python tpm.py
	mv TPM.txt
        mv TPM.extract.txt TPM.txt
	sed -i '1iName TPM' TPM.txt
	cd ../..
done
