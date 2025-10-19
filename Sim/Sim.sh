FN=$(wc -l < ./SRR7807484_1.fastq)
echo $FN
let read_number=$FN/4
echo "read number: "$read_number
for i in {3..10}
do
mkdir SimulationSample$i
/home/yuting/Software/RSEM-1.3.3/rsem-simulate-reads hisat_index/Index Multi.stat/Multi.model Multi.isoforms.results 0.25 $read_number SimulationSample$i/SimulationSample
done
