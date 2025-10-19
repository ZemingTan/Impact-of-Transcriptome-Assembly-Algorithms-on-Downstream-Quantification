for i in {3..10}
do
	cd SimulationSample$i
	awk '{print $1,$6 arr[0]}' SimulationSample.sim.isoforms.results > GroundTruth.zero.txt
	awk 'NR==1 || $2 !=0' GroundTruth.zero.txt > GroundTruth.txt
	rm GroundTruth.zero.txt
	cd ../
done
