#!/bin/bash
for i in {2..10}
do
	cd SimulationSample$i/cufflinks
	InputFile="gffall.SimulationSample.gtf.refmap"
	OutputFile="Extract.txt"
	head -n 1 gffall.SimulationSample.gtf.refmap >> Extract.txt
	while IFS= read -r line; do
        	if [[ $line == *"="* ]]; then
                	echo "$line" >> "$OutputFile"
        	fi
	done < "$InputFile"
	cd ../..
done
