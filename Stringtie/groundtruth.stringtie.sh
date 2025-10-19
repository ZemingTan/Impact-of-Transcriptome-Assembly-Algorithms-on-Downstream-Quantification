for i in {1..10}
do
	cd SimulationSample$i/stringtie
	cp ../../groundtruth.py .
	cp ../../Spearman.Stringtie.py .
 	python groundtruth.py
	cd ../..
done
