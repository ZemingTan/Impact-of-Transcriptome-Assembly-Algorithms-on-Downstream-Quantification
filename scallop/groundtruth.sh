for i in {1..10}
do
	cd SimulationSample$i/scallop
	cp ../../groundtruth.py .
	cp ../../Spearman.py .
 	python groundtruth.py
	cd ../..
done
